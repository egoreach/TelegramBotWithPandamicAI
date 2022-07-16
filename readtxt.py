from random import choice
# file  = open('Inf.txt','r',encoding='utf-8')
# print(file.read().split('/n'))


def filer():
    with open(r"Inf.txt", "r", encoding='utf-8') as fin:
        result = (fin.read()).split('\n')
    return result


def arbitrary():
    return choice(filer())