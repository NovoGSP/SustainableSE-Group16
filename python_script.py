import random
import os

samples = []

root = "Path\\to\\experiment"
energi_bridge = "path\\to\\energi\\bridge\\EnergiBridge-main\\target\\release\\energibridge -o "

for i in range(4):
    for j in range(30):
        samples.append(i)

if not os.path.exists(root + "\\results"):
    os.makedirs(root + "\\results")

vscode = 'REM Start typeLoremIpsum.exe in the background \nstart "" "'+ root + '\\vsCodeLorem.ahk" \n\n timeout /t 2 /nobreak > NUL \n\nREM Start energibridge in the background \nstart /wait ' + energi_bridge + root + '\\results\\results-{}.csv --summary timeout 15 \n\n'
notepad = 'REM Start typeLoremIpsum.exe in the background \nstart "" "'+ root + '\\notepadLorem.ahk" \n\n timeout /t 2 /nobreak > NUL \n\nREM Start energibridge in the background \nstart /wait ' + energi_bridge + root + '\\results\\results-{}.csv --summary timeout 15 \n\n'
notepad_plus = 'REM Start typeLoremIpsum.exe in the background \nstart "" "'+ root + '\\notepad++Lorem.ahk" \n\n timeout /t 2 /nobreak > NUL \n\nREM Start energibridge in the background \nstart /wait ' + energi_bridge + root + '\\results\\results-{}.csv --summary timeout 15 \n\n'
word = 'REM Start typeLoremIpsum.exe in the background \nstart "" "'+ root + '\\wordLoremIpsum.ahk" \n\n timeout /t 2 /nobreak > NUL \n\nREM Start energibridge in the background \nstart /wait ' + energi_bridge + root + '\\results\\results-{}.csv --summary timeout 15 \n\n'

random.shuffle(samples)

num_vs = 0
num_notepad = 0
num_plus = 0
word_num = 0

f = open("script.bat", "w")
f.write("@echo off \n \n")
for sample in samples:
    if sample == 0: 
        f.write(vscode.format("vs-{}".format(num_vs)))
        num_vs += 1
    if sample == 1: 
        f.write(notepad.format("note-{}".format(num_notepad)))
        num_notepad += 1
    if sample == 2: 
        f.write(notepad_plus.format("plus-{}".format(num_plus)))
        num_plus += 1
    if sample == 3:
        f.write(word.format("word-{}".format(word_num)))
        word_num += 1
    f.write("timeout 60 \n\n")
f.close()