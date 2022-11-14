import time
from operator import eq
from math import log10
import pyaudio #instalar de forma general no en env
import audioop  
import traceback
from rele import rele

class sound_scanner:
	def __init__(self, fun, nivel_minimo = 40):
		self.nivel_minimo = nivel_minimo
		self.fun = fun

		self.p = pyaudio.PyAudio()
		WIDTH = 2
		print(self.p.get_default_output_device_info())
		RATE = int(self.p.get_default_output_device_info()['defaultSampleRate'])
		DEVICE = self.p.get_default_output_device_info()['index']
		self.rms = 0
		self.anterior = 0
		self.estado = "habla"

		def callback(in_data, frame_count, time_info, status):
			self.rms = audioop.rms(in_data, WIDTH) / 32767
			return in_data, pyaudio.paContinue


		self.stream = self.p.open(format=self.p.get_format_from_width(WIDTH),
						output_device_index=DEVICE,
						channels=1,
						rate=RATE,
						input=True,
						output=False,
						stream_callback=callback)

	def start(self):
		self.stream.start_stream()
		self.anterior = 0
		self.estado = "habla"
		maximo = 1
		equ = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J"]
		prom = [len(equ)]*40
		index = 0
		while self.stream.is_active():
			try:
				db = log10(self.rms) + 6
				perfil  = db**4
				index += 1
				index = index % len(prom)
				prom[index] = perfil
				maximo = sum(prom) / len(prom)
				nivel  = (perfil / maximo) * len(equ)
				nivel = len(equ)-1 if nivel >= len(equ) else nivel
				if maximo < self.nivel_minimo:
					nivel = 1


				# print(f"\rSonando: {db > 0} --- anterior: {self.anterior} --- DB: {perfil}", end="") 
				if nivel > self.nivel_minimo:
					if nivel > self.anterior and self.estado == "calla":
						self.estado = "habla"
					elif nivel < self.anterior and self.estado == "habla":
						self.estado = "calla"
				else:
					self.estado = "calla"
				#print(f"\r\r{self.estado} | {index} | {round(nivel, 1)} | {round(maximo, 1)} | {''.join(equ[:int(nivel)])}", end="  "*(len(equ)-int(nivel)))

				self.fun(self.estado == "habla", 0.035)
				self.anterior = nivel
				# refresh every 0.3 seconds 
				time.sleep(0.001)
			except Exception as e:
				if e.args[0] == "math domain error":
					pass
				else:
					raise Exception(traceback.format_exc())

		self.stream.stop_stream()
		self.stream.close()

	def close(self):
		self.p.terminate()
