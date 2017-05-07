# MediumBot
Increase your likelihood to grow your Medium account by viewing articles based on your followed tags by liking articles and leaving comments on articles.

## About
It's hard to start out creating content with a small audience. Interacting with user's who have similar interests is the easiest way to build a social media platform but it is a long time consuming process to get there. Using the MediumBot you can drive user interaction how ever you want. Using the bot for an hour yeilded 15 notifications and 8 of those were followers.
<p align="center">
  <img src="https://image.ibb.co/eXT7gQ/notifications.png" alt="LinkedInBot Result" width="325" height="130">
</p>

## Requirements
MediumBot was developed under [Pyhton 2.7](https://www.python.org/downloads).

Before you can run the bot, you will need to install a few Python dependencies.

Note: Python 2.7.9 and later (on the python2 series), and Python 3.4 and later include pip by default, so you may have pip already. Otherwise, you can install [easy_install](https://pythonhosted.org/setuptools/easy_install.html) `sudo apt-get install python-setuptools` to install [pip](https://pypi.python.org/pypi/pip) `sudo easy_install pip`.

- [BeautifulSoup4](https://pypi.python.org/pypi/beautifulsoup4), for parsing html: `pip install BeautifulSoup4`
- [Selenium](http://www.seleniumhq.org/), for browser automation: `pip install Selenium`

If you plan to use Firefox (or Iceweasel) you don't need anything more.

For Chrome, first get the [webdriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) then put it in the same folder than the bot if you are on Windows, or in the `/usr/bin` folder if you are on OS X.

PhantomJS:
- On Windows, download the binary from the [official website](http://phantomjs.org) and put it in the same folder than the bot.
- On OS X Yosemite, the binary provided by the PhantomJS crew doesn't work (*selenium.common.exceptions.WebDriverException: Message: 'Can not connect to GhostDriver'*). You can either compile it by yourself or download the binary provided by the awesome [eugene1g](https://github.com/eugene1g/phantomjs/releases). Then put it in the `/usr/bin` folder.
- It's the same for Raspbian : compile it and put it in the `/usr/bin` folder or download the binary provided by the awesome [fg2it](https://github.com/fg2it/phantomjs-on-raspberry/tree/master/rpi-2-3/wheezy-jessie/v2.1.1).

If you want to built your own binaries, here is the [build instructions](http://phantomjs.org/build.html) for PhantomJS.

## Configuration
Before you run the bot, edit the configuration portion of the script. This will include your account login information (email, password, and service your login is through, etc.) and other logical values to make the bot more of your own. It's that simple!

```python
# Configure constants here
EMAIL = 'youremail@gmail.com'
PASSWORD = 'password'
LOGIN_SERVICE = 'Google, Twitter, or Facebook'
LIKE_POSTS = True
RANDOMIZE_LIKING_POSTS = True
MAX_LIKES_ON_POST = 50 # only like posts with less than X posts.
COMMENT_ON_POSTS = False
RANDOMIZE_COMMENTING_ON_POSTS = True
COMMENTS = ['Great read!', 'Good work keep it up!', 'Really enjoyed the content!', 'Very interesting!']
FOLLOW_USERS = False
RANDOMIZE_FOLLOWING_USERS = True
UNFOLLOW_USERS = False
RANDOMIZE_UNFOLLOWING_USERS = False
UNFOLLOW_USERS_BLACK_LIST = ['DontUnFollowMe']
USE_RELATED_TAGS = True
ARTICLES_PER_TAG = 250
VERBOSE = True
```

## Run
Once you have installed the required dependencies and edited the configuration constants, you can run the bot.

Make sure you are in the correct folder and run the following command: `python MediumBot.py`

Then, after choosing your favorite browser the bot will start visiting articles based on your tags and start liking and commenting articles or following and unfollowing users increase your visibility on Medium.

## Output
![MediumBot Demo Gif](http://g.recordit.co/j7gsUZQOJG.gif)
