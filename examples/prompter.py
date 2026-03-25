"""Japanese from the CJK examples."""

import sys
sys.path.append('./')

import pytoklib

if __name__ == '__main__':
    print("prompter.py <lang> <instructions>")
    
    with open(sys.argv[1]) as f: 
        s = f.read()
        s = s[s.find('---'):]
        res = pytoklib.ntoken.ntoken(s, pytoklib.sa1)
        for vi in res:
            print(vi[0])
            print(vi[1])
        
        with open(sys.argv[2]) as f2:
            prompt = f2.read()
            final = res
            final += prompt
            print(final)
            with open("output.txt", "w") as f3:
                f3.write(str(final))