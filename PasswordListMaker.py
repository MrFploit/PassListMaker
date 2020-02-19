# Password List Maker 1.0
# Code By it4min
# t.me/LinuxArmy
import os

data_list = []
word_list = []
characters = []

def add(word, met):
    if word == 's':
        pass
    elif word == 'S':
        pass
    else:
        if met == 'data':
            data_list.append(word)
        elif met == 'word':
            word_list.append(word)
        elif met == 'characters':
            characters.append(word)

def get_data():
    print ("\033[1;35m  For Skip Enter The s/S \033[1;m"+'\n')
    add(input("\033[1;32m>>> Fist Name : "), 'data')
    add(input(">>> Last Name : "), 'data')
    add(input(">>> Age : "), 'data')
    job = input(">>> Job Nane : ")
    if len(job) == 6:
        add(job, 'word')
        add(job, 'data')
    elif len(job) > 6:
        add(job, 'word')
        add(job, 'data')
    else:
        add(job, 'data')
    birthday = input(">>> Birthday (zzzz/yy/xx) : ")
    if birthday == 's':
        pass
    elif birthday == 'S':
        pass
    else:
        if '/' in birthday:
            birthday_s = birthday.split("/")
            if len(birthday_s) == 3:
                add(birthday_s[0]+birthday_s[0], 'word')
                add(birthday_s[2], 'data')
            else:
                pass
        else:
            pass
    while True:
        x = input(">>> Phone Number (Enter Phone Number, n/N): ")
        if x == 'n':
            break
        elif x == 'N':
            break
        else:
            if len(x) == 6:
                add(x, 'word')
                add(x, 'data')
            elif len(x) > 6:
                add(x, 'word')
                add(x, 'data')
            elif len(x) < 6:
                add(x, 'data')
    while True:
        x = input(">>> Other Words (Enter other words, n/N): ")
        if x == 'n':
            break
        elif x == 'N':
            break
        else:
            if len(x) == 6:
                add(x, 'word')
                add(x, 'data')
            elif len(x) > 6:
                add(x, 'word')
                add(x, 'data')
            elif len(x) < 6:
                add(x, 'data')
    while True:
        x = input("Add more characters(Enter Caracters, n/N): ")
        if x == 'n':
            break
        elif x == 'N':
            break
        else:
            add(x, 'characters')

banner = '''
\033[1;31m

  _____                _      _     _   
 |  __ \              | |    (_)   | |  
 | |__) |_ _ ___ ___  | |     _ ___| |_ 
 |  ___/ _` / __/ __| | |    | / __| __|
 | |  | (_| \__ \__ \ | |____| \__ \ |_ 
 |_|   \__,_|___/___/ |______|_|___/\__|
         __  __       _                   t.me/LinuxH
        |  \/  |     | |                  ----------------
        | \  / | __ _| | _____ _ __       Code By it4min
        | |\/| |/ _` | |/ / _ \ '__|    
        | |  | | (_| |   <  __/ |       
        |_|  |_|\__,_|_|\_\___|_|      
        \033[1;m
              
\033[92m https://github.com/it4min/passlistmaker \033[92m
 
          \033[1;33m           Tool Name: Password List Maker.
                     To move to the next step in this tool,
                     you need to press N/n and then enter ! \033[1;33m
                     
'''

def generat_save():
    f = open('Password-List.txt', 'a')
    for wr in word_list:
        f.write(wr+'\n')
    for da1 in data_list:
        for da2 in data_list:
            for chra in characters:
                f.write(da1+da2+'\n')
                f.write(da1+chra+da2+'\n')
    f.close()
    print()
    print ("\033[1;31mPassword List Maked in 'Password-List.txt' \033[1;31m"+'\n')

if __name__ == '__main__':
    os.system('clear')
    print (banner)
    get_data()
    generat_save()
