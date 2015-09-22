# HUEcli
Control Philips HUE lighting from the command line


### Setup connection to Bridge

```
hue setup
```


### List status of available lights

```
hue status
```

**Example Output**
```
Kitchen: OFF
Desk: ON
Bedroom: ON
```


### Control all lights

**Turn on**
```
hue lights on
```

**Turn off**
```
hue lights off
```


### Control a single light

**Turn on**
```
hue light [name_of_light] on
```

**Turn off**
```
hue light [name_of_light] off
```
