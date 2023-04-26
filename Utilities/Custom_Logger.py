import logging
import inspect

def CustomLogger(loggerName, logLevel = logging.DEBUG, FMT= '%(asctime)s: %(name)s: %(levelname)s: %(message)s'):

    # We can fetch the name of class or method calling this function by  (OPTIONAL, ignore this)
    parentName = inspect.stack()[1][3]

    logger = logging.getLogger(parentName)
    logger.setLevel(logLevel)

    fileName = loggerName + ".log"
    handler = logging.FileHandler(filename=fileName, mode="w")

    # handler = logging.FileHandler("{0}.log", mode="w")
    handler.setLevel(logLevel)

    # formatter = logging.Formatter('%(asctime)s: %(name)s: %(levelname)s: %(message)s', datefmt='%m/%d/%y %I:%M:%S:%p')
    formatter = logging.Formatter(fmt=FMT, datefmt='%m/%d/%y %I:%M:%S:%p')

    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger



