import logging
import os

from datetime import datetime

if not os.path.exists("translation_test.log"):
    open("translation_test.log", 'x')

now = datetime.now()
date = now.strftime("%Y/%m/%d %A %I:%M:%S%p")

logging.basicConfig(filename="translation_test.log", level=logging.DEBUG)
test_logger = logging.getLogger(' TIME: -{}- TEST ** '.format(date))
