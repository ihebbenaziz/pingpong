import requests
import time
import sys

ping_endpoint="http://127.0.0.1:5000/ping"
payload={'request': "ping"}
 
def send_one_request_per_second(header,response_json):
   while "pong" in str(response_json):
       r = requests.post(ping_endpoint, data=payload,headers=header)
       response_json = r.json()
       print(response_json)
       time.sleep(1)
def main():
   header=str(sys.argv[1])
   header = {"x-secret-key": header}
   response_json={'response': "pong"}
   while True:
    send_one_request_per_second(header,response_json)  
    time.sleep(60) 
      
 
main() 