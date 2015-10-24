#!/bin/python

import basc_py4chan
import sys
import time

#defining methods
def identicalDigits(inputList):
    commonNumber = inputList[0]
    identical = True
    for item in inputList:
        if commonNumber != int(item):
            identical = False
    return identical

def digitsGet(ID):
    numList = [int(c) for c in str(ID)]
    if identicalDigits(numList[-4:]):
        return "quads"
    elif identicalDigits(numList[-3:]):
        return "trips"
    elif identicalDigits(numList[-2:]):
        return "dubs"

#defining default variables
boardLetter = "b"
threadID = 0

dubs = False
trips = False
quads = False

outputIntoFile = False
outputFile = "NULL"

if len(sys.argv) == 1:
    print("Run ./dubsget --help to get help")
else:
    if sys.argv[1] == "--help":
        print("--board  | Select board to scan")
        print("--thread | Select thread ID to scan")
        print("--all   | Search for dubs, trips, and quads")
        print("--dubs   | Only scan for dubs")
        print("--trips  | Only scan for trips")
        print("--quads  | Only scan for quads")
        print("--output | Put output into file")
        print("GPL LICENSE GANOO/LUNIX -- ANON -- Python 3.*")
    if len(sys.argv) > 2:
        cliArgs = sys.argv[1:]
        arg = 0
        while arg < len(cliArgs):
            arg = arg + 1
            if cliArgs[arg - 1] == "--board":
                boardLetter = cliArgs[arg]
            elif cliArgs[arg - 1] == "--thread":
                threadID = int(cliArgs[arg])
            elif cliArgs[arg - 1] == "--all":
                dubs = True
                trips = True
                quads = True
            elif cliArgs[arg - 1] == "--dubs":
                dubs = True
            elif cliArgs[arg - 1] == "--trips":
                trips = True
            elif cliArgs[arg - 1] == "--quads":
                quads = True
            elif cliArgs[arg - 1] == "--times":
                times = int(cliArgs[arg])
            elif cliArgs[arg - 1] == "--delay":
                delay = int(cliArgs[arg])
            elif cliArgs[arg - 1] == "--output":
                outputIntoFile = True
                outputFile = cliArgs[arg]

        print("Here\'s what I\'m doing:")
        print("------------------------")
        print("Board: " + boardLetter)
        print("Thread ID: " + str(threadID))
        print("Dubs?: " + str(dubs).lower())
        print("Trips?: " + str(trips).lower())
        print("Quads?: " + str(quads).lower())
        print("Output to File?: " + str(outputIntoFile).lower())

        if outputIntoFile == True:
            print("Output File: " + outputFile)

        print("------------------------")

        if outputIntoFile == True:
            output = open(outputFile, 'w')

        board = basc_py4chan.Board(boardLetter)
        thread = board.get_thread(threadID)

        print("Starting the main connection loop...")
        print("Returning the posts in the thread...")

        winrars = 0

        posts = thread.posts
        updateNum = len(posts)
        print("Fetched " + str(updateNum) + " posts")

        print("Checking for WINRARS")
        print("---------------")

        for post in posts:
            if (digitsGet(post.post_id) == "quads") and (quads == True):
                if outputIntoFile == False:
                    print("WINRAR! Post " + str(post.post_id) + " has quads!")
                else:
                    output.write("WINRAR! Post " + str(post.post_id) + " has quads!" + "\n")
            if (digitsGet(post.post_id) == "trips") and (trips == True):
                if outputIntoFile == False:
                    print("WINRAR! Post " + str(post.post_id) + " has trips!")
                else:
                    output.write("WINRAR! Post " + str(post.post_id) + " has trips!" + "\n")
            if (digitsGet(post.post_id) == "dubs") and (dubs == True):
                if outputIntoFile == False:
                    print("WINRAR! Post " + str(post.post_id) + " has dubs!")
                else:
                    output.write("WINRAR! Post " + str(post.post_id) + " has dubs!" + "\n")
