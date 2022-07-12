#Importing The Required Modules
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

#Initializing Webdriver
browser = webdriver.Firefox()
browser.maximize_window()

#Opening Cricbuzz URL
browser.get('https://www.cricbuzz.com/cricket-match/live-scores') 
#Enter Team name with first letter capital and no extra whitespaces
team = 'India'
#Configuring Delay in seconds   
delay = 20
#Delay to wait sure website loads properly
wait = WebDriverWait(browser, delay)

#Trying to open team match page
try:
    continue_link = browser.find_element(By.PARTIAL_LINK_TEXT,team).click()
    #Hardcoding XPATH of first inning score (Valid If first Innings is going on)
    inningsScore = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH,"/html/body/div/div[2]/div[4]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/h2")))
    status = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH,"/html/body/div/div[2]/div[4]/div[3]/div[2]/div[1]/div[1]/div[1]/div[2]")))
    batsmanOneName = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH,"/html/body/div/div[2]/div[4]/div[3]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/a")))
    batsmanOneRuns = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH,"/html/body/div/div[2]/div[4]/div[3]/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]")))
    batsmanOneBalls = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH,"/html/body/div/div[2]/div[4]/div[3]/div[2]/div[1]/div[2]/div[1]/div[2]/div[3]")))
    batsmanTwoName = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH,"/html/body/div/div[2]/div[4]/div[3]/div[2]/div[1]/div[2]/div[1]/div[3]/div[1]/a")))
    batsmanTwoRuns = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH,"/html/body/div/div[2]/div[4]/div[3]/div[2]/div[1]/div[2]/div[1]/div[3]/div[2]")))
    batsmanTwoBalls = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH,"/html/body/div/div[2]/div[4]/div[3]/div[2]/div[1]/div[2]/div[1]/div[3]/div[3]")))
    bowlerName =  WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH,"/html/body/div/div[2]/div[4]/div[3]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/a")))
    bowlerOvers = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH,"/html/body/div/div[2]/div[4]/div[3]/div[2]/div[1]/div[2]/div[2]/div[2]/div[2]")))
    bowlerRuns = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH,"/html/body/div/div[2]/div[4]/div[3]/div[2]/div[1]/div[2]/div[2]/div[2]/div[4]")))
    bowlerWickets = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH,"/html/body/div/div[2]/div[4]/div[3]/div[2]/div[1]/div[2]/div[2]/div[2]/div[5]")))
    message = inningsScore.text+ "\n" + status.text + "\nBatting:\n" + batsmanOneName.text + "* " + batsmanOneRuns.text + " (" + batsmanOneBalls.text + ")\n" + batsmanTwoName.text + " " + batsmanTwoRuns.text + " (" + batsmanTwoBalls.text + ")\nBowling:\n" + bowlerName.text + " O: " + bowlerOvers.text +" R:" + bowlerRuns.text + " W: " + bowlerWickets.text
except:
    message = team + " is not playing a match right now."
#Closing the Browser
print(message)
browser.close()

