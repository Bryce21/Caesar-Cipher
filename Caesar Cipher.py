
def checkInput(intInput):
    if(intInput < 0 or intInput >= 25):
        print("Invalid input!")
        
def fillArrayWithAlphabet():
    arrayOfAlphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
                       "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
                       "W", "X", "Y", "Z"]
    return arrayOfAlphabet

def makeModifiedAlphabet(change, arrayOfAlphabet):
    modifiedAlphabet = [0]*26
    count = 0
    for x in range(0, 26):
        w = x + change
        if(w > 25):
            w = count
            count += 1
        modifiedAlphabet[x] = arrayOfAlphabet[w]
    return modifiedAlphabet
 
def makeDictionary(modifiedAlphabet):
    dictionary = {
        'A' : modifiedAlphabet[0],
        'B' : modifiedAlphabet[1],
        'C' : modifiedAlphabet[2],
        'D' : modifiedAlphabet[3],
        "E" : modifiedAlphabet[4],
        "F" : modifiedAlphabet[5],
        "G" : modifiedAlphabet[6],
        "H" : modifiedAlphabet[7],
        "I" : modifiedAlphabet[8],
        "J" : modifiedAlphabet[9],
        "K" : modifiedAlphabet[10],
        "L" : modifiedAlphabet[11],
        "M" : modifiedAlphabet[12],
        "N" : modifiedAlphabet[13],
        "O" : modifiedAlphabet[14],
        "P" : modifiedAlphabet[15],
        "Q" : modifiedAlphabet[16],
        "R" : modifiedAlphabet[17],
        "S" : modifiedAlphabet[18],
        "T" : modifiedAlphabet[19],
        "U" : modifiedAlphabet[20],
        "V" : modifiedAlphabet[21],
        "W" : modifiedAlphabet[22],
        "X" : modifiedAlphabet[23],
        "Y" : modifiedAlphabet[24],
        "Z" : modifiedAlphabet[25]
    }
    return dictionary

def encode(message, dictionary):
    encodedMessage = ""
    for x in range(0, len(message)):
        encodedMessage += dictionary[message[x]]
    return encodedMessage

def decode(encodedMessage, dictionary):
    message = ""
    for x in range(0, len(encodedMessage)):
        m = list(dictionary.keys())[list(dictionary.values()).index(encodedMessage[x])]
        message += m
    return message


intInput = int(input("Integer i | (0 < i < 26): "))
message = input("Message to encode: ")
message = message.upper()
message = message.replace(" ","")
checkInput(intInput)
arrayOfAlphabet = fillArrayWithAlphabet()
modifiedAlphabet = makeModifiedAlphabet(intInput, arrayOfAlphabet)
makeDictionary
#print(modifiedAlphabet)
dictionary = makeDictionary(modifiedAlphabet)
encodedMessage = encode(message, dictionary)
print(encodedMessage)
decodedMessage = decode(encodedMessage, dictionary)
print(decodedMessage)








