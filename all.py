import json
import random
import simpleaudio

with open("gen1-5.json","r") as f:
    pokemons = json.load(f)
random.shuffle(pokemons)
input("press Enter!")
for pokemon in pokemons:
    wav_obj = simpleaudio.WaveObject.from_wave_file("voice/" + pokemon["no"] + ".wav")
    wav_obj.play()
    print(pokemon["name"])