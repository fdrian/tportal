#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""cservant.py: OSINT - This is a simple Python script to search payment of civil servant."""

__author__      = "Adriano Freitas"
__copyright__   = "Copyright 2022, Night City"
__license__ = "GPL"
__version__ = "3.0"

import os
import commands
import datetime
import requests
import pycurl
from argparse import ArgumentParser

class color:
    FAIL = '\033[91m'
    BLUE = '\033[94m'
    BLUE2 = '\033[1;36m'
    INFO = '\033[93m'
    ENDC = '\033[0m'
    GREEN = '\033[1;32m'

VERSION = "1.0"
SAMPLES = """
[OSINT] Search Civil Servant Payments v1.0

This is a simple Python script to search payment of civil servant.

Type python main.py --help to show help

Command line examples:      
    python main.py [-o ORG] [-d DATE]
    python main.py -o <ORG> -d <YYYY-MM>
    python main.py --org SEFAZ --date 2021-01

    """

def download(uri):
    # exemplo URL - https://www.transparencia.am.gov.br/arquivos/2021/45_202101.pdf
    url = "https://www.transparencia.am.gov.br/arquivos/"
    ext = ".pdf"
    u = url + uri + ext
    r = requests.get(u)

    if r.status_code == 200:
        print("\n [d] " + color.BLUE + "Downloading..." + color.ENDC )        
        file = open('files/' + uri + ext, 'wb')        
        c = pycurl.Curl()
        c.setopt(c.HTTPHEADER, ['User-Agent:Mozilla/5.0 (X11; Linux x86_64; rv:101.0) Gecko/20100101 Firefox/101.0'])        
        c.setopt(c.URL, u)
        c.setopt(c.WRITEDATA, file)
        c.perform()
        c.close()
        
        if os.path.exists("files/" + uri + ext):
            print("\n [s] " + color.GREEN + "Success..." + color.ENDC) 
            return True
        else:
            return False
    
        
def search(org,dt):
    orgs = {"SEFAZ": "7","SEAD": "13","SSP": "45","UEA": "120","SEAP": "128"}   

    # UPPER Strings
    org = str.upper(org)

    if org in orgs:       
        year, month = map(int,dt.split('-'))

        if 2013 < year and year < 2023:
            dt = datetime.date(year, month, 1)
            date = dt.strftime("_%Y%m")
            uri = str(dt.year) + '/' + orgs[org] + date           
                        
            if download(uri):                
                print("\nSaved in files/" + uri + ".pdf")
            else:
                print("\n [e] " + color.FAIL + "Unknown error..." + color.ENDC )                

        else:
            print("\n [e] " + color.FAIL + "Invalid year..." + color.ENDC )            
            print("check the year entered. Value must be between 2014 and 2022")
    else:        
        print("\n [e] " + color.FAIL + "Org not found in our database..." + color.ENDC )

def main():  
    # Get arguments
    argp = ArgumentParser()
    argp = ArgumentParser(description="OSINT - This is a simple Python script to search payment of civil servant.", 
                          usage="./main.py [options] [-d YYYY-MM]")    
    argp.add_argument('-v', '--version', dest='version', action="store_true", help='Version')    
    argp.add_argument('-o', '--org', dest='org', required=False, help='Org to search')
    argp.add_argument('-d', '--date', dest='date',required=False, help='Date to search')    
    args = argp.parse_args()
    #print(vars(args))
    
    if args.version:
        print(SAMPLES)
    elif args.org and args.date:
        print("\n [i] " + color.INFO + "Checking..." + color.ENDC)
        search(args.org, args.date)
    else:        
        print(SAMPLES)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

    
