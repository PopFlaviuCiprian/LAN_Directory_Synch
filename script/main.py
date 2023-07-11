from dirsync import sync
import logging
import schedule
import time


def synchronize():
    sync(r'D:\\Test_backup/folder1', r'\\SERVER/Users/Public/Downloads', 'sync', purge=True, )  # this sync override the files in the second folder #create=True
    logging.basicConfig(filename="log.txt", level=logging.DEBUG,
                    format="%(asctime)s %(message)s")
    logging.debug("Debug logging test ...")
    logging.info("Program sync as expected")
    logging.warning("This event was logged")


schedule.every(10).seconds.do(synchronize)

while True:
    schedule.run_pending()
    time.sleep(2)
