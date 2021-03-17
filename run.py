import requests

def fetchData(channel='FotorTest', post='1', proxy=None):
    try:
        url = 'https://t.me/'+channel+'/'+post+'?embed=1'
        r = requests.get('https://ifconfig.me', proxies={'https':proxy}, verify=False)
        print(r.text)
        r = requests.post(url, timeout=20, proxies={'https':proxy}, verify=False)
        cookie = r.headers['set-cookie'].split(';')[0]
        key = r.text.split('data-view="')[1].split('"')[0]
        if 'stel_ssid' in cookie: 
            return {'key':key,'cookie':cookie}
        else:
            return False
    except Exception as e:
        return False
        
def addViewToPost(channel='FotorTest', post='1', key=None, cookie=None, proxy=None):
    try:
        r = requests.get('https://t.me/v/?views='+key, verify=False,  timeout=20, headers={
        'x-requested-with':'XMLHttpRequest',
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
        'referer':'https://t.me/'+channel+'/'+post+'?embed=1',
        'cookie':cookie}, proxies={'https':proxy}
        )
        return r.text
    except Exception as e:
        return False
        
def run(channel, post, proxy):
    s = fetchData(channel, post, 'socks5://'+proxy)
    if (type(s) is dict):
        l = addViewToPost(channel, post, s['key'], s['cookie'], 'socks5://'+proxy)
        if l != False: print('Proxy '+proxy+' finished its job successfully!')
    print('Thread with proxy '+proxy+' has been terminated.')

run('FotorTest', '3', '184.178.172.5:15303') 