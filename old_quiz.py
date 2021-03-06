import json
import random
import simpleaudio

with open("gen1-8.json","r") as f:
    pokemons = json.load(f)
random.shuffle(pokemons)
input("press Enter!")
for i,pokemon in enumerate(pokemons):
    print(str(i+1)+"/"+str(len(pokemons)))
    wav_obj = simpleaudio.WaveObject.from_wave_file("voice/" + pokemon["no"] + ".wav")
    c = 0
    while(c == 0):
        wav_obj.play()
        a = input("press Enter to answer!")
        c += 1
        if(a == "r"):
            c = 0
        if(a == "q"):
            exit()
    print(pokemon["name"])
    c = 0
    while(c == 0):
        b = input("press Enter to next!")
        if b == "q":
            exit()
        elif b == "r":
            wav_obj.play()
        else:
            break
