#!/usr/bin/env python3
'''Validate emails'''
import argparse
from validate_email import validate_email

parser = argparse.ArgumentParser()
parser.add_argument('mail_to_check')
args = parser.parse_args()


if (args.mail_to_check):
    #if (validate_email(args.mail_to_check)): # Just a simple format test: something@something.something
    #if (validate_email(args.mail_to_check, check_mx=True)): # Test format and check for Mail eXchanger
    if (validate_email(args.mail_to_check, verify=True)): # Test as above, but test for user as well
        print(args.mail_to_check)
    else:
        print(" ")
else:
    print("No Address Supplied")
