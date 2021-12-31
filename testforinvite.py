import json
import time
import requests
import traceback
import random




invite_code = 'PKD8KCyD'
tokens = ['ODUzNTA1MDAxNjQ4Njg1MDc3.Yadrgw.JuTBWB_jxIvuEPzphT-HA5OZzlc']


def join_guild_invite(user_token, invite_code):
    join_url = f"https://discord.com/api/v9/invites/{invite_code}"
    header = {'authorization': user_token}
    resp = requests.post(join_url, headers=header)
    print(join_url)
    if resp.status_code == 200:
        return True
    else:
        return False

for token in tokens:
    print(join_guild_invite(token, invite_code))
    time.sleep(random.randrange(4,20))