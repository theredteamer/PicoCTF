#!/bin/env python3

flag = ''
with  open ('enc', 'r') as f:
    encoded_char = f.read()
    
    for char in encoded_char:
        unicode_16 = ord(char)
        
        first_8bit = unicode_16 >> 8
        second_8bit = unicode_16 & 0xff
        
        first_char = chr(first_8bit)
        second_char = chr(second_8bit)
        
        flag += first_char
        flag += second_char
    
    print(flag)
    
