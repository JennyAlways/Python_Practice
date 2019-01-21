#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-key = 3

key = 3

#加密
def encrypt(message):
    letterList = list(message)                         
    encryptList = []                                           
    for i in range(len(letterList)):
        acsNum = ord (letterList[i])                          
        acsNum  = acsNum + key                         
        encryptList.append(chr (acsNum))               
        encryptMessage = "".join (encryptList)
    return encryptMessage

#解密
def decrypt(encryptedMessage):
    letterList = list(encryptedMessage)
    decryptList = []
    for i in range(len(letterList)):
        acsNum = ord (letterList[i])                          
        acsNum  = acsNum - key                         
        decryptList.append(chr (acsNum))
        decryptMessage = "".join (decryptList)
    return decryptMessage

temp1 = encrypt("helloworld")
print temp1

temp2 = decrypt(temp1)
print temp2
