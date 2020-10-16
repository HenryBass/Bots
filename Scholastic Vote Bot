from selenium import webdriver
import pyautogui
import time
import os.path

t0 = time.time() + 4.57

# How many votes to cast:
votecount = input("Votes to cast: ")

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
if os.path.isfile('AllVotes.txt'):
    f = open("AllVotes.txt", "r")
    totalvotes = f.read()
    f.close()
else:
    file = open('AllVotes.txt', 'w')
    file.write('')
    file.close()
    totalvotes = 1
print("All votes cast by bot: " + totalvotes)
print("Total Vote Count Saved")
print("Voting Start\n")
counter = 0
pyautogui.PAUSE = 0.00001
driver.get("https://classroommagazines.scholastic.com/election.html")
try:
    vote = driver.find_element_by_xpath(
        "/html/body/div[1]/div/div/div/div[1]/div[2]/div[4]/div[3]/div/div[1]/div[2]/button[3]")
    vote.click()
except:
    pass
vote = driver.find_element_by_class_name("ng-binding")
text0 = vote.text
text0 = text0.replace(" votes so far", "")
text0 = text0.replace(",", "")
print("Total votes in election: " + str(text0))
timeto100 = 0
while True:
    timeto100 += 1
    counter += 1
    try:
        driver.get("https://classroommagazines.scholastic.com/election/vote.html")
        vote = driver.find_element_by_class_name("student-vote-secondary-wrapper")
        vote.click()
        vote = driver.find_element_by_class_name("select-selected")
        vote.click()
        vote = driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div/div/div[2]/div[3]/div[2]/div/div[3]/div/div/div[2]/div[46]")
        vote.click()
        vote = driver.find_element_by_xpath(
            "html/body/div/div/div/div/div/div[2]/div[3]/div[2]/div/div[3]/div[2]/div/div")
        vote.click()
        vote = driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div/div/div[2]/div[3]/div[2]/div[1]/div[3]/div[2]/div/div[2]/div[9]")
        vote.click()
        vote = driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div/div[1]/div[2]/div[3]/div[2]/div/div[5]/div/button/p[1]")
        vote.click()
    except:
        print("Not all votes cast.")
        totalvotes = int(totalvotes)
        totalvotes += counter
        f = open("AllVotes.txt", "w")
        print("All votes:" + str(totalvotes))
        f.write(str(totalvotes))
        f.close()
        break
    #pyautogui.moveRel(0, 100)
    #pyautogui.moveRel(0, -100)
    print("Votes Cast: " + str(counter))
    if timeto100 == 100:
        t1 = time.time()
        timeElapsed = t1 - t0
        print("Time Elapsed: " + str(timeElapsed))
        driver.get("https://classroommagazines.scholastic.com/election.html")
        vote = driver.find_element_by_class_name("ng-binding")
        text = vote.text
        text = text.replace(" votes so far", "")
        text = text.replace(",", "")
        diff = int(text) - int(text0)
        print("Votes Counted: " + str(diff))
        timeto100 = 0
    if counter >= int(votecount):
        print("\nAll votes cast.")
        totalvotes = int(totalvotes)
        totalvotes += counter
        f = open("AllVotes.txt", "w")
        f.write(str(totalvotes))
        f.close()
        driver.close()
        time.sleep(5)
        quit()
