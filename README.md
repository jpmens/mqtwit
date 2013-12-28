# MQTWIT

MQTT to Twitter

Example:

```
mosquitto_pub -h hippo -t home/status/1 -m 'Hello peeps!'
```

Result:

![Screenshot](jmbp-783.jpg)

Requires:

* Twitter auth tokens
* MQTT broker
* Mosquitto.py 
* [Python Twitter](https://pypi.python.org/pypi/python-twitter)
