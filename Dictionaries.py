lijst = {"Douwe" : "Wooloo", "Karsten": "Magikarp"}
nummer = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}
dic4 = {}

print(lijst)
lijst["Test"] = "Test"
print(lijst)
del lijst["Douwe"]
print(lijst)

for key in lijst:
    lijst[key] = "bisharp"
    print (lijst[key])
print(lijst)

while "Mimikyu" not in lijst :
    print("pika")
    print(lijst)
    lijst["Mimikyu"] = "not pika"
    print(lijst)

print("xxxxxxxxxxx")
print("test 1")
for key in lijst:
    print(key)

print("test 2")
if "Mimikyu" in lijst:
    print("you have encountered a wild pokemon")
    print("A wild " + key + " appeared")

print("test 3")
print(dic1)
print(dic2)
print(dic3)
print(dic4)
for key in dic1:
    dic4[key] = dic1[key]
for  key in dic2:
    dic4[key] = dic2[key]
for key in dic3:
    dic4[key] = dic3[key]
print(dic4)
print(dic1)
print(dic2)
print(dic3)

print("test 4")
for key in nummer:
    nummer[key] = key*key

print(nummer)



