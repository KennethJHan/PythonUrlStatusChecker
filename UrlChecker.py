#!/usr/bin/python3

import urllib.request

url = input("Enter URL: ")

try:
    res = urllib.request.urlopen(url)
    print(res.status)
except:
    print("Error")



## USAGE
# Enter Address and Check URL is valid or invalid.

#Example1: Valid Address (https://www.google.com)
#Enter URL: https://www.google.com
#200

#Example2: Invalid Address (https://example.not.working.address....)
#Enter URL: https://example.not.working.address....
#Error
