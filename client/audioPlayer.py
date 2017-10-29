import wave
import pyaudio

chunk = 1024

class AudioPlayer:

	def __init__(self):
		return

	def playAudioByFilename(self, filename):

		self.wf = wave.open(filename + ".wav", "rb")
		p = pyaudio.PyAudio()

		self.stream = p.open(format=p.get_format_from_width(self.wf.getsampwidth()),
							 channels=self.wf.getnchannels(),
							 rate=self.wf.getframerate(),
							 output=True)

		data = self.wf.readframes(chunk)

		while len(data) > 0:
			self.stream.write(data)
			data = self.wf.readframes(chunk)

		self.stream.stop_stream()
		self.stream.close()
		p.terminate()

	def playAudioByWave(self, file):

		self.wf = wave.open(file)
		p = pyaudio.PyAudio()

		self.stream = p.open(format=p.get_format_from_width(self.wf.getsampwidth()),
							 channels=self.wf.getnchannels(),
							 rate=self.wf.getframerate(),
							 output=True)

		data = self.wf.readframes(chunk)

		while len(data) > 0:
			self.stream.write(data)
			data = self.wf.readframes(chunk)

		self.stream.stop_stream()
		self.stream.close()
		p.terminate()