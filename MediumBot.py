#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, random, sys, time, urlparse
from selenium import webdriver
from bs4 import BeautifulSoup
from random import shuffle

def Launch():
    # Check if the file 'config' exists, otherwise quit
    if os.path.isfile('config') == False:
        print 'Error! No configuration file.'
        sys.exit()

    # Check if the file 'visitedUsers.txt' exists, otherwise create it
    if os.path.isfile('visitedUsers.txt') == False:
        visitedUsersFile = open('visitedUsers.txt', 'wb')
        visitedUsersFile.close()

    # Browser choice
    print 'Choose your browser:'
    print '[1] Chrome'
    print '[2] Firefox/Iceweasel'
    print '[3] PhantomJS'

    while True:
        try:
            browserChoice = int(raw_input('Choice? '))
        except ValueError:
            print 'Invalid choice.',
        else:
            if browserChoice not in [1,2,3]:
                print 'Invalid choice.',
            else:
                break

    StartBrowser(browserChoice)


def StartBrowser(browserChoice):
    if browserChoice == 1:
        print '\nLaunching Chrome'
        browser = webdriver.Chrome()
    elif browserChoice == 2:
        print '\nLaunching Firefox/Iceweasel'
        browser = webdriver.Firefox()
    elif browserChoice == 3:
        print '\nLaunching PhantomJS'
        browser = webdriver.PhantomJS()

    if SignInToService(browser):
        print 'Success!\n'

    else:
        soup = BeautifulSoup(browser.page_source, "lxml")
        if soup.find('div', {'class':'alert error'}):
            print 'Error! Please verify your username and password.'
        elif browser.title == '403: Forbidden':
            print 'Medium is momentarily unavailable. Please wait a moment, then try again.'

    browser.quit()


def SignInToService(browser):

    # Open, load and close the 'config' file
    with open('config', 'r') as configFile:
        config = [line.strip() for line in configFile]
    configFile.close()

    serviceToSignWith = config[2].lower()
    signInCompleted = False
    print 'Signing in...'

    # Sign in
    browser.get('https://medium.com/m/signin?redirect=https%3A%2F%2Fmedium.com%2F')

    signInElement = browser.find_element_by_xpath('//button[contains(text(),"Sign in or sign up with email")]')
    signInElement.click()

    emailElement = browser.find_element_by_name('email')
    emailElement.send_keys(config[0])

    if serviceToSignWith == "google":

        try:
            browser.find_element_by_class_name('button--google').click()
            browser.find_element_by_id("next").click()
            time.sleep(3)
            # Enter password
            browser.find_element_by_id('Passwd').send_keys(config[1])
            browser.find_element_by_id('signIn').click()
            signInCompleted = True
        except:
            pass

    elif serviceToSignWith == "twitter":
        # TODO add this fun logic
        print 'Twitter'
    elif serviceToSignWith == "facebook":
        # TODO add this fun logic
        print 'Facebook'

    time.sleep(3)

    return signInCompleted


def ScrapeUsersFavoriteTagsUrls(browser):

    soup = BeautifulSoup(browser.page_source, "lxml")

    try:
        for ul in soup.find_all('ul', class_='tags--postTags'):
            for li in ul.find_all('li'):
                a = li.find('a')
                print a['href']
    except:
        print 'exception thrown'
        pass


def ScrollToBottomAndWaitForLoad(browser):

    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(4)


def LikePost(browser):
    # TODO: add logic to not like articles that have a certain threshold of likes
    print 'like'


if __name__ == '__main__':
    Launch()
