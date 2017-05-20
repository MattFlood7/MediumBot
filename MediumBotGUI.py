#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
MediumBot's configuration GUI to make it easier for non-technical users to use
the bot.
Note: this is a starting point for the GUI and is not finished.
"""

from Tkinter import *
from ttk import *

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
        emailTextField = Entry(self)
        emailTextField.grid(row=0, column=1)

        passwordLabel = Label(self, text="Password: ")
        passwordLabel.grid(sticky=W, pady=4, padx=5)
        passwordField = Entry(self)
        passwordField.grid(row=1, column=1)

        serviceLabel = Label(self, text="Service: ")
        serviceLabel.grid(sticky=W, pady=4, padx=5)
        #serviceField = Entry(self)
        #serviceField.grid(row=2, column=1)
        Radiobutton(self, text="Google", variable=1, value=0).grid(row=2, column = 1)
        Radiobutton(self, text="FaceBook", variable=2, value=0).grid(row=2, column = 2)
        Radiobutton(self, text="Twitter", variable=3, value=0).grid(row=2, column = 3)

        likePostsLabel = Label(self, text="Like Posts: ")
        likePostsLabel.grid(sticky=W, pady=4, padx=5)
        Checkbutton(self, text="", variable=likePosts).grid(row=3, column = 1)

        randomizeLikesLabel = Label(self, text="Randomize Likes: ")
        randomizeLikesLabel.grid(sticky=W, pady=4, padx=5)
        Checkbutton(self, text="", variable=randomizeLikes).grid(row=4, column = 1)

        maxLikesLabel = Label(self, text="Max Likes On Posts: ")
        maxLikesLabel.grid(sticky=W, pady=4, padx=5)
        maxLikesField = Entry(self)
        maxLikesField.grid(row=5, column=1)

        commentPostsLabel = Label(self, text="Comment On Posts: ")
        commentPostsLabel.grid(sticky=W, pady=4, padx=5)
        Checkbutton(self, text="", variable=commentOnPosts).grid(row=6, column = 1)

        randomizeCommentsLabel = Label(self, text="Randomize Comments: ")
        randomizeCommentsLabel.grid(sticky=W, pady=4, padx=5)
        Checkbutton(self, text="", variable=randomizeComments).grid(row=7, column = 1)

        commentsLabel = Label(self, text="Comments: ")
        commentsLabel.grid(sticky=W, pady=4, padx=5)
        commentsField = Entry(self)
        commentsField.grid(row=8, column=1)

        articleBlackListLabel = Label(self, text="Article Black List: ")
        articleBlackListLabel.grid(sticky=W, pady=4, padx=5)
        articleBlackListField = Entry(self)
        articleBlackListField.grid(row=9, column=1)

        followUsersLabel = Label(self, text="Follow Users: ")
        followUsersLabel.grid(sticky=W, pady=4, padx=5)
        Checkbutton(self, text="", variable=followUsers).grid(row=10, column = 1)

        randomizeFollowingLabel = Label(self, text="Randomize Following: ")
        randomizeFollowingLabel.grid(sticky=W, pady=4, padx=5)
        Checkbutton(self, text="", variable=randomizeFollowingUsers).grid(row=11, column = 1)

        unfollowUsersLabel = Label(self, text="Unfollow Users: ")
        unfollowUsersLabel.grid(sticky=W, pady=4, padx=5)
        Checkbutton(self, text="", variable=unfollowUsers).grid(row=12, column = 1)

        randomizeUnfollowingLabel = Label(self, text="Randomize Unfollowing: ")
        randomizeUnfollowingLabel.grid(sticky=W, pady=4, padx=5)
        Checkbutton(self, text="", variable=randomizeUnfollowingUsers).grid(row=13, column = 1)

        unfollowBlackListLabel = Label(self, text="Unfollow Black List: ")
        unfollowBlackListLabel.grid(sticky=W, pady=4, padx=5)
        unfollowBlackListField = Entry(self)
        unfollowBlackListField.grid(row=14, column=1)

        useRelatedTagsLabel = Label(self, text="Use Related Tags: ")
        useRelatedTagsLabel.grid(sticky=W, pady=4, padx=5)
        Checkbutton(self, text="", variable=useRelatedTags).grid(row=15, column = 1)

        articlesPerTagLabel = Label(self, text="Articles Per Tag: ")
        articlesPerTagLabel.grid(sticky=W, pady=4, padx=5)
        articlesPerTagField = Entry(self)
        articlesPerTagField.grid(row=16, column=1)

        verboseLabel = Label(self, text="Verbose Output: ")
        verboseLabel.grid(sticky=W, pady=4, padx=5)
        Checkbutton(self, text="", variable=verbose).grid(row=17, column = 1)

        #area = Text(self)
        #area.grid(row=1, column=0, columnspan=2, rowspan=4, padx=5, sticky=E+W+S+N)

        obtn = Button(self, text="Start Bot")
        obtn.grid(row=20, column=3)


def main():

    root = Tk()
    root.geometry("500x550+300+300")
    app = MediumBotGUI(root)
    root.mainloop()


if __name__ == '__main__':
    main()
