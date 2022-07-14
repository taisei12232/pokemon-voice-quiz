import json
import random
import simpleaudio

with open("gen1-5.json","r") as f:
    pokemons = json.load(f)
random.shuffle(pokemons)
input("press Enter!")
for pokemon in pokemons:
    wav_obj = simpleaudio.WaveObject.from_wave_file("voice/" + pokemon["no"] + ".wav")
    c = 0
    while(c == 0):
        play_obj = wav_obj.play()
        a = input("press Enter to answer!")
        c += 1
        if(a == "r"):
            c = 0
        if(a == "q"):
            exit()
    print(pokemon["name"])
    b = input("press Enter to next!")
    if b == "q":
        exit()