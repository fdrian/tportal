# Transparency Portal

## OSINT - This is a simple Python script to search payment of civil servant on Transparency Portal.


<p align="center">
  <a href="#installation">Installation</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#usage">Usage</a> 
</p>

## Installation

```console
# clone the repo
$ git clone https://github.com/adrian-ofreitas/tportal.git

# change the working directory to tportal
$ cd tportal/

# install the requirements
$ python3 -m pip install -r requirements.txt
```

## Usage

```console
$ python3 tportal --help
usage: python main.py [-o ORG] [-d DATE]

OSINT - This is a simple Python script to search payment of civil servant.

options:
  -h, --help            show this help message and exit
  -v, --version         Version
  -o ORG, --org ORG     Org to search
  -d DATE, --date DATE  Date to search
```

To search file with payments of June:
```
python3 tportal --org UEA --date 2022-06
```
