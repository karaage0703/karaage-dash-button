# -*- coding: utf-8 -*-
from bottle import route,run,request,response,hook
import threading
import json
import subprocess

class KaraageDashThread(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)

  def run(self):
    print("dash roomba")
    cmd='rostopic pub /set_clean_mode ca_msgs/CleanMode "mode: 1"'
    subprocess.call(cmd, shell=True)

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

run(host='192.168.xx.xx', port=10082, debug=True)
