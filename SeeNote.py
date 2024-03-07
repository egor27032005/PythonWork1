def see():
    file = open("  Note_List.txt","r")
    f = file.read().split()
    t = 0
    for i in range(0,len(f),3):
        t += 1
        print(t,f[i])
def seeAll():
    file = open("  Note_List.txt","r")
    f = file.read().split("\n")
    file.close()
    for i in range(len(f)-1):
        t = f[i].split(" : ")
        hand = t[0]
        file2 = open(hand+".txt","r")
        f2 = file2.read().split()
        print(hand, end = " : ")
        print(f2[0])
        file2.close()