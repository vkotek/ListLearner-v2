# -*- coding: utf-8 -*-

# FOR EACH USER GET WORDS, GET DEFS, EMAIL IT

import configparser
import mailer


users_file = 'users.ini'
users = configparser.RawConfigParser()
users.read(users_file)

# FOR EACH USER
for user in users.sections():

    # GET USER CONFIG
    username = users.get(user, 'username')
    email = users.get(user, 'email')
    lang = users.get(user, 'lang')
    step = users.get(user, 'step')
    cursor = users.get(user, 'cursor')
    

    # GET WORDS
    

    # GET DEFINITIONS

    # EMAIL IT
