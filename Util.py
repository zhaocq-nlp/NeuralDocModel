# encoding=utf-8

import sys


# output log each line
def println_log(content = ''):
    print content


# output log
def print_log(context = ''):
    print context,


# output err
def print_err(content = ''):
    print >> sys.stderr, content,


# output err
def println_err(content = ''):
    print >> sys.stderr, content
