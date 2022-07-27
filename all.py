import json
import random
import simpleaudio

with open("gen1-8.json","r") as f:
    pokemons = json.load(f)
random.shuffle(pokemons)
input("press Enter!")
faileds = []
for pokemon in pokemons:
    try:
        wav_obj = simpleaudio.WaveObject.from_wave_file("voice/" + pokemon["no"] + ".wav")
        wav_obj.play()
    except:
        print(pokemon["no"])
        print(pokemon["name"])
        faileds.append(pokemon["no"])

import librosa
import soundfile as sf

for i in faileds:
    try:
        y, sr = librosa.core.load('./voice/'+i+'.wav', sr=44100, mono=True) # 22050Hz、モノラルで読み込み
        sf.write('./voice/'+i+'.wav', y, sr, subtype="PCM_16") 
    except:
        print(i)