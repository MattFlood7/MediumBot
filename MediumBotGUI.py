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

        service = IntVar()
        likePosts = IntVar()
        randomizeLikes = IntVar()
        commentOnPosts = IntVar()
        randomizeComments = IntVar()
        followUsers = IntVar()
        randomizeFollowingUsers = IntVar()
        unfollowUsers = IntVar()
        randomizeUnfollowingUsers = IntVar()
        useRelatedTags = IntVar()
        verbose = IntVar()

        self.parent.title("Medium Bot")
        self.pack(fill=BOTH, expand=True)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(5, pad=7)

        Label(self, text="Email: ").grid(sticky=W, pady=4, padx=5)
        self.emailTextField = Entry(self, width = 100)
        self.emailTextField.grid(row=0, column=1, columnspan = 3)
        self.emailTextField.insert(10, mediumBotVariables["EMAIL"])

        Label(self, text="Password: ").grid(sticky=W, pady=4, padx=5)
        self.passwordField = Entry(self, show="*", width = 100)
        self.passwordField.grid(row=1, column=1, columnspan = 3)
        self.passwordField.insert(10, mediumBotVariables["PASSWORD"])

        Label(self, text="Service: ").grid(sticky=W, pady=4, padx=5)
        self.serviceDropDown = Combobox(self, values=["Google", "Facebook", "Twitter"], width = 100)
        self.serviceDropDown.grid(row=2, column=1, columnspan = 3)

        Label(self, text="Like Posts: ").grid(sticky=W, pady=4, padx=5)
        self.likePostsCheckBox = Checkbutton(self, text="", variable=likePosts)
        self.likePostsCheckBox.grid(row=3, column = 1, columnspan = 3)

        Label(self, text="Randomize Likes: ").grid(sticky=W, pady=4, padx=5)
        self.randomizeLikesCheckBox = Checkbutton(self, text="", variable=randomizeLikes)
        self.randomizeLikesCheckBox.grid(row=4, column = 1, columnspan = 3)

        Label(self, text="Max Likes On Posts: ").grid(sticky=W, pady=4, padx=5)
        self.maxLikesField = Entry(self, width = 100)
        self.maxLikesField.grid(row=5, column=1, columnspan = 3)
        self.maxLikesField.insert(10, mediumBotVariables["MAX_LIKES_ON_POST"])

        Label(self, text="Comment On Posts: ").grid(sticky=W, pady=4, padx=5)
        self.commentPostsCheckBox = Checkbutton(self, text="", variable=commentOnPosts)
        self.commentPostsCheckBox.grid(row=6, column = 1, columnspan = 3)

        Label(self, text="Randomize Comments: ").grid(sticky=W, pady=4, padx=5)
        self.randomizeCommentsCheckBox = Checkbutton(self, text="", variable=randomizeComments)
        self.randomizeCommentsCheckBox.grid(row=7, column = 1, columnspan = 3)

        Label(self, text="Comments: ").grid(sticky=W, pady=4, padx=5)
        self.commentsField = Entry(self, width = 100)
        self.commentsField.grid(row=8, column=1, columnspan = 3)
        self.commentsField.insert(10, mediumBotVariables["COMMENTS"])

        Label(self, text="Article Black List: ").grid(sticky=W, pady=4, padx=5)
        self.articleBlackListField = Entry(self, width = 100)
        self.articleBlackListField.grid(row=9, column=1, columnspan = 3)
        self.articleBlackListField.insert(10, mediumBotVariables["ARTICLE_BLACK_LIST"])

        Label(self, text="Follow Users: ").grid(sticky=W, pady=4, padx=5)
        self.followUsersCheckBox = Checkbutton(self, text="", variable=followUsers)
        self.followUsersCheckBox.grid(row=10, column = 1, columnspan = 3)

        Label(self, text="Randomize Following: ").grid(sticky=W, pady=4, padx=5)
        self.randomizeFollowingCheckBox = Checkbutton(self, text="", variable=randomizeFollowingUsers)
        self.randomizeFollowingCheckBox.grid(row=11, column = 1, columnspan = 3)

        Label(self, text="Unfollow Users: ").grid(sticky=W, pady=4, padx=5)
        self.unfollowUsersCheckBox = Checkbutton(self, text="", variable=unfollowUsers)
        self.unfollowUsersCheckBox.grid(row=12, column = 1, columnspan = 3)

        Label(self, text="Randomize Unfollowing: ").grid(sticky=W, pady=4, padx=5)
        self.randomizeUnfollowingCheckBox = Checkbutton(self, text="", variable=randomizeUnfollowingUsers)
        self.randomizeUnfollowingCheckBox.grid(row=13, column = 1, columnspan = 3)

        Label(self, text="Unfollow Black List: ").grid(sticky=W, pady=4, padx=5)
        self.unfollowBlackListField = Entry(self, width = 100)
        self.unfollowBlackListField.grid(row=14, column=1, columnspan = 3)
        self.unfollowBlackListField.insert(10, mediumBotVariables["UNFOLLOW_USERS_BLACK_LIST"])

        Label(self, text="Use Related Tags: ").grid(sticky=W, pady=4, padx=5)
        self.useRelatedTagsCheckBox = Checkbutton(self, text="", variable=useRelatedTags)
        self.useRelatedTagsCheckBox.grid(row=15, column = 1, columnspan = 3)

        Label(self, text="Articles Per Tag: ").grid(sticky=W, pady=4, padx=5)
        self.articlesPerTagField = Entry(self, width = 100)
        self.articlesPerTagField.grid(row=16, column=1, columnspan = 3)

        Label(self, text="Verbose Output: ").grid(sticky=W, pady=4, padx=5)
        self.verboseCheckBox = Checkbutton(self, text="", variable=verbose)
        self.verboseCheckBox.grid(row=17, column = 1, columnspan = 3)

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

        return True


    def updateMediumBot(self):
        """
        Update the MediumBot with the values in the GUI. Called when the start buttton
        is clicked.
        """

        print "TODO"


    def updateMediumBotVariable(self, variableToUpdate, value):
        """
        Update a variable in the MediumBot.py file.
        variableToUpdate: the variable that is being update in MediumBot.py.
        value: value to update the variable in MediumBot.py to.
        """

        fh, abs_path = mkstemp()
        with open(abs_path,'w') as newFile:

            with open(FILE_PATH) as oldFile:

                for line in oldFile:
                    if variableToUpdate in line and " = " in line and "if" not in line and "elif" not in line:
                        newFile.write(variableToUpdate+" = "+value)
                    else:
                        newFile.write(line)

        close(fh)
        remove(FILE_PATH)
        move(abs_path, FILE_PATH)


def main():
    """
    Set the gui's window size, initialize and launch
    """

    root = Tk()
    root.geometry("500x550+300+300")
    app = MediumBotGUI(root)
    root.mainloop()


if __name__ == '__main__':
    main()
