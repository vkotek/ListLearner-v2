# -*- coding: utf-8 -*-

# FOR EACH USER GET WORDS, GET DEFS, EMAIL IT

import configparser
import mailer
import dictionary


users_file = 'users.ini'
users = configparser.RawConfigParser()
users.read(users_file)

# FOR EACH USER
for user in users.sections():

    # GET USER CONFIG
    username = users.get(user, 'username')
    email = users.get(user, 'email')
    lang = users.get(user, 'lang')
    step = int(users.get(user, 'step'))
    cursor = int(users.get(user, 'cursor'))
    

    # GET WORDS
    lang_file = lang + ".txt"
    with open(lang_file, 'r') as f:
        words = [line.rstrip('\n') for line in f]
        words = words[ cursor : cursor+step ]
        f.close()
    print(words)

    # GET DEFINITIONS
    d = dictionary.connect(lang)
    for word in words:
        df = d.get(word)
        body[word] = df
    
    print(body)
        
    

    # EMAIL IT
