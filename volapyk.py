from random import choice, randint


introductions = [
    'Hahaha, ja lige nøjagtig!',
    'Nåh, ok.',
    'Ja, hér har du i hvert fald en respons:\n',
    'Nej, og lige til orientering:'
    ]

endings = [
    'ik\'?',
    'eller andre!?',
    'men som regel.',
    '...',
    'og sådan... - Tror du at der kan eksistere kærlighed mellem robot og menneske? Ja eller nej?'
    ]

fillers = [
    ', der',
    'er',
    'er. \n\nDerfor',
    ', som',
    'jeg',
    'du er. \n\nFor',
    'vi',
    ', den',
    'det. \n\nSåledes',
    'det',
    'at',
    'har. \n\nHer',
    ', for du',
    'i',
    'på',
    ', men', 
    'ikke',
    'man',
    'må',
    'fordi',
    ', derfor',
    ]

huge_list = []

with open('dicts.txt', 'r') as dicts:
    for word in dicts.read().splitlines():
        if word.endswith('sb'):
            new_word = word.replace("sb", "")
            huge_list.append(new_word)
        else:
            huge_list.append(word)

##print("\nthere are {0} words in huge_list\n".format(len(huge_list)))
    
def volapyk(constant=None):
    cool_list = []
    
    for i in range(constant):
        cool_list.append(choice(huge_list))

    number = 0
    
    while number <= len(cool_list):
        number = number + randint(1,3)
        if number < len(cool_list):
            cool_list[int(number)] = choice(fillers)
        else:
            break
        
    cool_string = ' '.join(cool_list)
    cool_string = cool_string.replace(' ,', ',')
    #return (cool_string)
    print(choice(introductions), cool_string.capitalize(), choice(endings))

##    sentence = choice(introductions), cool_string.capitalize(), choice(endings)
##    sentence = str(sentence)
##    print(sentence)
    
volapyk(36)
    












