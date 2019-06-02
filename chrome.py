import time, config 
from selenium import webdriver  
from selenium.webdriver.chrome.options import Options

#this function fixes 696481 Chrome bug, where file downloads do not work in headless mode
def enable_download_in_headless_chrome(browser, download_dir):
    #add missing support for chrome "send_command"  to selenium webdriver
    browser.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
    params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
    browser.execute("send_command", params)

def setup_chrome():
    chrome_options = Options()
    chrome_options.binary_location = config.CHROME['binary']
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(executable_path=config.CHROME['driver'], chrome_options=chrome_options)
    driver.set_window_size(1024, 768)
    enable_download_in_headless_chrome(driver, config.CHROME['downloads'])
    return driver
