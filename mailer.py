import requests


class Mailer(object):

    # Get mailgun config from file
    def __init__(self, cfg_file):
        import configparser
        cfg = configparser.RawConfigParser()
        cfg.read(cfg_file)
        mg = "mailgun" #section name
        self.api_key = cfg.get(mg, 'api_key')
        self.mg_from = cfg.get(mg, 'from_mail')
        self.mg_sub = cfg.get(mg, 'subject')

    # Send message
    def send_message(self, to, body):
        return requests.post(
            "https://api.mailgun.net/v3/kotek.co/messages",
            auth=("api", self.api_key),
            data={
                "from": self.mg_from,
                "to": to,
                "subject": self.mg_sub,
                "html": body})

if __name__ == "__main__":
    m = Mailer("config.ini")
    print(m.send_message(["kotek.vojtech@gmail.com"],"Hello. this is a test"))
