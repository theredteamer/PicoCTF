#!/bin/env python3

import ast

def extract(raw_list):
    flag = ''
    for item in raw_list:
        for string in item:
            if isinstance(string, str):
                flag += chr(int(string, 16))
    
    return flag

def main():
    f = open('scrambled_flag.txt', 'r')
    data = f.read().strip()
    
    raw_list = ast.literal_eval(data)

    flag = extract(raw_list)
    print(flag)
    
if __name__ == '__main__':
    main()
