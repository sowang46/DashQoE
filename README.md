# DashQoE - Dash client for QoE measurement

Measure DASH video streaming QoE with reference [dash.js](https://github.com/Dash-Industry-Forum/dash.js/) client and selenium.

## Usage

Install required Python libraries: 

```
pip install -r requirements.txt
```

Install the web drivers for selenium following [this](https://github.com/SeleniumHQ/selenium/blob/trunk/py/docs/source/index.rst)

Open "monitoring.html" in your target browser and check if the video loads and plays.

Run the python script. For example:
```
python3 monitor.py -d Firefox -p 60
# python3 monitor.py -h
```