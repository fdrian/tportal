#!/bin/python
# Adriano Freitas - adrianofreitas.me ® 2022

# OSINT - This is a simple Python script to search payment of civil servant.

import datetime
import requests
import pycurl

def get_info(uri):
    # exemplo URL - https://www.transparencia.am.gov.br/arquivos/2021/45_202101.pdf
    url = "https://www.transparencia.am.gov.br/arquivos/"
    ext = ".pdf"
    u = url + uri + ext
    r = requests.get(u)

    if r.status_code == 200:
        print(r.status_code)
        file = open('files/' + uri + ext, 'wb')
        c = pycurl.Curl()
        c.setopt(c.HTTPHEADER, ['User-Agent:Mozilla/5.0 (X11; Linux x86_64; rv:101.0) Gecko/20100101 Firefox/101.0'])
        c.setopt(c.URL, u)
        c.setopt(c.WRITEDATA, file)
        c.perform()
        c.close()
    else:
        print(r.status_code)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    orgs = {"SEFAZ": "7","SEAD": "13","SSP": "45","UEA": "120","SEAP": "128"}

    print(orgs)
    org = str.upper(input('Type org name. Ex: SEFAZ: '))

    if org in orgs:

        dt = input('Year(2015-2022) and month.Format YYYY-MM: ')
        year, month = map(int,dt.split('-'))

        if 2013 < year and year < 2023:
            dt = datetime.date(year, month, 1)
            date = dt.strftime("_%Y%m")
            uri = str(dt.year) + '/' + orgs[org] + date
            get_info(uri)

        else:
            print("Invalid year...")
    else:
        print("Invalid org...")
