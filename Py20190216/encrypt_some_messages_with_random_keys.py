#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-key = 3

import random

keyDict = {}

#加密
def encrypt(*messageTuple):
    global keyDict
    encryptMessageList = []
    for message in messageTuple:
        keyList = []
        letterList = list(message)                         
        encryptList = []                                           
        for i in range(len(letterList)):
            acsNum = ord (letterList[i])
            key =random.randint(1,20)
            keyList.append(key)
            acsNum  = acsNum + key
            encryptList.append(chr (acsNum))               
        encryptMessage = "".join (encryptList)
        encryptMessageList.append(encryptMessage)
        keyDict[encryptMessage] =keyList
    return encryptMessageList

#解密
def decrypt(encryptedMessage):
    rList = []
    for eMessage in encryptedMessage:
        letterList = list(eMessage)
        keyList = keyDict[eMessage]
        decryptList = []
        print eMessage
        for i in range(len(letterList)):
            key=keyList[i]
            acsNum = ord (letterList[i])                          
            acsNum  = acsNum - key                         
            decryptList.append(chr (acsNum))
        decryptMessage = "".join (decryptList)
        rList.append(decryptMessage)       
    return rList

temp1 = encrypt("abc","123")
print temp1
print keyDict


temp2 = decrypt(temp1)
print temp2
