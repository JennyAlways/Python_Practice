#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-key = 3

key=3


#加密
def encrypt(*messageTuple):
    mList = []
    for message in messageTuple:
        letterList = list(message)                         
        encryptList = []                                           
        for i in range(len(letterList)):
            acsNum = ord (letterList[i])                          
            acsNum  = acsNum + key                         
            encryptList.append(chr (acsNum))               
        encryptMessage = "".join (encryptList)
        mList.append(encryptMessage)
    return mList



#解密
def decrypt(encryptedMessage):
    rList = []
    for eMessage in encryptedMessage:
        letterList = list(eMessage)
        decryptList = []
        print eMessage
        for i in range(len(letterList)):
            acsNum = ord (letterList[i])                          
            acsNum  = acsNum - key                         
            decryptList.append(chr (acsNum))
        decryptMessage = "".join (decryptList)
        rList.append(decryptMessage)       
    return rList

temp1 = encrypt("abc","123","cyljn","ryycyr","sk")
print temp1

temp2 = decrypt(temp1)
print temp2
