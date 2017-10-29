import requests
import time
import websocket
import _thread
import random
import json
import audioPlayer
import io

wsUri = "ws://node-red-001.au-syd.mybluemix.net/websocket/command"
speechUri = "https://node-red-001.au-syd.mybluemix.net/tts"
sessionId = 0

def playFile(filename):
	print("Play: " + filename)
	player = audioPlayer.AudioPlayer()
	player.playAudioByFilename(filename)

def playWave(file):
	player = audioPlayer.AudioPlayer()
	player.playAudioByWave(file)

def speech(text):
	print("Speech Request:" + text)
	r = requests.get(speechUri, params={'text': text})
	f = open(text + ".wav", 'wb')
	f.write(r.content)
	f.close()

	playFile(text)

def on_message(ws, message):
	print(message)
	command = json.loads(message)
	if "play" in command:
		filename = command["play"]
		_thread.start_new_thread(playFile, (filename,))
		# th = threading.Thread(target=playFile(filename))
		# th.start()
	if "speech" in command:
		text = command["speech"]
		_thread.start_new_thread(speech, (text,))
		# th = threading.Thread(target=speech(text))
		# th.start()

def on_error(ws, error):
	print(error)

def on_close(ws):
	print("### closed ###")

def on_open(ws):
	sessionId = random.randint(0,1000000000)
	ws.send("Hello %d" % sessionId)

if __name__ == "__main__":
	websocket.enableTrace(True)
	ws = websocket.WebSocketApp(wsUri,
							  on_message = on_message,
							  on_error = on_error,
							  on_close = on_close)
	ws.on_open = on_open
	ws.run_forever(ping_interval=30, ping_timeout=15)