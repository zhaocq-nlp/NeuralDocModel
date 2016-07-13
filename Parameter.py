# -*- coding: utf-8 -*-
import os
import sys
from Util import *


def cmd_parser(argv):
    # start program and parse command line
    println_log('Parsing command line...')
    parameter = Parameter(argv)
    if parameter.contains('config'):
        config_filename = parameter.get('config')
        println_log('Reading configuration from "' + config_filename + '".')
        parameter.parse_config(config_filename)
        parameter.parse_command(sys.argv)
        println_log('Finish reading configuration file.')
    println_log('Program configurations are as follows:')
    parameter.output_para(sys.stdout)
    return parameter


class Parameter:

    # constructor
    def __init__(self, command):
        # parameters
        self.para = {}
        self.parse_command(command)

    def parse_command(self, command):
        for i in range(1, len(command)):
            if command[i][0] != '-':
                continue
            if i + 1 < len(command) and command[i + 1][0] == '-':
                self.para[command[i][1:].lower().strip()] = True
            elif i + 1 < len(command) and command[i + 1][0] != '-':
                self.para[command[i][1:].lower().strip()] = command[i + 1].strip()

    # parse config file
    def parse_config(self, config_filename):
        # if config file exits
        if not os.path.isfile(config_filename):
            println_err("Fail to open config file: \"" + config_filename + "\". Config file does not exist.")
            sys.exit()
        # open config file and read configurations
        config_file = open(config_filename)  # open file for reading
        for one_line in config_file:
            if one_line.strip().__len__() == 0:
                continue
            if one_line[0] == '#':
                continue
            one_line = (one_line.split('#'))[0].strip()
            keyvalue = one_line.split('=')
            self.para[keyvalue[0].lower().strip()] = keyvalue[1].strip()
        config_file.close()

    # contains
    def contains(self, key):
        if key in self.para:
            return True
        else:
            return False

    # get parameter
    def get(self, key, default=None):
        if key in self.para.keys():
            return self.para.get(key)
        if default is None:
            println_err('Fail to get parameter "%s"' % key)
            sys.exit()
        return default

    # get integer
    def getint(self, key, default = None):
        if key in self.para.keys():
            return int(self.para.get(key))
        if default is None:
            println_err('Fail to get parameter "%s"' % key)
            sys.exit()
        return default

    # get boolean
    def getbool(self, key, default = None):
        if key in self.para.keys():
            return self.para.get(key).lower() == 'true'
        if default is None:
            println_err('Fail to get parameter "%s"' % key)
            sys.exit()
        return default

    # get float
    def getfloat(self, key, default = None):
        if key in self.para.keys():
            return float(self.para.get(key))
        if default is None:
            println_err('Fail to get parameter "%s"' % key)
            sys.exit()
        return default

    # get list
    def get_list(self, key):
        if key in self.para:
            return self.para.get(key).split(';')
        else:
            return None

    def output_para(self, redirect):
        for each_key in self.para:
            print >> redirect, '\t' + each_key + ': ' + self.para[each_key]
