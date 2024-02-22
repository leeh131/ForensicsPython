import logging
import time
import _Psearch

if __name__ == '__main__':

    PSEARCH_VERSION = '1.1'
       
    # Turn on Logging
    logging.basicConfig(filename='pSearchLog.log',level=logging.DEBUG,format='%(asctime)s %(message)s')

    # Process the Command Line Arguments
    _Psearch.ParseCommandLine()
   
    log = logging.getLogger('main._Psearch')
    log.info("p-search version" + PSEARCH_VERSION+ " started")

    # Record the Starting Time
    startTime = time.time()
    
    # Perform Keyword Search
    _Psearch.SearchWords()
    
    # Record the Ending Time
    endTime = time.time()    
    duration = endTime - startTime   
    
    logging.info('Elapsed Time: ' + str(duration) + ' seconds')
    logging.info('')
    logging.info('Program Terminated Normally')
