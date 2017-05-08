# -*- coding: utf-8 -*-
from bottle import route,run,request,response,hook
# import requests
import threading
import pigpio
import json
import time

PIN = 24

pi = pigpio.pi()
pi.set_mode(PIN, pigpio.OUTPUT)
 
def led_off():
  pi.set_PWM_dutycycle(PIN, 0)


class KaraageDashThread(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)

  def run(self):
    pi.set_PWM_dutycycle(PIN, 255)
    # requests.get('http://maker.ifttt.com/trigger/papa_dash/with/key/xxxxxxxxxxxxxxxxxxxxxxx')
    time.sleep(60)
    led_off()

@hook('after_request')
def header_json():
  response.content_type = 'application/json'


def control_response_json(value):
  obj = {'control':value}
  return json.dumps(obj)

@route('/call')
def control_call():
  th = KaraageDashThread()
  th.start()
  return control_response_json("call")

run(host='192.168.xxx.xxx', port=10080, debug=True)
