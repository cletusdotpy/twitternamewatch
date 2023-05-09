# Script to secure my namesake (@cletus) on Twitter
# This shit cost me $80... better get it.

bearertoke = "ENTER_YOURS"
user_id = "ENTER_YOURS"

import requests
import json
import time
import sys
import winsound

run = True

while run:
    url = f'https://api.twitter.com/2/users/by?usernames={user_id}&user.fields=created_at'
    headers = {
        'Authorization': f'Bearer {bearertoke}'
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("BAD RESPONSE GO GET EM TIGER")
        frequency = 1000
        duration = 5000
        winsound.Beep(frequency, duration)
        run = False
        break

    user_data = json.loads(response.text)['data'][0]
    created_at = user_data['created_at']

    print('\n'+created_at)
    for remaining in range(60, 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write("{:2d} seconds remaining.".format(remaining))
        sys.stdout.flush()
        time.sleep(1)
