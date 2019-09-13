pokemon_list = {"mimikyu, wooloo"}

def test():
    print("You have encountered a wild pokemon!")
    print("A wild " + str(poke)  + " appeared")

#print("xxxxxxxxxx")

#print("test 1")

def hello_world():
    for i in range(10):
        print("Hello world " + str(i + 1))

def tafel_5():
    for i in range(10):
        print(str(5*(i+1)))

#print("test 2")

def test(poke):
    print("You have encountered a wild pokemon!")
    print("A wild " + str(poke)  + " appeared")

#print("test 3")
def names(naam):
    print(naam + " :")
    for i in range(len(naam)):
        a = i + 1
        print(str(naam[i])*a)

#names("mies")

#print("Test 4");

def max_van_3(r, b, g):
    if (r > b):
        if (r > g):
            return r
    if (b > r):
        if (b > g):
            return b
    if (g > r):
        if (g > b):
            return g

#print(max_van_3(10, 11, 9))

#print("Test 5")
array = []
def tester101(mijmij):
    for i in range(len(mijmij)):
        i += 1
        p = i * -1
        array.append(mijmij[p])
        print(array)
    return array
#fullStr = ''.join(tester101("STEG"))
#print(fullStr)

#print("Test 6")

def is_priemgetal(getal):
        if (getal <= 3):
            print(getal)
            return "primus"
        for i in range(2,getal):
            if( (getal % i) == 0):
                print("WHAAAA")
                return "not optimus prime"
            else:
                return "Optimus Prime LOCATED"
        else:
            return "No Prime here"
#print(is_priemgetal(5))

print("Test 7")
    array = []
def tester404(mijmij):
    for i in range(len(mijmij)):
        i += 1
        p = i * -1
        array.append(mijmij[p])
        print(array)
    string = ''.join(array)
    if (string == mijmij):
        return array
    else :
        return "FALSE"
#fullStr = ''.join(tester404("tacocat"))
#print(fullStr)


