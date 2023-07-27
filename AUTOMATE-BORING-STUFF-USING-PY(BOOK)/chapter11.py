"""
try:
    raise Exception('This is the error message.')
except:
    errorFile = open('test.txt', 'r')
    print('The traceback info was written to errorInfo.txt.')
    errorFile.close()
"""
"""
ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
ages.sort(reverse=True)
print(ages)
assert ages[0] <=ages[-1]
"""


import logging

logging.basicConfig(level=logging.INFO,filename='log.log',filemode='w')
try:
    1/0
except:
    logging.exception("ZeroDivisionError")
    raise Exception('yeh kya ho rha h')


"""
logging.debug('debug')
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.critical('critical')
"""