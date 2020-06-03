#!/usr/bin/env python3

# messages
msg = ' library not installed'
repo = 'https://github.com/googleapis/python-firestore'

# colors and shit
good = '\033[92m[+]\033[0m'
bad = '\033[91m[-]\033[0m'

def checkFirestore():
    try:
        from google.cloud import firestore
        return True
    except Exception as firestoreNotInstalledException:
        print (f'Firestore{msg}')
        print (f'Please run -> git clone {repo}, and follow installation process')
        exit()

def checkPathLib():
    try:
        from pathlib import Path
        return True
    except Exception as pathlibNotInstalledException:
        print (f'Path module from pathlib{msg}')

def checkJSON():
    try:
        import json
        return True
    except Exception as jsonNotInstalledException:
        print (f'JSON module{msg}')

def main():
    print ('This script only detects if something is missing')
    json = checkJSON()
    path = checkPathLib()
    firestore = checkFirestore()

    if json == True:
        print (f'%s JSON' % good)
    else:
        print (f'%s JSON' % bad)

    if path == True:
        print (f'%s Pathlib' % good)
    else:
        print (f'%s Pathlib' % bad)

    if firestore == True:
        print (f'%s firestore' % good)
    else:
        print (f'%s firestore' % bad)

if __name__ == '__main__':
    main()
