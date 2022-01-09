from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask import request
import time

app = Flask(__name__)

def any_request():
  return request.path

limiter = Limiter(
    app,
    key_func= any_request,
    default_limits=["2/second"]
)
first_throttle_time=time.time()
first_throttle=0

def get_header():
  return request.headers.get('x-secret-key')  
  
def get_throttle_age(): 
  global first_throttle, First_throttle_time
  if first_throttle==0:
    First_throttle_time=time.time()
    first_throttle=1
  diff = time.time() - First_throttle_time
  return diff
  

@app.route("/ping",methods=['GET', 'POST'])
@limiter.limit("10/minute", key_func=get_header, override_defaults=False)
def ping_me():
  global first_throttle, First_throttle_time
  first_throttle =0
  print("first_throttle")
  print(first_throttle)
  return "{ \"response\": \"pong\" }"
  
@app.errorhandler(429)
def ratelimit_handler(e):
  throttle_age= get_throttle_age()
  return "{ \"message\": \"request throttled request\", \"throttle_age\": "+str(throttle_age)+" }"