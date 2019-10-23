# Simple Email Validator
This is just a quickie function wrapper that will, when fed an email address, let you know if it is a valid email.

You use it in the following manner:
``` 
$ ./email_validate foo@example.com
```
If the email is valid, it returns the email.  If not, it returns a single space.
There are a couple of prerequisites.  Python3 and pip, of course, plus the 
validate_email library found at: https://pypi.org/project/validate_email/

To install them, type:
```
$ sudo pip3 install validate_email;
$ sudo pip3 install py3dns;


