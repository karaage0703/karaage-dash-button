# -*- coding: utf-8 -*-
from bottle import route,run,request,response,hook
import threading
import json
import subprocess
import ConfigParser
from os import path

class KaraageDashThread(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)

  def run(self):
    print("papamama dash")
    cmd='aplay ~/karaage-dash-button/papamama_dash.wav'
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

config_file = ConfigParser.SafeConfigParser()
config_file_path = path.dirname(path.abspath( __file__ )) + "/.config"
config_file.read(config_file_path)
hosturl = config_file.get("settings","hosturl")
run(host=hosturl, port=10080, debug=True)
