# -*- coding: utf-8 -*-
from bottle import route,run,request,response,hook
import threading
import json
import twython
import ConfigParser
from os import path
import datetime

class KaraageDashThread(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)

  def run(self):
    print("dash yakan")
    tweet_str = "@karaage0703 やかん沸かして！" + datetime.datetime.today().strftime("%Y/%m/%d %H:%M:%S")

    consumerKey = config_file.get("twitter_settings","consumerKey")
    consumerSecret = config_file.get("twitter_settings","consumerSecret")
    accessToken = config_file.get("twitter_settings","accessToken")
    accessSecret = config_file.get("twitter_settings","accessSecret")

    api = twython.Twython(app_key=consumerKey,
                  app_secret=consumerSecret,
                  oauth_token=accessToken,
                  oauth_token_secret=accessSecret)

    try:
        api.update_status(status=tweet_str)
    except twython.TwythonError as e:
        print e

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
run(host=hosturl, port=10081, debug=True)
