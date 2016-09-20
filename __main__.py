# -*- coding: utf-8 -*-

# FOR EACH USER GET WORDS, GET DEFS, EMAIL IT

import configparser
import mailer
import dictionary

cfg_file = 'config.ini'

# Open users file with configparser
users_file = 'users.ini'
users = configparser.RawConfigParser()
users.read(users_file)

# Create mailer instance
m = mailer.Mailer(cfg_file)

# Create dictionary instance
d = dictionary.dct(cfg_file)


# FOR EACH USER
for user in users.sections():

    # GET USER CONFIG
    username = users.get(user, 'username')
    email = [users.get(user, 'email')]
    lang = users.get(user, 'lang')
    step = int(users.get(user, 'step'))
    cursor = int(users.get(user, 'cursor'))
    
    # Update cursor for user
    users.set(user, 'cursor', cursor + step )
    users.write(open(users_file, 'w+'))
    

    # GET WORDS
    lang_file = "lists/" + lang + ".txt"
    with open(lang_file, 'r') as f:
        words = [line.rstrip('\n') for line in f]
        words = words[ cursor : cursor+step ]
        f.close()
    print(words)

    # GET DEFINITIONS
    body = []
    for word in words:
        a = ""
        df = d.get(word ,lang + "-en")
        for f in df:
            for t in f['tr']:
                a += "<br><b>%s</b> - <i>%s</i><br>" % (t['text'],t['pos'])
                try:
                    if len(t['ex'])>0:
                        a += "<h5>EXAMPLES:</h5><ul>"
                    for ex in t['ex']:
                        a += "<li><b>%s</b>:  <i>%s</i></li>" % (ex['text'],ex['tr'][0]['text'])
                    a += "</ul>"
                except:
                    continue

        line = "<h2>%s</h2><br>%s<hr>" % (word,"".join(a))
        body.append(line)

    # Join all words and defs into mail body
    body = "".join(body)
    body += "<br><br><a href=\"https://tech.yandex.com/dictionary/\">Powered by Yandex.Dictionary</a>"

    
    print(body)

    # EMAIL IT
    m.send_message(email, str(body))
   
