import pathlib
import Time
import GetNote
import Delete
import CreateNote


def editHeadNote():
    head = GetNote.getHeadNote()
    file = open("  Note_List.txt", "r")
    f = file.read().split("\n")
    file.close()
    file = open("  Note_List.txt", "w")
    newHead = GetNote.getEditHead()
    file.write(newHead + " : " + Time.getTime())
    file.write("\n")
    for i in range(len(f)):
        t=f[i].split(" : ")
        if (t[0] != head):
            file.write(f[i])
            file.write("\n")
    file.close()
    file1 = open(head + ".txt")
    text = file1.read().split()
    file1.close()
    Delete.deleteNoteHead(head)
    CreateNote.createNote(newHead, text[0])
def editNote():
    head = GetNote.getHeadNote()
    file1 = open(head + ".txt","w")
    newNote = GetNote.getEditNote()
    file1.write(newNote)
    file1.close()

    file = open(" Note_List.txt", "r")
    f = file.read().split("\n")
    file.close()
    file = open(" Note_List.txt", "w")
    file.write(head + " : " + Time.getTime())
    file.write("\n")
    for i in range(len(f)):
        t = f[i].split(" : ")
        if (t[0] != head):
            file.write(f[i])
            file.write("\n")
    file.close()

