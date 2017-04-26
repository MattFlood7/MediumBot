#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Matt Flood

import os, random, sys, time, urlparse
from selenium import webdriver
from bs4 import BeautifulSoup
from random import shuffle

# Configure constants here
EMAIL = 'youremail@gmail.com'
PASSWORD = 'password'
LOGIN_SERVICE = 'Google, Twitter, or Facebook'
LIKE_POSTS = True
MAX_LIKES_ON_POST = 50 # only like posts with less than X posts.
COMMENT_ON_POSTS = True
COMMENTS = ['Great read!', 'Good work keep it up!', 'Really enjoyed the article!', 'Very interesting!']
USE_RELATED_TAGS = True
ARTICLES_PER_TAG = 250

def Launch():
    """
    Launch the Medium bot and ask the user what browser they want to use.
    """

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
    """
    Based on the option selected by the user start the selenium browser.
    browserChoice: browser option selected by the user.
    """

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
        MediumBot(browser)

    else:
        soup = BeautifulSoup(browser.page_source, "lxml")
        if soup.find('div', {'class':'alert error'}):
            print 'Error! Please verify your username and password.'
        elif browser.title == '403: Forbidden':
            print 'Medium is momentarily unavailable. Please wait a moment, then try again.'

    browser.quit()


def SignInToService(browser):
    """
    Using the selenium browser passed and the config file login to Medium to
    begin the botting.
    browser: the selenium browser used to login to Medium.
    """

    serviceToSignWith = LOGIN_SERVICE.lower()
    signInCompleted = False
    print 'Signing in...'

    # Sign in
    browser.get('https://medium.com/m/signin?redirect=https%3A%2F%2Fmedium.com%2F')

    signInElement = browser.find_element_by_xpath('//button[contains(text(),"Sign in or sign up with email")]')
    signInElement.click()

    emailElement = browser.find_element_by_name('email')
    emailElement.send_keys(EMAIL)

    if serviceToSignWith == "google":

        try:
            browser.find_element_by_class_name('button--google').click()
            browser.find_element_by_id("next").click()
            time.sleep(3)
            # Enter password
            browser.find_element_by_id('Passwd').send_keys(PASSWORD)
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


def MediumBot(browser):
    """
    Start botting Medium
    browser: selenium browser used to interact with the page
    """

    tagURLsQueued = []

    # Infinite loop
    while True:

        tagURLsQueued = ScrapeUsersFavoriteTagsUrls(browser)

        while tagURLsQueued:

            articleURLsQueued = []
            shuffle(tagURLsQueued)
            tagURL = tagURLsQueued.pop()

            # Note: This is dones this way to add some timing between liking and
            # commenting on posts to throw any bot finder logic off
            tagURLsQueued.append(NavigateToURLAndScrapeRelatedTags(browser, tagURL))
            articleURLsQueued = ScrapeArticlesOffTagPage(browser)

            while articleURLsQueued:

                print "Tags in Queue: "+str(len(tagURLsQueued))+" Articles in Queue: "+str(len(articleURLsQueued))
                articleURL = articleURLsQueued.pop()
                LikeAndCommentOnPost(browser, articleURL)

        print '\nPause for 1 hour to wait for new articles to be posted\n'
        time.sleep(3600+(random.randrange(0, 10))*60)


def ScrapeUsersFavoriteTagsUrls(browser):
    """
    Scrape the urls for the user's favorite tags. We will use these to go off
    when interacting with articles.
    browser: selenium webdriver used for beautifulsoup.
    """

    soup = BeautifulSoup(browser.page_source, "lxml")
    tagURLS = []
    print 'Gathering your favorited tags'

    try:
        for ul in soup.find_all('ul', class_='tags--postTags'):
            for li in ul.find_all('li'):
                a = li.find('a')
                tagURLS.append(a['href'])
                print a['href']
    except:
        print 'Exception thrown in ScrapeUsersFavoriteTagsUrls()'
        pass
    print ''

    return tagURLS


