from time import sleep
from time import time as ts
from selenium import webdriver 
from selenium.webdriver.common.by import By
import os
import logging
import argparse
import matplotlib.pyplot as plt

def plot(data):
    plt.figure(figsize=(8, 3))
    plt.plot(data['timeData'], data['bufferLevelData'], 'b--', label="Buffer Level (secs)")
    plt.scatter(data['timeData'], data['bufferLevelData'])
    plt.xlabel("Playback time (secs)")
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()

def scrap(driver, args):
    url = "file://"+os.getcwd()+"/monitoring.html"
    driver.get(url)
    sleep(1)
    assert driver.title == "DashQoE", "Cannot open DashQoE page"

    # Check if video is ready to play
    for ii in range(10):
        if driver.find_element(By.ID, "isReady").text == '1':
            break
        sleep(1)
    if ii == 9:
        logging.info('[scrap] Video not ready after 10 seconds')
        return None
    print('[scrap] Video ready. Starting scraping...')

    # Scraping loop
    bufferLevelData = []
    timeData = []
    qualityLevelData = []
    timestamps = []
    for ii in range(args.period):
        bufferLevel = float(driver.find_element(By.ID, "bufferLevel").text)
        time = int(driver.find_element(By.ID, "time").text)
        framerate = int(driver.find_element(By.ID, "framerate").text)
        resolution = int(driver.find_element(By.ID, "resolution").text)

        print(f'[scrap] Current playback time: {time}, buffer level: {bufferLevel}, framerate: {framerate}, resolution: {resolution}', end='\r')
        bufferLevelData.append(bufferLevel)
        timeData.append(time)
        qualityLevelData.append((framerate, resolution))
        timestamps.append(ts())
        sleep(1)
    return {"timestamps": timestamps, "timeData": timeData, "bufferLevelData": bufferLevelData, "qualityLevelData": qualityLevelData}

def main(args):
    assert args.driver=="Chrome" or "Firefox", "Driver type not supported!"
    assert 0<args.period<=600, "Invalid measurement period (0-600s)"

    if args.driver=="Firefox":
        options = webdriver.FirefoxOptions() 
        if not args.gui:
            options.add_argument('-headless')
        with webdriver.Firefox(options=options) as driver: 
            data = scrap(driver, args)
    else:
        options = webdriver.ChromeOptions() 
        options.headless = args.gui
        with webdriver.Chrome(options=options) as driver: 
            data = scrap(driver, args)
    plot(data)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    parser = argparse.ArgumentParser(description='DashQoE -- monitor video streaming QoE with Dash.js')
    parser.add_argument('-d', '--driver', type=str, default="Firefox", help='web driver: Chrome or Firefox')
    parser.add_argument('-g', '--gui', action='store_true', help='Display web gui while scraping')
    parser.add_argument('-p', '--period', type=int, default=60, help='Measurement period in seconds (Maximum 600 seconds)')
    main(parser.parse_args())