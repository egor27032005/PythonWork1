import CreateNote
import Time

i=0
def getBodyNote():
    print("Введите заметку: ")
    s = input()
    return s

def getEditHead():
    print("Введите новый зоголовок заметки: ")
    s = input()
    return " "+s
def getEditNote():
    print("Введите новую заметку: ")
    s = input()
    return s

def getHeadNote():
    print("Введите зоголовок заметки: ")
    s = input()
    return " "+s


def getI():
    global i
    return i

def getNote():
    hand = getHeadNote()
    body = getBodyNote()
    time = Time.getTime()
    CreateNote.createNote(hand, body)
    CreateNote.allHands(hand,time)
