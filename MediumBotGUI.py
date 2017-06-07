#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: Matt Flood

"""
MediumBot's configuration GUI to make it easier for non-technical users to use
the bot.
Note: this is a starting point for the GUI and is not finished.
"""

from Tkinter import *
from ttk import *
from tempfile import mkstemp
from shutil import move
from os import remove, close
import os
import re

FILE_PATH = "MediumBot.py"

class MediumBotGUI(Frame):

    def __init__(self, parent):
        """
        Initilaize the MediumBotGUI object.
        """
        Frame.__init__(self, parent)

        self.parent = parent
        self.initUI()


    def initUI(self):
        """
        Initialize the user interface.
        """

        mediumBotVariables = self.parseMediumBot()

        self.parent.title("Medium Bot")
        self.pack(fill=BOTH, expand=True)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(5, pad=7)
        self.initEmailUI(mediumBotVariables)
        self.initPasswordUI(mediumBotVariables)
        self.initLoginServiceUI(mediumBotVariables)
        self.initDriverUI(mediumBotVariables)
        self.initLikePostsUI(mediumBotVariables)
        self.initRandomizeLikesUI(mediumBotVariables)
        self.initMaxLikesUI(mediumBotVariables)
        self.initCommentUI(mediumBotVariables)
        self.initRandomizeCommentsUI(mediumBotVariables)
        self.initCommentsUI(mediumBotVariables)
        self.initArticleBlackListUI(mediumBotVariables)
        self.initFollowUsersUI(mediumBotVariables)
        self.initRandomizeFollowingUI(mediumBotVariables)
        self.initUnFollowUsersUI(mediumBotVariables)
        self.initRandomizeUnFollowingUI(mediumBotVariables)
        self.initUnFollowingUsersBlackListUI(mediumBotVariables)
        self.initUseRelatedTagsUI(mediumBotVariables)
        self.initArticlesPerTagUI(mediumBotVariables)
        self.initVerboseUI(mediumBotVariables)
        self.initStartButton()


    def initEmailUI(self, mediumBotVariables):
        """
        Initialize the Email UI
        mediumBotVariables: variables pulled from the MediumBot.py file
        """

        Label(self, text="Email: ").grid(sticky=W, pady=4, padx=5)
        self.emailField = Entry(self, width = 100)
        self.emailField.grid(row=0, column=1, columnspan = 3)
        self.emailField.insert(10, mediumBotVariables["EMAIL"])


    def initPasswordUI(self, mediumBotVariables):
        """
        Initialize the Password UI
        mediumBotVariables: variables pulled from the MediumBot.py file
        """

        Label(self, text="Password: ").grid(sticky=W, pady=4, padx=5)
        self.passwordField = Entry(self, show="*", width = 100)
        self.passwordField.grid(row=1, column=1, columnspan = 3)
        self.passwordField.insert(10, mediumBotVariables["PASSWORD"])


    def initLoginServiceUI(self, mediumBotVariables):
        """
        Initialize the Login Service UI
        mediumBotVariables: variables pulled from the MediumBot.py file
        """

        Label(self, text="Service: ").grid(sticky=W, pady=4, padx=5)
        self.serviceDropDown = Combobox(self, values=["Google", "Facebook", "Twitter"], width = 100)
        self.serviceDropDown.grid(row=2, column=1, columnspan = 3)

        if "Google, Twitter, or Facebook" not in mediumBotVariables["LOGIN_SERVICE"]:
            if "google" in mediumBotVariables["LOGIN_SERVICE"].lower():
                self.serviceDropDown.current(0)
            elif "facebook" in mediumBotVariables["LOGIN_SERVICE"].lower() or "iceweasel" in mediumBotVariables["LOGIN_SERVICE"].lower():
                self.serviceDropDown.current(1)
            elif "twitter" in mediumBotVariables["LOGIN_SERVICE"].lower():
                self.serviceDropDown.current(2)


    def initDriverUI(self, mediumBotVariables):
        """
        Initialize the Driver UI
        mediumBotVariables: variables pulled from the MediumBot.py file
        """

        Label(self, text="Driver: ").grid(sticky=W, pady=4, padx=5)
        self.driverDropDown = Combobox(self, values=["Chrome", "Firefox/Iceweasel", "PhantomJS"], width = 100)
        self.driverDropDown.grid(row=3, column=1, columnspan = 3)
        self.driverDropDown.current(0)

        if "Google, Twitter, or Facebook" not in mediumBotVariables["LOGIN_SERVICE"].lower():
            if "chrome" in mediumBotVariables["DRIVER"].lower():
                self.driverDropDown.current(0)
            elif "firefox" in mediumBotVariables["DRIVER"].lower() or "iceweasel" in mediumBotVariables["DRIVER"].lower():
                self.driverDropDown.current(1)
            elif "phantomjs" in mediumBotVariables["DRIVER"].lower():
                self.driverDropDown.current(2)


    def initLikePostsUI(self, mediumBotVariables):
        """
        Initialize the Like Posts UI
        mediumBotVariables: variables pulled from the MediumBot.py file
        """

        Label(self, text="Like Posts: ").grid(sticky=W, pady=4, padx=5)
        self.likePosts = StringVar(value=mediumBotVariables["LIKE_POSTS"])
        self.likePostsCheckBox = Checkbutton(self, text="", variable=self.likePosts, onvalue='True', offvalue='False')
        self.likePostsCheckBox.grid(row=4, column = 1, columnspan = 3)


    def initRandomizeLikesUI(self, mediumBotVariables):
        """
        Initialize the Randomize Likes UI
        mediumBotVariables: variables pulled from the MediumBot.py file
        """

        Label(self, text="Randomize Likes: ").grid(sticky=W, pady=4, padx=5)
        self.randomizeLikes = StringVar(value=mediumBotVariables["RANDOMIZE_LIKING_POSTS"])
        self.randomizeLikesCheckBox = Checkbutton(self, text="", variable=self.randomizeLikes, onvalue='True', offvalue='False')
        self.randomizeLikesCheckBox.grid(row=5, column = 1, columnspan = 3)


    def initMaxLikesUI(self, mediumBotVariables):
        """
        Initialize the Max Likes UI
        mediumBotVariables: variables pulled from the MediumBot.py file
        """

        Label(self, text="Max Likes On Posts: ").grid(sticky=W, pady=4, padx=5)
        self.maxLikesField = Entry(self, width = 100)
        self.maxLikesField.grid(row=6, column=1, columnspan = 3)
        self.maxLikesField.insert(10, mediumBotVariables["MAX_LIKES_ON_POST"])


    def initCommentUI(self, mediumBotVariables):
        """
        Initialize the Comment UI
        mediumBotVariables: variables pulled from the MediumBot.py file
        """

        Label(self, text="Comment On Posts: ").grid(sticky=W, pady=4, padx=5)
        self.commentOnPosts = StringVar(value=mediumBotVariables["COMMENT_ON_POSTS"])
        self.commentPostsCheckBox = Checkbutton(self, text="", variable=self.commentOnPosts, onvalue='True', offvalue='False')
        self.commentPostsCheckBox.grid(row=7, column = 1, columnspan = 3)


    def initRandomizeCommentsUI(self, mediumBotVariables):
        """
        Initialize the Randomize Comments UI
        mediumBotVariables: variables pulled from the MediumBot.py file
        """

        Label(self, text="Randomize Comments: ").grid(sticky=W, pady=4, padx=5)
        self.randomizeComments = StringVar(value=mediumBotVariables["RANDOMIZE_COMMENTING_ON_POSTS"])
        self.randomizeCommentsCheckBox = Checkbutton(self, text="", variable=self.randomizeComments, onvalue='True', offvalue='False')
        self.randomizeCommentsCheckBox.grid(row=8, column = 1, columnspan = 3)


    def initCommentsUI(self, mediumBotVariables):
        """
        Initialize the Comments UI
        mediumBotVariables: variables pulled from the MediumBot.py file
        """

        Label(self, text="Comments: ").grid(sticky=W, pady=4, padx=5)
        self.commentsField = Entry(self, width = 100)
        self.commentsField.grid(row=9, column=1, columnspan = 3)
        self.commentsField.insert(10, mediumBotVariables["COMMENTS"])


    def initArticleBlackListUI(self, mediumBotVariables):
        """
        Initialize the Article Black List UI
        mediumBotVariables: variables pulled from the MediumBot.py file
        """

        Label(self, text="Article Black List: ").grid(sticky=W, pady=4, padx=5)
        self.articleBlackListField = Entry(self, width = 100)
        self.articleBlackListField.grid(row=10, column=1, columnspan = 3)
        self.articleBlackListField.insert(10, mediumBotVariables["ARTICLE_BLACK_LIST"])


    def initFollowUsersUI(self, mediumBotVariables):
        """
        Initialize the Follow Users UI
        mediumBotVariables: variables pulled from the MediumBot.py file
        """

        Label(self, text="Follow Users: ").grid(sticky=W, pady=4, padx=5)
        self.followUsers = StringVar(value=mediumBotVariables["FOLLOW_USERS"])
        self.followUsersCheckBox = Checkbutton(self, text="", variable=self.followUsers, onvalue='True', offvalue='False')
        self.followUsersCheckBox.grid(row=11, column = 1, columnspan = 3)


    def initRandomizeFollowingUI(self, mediumBotVariables):
        """
        Initialize the Randomize Following UI
        mediumBotVariables: variables pulled from the MediumBot.py file
        """

        Label(self, text="Randomize Following: ").grid(sticky=W, pady=4, padx=5)
        self.randomizeFollowingUsers = StringVar(value=mediumBotVariables["RANDOMIZE_FOLLOWING_USERS"])
        self.randomizeFollowingCheckBox = Checkbutton(self, text="", variable=self.randomizeFollowingUsers, onvalue='True', offvalue='False')
        self.randomizeFollowingCheckBox.grid(row=12, column = 1, columnspan = 3)


    def initUnFollowUsersUI(self, mediumBotVariables):
        """
        Initialize the UnFollow Users UI
        mediumBotVariables: variables pulled from the MediumBot.py file
        """

        Label(self, text="Unfollow Users: ").grid(sticky=W, pady=4, padx=5)
        self.unfollowUsers = StringVar(value=mediumBotVariables["UNFOLLOW_USERS"])
        self.unfollowUsersCheckBox = Checkbutton(self, text="", variable=self.unfollowUsers, onvalue='True', offvalue='False')
        self.unfollowUsersCheckBox.grid(row=13, column = 1, columnspan = 3)


    def initRandomizeUnFollowingUI(self, mediumBotVariables):
        """
        Initialize the Randomize UnFollowing UI
        mediumBotVariables: variables pulled from the MediumBot.py file
        """

        Label(self, text="Randomize Unfollowing: ").grid(sticky=W, pady=4, padx=5)
        self.randomizeUnfollowingUsers = StringVar(value=mediumBotVariables["RANDOMIZE_UNFOLLOWING_USERS"])
        self.randomizeUnfollowingCheckBox = Checkbutton(self, text="", variable=self.randomizeUnfollowingUsers, onvalue='True', offvalue='False')
        self.randomizeUnfollowingCheckBox.grid(row=14, column = 1, columnspan = 3)


    def initUnFollowingUsersBlackListUI(self, mediumBotVariables):
        """
        Initialize the UnFollowing Users Black List UI
        mediumBotVariables: variables pulled from the MediumBot.py file
        """

        Label(self, text="Unfollow Black List: ").grid(sticky=W, pady=4, padx=5)
        self.unfollowBlackListField = Entry(self, width = 100)
        self.unfollowBlackListField.grid(row=15, column=1, columnspan = 3)
        self.unfollowBlackListField.insert(10, mediumBotVariables["UNFOLLOW_USERS_BLACK_LIST"])


    def initUseRelatedTagsUI(self, mediumBotVariables):
        """
        Initialize the Use Related Tags UI
        mediumBotVariables: variables pulled from the MediumBot.py file
        """

        Label(self, text="Use Related Tags: ").grid(sticky=W, pady=4, padx=5)
        self.useRelatedTags = StringVar(value=mediumBotVariables["USE_RELATED_TAGS"])
        self.useRelatedTagsCheckBox = Checkbutton(self, text="", variable=self.useRelatedTags, onvalue='True', offvalue='False')
        self.useRelatedTagsCheckBox.grid(row=16, column = 1, columnspan = 3)


    def initArticlesPerTagUI(self, mediumBotVariables):
        """
        Initialize the Articles Per Tag UI
        mediumBotVariables: variables pulled from the MediumBot.py file
        """

        Label(self, text="Articles Per Tag: ").grid(sticky=W, pady=4, padx=5)
        self.articlesPerTagField = Entry(self, width = 100)
        self.articlesPerTagField.grid(row=17, column=1, columnspan = 3)
        self.articlesPerTagField.insert(10, mediumBotVariables["ARTICLES_PER_TAG"])


    def initVerboseUI(self, mediumBotVariables):
        """
        Initialize the Verbose UI
        mediumBotVariables: variables pulled from the MediumBot.py file
        """

        Label(self, text="Verbose Output: ").grid(sticky=W, pady=4, padx=5)
        self.verbose = StringVar(value=mediumBotVariables["VERBOSE"])
        self.verboseCheckBox = Checkbutton(self, text="", variable=self.verbose, onvalue='True', offvalue='False')
        self.verboseCheckBox.grid(row=18, column = 1, columnspan = 3)


    def initStartButton(self):
        """
        Initialize the Start Button UI
        """

        startButton = Button(self, text="Start Bot", command=self.runMediumBot)
        startButton.grid(row=20, column=3)


    def parseMediumBot(self):
        """
        Get the user's current set values in MediumBot.py to display in the fields.
        """

        lines = [line.rstrip('\n') for line in open(FILE_PATH)]
        charsToRemove = ["'", "[", "]", '"']
        mediumBotVariables = {}
        atStartOfVariables = False

        for line in lines:

            if not atStartOfVariables and "=" in line:
                atStartOfVariables = True
            elif atStartOfVariables and "=" not in line:
                break

            if atStartOfVariables:

                mediumBotVar = line.split(" = ")
                for charToRemove in charsToRemove:
                    mediumBotVar[1] = mediumBotVar[1].replace(charToRemove,"")

                mediumBotVariables[mediumBotVar[0]] = mediumBotVar[1]

        return mediumBotVariables


    def runMediumBot(self):
        """
        Run the MediumBot
        """

        if self.validateFieldValues():
            self.updateMediumBot()
            self.parent.destroy()
            os.system("python "+FILE_PATH)


    def validateFieldValues(self):
        """
        Validate the values entered in the fields
        """
        
        return True


    def updateMediumBot(self):
        """
        Update the MediumBot with the values in the GUI. Called when the start buttton
        is clicked.
        """

        self.updateMediumBotVariable("EMAIL = '"+self.emailField.get()+"'")
        self.updateMediumBotVariable("PASSWORD = '"+self.passwordField.get()+"'")
        self.updateMediumBotVariable("LOGIN_SERVICE = '"+self.serviceDropDown.get()+"'")
        self.updateMediumBotVariable("DRIVER = '"+self.driverDropDown.get()+"'")
        self.updateMediumBotVariable("LIKE_POSTS = "+self.likePosts.get())
        self.updateMediumBotVariable("RANDOMIZE_LIKING_POSTS = "+self.randomizeLikes.get())
        self.updateMediumBotVariable("MAX_LIKES_ON_POST = "+self.maxLikesField.get())
        self.updateMediumBotVariable("COMMENT_ON_POSTS = "+self.commentOnPosts.get())
        self.updateMediumBotVariable("RANDOMIZE_LIKING_POSTS = "+self.randomizeComments.get())
        commentsConverted = self.convertStringToArrayString(self.commentsField.get())
        self.updateMediumBotVariable("COMMENTS = "+commentsConverted)
        articlesConverted = self.convertStringToArrayString(self.articleBlackListField.get())
        self.updateMediumBotVariable("ARTICLE_BLACK_LIST = "+articlesConverted)
        self.updateMediumBotVariable("FOLLOW_USERS = "+self.followUsers.get())
        self.updateMediumBotVariable("RANDOMIZE_FOLLOWING_USERS = "+self.randomizeFollowingUsers.get())
        self.updateMediumBotVariable("UNFOLLOW_USERS = "+self.unfollowUsers.get())
        self.updateMediumBotVariable("RANDOMIZE_UNFOLLOWING_USERS = "+self.randomizeUnfollowingUsers.get())
        unfollowConverted = self.convertStringToArrayString(self.unfollowBlackListField.get())
        self.updateMediumBotVariable("UNFOLLOW_USERS_BLACK_LIST = "+unfollowConverted)
        self.updateMediumBotVariable("USE_RELATED_TAGS = "+self.useRelatedTags.get())
        self.updateMediumBotVariable("ARTICLES_PER_TAG = "+self.articlesPerTagField.get())
        self.updateMediumBotVariable("VERBOSE = "+self.verbose.get())


    def validateEmail(self):
        """
        Validate the email address passed is a valid email.
        return: true if the email is valid : false if the email is not valid.
        """

        result = False
        email = self.emailField.get()

        if email:
            result = re.match(r"[^@]+@[^@]+\.[^@]+", email)

        return result


    def validatePassword(self):
        """
        Validate the password passed is ot empty.
        return: true if the password is valid : false if the password is not valid.
        """

        result = False

        if self.passwordField.get():
            result = True

        return result


    def validateMaxLikesOnPost(self):
        """
        Validate the max likes value passed is valid.
        return: true if the max likes value is valid : false if the max likes value is not valid.
        """

        return self.isNumberValid(self.maxLikesField.get())


    def validateComments(self):
        """
        Validate the comments passed are valid comments.
        return: true if the comments are valid : false if the comments are not valid.
        """

        return self.notContainSpecialChars(self.commentsField.get())


    def validateArticleBlackList(self):
        """
        Validate the article black list passed is valid.
        return: true if the article black list is valid : false if the article black list is not valid.
        """

        return self.notContainSpecialChars(self.articleBlackListField.get())


    def validateUnfollowBlackList(self):
        """
        Validate the unfollow black list passed is valid.
        return: true if the unfollow blacklist is valid : false if the unfollow blacklist is not valid.
        """

        return self.notContainSpecialChars(self.unfollowBlackListField.get())


    def validateArticlesPerTag(self):
        """
        Validate the articles per tag value passed is valid.
        return: true if the articles per tag value is valid : false if the articles per tag value is not valid.
        """

        return self.isNumberValid(self.articlesPerTagField.get())


    def notContainSpecialChars(self, value):
        """
        Validate the string does not have any special characters.
        value: string to validate that special characters do not exist.
        """

        return not set('[~!@#$%^&*()_+{}":;\']+$').intersection(value)


    def isNumberValid(self, value):
        """
        Validate the number passed is a valid number.
        value: the number to validate.
        return: true if the number is valid : false if the number is not valid.
        """

        result = False

        if value:
            result = isinstance(value, int)

        return result


    def updateMediumBotVariable(self, value):
        """
        Update a variable in the MediumBot.py file.
        value: value to update the variable in MediumBot.py to.
        """

        variableToUpdate = value.split()[0]
        fh, abs_path = mkstemp()

        with open(abs_path,'w') as newFile:

            with open(FILE_PATH) as oldFile:

                for line in oldFile:
                    if (variableToUpdate+" =" in line and " = " in line
                        and "if" not in line and "elif" not in line
                        and ".lower()" not in line and "(" not in line
                        and ((variableToUpdate == "FOLLOW_USERS"
                        and "UNFOLLOW_USERS" not in line) or variableToUpdate != "FOLLOW_USERS")):

                        newFile.write(value+"\n")
                    else:
                        newFile.write(line)

        close(fh)
        remove(FILE_PATH)
        move(abs_path, FILE_PATH)


    def convertStringToArrayString(self, valueToConvert):
        """
        Convert the comma deliminated string to an array formatted string.
        valueToConvert: string to convert in to an array formatted string.
        return: the formatted string.
        """

        array = [x.strip() for x in valueToConvert.split(',')]
        result = ""

        for val in array:
            if result != "":
                result = result+", '"+val+"'"
            else:
                result = "'"+val+"'"

        return "["+result+"]"


def main():
    """
    Set the gui's window size, initialize and launch
    """

    root = Tk()
    root.geometry("500x570+300+300")
    app = MediumBotGUI(root)
    root.mainloop()


if __name__ == '__main__':
    main()
