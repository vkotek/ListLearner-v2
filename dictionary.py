import configparser, json, urllib.request, urllib.parse, sys


class dct(object):

    def __init__(self, cfg_file):
        self.config = configparser.RawConfigParser()
        self.config.read(cfg_file)
        self.cfg_url = self.config.get('yandex','url')
        self.cfg_key = self.config.get('yandex','key')

    def get(self, word, lang):
        url = self.cfg_url.format(self.cfg_key, lang, word)
        url = urllib.parse.quote(url, safe=':/?&=')
        
        try:
            with urllib.request.urlopen(url) as data:
                data = json.loads(data.read().decode('utf8'))
                data = data['def']
            return data     
        except:
            e = sys.exc_info()
            error = "Error getting definition. Sorry.\n\n%s\n\n%s" % (url,e)