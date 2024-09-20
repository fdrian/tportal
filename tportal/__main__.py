#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""cservant.py: OSINT - This is a simple Python script to search payment of civil servant."""

__author__      = "Drian"
__copyright__   = "Copyright 2024"
__license__ = "GPL"
__version__ = "3.0"

import os
import datetime
import requests
from argparse import ArgumentParser


class color:
    FAIL = '\033[91m'
    BLUE = '\033[94m'
    GREEN = '\033[1;32m'
    INFO = '\033[93m'
    ENDC = '\033[0m'

orgs = {
    "SEFAZ": "7",
    "SEAD": "13",
    "PC": "23",
    "SSP": "45",
    "UEA": "120",
    "SEAP": "128",
    "ADAF": "158",
    "ADS": "117",
    "DETRAN": "63",
    "CBMAM": "91"
}

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
    url = "https://www.transparencia.am.gov.br/arquivos/"
    ext = ".pdf"
    link = url + uri + ext
    print("\n [d] " + color.BLUE + "Downloading... " + color.ENDC + uri + ext)

    # Create the necessary directory structure
    file_path = 'files/' + uri + ext
    directory = os.path.dirname(file_path)
    
    if not os.path.exists(directory):
        os.makedirs(directory)

    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:130.0) Gecko/20100101 Firefox/130.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br, zstd',
            'DNT': '1',
            'Sec-GPC': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache'
        }
        r = requests.get(link, headers=headers)

        if r.status_code == 200:
            with open(file_path, 'wb') as f:
                f.write(r.content)
            print("\n [s] " + color.GREEN + "Success..." + color.ENDC)
            return True
        else:
            print("\n [e] " + color.FAIL + f"Failed to download. Status code: {r.status_code}" + color.ENDC)
            return None

    except Exception as e:
        print("\n [e] " + color.FAIL + f"An error occurred: {e}" + color.ENDC)
        return None

def search(org, dt):
    # UPPER Strings
    org = str.upper(org)

    if org in orgs:
        year, month = map(int, dt.split('-'))

        if 2013 < year < 2026:
            dt = datetime.date(year, month, 1)
            date = dt.strftime("_%Y%m")
            uri = str(dt.year) + '/' + orgs[org] + date

            if download(uri):
                print("\nSaved in files/" + uri + ".pdf")
            else:
                print("\n [e] " + color.FAIL + "Unknown error..." + color.ENDC)

        else:
            print("\n [e] " + color.FAIL + "Invalid year..." + color.ENDC)
            print("Check the year entered. Value must be between 2014 and 2025")
    else:
        print("\n [e] " + color.FAIL + "Org not found in our database..." + color.ENDC)

def main():
    # Get arguments
    argp = ArgumentParser(description="OSINT - This is a simple Python script to search payment of civil servant.",
                          usage="python main.py [-o ORG] [-d DATE]")
    argp.add_argument('-v', '--version', dest='version', action="store_true", help='Version')
    argp.add_argument('-o', '--org', dest='org', required=False, help='Org to search')
    argp.add_argument('-d', '--date', dest='date', required=False, help='Date to search')
    args = argp.parse_args()

    if args.version:
        print(SAMPLES)
    elif args.org and args.date:
        print("\n [i] " + color.INFO + "Checking..." + color.ENDC)
        search(args.org, args.date)
    else:
        print(SAMPLES)
        print("List of Orgs available...")
        list_of_orgs = str(list(orgs.keys()))
        print(list_of_orgs.replace("'", "", 100))
        print("\n")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
