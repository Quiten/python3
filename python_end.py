i = 1
opening = True
funct = ""

def functies_end():    
    print("Stopping code")
    print("~~~~~~~")
    waiter = True
    funct = "esc"

def functies_num():
    with open("memes.txt", "r") as reader_num :
        reader_regel = int(input("Uit welke regel?"))
        value_1 = reader_num.readlines()
        value_2 = value_1[reader_regel-1]
        if (isinstance(int(value_2),int)):
            print(value_2)
        else :
                print("was not an number")
        waiter = False
        loop(funct, waiter)

def functies_del():
            with open("memes.txt","r") as b:
                line = b.readlines()
            with open("memes.txt", "a") as b:
                for i, value in enumerate(line, 1):
                    print(i, value)
                regel = input("Welke regel wilt u verwijderen? : ")
                if (regel != "alles"):
                    regel2= int(regel)
                    if (isinstance(regel2, int)):
                        del line[regel2-1]
                        with open("memes.txt", "w") as c:
                            c.writelines(line)
                            print(line)
                    else:
                        print("error 345")
                    waiter = False
                    loop(funct, waiter)
                elif (regel == "alles"):
                    with open("memes.txt",  "w") as c:
                        for i in line :
                            del line[0]
                    waiter = False
                    loop(funct, waiter)
                else:
                    print("error 543")
                    waiter = False
                    loop(funct, waiter)

def functies_toev():
            keuze = input("freestyle of locked ")
            if (keuze == "locked"):
                word = input("Woord ")
                nummero = input("Nummer ")
                with open("memes.txt", "a") as a:
                    a.write("Woord : " + word + " , Nummer : " + nummero + "\n")
                waiter = False
                loop(funct, waiter)
            elif (keuze == "freestyle"):
                freestyle_text = input("Wat moet er in de .txt bestand ")
                print(freestyle_text)
                with open("memes.txt", "a") as a:
                    a.write(freestyle_text + "\n")
                waiter = False
                loop(funct, waiter)
            else:
                print("error_writer")
                waiter = False
                loop(funct, waiter)

def functies_read():
            with open("memes.txt", "r") as b:
                line = b.readlines()
                regel = input("Welke regel ? ; ")
                if (regel != "alles"):
                    regel2= int(regel)
                    if (isinstance(regel2, int)):
                        print(line[regel2-1])
                    else:
                        print("Failure")
                    waiter = False
                    loop(funct, waiter)
                elif (regel == "alles"):
                    for i, value in enumerate(line,1):
                        print(i, value)
                    waiter = False
                    loop(funct, waiter)
                else:
                    print("false")
                    waiter = False
                    loop(funct, waiter)

def functies(funct, waiter):
    
    nummer = 1
    while(funct != "esc"):
        if (funct == "toev"):
            functies_toev()

        elif (funct == "read"):
            functies_read()
        elif (funct == "del"):
            functies_del()
        elif (funct == "num"):
            functies_num()
    else :
        functies_end()

def begin_code():
    funct = ""
    commandos = ["toev", "read", "del", "num","esc"]
    while not funct in commandos:
        print("~~~~~~~")    
        print("toev : woord toevoegen")
        print("read : regel(s) lezen")
        print("del   : regel verwijderen")
        print("num : nummer")
        print("esc  : Programma stoppen")
        funct = input("iets : ")
        waiter = True
        opening = False
        print("~~~~~~~")
        if (funct in commandos):
            functies(funct, waiter)

def loop(funct, waiter):
    while (funct != "esc"):
        if (waiter == False):
            begin_code()
        else:
            print("stopped")

if (opening == True):
    opening = False
    begin_code()
else:
    print("ended")
