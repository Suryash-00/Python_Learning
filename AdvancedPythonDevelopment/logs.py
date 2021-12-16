import logging

logger= logging.getLogger('test_logger')

logging.basicConfig(format='%(asctime)s %(levelname)-8s %(filename)s: %(lineno)d %(message)s', level=logging.DEBUG, filename= 'textlog.txt')

logger.info("This will not show as default")
logger.warning("This will show as default")
logger.error("There's an error!")