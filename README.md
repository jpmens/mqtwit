# MQTWIT

This program subscribes to an [MQTT] topic, extracts the text (!) payload,
truncates that to about 140 and tweets the result on a configurable Twitter
account.

### History

Around 2013 (or whenever it was that Twitter changed their API) I had a bunch
of programs which tweeted things. Some I'd written in Perl others in Python,
etc. On the day of the API change, everything broke. I had to chase down all my
scripts, again try and find libraries I'd used, etc. It turned out most of
those libs had either been abandoned or not yet updated -- chaos.

Never again. 

Simultaneously I was doing more and more [MQTT], and it occurred to me to have
a "single point of exit" (or failure? :-) to Twitter. That's how _mqtwit_ was
born.

### Example

```
mosquitto_pub -t home/status/1 -m 'Hello peeps!'
```

Result:

![Screenshot](jmbp-783.jpg)

### Configuration

Export an environment variable called `MQTWITCONF` containing the path of
your configuration file (defaults to `mqtwit.conf`). This allows you to
run multiple instances with different Twitter accounts, if you need that.

Configure `mqtwit.conf` by copying the sample file `mqtwit.conf.sample`
and adjust to your environment.

```
# Twitter
consumer_key            = 'xxxxxxxxxxxxxxxxxxxxxx'
consumer_secret         = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
token                   = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
token_secret            = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

# Optional: lat, long, place for adding Geo location to your tweets
lat     = None
lon     = None
place   = None

mqtt_broker = 'localhost'
mqtt_broker_port = 1883

topic = 'home/status/#'

# Optional: credentials for broker (may be None)
username = None
password = None
```

### Requirements

* Twitter auth tokens
* MQTT broker (e.g. [Mosquitto](http://mosquitto.org))
* Mosquitto.py 
* [Python Twitter](https://pypi.python.org/pypi/python-twitter)

  [MQTT]: http://mqtt.org
