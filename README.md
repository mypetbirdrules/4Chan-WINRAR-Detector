# 4Chan-WINRAR-Detector
The script parses a 4chan thread and finds people with dubs, trips, or quads. Arguably useful.

Install the needed dependencies:

>sudo pip install basc_py4chan


The script is designed to run in Python 3 but it may run in Python 2 [Not Recommended].

The script requires certain flags to be used regardless or the script will fail.
Here they are:

>--board

>--thread

Writing results to a file is also supported:

> ./dubsget.py --board [BOARD] --thread [THREAD ID] --all --output allgets.txt
