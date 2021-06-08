#!/usr/bin/env python3

from secrets import choice

from Vocabulary import vocabulary

level = 1

def testVocabWords(amount):
    for i in range(0, amount):
        word = choice(vocabulary)
        testVocabWord(word)

def testVocabWord(word):
    print(word['word'], end='')
    input('')
    if 'reading' in word:
        print(word['reading'], end='')
        input('')
    if 'type' in word:
        print(word['definition'] + ' (' +  word['type'] + ')', end='')
    else:
        print(word['definition'], end='')
    input('')
    if 'related' in word:
        for related in word['related']:
            print('TODO: ' + related)

if level == 1:
    testVocabWords(10)
else:
    print('Not Ready')
