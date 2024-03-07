import GetNote
import SeeNote
import Delete
import EditNote
import Menu
Menu.menuPrint()
run = True
while(run):
    comand = input()
    match comand:
        case "add":
            GetNote.getNote()
            Menu.team()
        case "see":
             SeeNote.see()
        case "exit":
            run = False
        case "delete":
            Delete.deleteNote()
            Menu.team()
        case "seeAll":
            SeeNote.seeAll()
            Menu.team()
        case "editHand":
            EditNote.editHeadNote()
            Menu.team()
        case "seeAll":
            SeeNote.seeAll()
            Menu.team()
        case "editNote":
            EditNote.editNote()
            Menu.team()
        case "menu":
            Menu.menuPrint()
