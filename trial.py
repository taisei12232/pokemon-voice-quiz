import json
import simpleaudio
import sys
import random

args = sys.argv
with open("gen1-8.json","r") as f:
    pokemons = json.load(f)
if(len(args) < 2):
    print("ポケモンの名前を入力してください")
    exit()

if(args[1] == "ポケモン"):
    random.shuffle(pokemons)
    for pokemon in pokemons:
        wav_obj = simpleaudio.WaveObject.from_wave_file("voice/" + pokemon["no"] + ".wav")
        wav_obj.play()
    exit()

c = 0
for pokemon in pokemons:
    if(pokemon["name"] == args[1]):
        wav_obj = simpleaudio.WaveObject.from_wave_file("voice/" + pokemon["no"] + ".wav")
        played = wav_obj.play()
        played.wait_done()
        c += 1
if c == 0:
    print("not found")
