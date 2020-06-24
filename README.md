Fireclient
===========

Python client for automating multiple redudant changes to Firestore without entering the web UI

<p align="center"><img src="https://github.com/DiracSpace/Fireclient/blob/master/Fireclient-pictures/fireclient-v0.1.4-patch-02.png" /></p>

Installation
-------------
The python version >= 3.8.3 with the following packages:
1. subprocess
2. JSON
3. pathlib
4. [Googleapis/Python Client](https://github.com/googleapis/python-firestore)

Important
---------
You will need the keyfile.json file from Cloud Firestore located in Project Settings > Integrated Services > Generate new keyfile. The script detects and tells you how to export the path of keyfile.json for correct execution.

# Note
Only tested on Linux distributions - June 2, 2020. Will proceed to make adjustments for Windows based operating systems
