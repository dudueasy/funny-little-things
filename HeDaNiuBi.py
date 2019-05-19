#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import time
import random

name=input("Do you think HeDa Niubi? Y/N \n")

for i in range(101):
    if name.lower()=='y': 
        s = "\r崇拜值提升中 {0}% {1}".format(i,'#'*i)    

        sys.stdout.write(s)
        sys.stdout.flush()           

        time.sleep(0.1)
    else: 
        s = "He Da Niubi"
        style = random.randint(0, 8)
        fg =  random.randint(30, 38)
        bg = random.randint(40,48)
        format = ';'.join([str(style), str(fg), str(bg)])
        s1 = "\r\x1b[{0}m {1} \x1b[0m".format (format, s) 

        sys.stdout.write(s1)
        sys.stdout.flush()           
        time.sleep(0.1)

if name.lower()=='y': 
    print("\nYes ! He Da IS Niu Bi!!")
elif name.lower()=='n': 
    s3 = '\x1b[5;{0};{1}m He Da Niu Bi Anyway! \x1b[0m'.format(
            random.randint(30,38), 
            random.randint(40,48),
            )  
    print("\n{0}".format(s3))




