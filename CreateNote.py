import json
import datetime
import pathlib
def createNote(hand, body):
    my_file = open(hand+".txt","a")
    my_file.write(body)
    my_file.write("\n")
    my_file.close()

def allHands(hand,time):
    lines = []
    with open("  Note_List.txt", 'r') as file:
        for line in file:
            line = line.strip("\n")  # удаляем лишние пробелы в начале и конце строки
            if line:  # проверяем, что строка не пустая
                lines.append(line)
    file2 = open("  Note_List.txt", "w")
    note = hand+" : "+time
    file2.write(note)
    file2.write("\n")
    for i in range(len(lines)):
        file2.write(lines[i])
        file2.write("\n")
    file2.close()
