# -*- coding: utf-8 -*-

import random
def encrypt(*messageTuple):
    keyDict = {}
    encryptMessageList = []
    for message in messageTuple:
        keyList = []
        letterList = list(message)                         
        encryptList = []                                           
        for i in range(len(letterList)):
            acsNum = ord (letterList[i])
            key =random.randint(0,9)
            keyList.append(str(key))
            acsNum  = acsNum + key
            encryptList.append(chr (acsNum))               
        encryptMessage = "".join (encryptList)
        encryptMessageList.append(encryptMessage)
        keyDict[encryptMessage] = "".join(keyList)
    
    FILENAME = "key.txt"
    keyFile = open(FILENAME, "a")
    for key in keyDict.keys():
        keyFile.write(key+":"+keyDict[key]+"\n")
    keyFile.close()
    return encryptMessageList

result = encrypt("abc","cde","efg")
print result

def decrypt(encryptMessageTurple):
    rList = []
    keyList = []
    keyDict = {}
    FILENAME = "key.txt"
    keyFile = open(FILENAME, "r")
    keyData = keyFile.readlines()
    keyFile.close()
    for keyLine in keyData:
        keyList.append(keyLine.strip().split(":"))
    for key in keyList:
        keyDict[key[0]] = key[1]
    print keyDict

    for eMessage in encryptMessageTurple:
        letterList = list(eMessage)
        keyList = keyDict[eMessage]
        decryptList = []
        print eMessage
        for i in range(len(letterList)):
            key=keyList[i]
            acsNum = ord (letterList[i])
            acsNum = acsNum - int(key)
            decryptList.append(chr (acsNum))
        decryptMessage = "".join (decryptList)
        rList.append(encryptMessageTurple)       
    return rList
    
decrypt(result)
