import time, boto3, chrome, config 
from selenium.webdriver.common.keys import Keys  
import github

def request_benchmarks(driver):
    driver.get("https://learn.cisecurity.org/benchmarks")
    
    #giving the page some extra time to do what it needs to do
    time.sleep(20)
    
    #accept conditions
    link = driver.find_elements_by_css_selector('#c-buttons > a.c-button')[0]
    link.click()
    
    #find all inputs on the page and fill in the ones that matter
    inputs = driver.find_elements_by_css_selector('input')
    for i in inputs:
        n = i.get_property('name')
        if n == 'firstname':
            i.click()
            i.send_keys('a')
        if n == 'lastname':
            i.click()
            i.send_keys('a')
        if n == 'email':
            i.click()
            i.send_keys(config.EMAIL)
    
    #some inputs are <select> elements, we have to click those
    inputs = driver.find_elements_by_css_selector('select')
    for i in inputs:
        i.click()
        options = i.find_elements_by_xpath(".//*")
        for o in options:
            if o.get_property('value') != "":
                o.click()
                break;    
    
    #also need to check some check boxes
    inputs = driver.find_elements_by_css_selector('.hs-form-booleancheckbox-display input')
    for i in inputs:
        i.send_keys(Keys.SPACE)
    
    #submit form
    button = driver.find_elements_by_css_selector('.hs-button.primary.large')[0]
    button.click()

def download_benchmarks(driver):
    #get the download URL from the email
    sqs = boto3.resource('sqs', region_name=config.REGION)
    queue = sqs.Queue(config.QUEUE_URL)
    done = False
    # Process messages by printing out body and optional author name
    for message in queue.receive_messages():
        url = message.body
        message.delete()
        if not done:
            done = True
            print('Downloading the benchmarks from: %s'.format(url))
            driver.get(url)
            #giving the page some extra time to do what it needs to do
            print('sleeping for 60, just to make sure everything is ready')
            time.sleep(60)
            links = driver.find_elements_by_css_selector('[title="Download PDF"]')
            print("got " + str(len(links)) + " links")
            c = 0
            for link in links:
                c = c+1
                print("getting " + str(c) + "/" + str(len(links)) + " link ")
                link.click()
                driver.get(link.get_attribute('href'))
            print("wait a minute to finish downloading the benchmarks")
            time.sleep(60)
            print("close Chrome")
            driver.quit()

driver = chrome.setup_chrome()
print('requesting benchmarks')
request_benchmarks(driver)

print('waiting 60 seconds before checking email')
#wait for 60 seconds before checking email
time.sleep(60)

print('downloading benchmarks')
download_benchmarks(driver)

print('commiting to github')
github.commit()
print('benchmarks_mirror_utility_done')
