# flagWarehouse
Flag submission system for Attack/Defense CTFs.

### Installation
```
git clone https://github.com/ecavicc/flagWarehouse.git
cd flagWarehouse/server
pip3 install -r requirements.txt
```
### Configuration
Edit the parameters in [config.py](server/config.py)

- `WEB_PASSWORD`: the password to access the web interface
- `FLAG_FORMAT`: string containing the regex format of the flags
- `YOUR_TEAM`: the ip address of your team
- `TEAMS`: the ip addresses of the teams in the competition
- `ROUND_DURATION`: the duration of a round (or *tick*) in seconds
- `FLAG_ALIVE`: the number of seconds a flag can be considered valid
- `SUB_LIMIT`: number of flags that can be sent to the organizers' server each `SUB_INTERVAL`
- `SUB_INTERVAL`: interval in seconds for the submission; if the submission round takes more than the number of seconds
                  specified, the background submission loop will not sleep
- `SUB_URL`: the url used for the verification of the flags
- `SUB_ACCEPTED`: the string used to verify whether the verification server accepted the flag

There is also the environment variable `FLASK_DEBUG` in [run.sh](server/run.sh): if set, any edit to the source files
(including the configuration file) while the server is running will trigger a restart with the new parameters.
Take note that **the submission loop will not be restarted automatically**, even in debug mode, so if you need to change
parameters that influence its behaviour, please restart the server manually.

### Usage
```
chmod +x run.sh
./run.sh
```
The web interface can be accessed on port 5000. To log in, use any username and the password you set.

### Deployment (optional)
Given that most CTFs only last some hours and teams are usually not *that* big, the quickest and least painful approach
would be to self host the application and to use [ngrok](https://ngrok.com/).

## Client
The client is a simple Python script that runs all the programs (both scripts and binaries) in a specific directory.
The programs *need* to run only one time on one target (the target IP address is passed via argv by the client). For a
basic template, please refer to [example.py](client/exploits/example.py).

- REMBEMBER:
   - Attack scripts must have coherent names
   - Attack scripts must have `#!/usr/bin/env python` at the beginning
   - Attack scripts must be executable

Right now, the module `requests` is still needed and listed in [requirements.txt](client/requirements.txt). In the
future, I might use `urllib` in order to avoid external dependencies.
