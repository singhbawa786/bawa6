#!/bin/sh

clear
echo ""
 echo"\033[31m  ____  "\033[31m                   
echo"\033[31m |  _ \                    
 echo"\033[31m| |_) | __ ___      ____ _ "\033[31m
echo""\033[31m  |  _ < / _` \ \ /\ / / _` |"\033[31m
echo""\033[31m | |_) | (_| |\ V  V / (_| |"\033[31m
echo""\033[31m |____/ \__,_| \_/\_/ \__,_|"\033[31m
                            
                            

echo "####################################"
echo " Authoe : singhbawa786"
echo " Tool   : http-bawa-generator "
echo "####################################"
echo ""

echo -n "\033[0;36m[*] Target Url : "
read asu
if [ ! -z $asu ]
then
echo "[*] Scanning..."
nmap -p 80 -sV --script=http-sitemap-generator $asu
else
echo "\033[31m[+] please Enter url :{! "
fi

