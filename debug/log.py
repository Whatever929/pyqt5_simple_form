import logging

class Log(logging.Logger):
    def __init__(self, logger_name, file):
        # Clear the output log file
        super().__init__(logger_name)
        with open(file, "w") as out:
            pass
        f_handler = logging.FileHandler(file)
        f_formatter = logging.Formatter('%(name)s module (%(levelname)s) --- %(message)s')
        f_handler.setFormatter(f_formatter)
        self.addHandler(f_handler)
