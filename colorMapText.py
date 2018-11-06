# -*- coding:utf-8 -*-
'''
Created on 2018��10��11��
This program is used to convert color text to '' form and numbered
@author: Jingyuan Liu
'''

colorMap = []
with open('numSeqColorMap.txt', 'a') as fileWrite:
    with open('colorMap.txt', 'r') as filein:
        num = 0
        for line in filein:
            num += 1
            print("'"+line.rstrip('\n')+"',")
            colorMap.append("'"+line.rstrip('\n')+"',")
            fileWrite.write("'"+line.rstrip('\n')+"',")
        print(str(num))
        fileWrite.write('\n'+str(num)+'\n\n')
    fileWrite.close()
    
with open('numSeqColorMap.txt', 'a') as fileWrite:
    numSeq = -1
    for i in range(39):
        for j in range(4):
            numSeq += 1
            print(str(numSeq+1)+'['+str(i)+']'+'['+str(j)+'] '+ colorMap[numSeq])
            fileWrite.write(str(numSeq+1)+'['+str(i)+']'+'['+str(j)+'] '+ colorMap[numSeq] +'\n')
    fileWrite.write('\n')
    fileWrite.close()   

with open('numSeqColorMap.txt', 'a') as fileWrite:
    numS = -1
    for i in range(39):
        for j in range(4):
            numS += 1
            print('['+str(i)+']'+'['+str(j)+'] '+ colorMap[numS])
            fileWrite.write('['+str(i)+']'+'['+str(j)+'] '+ colorMap[numS])
        fileWrite.write('\n')
    fileWrite.close()         