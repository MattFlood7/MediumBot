# MediumBot
Increase your likelihood to grow your Medium account by viewing articles based on your followed tags by liking articles and leaving comments on articles.

## Note
This project is a work in progress and is not yet complete.

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
Before you run the bot, edit the `config` file to add your account login informations (email, password, and service your login is through Google, Twitter, or Facebook). It's that simple!

## Run
Once you have installed the required dependencies and edited the `config` file, you can run the bot.

Make sure you are in the correct folder and run the following command: `python MediumBot.py`

Then, after choosing your favorite browser the bot will start visiting articles based on your tags and start liking and leaving comments increase your  visibility on Medium.
