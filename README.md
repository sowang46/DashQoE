# DashQoE - Dash client for QoE measurement

Measure DASH video streaming QoE with reference [dash.js](https://github.com/Dash-Industry-Forum/dash.js/) client and selenium.

## Basic usage

Install Firefox: `sudo apt install firefox-esr`

Install required Python libraries: 

```
pip install -r requirements.txt
```

Install the web drivers for selenium following [this](https://github.com/SeleniumHQ/selenium/blob/trunk/py/docs/source/index.rst)

Open "monitoring.html" in your target browser and check if the video loads and plays.

Run the python script. For example:
```
python3 monitor_dash.py -d Firefox -p 60
# python3 monitor_dash.py -h
```

## Measure DASH QoE under Mahimahi traffic regulation

Install Mahimahi from the package manager:
```
sudo apt install mahimahi
```

Enable IP forwarding. This needs to be done on every boot:
```
sudo sysctl -w net.ipv4.ip_forward=1
```

Start a Mahimahi LinkShell with a trace file, for example: 
```
mm-link traces/drx_20_4_100Mbps_trace traces/drx_20_4_100Mbps_trace    # The first trace file is applied on downlink and the second one on uplink
```

Then start the monitoring script within the 
```
[Link] foo@bar:~$ python3 monitor.py -d Firefox -p 60
```