import pathlib
import GetNote

def deleteNoteHead(head):
    file = pathlib.Path(head+".txt")
    file.unlink()
    #deleteNote(hand)

def deleteNote():
    head = GetNote.getHeadNote()
    deleteNoteHead(head)
    file = open("  Note_List.txt", "r")
    f = file.read().split("\n")
    file.close()
    for i in range(len(f)-1):
        s = f[i].split(" : ")
        if(s[0] == head):
            f.remove(f[i])
    file = open("  Note_List.txt", "w")
    for i in range(len(f)):
       file.write(f[i])
       file.write("\n")
    file.close()