#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import time
import random


s3 = None 
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
        s3 = s1

        sys.stdout.write(s1)
        sys.stdout.flush()           
        time.sleep(0.1)

if name.lower()=='y': 
    print("\nYes ! He Da Nu Bi!!")
elif name.lower()=='n': 
    print("\nHe Da Nu Bi anyway")

