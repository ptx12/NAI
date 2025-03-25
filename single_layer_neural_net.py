import re
from collections import Counter

zero_dict = {chr(i) : 0 for i in range(ord('a'),ord('z') + 1)}

def loadfile(filename : str) -> list:
    try:
        with open(filename, 'r',errors='ignore') as x:
            result = []

            for line in x.readlines():
                lang = line.split(',')[0]
                result.append([
                    lang, re.sub(r'[^a-zA-Z]', '', line[len(lang):].lower()) 
                ])
            return result
            
    except FileExistsError:
        print("file not found")

def process_language(input_string):
    for language in input_string:

        sorted_letters = sorted((zero_dict | dict(Counter(language[1]))).items())

        letter_vec = [x[1] for x in sorted_letters]
        print(len(letter_vec))

process_language(loadfile('lang.test.csv'))

        