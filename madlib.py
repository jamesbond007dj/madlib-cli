import sys
import re
s = f"""
{'*'*35}
{'*'*2} \U0001f600"Welcome to MADLIB GAME!!!"\U0001f600"{'*'*2}
{'*'*2} \U0001F923"  Are you ready for FUN? "\U0001F923"{'*'*2}
{'*'*2}To quit at any time, type"quit""\U0001F612"
{'*'*35}

{'*'*35}
{'*'*2} If you ready ROCK N ROLL  \U0001F644   {'*'*2}
{'*'*2} Please type your name & enter \U0001F929
{'*'*35}
"""
print(s)
x = input()
print('Hello, ' + x +'! Please press enter again.')

def read_file(path):
    string = []
    try:
        with open('./game.txt') as f:
            test = f.read()
            string.append(test)

    except FileNotFoundError as e:
        print('bunk')
        print(str(e))

    return string


def get_arr():
    string = read_file('game.txt')
    chars = str(string)
    rip = chars.replace('"', '').replace('{Adjective}', ' 2 ').replace('{A First Name}', ' 3').replace('{Past Tense Verb}', ' 4 ').replace('{Plural Noun}', ' 6 ').replace('{Small Animal}', ' 7 ').replace('{Large Animal}',' 8 ').replace('{Number}', ' 9 ').replace("{A Girl's Name}", ' & ' ).replace('{Number 1-50}', ' $ ').replace("{First Name's}", ' # ')
    regex = re.findall(r"[2346789&$#]" , rip)


# get_arr()

# def mad_libs()
#     for

# adj1 =



# lst = {

# }

# def exit_app():
#     print('adios!!! See U soon''\U0001F62A')
#     sys.exit()

def exit_app():
    print('adios')
    sys.exit()


while True:
    answer = input ('')
    if answer == 'quit':
        exit_app()
    else:
        inputs = []
        inputs.append(str(input(x+' enter an adjective: ')))
        inputs.append(str(input('enter another adjective: ')))
        inputs.append(str(input('enter a first name: ')))
        inputs.append(str(input('enter a past tense verb: ')))
        inputs.append(str(input('enter a first name: ')))
        inputs.append(str(input('enter adjective: ')))
        inputs.append(str(input('enter adjective: ')))
        inputs.append(str(input('enter plural noun: ')))
        inputs.append(str(input('enter name of a small animal: ')))
        inputs.append(str(input('enter name of alarge animal: ')))
        inputs.append(str(input('enter a womans name: ')))
        inputs.append(str(input('enter adjective: ')))
        inputs.append(str(input('enter plural noun: ')))
        inputs.append(str(input('enter adjective: ')))
        inputs.append(str(input('enter plural noun: ')))
        inputs.append(str(input('enter a number 1 - 50: ')))
        inputs.append(str(input('enter a first name: ')))
        inputs.append(str(input('enter a number: ')))
        inputs.append(str(input('enter a plural noun: ')))
        inputs.append(str(input('enter a number: ')))
        inputs.append(str(input('enter a plural noun: ')))


return inputs


