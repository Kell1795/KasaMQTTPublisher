# KasaMQTTPublisher
Python script leveraging python-kasa to collect real time power consumption and post to an mqtt broker

# State
Initial release. Python scripts include a lot of redundancy, inconsistency, and irrelevant lines. The initial goal was to push the code into being operational. I'm hoping to come back to this and modify the code to be cleaner after I finish the rest of the workflow. Security and TLS/SSL has not been set up yet. I'll plan to harden the security of the devices later on. 

#Usage
Required input is a kasa device unsecurely connected to an internal network. User should input the device ip and the mqtt broker into the code. Python script will publish wattage in {"e":<wattage>,"n":<name>} format that can be subscribed to by an mqtt subscriber. 

