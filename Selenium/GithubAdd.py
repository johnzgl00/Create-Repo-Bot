from selenium import webdriver

username = "username" # Add username here
password = "password" # Add password here
repoName = str(input("Enter Repository Name: "))
description = str(input("Enter Description: "))

signInXpath = "/html/body/div[1]/header/div/div[2]/div[2]/a[1]" # xpath of sign in button on the main page
usernameXpath = "//*[@id='login_field']" # xpath of username text field in login page
passwordXpath = "//*[@id='password']" # xpath of password text field in login page
signIn2Xpath = "/html/body/div[3]/main/div/div[4]/form/div/input[12]" # xpath of sign in button login page
newRepoXpath = "/html/body/div[4]/div/aside[1]/div[2]/div[1]/div/h2/a" # xpath of green new button in main page
repoFieldXpath = "//*[@id='repository_name']" # xpath of repoField
descriptionXpath = "//*[@id='repository_description']" # xpath of description field
createXpath = "/html/body/div[4]/main/div/form/div[4]/button" # xpath of create button

driver = webdriver.Firefox()		 # setting up browser (you can change it to Chrome if you like)
driver.get("https://www.github.com") # page to navigate

signIn = driver.find_element_by_xpath(signInXpath) # click sign in button
signIn.click()

usernamefield = driver.find_element_by_xpath(usernameXpath) # fill username field
usernamefield.send_keys(username)

passwordfield = driver.find_element_by_xpath(passwordXpath) # fill password field
passwordfield.send_keys(password)

signIn2 = driver.find_element_by_xpath(signIn2Xpath) # click sign in button
signIn2.click()

newRepo = driver.find_element_by_xpath(newRepoXpath) # click green new button
newRepo.click()

repoField = driver.find_element_by_xpath(repoFieldXpath) # fill repoName field
repoField.send_keys(repoName)

descriptionField = driver.find_element_by_xpath(descriptionXpath) # fill description field
descriptionField.send_keys(description)

create = driver.find_element_by_xpath(createXpath) # click create button
create.click()
