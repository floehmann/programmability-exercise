#!/usr/bn/env python

from jsonrpclib import Server

switch = Server ("http://arista:arista@192.168.0.1/command-api")
response = switch.runCmds( 1, ["show version"] )
print response
