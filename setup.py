import configparser
import os

cfg_file = "config.ini"
usrs_file = "users.ini"


def ask_y(text): # Simple 'yes' question
    ans = input(text)
    if ( ans == 'y' ) or ( ans == 'yes' ):
        return True
    else:
        return False

def main():
    
    # CONFIG
    
    # Check if config file exists
    if os.path.isfile(cfg_file):
        # Have users? list users, else make user
        users = configparser.RawConfigParser()
        users.read(cfg_file)
    else: # if config not found, ask to create it
        if not ( ask_y("Config file not found. Create new? ") ):
            exit("Bye!")
        config_setup() # New conig file setup

    # USERS
    
    # Check if users file exists
    if os.path.isfile(usrs_file):
        users = configparser.RawConfigParser()
        users.read(usrs_file)
        # If there are users, list them
        if users.sections():
            print("ID\tUsername")
            [ print(user+"\t"+users.get(user, 'username')) for user in users.sections() ]
            if ask_y("Add new?"):
                add_user(users)
        else: # If none found, ask to add
            if ask_y("No users found in file. Add new?"):
                add_user(users)
            else:
                exit()
    else: # IF no users file found
        print("No users found file. Please add user..")
        add_user(users)

# Add new user to usrs_file
def add_user(users):
    user_id = len(users.sections()) + 1
    username = input("Username: ")
    email = input("Email: ")
    lang = input("Language: ")
    step = input("Words per day: ")
    users.add_section(user_id)
    users.set(user_id, 'username', username)
    users.set(user_id, 'email', email)
    users.set(user_id, 'lang', lang)
    users.set(user_id, 'step', step)
    users.set(user_id, 'cursor', '0')
    with open(usrs_file, 'w+') as f:
        users.write(f)
        

def config_setup():
    config = configparser.RawConfigParser()
    print("Setup mailgun and mail")
    config.add_section('mailgun')
    config.set('mailgun', 'api_key', input("mailgun API key: ") )
    config.set('mailgun', 'from_mail', input("From mail 'name <email>': ") )
    config.set('mailgun', 'subject', input("Mail subject: ") )
    print("Setup yandex dictionary")
    config.add_section('yandex')
    config.set('yandex', 'url', 'https://dictionary.yandex.net/api/v1/dicservice.json/lookup?key={}&lang={}&text={}' )
    config.set('yandex', 'api_key', input("Yandex API key: ") )
    with open(cfg_file, 'w+') as f:
        config.write(f)
        print("Config file created.")
        

"""
try:
    with open(cfg_file) as f:
        configparser.RawConfigParser()
        
except:
    print("not found")  
"""

if __name__ == "__main__":
    main()