def NavigateToURLAndScrapeRelatedTags(browser, tagURL):
    """
    Navigate to the tag url passed. If the USE_RELATED_TAGS is set scrape the
    related tags found as well.
    browser: selenium webdriver used for beautifulsoup.
    tagURL: the tag page to navigate to before scraping urls
    return: list of other tag urls to add to navigate to and bot.
    """

    browser.get(tagURL)
    tagURLS = []

    if USE_RELATED_TAGS:
        print 'Gathering tags related to : '+tagURL
        soup = BeautifulSoup(browser.page_source, "lxml")

        try:
            for ul in soup.find_all('ul', class_='tags--postTags'):
                for li in ul.find_all('li'):
                    a = li.find('a')
                    if 'followed' not in a['href']:
                        tagURLS.append(a['href'])
                        print a['href']
        except:
            print 'Exception thrown in NavigateToURLAndScrapeRelatedTags()'
            pass
        print ''

    return tagURLS


def ScrapeArticlesOffTagPage(browser):
    """
    Scrape articles to navigate to from the tag's url.
    browser: selenium webdriver used for beautifulsoup.
    return: a list of article urls
    """

    articleURLS = []
    print 'Gathering your articles for the tag :'+browser.current_url

    browser.find_element_by_xpath('//a[contains(text(),"Latest stories")]').click()
    time.sleep(2)

    for counter in range(1,ARTICLES_PER_TAG/10):
        ScrollToBottomAndWaitForLoad(browser)

    try:
        for a in browser.find_elements_by_xpath(('//div[@class="postArticle postArticle--short '
        'js-postArticle js-trackedPost"]/div[2]/a')):
            print a.get_attribute("href")
            articleURLS.append(a.get_attribute("href"))
    except:
        print 'Exception thrown in ScrapeArticlesOffTagPage()'
        pass
    print ''

    return articleURLS


def LikeAndCommentOnPost(browser, articleURL):
    """
    Like and/or comment on the post that has been navigated to.
    browser: selenium browser used to find the like button and click it.
    articleURL: the url of the article to navigate to and like and/or comment
    """

    likeButtonXPath = '//div[@data-source="post_actions_footer"]/button'
    browser.get(articleURL)
    ScrollToBottomAndWaitForLoad(browser)

    if LIKE_POSTS:
        try:
            likeButton = browser.find_element_by_xpath(likeButtonXPath)
            numLikesElement = browser.find_element_by_xpath(likeButtonXPath+"/following-sibling::button")
            buttonStatus = likeButton.get_attribute("data-action")

            if likeButton.is_displayed() and buttonStatus == "upvote":
                if int(numLikesElement.text) < MAX_LIKES_ON_POST:
                    print 'Liking the article : \"'+browser.title+'\"'
                    likeButton.click()
                else:
                    print 'Article \"'+browser.title+'\" has more likes than your threshold.'
            else :
                print 'Article \"'+browser.title+'\" is already liked.'

        except:
            print 'Exception thrown when trying to like the article: '+browser.title
            pass

    if COMMENT_ON_POSTS:

        # Determine if the account has already commented on the post.
        usersName = browser.find_element_by_xpath('//div[@class="avatar"]/img').get_attribute("alt")
        alreadyCommented = False

        try:
            alreadyCommented = browser.find_element_by_xpath('//a[text()[contains(.,"'+usersName+'")]]').is_displayed()
        except:
            pass

        #TODO Find method to comment when the article is not hosted on medium.com currently
        #     found issues with the logic below when not on medium.com.
        if 'medium.com' in browser.current_url:
            if alreadyCommented == False:

                comment = random.choice(COMMENTS)

                try:
                    print 'Commenting \"'+comment+'\" on the article : \"'+browser.title+'\"'
                    commentButton = browser.find_element_by_xpath('//button[@data-action="respond"]')
                    commentButton.click()
                    time.sleep(5)
                    browser.find_element_by_xpath('//div[@role="textbox"]').send_keys(comment)
                    time.sleep(20)
                    browser.find_element_by_xpath('//button[@data-action="publish"]').click()
                    time.sleep(5)
                except:
                    print 'Exception thrown when trying to comment on the article: '+browser.title
                    pass
            else:
                print 'We have already commented on this article: '+browser.title
        else:
            print 'Cannot comment on an article that is not hosted on Medium.com'

    print ''


def ScrollToBottomAndWaitForLoad(browser):
    """
    Scroll to the bottom of the page and wait for the page to perform it's lazy laoding.
    browser: selenium webdriver used to interact with the browser.
    """

    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(4)


if __name__ == '__main__':
    Launch()
