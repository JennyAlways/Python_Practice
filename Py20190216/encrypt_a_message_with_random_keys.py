#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-key = 3

def encrypt(message):
    letterList = list(message)                         
    encryptList = []                                           
    for i in range(len(letterList)):
        acsNum = ord (letterList[i])                          
        acsNum  = acsNum + key                         
        encryptList.append(chr (acsNum))               
        encryptMessage = "".join (encryptList)
    return encryptMessage
