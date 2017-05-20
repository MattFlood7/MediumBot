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

        mediumBotVariables = parseMediumBot()

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

        emailLabel = Label(self, text="Email: ")
        emailLabel.grid(sticky=W, pady=4, padx=5)
        emailTextField = Entry(self, width = 100)
        emailTextField.grid(row=0, column=1, columnspan = 3)
        emailTextField.insert(10, mediumBotVariables["EMAIL"])

        passwordLabel = Label(self, text="Password: ")
        passwordLabel.grid(sticky=W, pady=4, padx=5)
        passwordField = Entry(self, show="*", width = 100)
        passwordField.grid(row=1, column=1, columnspan = 3)
        passwordField.insert(10, mediumBotVariables["PASSWORD"])

        serviceLabel = Label(self, text="Service: ")
        serviceLabel.grid(sticky=W, pady=4, padx=5)
        serviceDropDown = Combobox(self, values=["Google", "Facebook", "Twitter"], width = 100)
        serviceDropDown.grid(row=2, column=1, columnspan = 3)

        likePostsLabel = Label(self, text="Like Posts: ")
        likePostsLabel.grid(sticky=W, pady=4, padx=5)
        Checkbutton(self, text="", variable=likePosts).grid(row=3, column = 1, columnspan = 3)

        randomizeLikesLabel = Label(self, text="Randomize Likes: ")
        randomizeLikesLabel.grid(sticky=W, pady=4, padx=5)
        Checkbutton(self, text="", variable=randomizeLikes).grid(row=4, column = 1, columnspan = 3)

        maxLikesLabel = Label(self, text="Max Likes On Posts: ")
        maxLikesLabel.grid(sticky=W, pady=4, padx=5)
        maxLikesField = Entry(self, width = 100)
        maxLikesField.grid(row=5, column=1, columnspan = 3)
        maxLikesField.insert(10, mediumBotVariables["MAX_LIKES_ON_POST"])

        commentPostsLabel = Label(self, text="Comment On Posts: ")
        commentPostsLabel.grid(sticky=W, pady=4, padx=5)
        Checkbutton(self, text="", variable=commentOnPosts).grid(row=6, column = 1, columnspan = 3)

        randomizeCommentsLabel = Label(self, text="Randomize Comments: ")
        randomizeCommentsLabel.grid(sticky=W, pady=4, padx=5)
        Checkbutton(self, text="", variable=randomizeComments).grid(row=7, column = 1, columnspan = 3)

        commentsLabel = Label(self, text="Comments: ")
        commentsLabel.grid(sticky=W, pady=4, padx=5)
        commentsField = Entry(self, width = 100)
        commentsField.grid(row=8, column=1, columnspan = 3)
        commentsField.insert(10, mediumBotVariables["COMMENTS"])

        articleBlackListLabel = Label(self, text="Article Black List: ")
        articleBlackListLabel.grid(sticky=W, pady=4, padx=5)
        articleBlackListField = Entry(self, width = 100)
        articleBlackListField.grid(row=9, column=1, columnspan = 3)
        articleBlackListField.insert(10, mediumBotVariables["ARTICLE_BLACK_LIST"])

        followUsersLabel = Label(self, text="Follow Users: ")
        followUsersLabel.grid(sticky=W, pady=4, padx=5)
        Checkbutton(self, text="", variable=followUsers).grid(row=10, column = 1, columnspan = 3)

        randomizeFollowingLabel = Label(self, text="Randomize Following: ")
        randomizeFollowingLabel.grid(sticky=W, pady=4, padx=5)
        Checkbutton(self, text="", variable=randomizeFollowingUsers).grid(row=11, column = 1, columnspan = 3)

        unfollowUsersLabel = Label(self, text="Unfollow Users: ")
        unfollowUsersLabel.grid(sticky=W, pady=4, padx=5)
        Checkbutton(self, text="", variable=unfollowUsers).grid(row=12, column = 1, columnspan = 3)

        randomizeUnfollowingLabel = Label(self, text="Randomize Unfollowing: ")
        randomizeUnfollowingLabel.grid(sticky=W, pady=4, padx=5)
        Checkbutton(self, text="", variable=randomizeUnfollowingUsers).grid(row=13, column = 1, columnspan = 3)

        unfollowBlackListLabel = Label(self, text="Unfollow Black List: ")
        unfollowBlackListLabel.grid(sticky=W, pady=4, padx=5)
        unfollowBlackListField = Entry(self, width = 100)
        unfollowBlackListField.grid(row=14, column=1, columnspan = 3)
        unfollowBlackListField.insert(10, mediumBotVariables["UNFOLLOW_USERS_BLACK_LIST"])

        useRelatedTagsLabel = Label(self, text="Use Related Tags: ")
        useRelatedTagsLabel.grid(sticky=W, pady=4, padx=5)
        Checkbutton(self, text="", variable=useRelatedTags).grid(row=15, column = 1, columnspan = 3)

        articlesPerTagLabel = Label(self, text="Articles Per Tag: ")
        articlesPerTagLabel.grid(sticky=W, pady=4, padx=5)
        articlesPerTagField = Entry(self, width = 100)
        articlesPerTagField.grid(row=16, column=1, columnspan = 3)

        verboseLabel = Label(self, text="Verbose Output: ")
        verboseLabel.grid(sticky=W, pady=4, padx=5)
        Checkbutton(self, text="", variable=verbose).grid(row=17, column = 1, columnspan = 3)

        obtn = Button(self, text="Start Bot")
        obtn.grid(row=20, column=3)


def parseMediumBot():
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


def updateMediumBot():
    """
    Update the MediumBot with the values in the GUI. Called when the start buttton
    is clicked.
    """

    print "TODO"

def updateMediumBotVariable(variableToUpdate, value):
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
