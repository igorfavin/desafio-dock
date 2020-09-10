#!/usr/bin/env python3
#Coleta_Torlist
#Author: Igor Stinieski Favin
#Email: igorstinieskifavin@gmail.com
#Goal: Collect the IPs from the torlist and save it in a file
#08/09/2020

from requests import get
from time import strftime
from subprocess import call

r = get("https://www.dan.me.uk/torlist/?exit")

timestr = strftime("%d-%m-%Y-%H-%M-%S")

call(['mkdir ./torlist'], shell=True)

arquivo = open("./torlist/Lista_ips_"+timestr+".txt","w")
arquivo.write(r.text)
arquivo.close()

call(['aws s3 cp ./torlist/* s3://aws-desafio-dock'], shell=True)
call(['rm -rf ./torlist/*'], shell=True)
