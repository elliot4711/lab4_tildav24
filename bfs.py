from bintreeFile import Bintree
svenska = Bintree()

with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()
        svenska.put(ordet)      

startord = input("Skriv in ditt startord: ")
slutord = input("Skriv in ditt slutord: ")

gamla = Bintree()

alphabet = ["a", "b", "c", "d", "e","f","g","h","i","j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v","w","x","y","z", "å","ä", "ö"]

def makechildren(startord):
    gamla.put(startord)
    original = startord
    ord = list(original)
    for i in range(len(startord)):
        startord = list(original)
        for j in range(len(alphabet)):
            startord[i] = alphabet[j]
            ord1 = startord[0] + startord[1] + startord[2]
            #print(ord1)
            if ord1 in svenska:
                if ord1 not in gamla: 
                    print(ord1)
                    gamla.put(ord1)

makechildren(startord)