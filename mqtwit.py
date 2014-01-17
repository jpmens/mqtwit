#!/usr/bin/env python

# Copyright (c) 2013 Jan-Piet Mens <jpmens()gmail.com>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
# 3. Neither the name of mosquitto nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

__author__ = "Jan-Piet Mens"
__copyright__ = "Copyright (C) 2013 by Jan-Piet Mens"

import twitter  # pip install python-twitter
                # https://pypi.python.org/pypi/python-twitter
                # https://github.com/bear/python-twitter
import mosquitto
import time
import sys
import os

def on_connect(mosq, userdata, rc):
    print("Connect: rc: "+str(rc))

    mqttc.subscribe(conf['topic'], 0)

def on_message(mosq, userdata, msg):
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))

    topic = msg.topic
    payload = str(msg.payload)

    # text = topic + ': ' + payload
    text = payload
    text = text[0:138]      # truncate for twitter

    tweet(userdata['conf'], text)


def on_disconnect(mosq, userdata, rc):
    print "OOOOPS! disconnect"

def tweet(conf, status):

    twapi = twitter.Api(
        consumer_key        = conf['consumer_key'],
        consumer_secret     = conf['consumer_secret'],
        access_token_key    = conf['token'],
        access_token_secret = conf['token_secret']
    )

    lat     = conf['lat']
    lon     = conf['lon']
    place   = conf['place']

    try:
        res = twapi.PostUpdate(status,  latitude=lat, longitude=lon, place_id=place,
                                display_coordinates=True, trim_user=False)
    except twitter.TwitterError, e:
        print "mqtwit: ", str(e)
    except:
        pass

if __name__ == '__main__':

    conf = {}

    try:
        execfile(os.getenv('MQTWITCONF', 'mqtwit.conf'), conf)
    except Exception, e:
        print "Cannot load configuration file: %s" % str(e)
        sys.exit(1)

    mqttc = mosquitto.Mosquitto(userdata = dict(conf=conf))
    mqttc.on_message = on_message
    mqttc.on_connect = on_connect
    mqttc.on_disconnect = on_disconnect

    if conf['username'] is not None:
        mqttc.username_pw_set(conf['username'], conf['password'])

    mqttc.connect(conf['mqtt_broker'], int(conf['mqtt_broker_port']), 60)

    try:
        mqttc.loop_forever()
    except KeyboardInterrupt:
        sys.exit(0)

