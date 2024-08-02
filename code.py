import board
import busio
import time
import audiocore
import audiopwmio
import adafruit_mpr121

# Initialize I2C bus and MPR121
i2c = busio.I2C(board.SCL, board.SDA)
mpr121 = adafruit_mpr121.MPR121(i2c)

# Initialize the speaker on pin RX
audio = audiopwmio.PWMAudioOut(board.RX)

'''
0 - hello
1 - help
2 - yes
3 - no
4 - water
7 - food
8 - bathroom
9 - play
10 - happy
11 - sad
'''

def play_wav(file_name):
    with open(file_name, "rb") as f:
        wav = audiocore.WaveFile(f)
        audio.play(wav)
        while audio.playing:
            pass

while True:
    # Loop through all 12 inputs (0-11)
    bool_array = 12*[False]
    for i in range(12):
        if mpr121[i].value:
            wav_file = f"{i}.wav"
            print(f"Playing {wav_file}")          
            bool_array[i] = True
            play_wav(wav_file)
            time.sleep(0.25)
    print(bool_array)
