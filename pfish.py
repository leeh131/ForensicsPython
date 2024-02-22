

# 
# p-fish : Python File System Hash Program
# sample program usage:  > python pfish.py --sha256 -v -d c:\TESTDIR\ -r c:\TESTDIR\
#
#'''
#usage: Python file system hashing .. 
#python p-fish [-h] [-v] (--md5 | --sha256 | --sha512) -d ROOTPATH -r REPORTPATH
#arguments:
#  -h, --help            show this help message and exit
#  -v, --verbose       allows progress messages to be displayed
#  --md5                  specifies MD5 algorithm
#  --sha256              specifies SHA256 algorithm
#  --sha512              specifies SHA512 algorithm
#  -d                    specify the root path for hashing
#  -r                   specify the path where reports and logs will be written
  
 # e.g.         python pfish.py --sha256 -v -d c:\TESTDIR\ -r c:\TESTDIR\
#

import logging                   
import time                        
import sys                           
import _pfish                       

if __name__ == '__main__':

    PFISH_VERSION = '1.0'
    
    # Turn on Logging
    logging.basicConfig(filename='pFishLog.log',level=logging.DEBUG,format='%(levelname)s:%(asctime)s %(message)s %(funcName)s %(filename)s %(processName)s')

    # Process the Command Line Arguments
    _pfish.ParseCommandLine()

    # Record the Starting Time
    startTime = time.time()
    
    # Record the Welcome Message
    logging.info('')
    logging.info('Welcome to p-fish version 1.0 ... New Scan Started')
    logging.info('')
    _pfish.DisplayMessage('Welcome to p-fish ... version '+ PFISH_VERSION)

    # Record some information regarding the system
    logging.info('System: '+ sys.platform)
    logging.info('Version: '+ sys.version)
    
    # Traverse the file system directories and hash the files
    filesProcessed = _pfish.WalkPath()

    # Record the end time and calculate the duration
    endTime = time.time()
    duration = endTime - startTime
    
    
    logging.info('Files Processed: ' + str(filesProcessed) )
    logging.info('Elapsed Time: ' + str(duration) + ' seconds')
    logging.info('')
    logging.info('Program Terminated Normally')
    logging.info('')

    _pfish.DisplayMessage("Program End")
    
