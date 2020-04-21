import requests
import time
saveFile = 'game.sav'

while(True):
    try:
        res = requests.get('http://httpbin.org/status/200')
        statusCodeBytes = bytes([int(res.status_code)])

        with open(saveFile, 'r+b') as f:
            offset = int('FF', base=16)
            f.seek(offset)
            f.write(statusCodeBytes)
    except:
        print('Waiting for Save...')

    time.sleep(1)
