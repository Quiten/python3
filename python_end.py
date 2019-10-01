i = 1
opening = "true"

def number_checker():
    a = open("memes.txt", "r")
    lines = a.readlines()
    print(lines)
    a.close()


def nummer_erbij(getal):
    return getal + 1

def gevoel(hoe, waiter):
    nummer = 1
    while(hoe != "esc"):
        if (hoe == "toev"):
            keuze = input("freestyle of locked ")
            if (keuze == "locked"):
                word = input("Woord ")
                nummero = input("Nummer ")
                with open("memes.txt", "a") as a:
                    a.write("Woord : " + word + " , Nummer : " + nummero + "\n")
                waiter = "false"
                looper(hoe, waiter)
            elif (keuze == "freestyle"):
                freestyle_text = input("Wat moet er in de .txt bestand ")
                print(freestyle_text)
                with open("memes.txt", "a") as a:
                    a.write(freestyle_text + "\n")
                waiter = "false"
                looper(hoe, waiter)
            else:
                print("error_writer")
                waiter = "false"
                looper(hoe, waiter)


        elif (hoe == "read"):
            with open("memes.txt", "r") as b:
                line = b.readlines()
                regel = input("Welke regel ? ; ")
                if (regel != "alles"):
                    regel2= int(regel)
                    if (isinstance(regel2, int)):
                        print(line[regel2-1])
                    else:
                        print("Failure")
                    waiter = "false"
                    looper(hoe, waiter)
                elif (regel == "alles"):
                    for i, value in enumerate(line,1):
                        print(i, value)
                    waiter = "false"
                    looper(hoe, waiter)
                else:
                    print("dwadwaa")
                    waiter = "false"
                    looper(hoe, waiter)
        elif (hoe == "del"):
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
                    waiter = "false"
                    looper(hoe, waiter)
                elif (regel == "alles"):
                    with open("memes.txt",  "w") as c:
                        for i in line :
                            del line[0]
                    waiter = "false"
                    looper(hoe, waiter)
                else:
                    print("error 543")
                    waiter = "false"
                    looper(hoe, waiter)
        elif (hoe == "num"):
            with open("memes.txt", "r") as reader_num :
                reader_regel = int(input("Uit welke regel?"))
                value_1 = reader_num.readlines()
                value_2 = value_1[reader_regel-1]
                value_3 = int(value_2)
                print(value_3)
                waiter = "false"
                looper(hoe, waiter)
        else:
            print("?")
    print("Stopping code")
    print("~~~~~~~")
    waiter = "true"
    hoe = "done"
    looper(hoe,waiter)
def begin_code():
    hoe = ""
    commandos = ["toev", "read", "del", "num","esc"]
    while not hoe in commandos:
        print("~~~~~~~")
        print("toev : woord toevoegen")
        print("read : regel(s) lezen")
        print("del   : regel verwijderen")
        print("num : nummer")
        print("esc  : Programma stoppen")
        hoe = input("iets : ")
        waiter = "true"
        opening = "false"
        print("~~~~~~~")
        if (hoe in commandos):
            gevoel(hoe, waiter)

def looper(hoe, waiter):
    while (hoe != "esc"):
        if (waiter == "false"):
            begin_code()
        else:
            print("stopped")

if (opening == "true"):
    opening = "false"
    begin_code()
else:
    print("ended")
