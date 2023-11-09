import requests

url = 'https://github.com/upx/upx/releases/download/v4.2.1/upx-4.2.1-win64.zip'

r = requests.get(url, allow_redirects=True)

if r.ok:
    print('requests ok')

    with open('upx-4.2.1-win64.zip', 'wb') as f:
        f.write(r.content)
        f.close()
    
    print('download ok')
else:
    print("requests error")
