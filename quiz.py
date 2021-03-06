import json
import random
import simpleaudio
import subprocess

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
        a = input("press Enter to answer!\n")
        c += 1
        if(a == "r"):
            c = 0
        if(a == "q"):
            exit()
    cmd = 'toilet -w $(tput cols) -f mono12 "' + pokemon["displayname"] + '"'
    #print(cmd)
    subprocess.call(cmd,shell=True)
    c = 0
    if(i+1 == len(pokemons)):
        print("finished!")
        exit()
    while(c == 0):
        b = input("press Enter to next!")
        if b == "q":
            exit()
        elif b == "r":
            wav_obj.play()
        else:
            break