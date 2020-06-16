#!/usr/bin/env python
import sys
import argparse
import boto3
import urllib.request, urllib.error, urllib.parse
import time
from datetime import datetime
import socket

def get_public_dns_hostname():
    # curl http://169.254.169.254/latest/meta-data/public-hostname
    response = urllib.request.urlopen('http://169.254.169.254/latest/meta-data/public-hostname')
    public_dns = response.read()
    return public_dns

def get_private_ip():
    # curl http://169.254.169.254/latest/meta-data/local-ipv4
    response = urllib.request.urlopen('http://169.254.169.254/latest/meta-data/local-ipv4')
    private_ip = response.read()
    return private_ip

def get_all_metadata_id():
    # curl http://169.254.169.254/latest/meta-data/local-ipv4
    response = urllib.request.urlopen('http://169.254.169.254/latest/meta-data')
    all_metadata_id = response.read()
    return all_metadata_id

def main():
    # get_all_metadata_id() : To get all possible metadata_id's can append values at end of /latest/meta-data/<>

    private_ip = get_private_ip()
    public_dns = get_public_dns_hostname()
    print (private_ip)
    print (public_dns)

if __name__ == '__main__':
    sys.exit(main())