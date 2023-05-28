import random
def ua():
    data = open('ua.txt', 'r', encoding='utf-8').readlines()

    a = random.choice(data)
    return a