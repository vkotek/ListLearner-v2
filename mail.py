api_key = "key-0500f40586ec016cbd2c131ea2222ae2"
d_from = "Admin <admin@kotek.co>"
d_to = ["kotek.vojtech@gmail.com"]
d_sub = "Hello"
d_txt = "Testing mailgun"

def send_message(to, body):
    import requests
    return requests.post(
        "https://api.mailgun.net/v3/kotek.co/messages",
        auth=("api", api_key),
        data={
            "from": d_from,
            "to": to,
            "subject": d_sub,
            "text": body})

print(send_message())
