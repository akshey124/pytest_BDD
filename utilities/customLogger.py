import logging
import os


class LogGen:
    @staticmethod
    def loggen():
        log_path = 'C:\\Users\\akshe\\PycharmProjects\\Hybridframework\\Logs\\automation.log'

        # Ensure the directory exists
        os.makedirs(os.path.dirname(log_path), exist_ok=True)

        logger = logging.getLogger()
        fhandler = logging.FileHandler(filename=log_path, mode='a')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fhandler.setFormatter(formatter)

        logger.setLevel(logging.DEBUG)
        logger.addHandler(fhandler)

        return logger
