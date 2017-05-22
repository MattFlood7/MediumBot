#!/usr/bin/python
# -*- coding: utf-8 -*-

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

        Label(self, text="Email: ").grid(sticky=W, pady=4, padx=5)
        self.emailField = Entry(self, width = 100)
        self.emailField.grid(row=0, column=1, columnspan = 3)
        self.emailField.insert(10, mediumBotVariables["EMAIL"])

        Label(self, text="Password: ").grid(sticky=W, pady=4, padx=5)
        self.passwordField = Entry(self, show="*", width = 100)
        self.passwordField.grid(row=1, column=1, columnspan = 3)
        self.passwordField.insert(10, mediumBotVariables["PASSWORD"])

        Label(self, text="Service: ").grid(sticky=W, pady=4, padx=5)
        self.serviceDropDown = Combobox(self, values=["Google", "Facebook", "Twitter"], width = 100)
        self.serviceDropDown.grid(row=2, column=1, columnspan = 3)

        Label(self, text="Driver: ").grid(sticky=W, pady=4, padx=5)
        self.driverDropDown = Combobox(self, values=["Chrome", "Firefox/Iceweasel", "PhantomJS"], width = 100)
        self.driverDropDown.grid(row=3, column=1, columnspan = 3)

        Label(self, text="Like Posts: ").grid(sticky=W, pady=4, padx=5)
        self.likePosts = StringVar(value=mediumBotVariables["LIKE_POSTS"])
        self.likePostsCheckBox = Checkbutton(self, text="", variable=self.likePosts, onvalue='True', offvalue='False')
        self.likePostsCheckBox.grid(row=4, column = 1, columnspan = 3)

        Label(self, text="Randomize Likes: ").grid(sticky=W, pady=4, padx=5)
        self.randomizeLikes = StringVar(value=mediumBotVariables["RANDOMIZE_LIKING_POSTS"])
        self.randomizeLikesCheckBox = Checkbutton(self, text="", variable=self.randomizeLikes, onvalue='True', offvalue='False')
        self.randomizeLikesCheckBox.grid(row=5, column = 1, columnspan = 3)

        Label(self, text="Max Likes On Posts: ").grid(sticky=W, pady=4, padx=5)
        self.maxLikesField = Entry(self, width = 100)
        self.maxLikesField.grid(row=6, column=1, columnspan = 3)
        self.maxLikesField.insert(10, mediumBotVariables["MAX_LIKES_ON_POST"])

        Label(self, text="Comment On Posts: ").grid(sticky=W, pady=4, padx=5)
        self.commentOnPosts = StringVar(value=mediumBotVariables["COMMENT_ON_POSTS"])
        self.commentPostsCheckBox = Checkbutton(self, text="", variable=self.commentOnPosts, onvalue='True', offvalue='False')
        self.commentPostsCheckBox.grid(row=7, column = 1, columnspan = 3)

        Label(self, text="Randomize Comments: ").grid(sticky=W, pady=4, padx=5)
        self.randomizeComments = StringVar(value=mediumBotVariables["RANDOMIZE_COMMENTING_ON_POSTS"])
        self.randomizeCommentsCheckBox = Checkbutton(self, text="", variable=self.randomizeComments, onvalue='True', offvalue='False')
        self.randomizeCommentsCheckBox.grid(row=8, column = 1, columnspan = 3)

        Label(self, text="Comments: ").grid(sticky=W, pady=4, padx=5)
        self.commentsField = Entry(self, width = 100)
        self.commentsField.grid(row=9, column=1, columnspan = 3)
        self.commentsField.insert(10, mediumBotVariables["COMMENTS"])

        Label(self, text="Article Black List: ").grid(sticky=W, pady=4, padx=5)
        self.articleBlackListField = Entry(self, width = 100)
        self.articleBlackListField.grid(row=10, column=1, columnspan = 3)
        self.articleBlackListField.insert(10, mediumBotVariables["ARTICLE_BLACK_LIST"])

        Label(self, text="Follow Users: ").grid(sticky=W, pady=4, padx=5)
        self.followUsers = StringVar(value=mediumBotVariables["FOLLOW_USERS"])
        self.followUsersCheckBox = Checkbutton(self, text="", variable=self.followUsers, onvalue='True', offvalue='False')
        self.followUsersCheckBox.grid(row=11, column = 1, columnspan = 3)

        Label(self, text="Randomize Following: ").grid(sticky=W, pady=4, padx=5)
        self.randomizeFollowingUsers = StringVar(value=mediumBotVariables["RANDOMIZE_FOLLOWING_USERS"])
        self.randomizeFollowingCheckBox = Checkbutton(self, text="", variable=self.randomizeFollowingUsers, onvalue='True', offvalue='False')
        self.randomizeFollowingCheckBox.grid(row=12, column = 1, columnspan = 3)

        Label(self, text="Unfollow Users: ").grid(sticky=W, pady=4, padx=5)
        self.unfollowUsers = StringVar(value=mediumBotVariables["UNFOLLOW_USERS"])
        self.unfollowUsersCheckBox = Checkbutton(self, text="", variable=self.unfollowUsers, onvalue='True', offvalue='False')
        self.unfollowUsersCheckBox.grid(row=13, column = 1, columnspan = 3)

        Label(self, text="Randomize Unfollowing: ").grid(sticky=W, pady=4, padx=5)
        self.randomizeUnfollowingUsers = StringVar(value=mediumBotVariables["RANDOMIZE_UNFOLLOWING_USERS"])
        self.randomizeUnfollowingCheckBox = Checkbutton(self, text="", variable=self.randomizeUnfollowingUsers, onvalue='True', offvalue='False')
        self.randomizeUnfollowingCheckBox.grid(row=14, column = 1, columnspan = 3)

        Label(self, text="Unfollow Black List: ").grid(sticky=W, pady=4, padx=5)
        self.unfollowBlackListField = Entry(self, width = 100)
        self.unfollowBlackListField.grid(row=15, column=1, columnspan = 3)
        self.unfollowBlackListField.insert(10, mediumBotVariables["UNFOLLOW_USERS_BLACK_LIST"])

        Label(self, text="Use Related Tags: ").grid(sticky=W, pady=4, padx=5)
        self.useRelatedTags = StringVar(value=mediumBotVariables["USE_RELATED_TAGS"])
        self.useRelatedTagsCheckBox = Checkbutton(self, text="", variable=self.useRelatedTags, onvalue='True', offvalue='False')
        self.useRelatedTagsCheckBox.grid(row=16, column = 1, columnspan = 3)

        Label(self, text="Articles Per Tag: ").grid(sticky=W, pady=4, padx=5)
        self.articlesPerTagField = Entry(self, width = 100)
        self.articlesPerTagField.grid(row=17, column=1, columnspan = 3)
        self.articlesPerTagField.insert(10, mediumBotVariables["ARTICLES_PER_TAG"])

        Label(self, text="Verbose Output: ").grid(sticky=W, pady=4, padx=5)
        self.verbose = StringVar(value=mediumBotVariables["VERBOSE"])
        self.verboseCheckBox = Checkbutton(self, text="", variable=self.verbose, onvalue='True', offvalue='False')
        self.verboseCheckBox.grid(row=18, column = 1, columnspan = 3)

        obtn = Button(self, text="Start Bot", command=self.runMediumBot)
        obtn.grid(row=20, column=3)


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
        # TODO

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
        self.updateMediumBotVariable("RANDOMIZE_FOLLOWING_USERS = "+self.randomizeUnfollowingUsers.get())
        self.updateMediumBotVariable("UNFOLLOW_USERS = "+self.unfollowUsers.get())
        self.updateMediumBotVariable("RANDOMIZE_UNFOLLOWING_USERS = "+self.randomizeUnfollowingUsers.get())
        unfollowConverted = self.convertStringToArrayString(self.unfollowBlackListField.get())
        self.updateMediumBotVariable("UNFOLLOW_USERS_BLACK_LIST = "+unfollowConverted)
        self.updateMediumBotVariable("USE_RELATED_TAGS = "+self.useRelatedTags.get())
        self.updateMediumBotVariable("ARTICLES_PER_TAG = "+self.articlesPerTagField.get())
        self.updateMediumBotVariable("VERBOSE = "+self.verbose.get())


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
                    if variableToUpdate in line and " = " in line and "if" not in line and "elif" not in line and ".lower()" not in line:
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

        return ""


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
