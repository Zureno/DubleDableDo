#!/usr/bin/env python3

import threading
import paramiko
import subprocess
from cowpy import cow

def ssh_command(ip,user,passwd,command):
	cow_cli = cow.get_cow('turtle')
	cheese = cow_cli()
	msg = cheese.milk("Hi there!!. Do you like my new SSH-client")
	print(msg)
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect(ip,username=user,password=passwd)
	ssh_session = client.get_transport().open_session()
	if ssh_session.active:
		ssh_session.exec_command(command)
		print (ssh_session.recv(1024))
	return
ssh_command('127.0.0.1','praghav','zurenofreak','id')
