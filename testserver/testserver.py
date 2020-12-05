import requests
import time
from timeloop import Timeloop
from datetime import timedelta
import psutil
import json

# Configure your data here
time_interval_in_seconds = 60
login_data = {
	'username': 'testuser',
	'password': 'WzkW49JLNNEave9'
	}
server_id = "1"
# Please ensure that this user and server do exist in Ponton database

tl = Timeloop()

response_login = requests.post("http://0.0.0.0:8000/api/auth-get-token/", data=login_data)
response_json = response_login.json()
token = "Token " + response_json["token"]
print("Succesfully logged in")

@tl.job(interval=timedelta(seconds=time_interval_in_seconds))
def check_and_report_cpu_state():
	address = "http://0.0.0.0:8000/api/server/" + server_id + "/"
	server_data = {}
	cpu_state = psutil.cpu_percent()
	server_data["cpu_state"] = cpu_state
	server_headers = {'Authorization': token}
	response = requests.put(address, headers=server_headers, data=server_data)
	print(response.json())

if __name__ == '__main__':
	tl.start(block=True)
