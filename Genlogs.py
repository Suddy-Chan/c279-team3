import logging
import datetime

x=datetime.datetime.now().strftime("%Y%m%d")
logging.basicConfig(filename="log_%s.txt"%x, level=logging.DEBUG, format="%(asctime)s %(message)s")
logging.debug("Debug logging test...")
logging.info("Program is working as expected")
logging.warning("Warning, the program may not function properly")
logging.error("The program encountered an error")
logging.critical("The program crashed")
