# dummy_app.py
import os

from logger import Logger

log = Logger(console=True)

class DummyApp:

    def __init__(self):
        log.debug(message="created dummy app")

    def generate_log_messages(self):

        log.info(message="starting dummy run")

        warn = self.busted_function()

        log.warning(warn)

        if os.path.exists("config.yaml"):

            log.debug("loading config file...")

        else:

            log.error("config file not found")

        try:

            log.debug("performing math operation")

            return 1 / 0

        except ZeroDivisionError as ex:
            print(type(ex))
            # log.critical(f"Critical math misunderstanding: {repr(ex)} : {ex}")
            log.critical(message="Critical math misunderstanding", ex=ex)

    def busted_function(self):

        return "Something might be wrong"

app = DummyApp()

app.generate_log_messages()
