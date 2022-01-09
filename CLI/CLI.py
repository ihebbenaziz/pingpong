import requests
import time
import sys

payload={'request': "ping"}
 
def send_one_request_per_second(endpoint,header,response_json):
   while "pong" in str(response_json):
       r = requests.post(endpoint, data=payload,headers=header)
       response_json = r.json()
       print(response_json)
       time.sleep(1)
def main():
   endpoint=str(sys.argv[1])
   header=str(sys.argv[2])
   header = {"x-secret-key": header}
   response_json={'response': "pong"}
   while True:
    send_one_request_per_second(endpoint,header,response_json)  
    time.sleep(60) 
      
 
main() 