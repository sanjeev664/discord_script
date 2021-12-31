import requests
import pandas as pd

df=pd.read_csv('Token.csv')

for i in range(0,len(df['Channel_Id'])):
   
    def send_msg(channel_id, client_token, msg):
        payload = {'content': str(msg)}
        header = {'authorization': client_token}
        group_url = f'https://discord.com/api/v9/channels/{channel_id}/messages'
        resp = requests.post(group_url,data=payload, headers=header)
        if resp.status_code == 200:
            return True
        else:
            try:
                err = resp.json()
                return err['message']
            except:
                return False
    if __name__ == '__main__':
        send_msg(df['Channel_Id'][i],df['Client_Token'][i],df['Message'][i])