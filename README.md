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

### Requirements

* Twitter auth tokens
* MQTT broker (e.g. [Mosquitto](http://mosquitto.org)
* Mosquitto.py 
* [Python Twitter](https://pypi.python.org/pypi/python-twitter)
* [MQTT]: http://mqtt.org
