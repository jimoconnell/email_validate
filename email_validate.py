#!/usr/bin/env python3
'''Validate emails'''
# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import argparse
from validate_email import validate_email

#class bcolors:
#    HEADER = '\033[95m'
#    OKBLUE = '\033[94m'
#    OKGREEN = '\033[92m'
#    WARNING = '\033[93m'
#    FAIL = '\033[91m'
#    ENDC = '\033[0m'
#    BOLD = '\033[1m'
#    UNDERLINE = '\033[4m'

parser = argparse.ArgumentParser()
parser.add_argument('mail_to_check')
args = parser.parse_args()
#print(chr(27)+'[2j')
#print('\033c')
#print('\x1bc')


#def yes_or_no(question):
#    answer = input(question + "(y/n): ").lower().strip()
#    print("")
#    while not(answer == "y" or answer == "yes" or \
#    answer == "n" or answer == "no"):
#        print("Input yes or no")
#        answer = input(question + "(y/n):").lower().strip()
#        print("")
#    if answer[0] == "y":
#        return True
#    else:
#        return False
#print(args.echo)
# This is some leftover code from a different program that I might decide to re-use, so, leaving it for now:
#if yes_or_no("This script will send emails to actual customers specified in " + args.query + ".  \nAre you sure?"):
#    print("Lmao :D")
#else:
#    print(bcolors.FAIL + "Operation cancelled. \nNo mail sent!\n ")
#    exit()

if (args.mail_to_check):
    #if (validate_email(args.mail_to_check)): # Just a simple format test: something@something.something
    #if (validate_email(args.mail_to_check, check_mx=True)): # Test format and check for Mail eXchanger
    if (validate_email(args.mail_to_check, verify=True)): # Test as above, but test for user as well
        #print(bcolors.OKGREEN + mail_to_check + " appears to be valid" + bcolors.ENDC)
        print(args.mail_to_check)
    else:
        #print(bcolors.FAIL + mail_to_check + " appears to be invalid" + bcolors.ENDC)
        print(" ")
else:
    #print(bcolors.FAIL + mail_to_check  + " email appears to be null" + bcolors.ENDC)
    print("No Address Supplied")
