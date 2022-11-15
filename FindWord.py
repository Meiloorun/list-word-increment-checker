import sys

words = []
file = open(sys.argv[1], "r")
for x in file:
    words.append(x)

found = False

for word in words:
    seperatedWord = list(word)
    print(word)
    if (ord(seperatedWord[0]) + 14) > 90:
        seperatedWord[0] = chr((ord(seperatedWord[0]) + 14) - 26)
    else:
        seperatedWord[0] = chr(ord(seperatedWord[0]) + 14)

    if (ord(seperatedWord[1]) + 3) > 90:
        seperatedWord[1] = chr((ord(seperatedWord[1]) + 3) - 26)
    else:
        seperatedWord[1] = chr(ord(seperatedWord[1]) + 3)

    if (ord(seperatedWord[2]) + 3) > 90:
        seperatedWord[2] = chr((ord(seperatedWord[2]) + 3) - 26)
    else:
        seperatedWord[2] = chr(ord(seperatedWord[2]) + 3)

    if (ord(seperatedWord[3]) + 7) > 90:
        seperatedWord[3] = chr((ord(seperatedWord[3]) + 7) - 26)
    else:
        seperatedWord[3] = chr(ord(seperatedWord[3]) + 7)

    if (ord(seperatedWord[4]) - 18) < 65:
        seperatedWord[4] = chr((ord(seperatedWord[4]) - 18) + 26)
    else:
        seperatedWord[4] = chr(ord(seperatedWord[4]) - 18)

    if (ord(seperatedWord[5]) + 18) > 90:
        seperatedWord[5] = chr((ord(seperatedWord[5]) + 18) - 26)
    else:
        seperatedWord[5] = chr(ord(seperatedWord[5]) + 18)

    if (ord(seperatedWord[6]) + 6) > 90:
        seperatedWord[6] = chr((ord(seperatedWord[6]) + 6) - 26)
    else:
        seperatedWord[6] = chr(ord(seperatedWord[6]) + 6)

    if (ord(seperatedWord[7]) - 2) < 65:
        seperatedWord[7] = chr((ord(seperatedWord[7]) - 2) + 26)
    else:
        seperatedWord[7] = chr(ord(seperatedWord[7]) - 2)

    if (ord(seperatedWord[8]) + 16) > 90:
        seperatedWord[8] = chr((ord(seperatedWord[8]) + 16) - 26)
    else:
        seperatedWord[8] = chr(ord(seperatedWord[8]) + 16)

    if (ord(seperatedWord[9]) + 7) > 90:
        seperatedWord[9] = chr((ord(seperatedWord[9]) + 7) - 26)
    else:
        seperatedWord[9] = chr(ord(seperatedWord[9]) + 7)

    newWord = ''.join(seperatedWord)
    print(newWord)

    if newWord in words:
        found = True
        print("Found")
        print(word + '' + newWord)
        break
    else:
        found = False

if found == False:
    print("Not Found")