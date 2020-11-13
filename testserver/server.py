import requests
import time
from timeloop import Timeloop
from datetime import timedelta
import psutil
import json

tl = Timeloop()
time_interval_in_seconds = 60

login_data = {"username": "usser","password": "WzkW49JLNNEave9"}
response_login = requests.post("http://web:8000/api/auth-get-token/", data=login_data)
token = response_login.json()

@tl.job(interval=timedelta(seconds=time_interval_in_seconds))
def check_and_report_cpu_state():
	cpu_state = psutil.cpu_percent()
	address = "http://web:8000/api/server/1/"
	data = {
    	 "cpu_state": cpu_state
	}
	data["token"] = token["token"]
	response = requests.post(address, data=data)
	print(response)
	print(cpu_state)

if __name__ == '__main__':
	tl.start(block=True)
