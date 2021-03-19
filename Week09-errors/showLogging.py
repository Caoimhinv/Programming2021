import logging
# logging.basicConfig(level =logging.INFO)
# logging.basicConfig(level =logging.ERROR)
logging.basicConfig(filename='./debugging.log', 
    filemode='a', 
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s - line: %(lineno)d')
name = "Joe"

logging.error("this is an error")
logging.critical("hiya")
logging.warning("don't know %s", name)
logging.info("still going")
logging.debug("and so is this")