# logger.py
import inspect
import logging
import warnings
import traceback
from colorama import Fore


class Logger:

    def __init__(self, name=__name__, log_file: str=None, console: bool=True):

        if any([log_file, console]) is True:

            pass

        else:

            warning_msg = (
                "Is the logger correctly configured? It's not sending log messages anywhere: "
                f"log_file={log_file}, console={console}"
                )

            with warnings.catch_warnings(record=True) as w:

                warnings.simplefilter("always", UserWarning)

                warnings.warn(warning_msg, UserWarning)

            for warning in w:

                if issubclass(warning.category, UserWarning):

                    print(f"{Fore.RED}{warning.category.__name__}: {Fore.RESET}{warning.message}")

        self.logger = logging.getLogger(name)

        self.logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")

        if log_file is not None:

            file_handler = logging.FileHandler(log_file)

            file_handler.setLevel(logging.DEBUG)

            file_handler.setFormatter(formatter)

            self.logger.addHandler(file_handler)

        if console is True:

            console_handler = logging.StreamHandler()

            console_handler.setLevel(logging.DEBUG)

            console_handler.setFormatter(formatter)

            self.logger.addHandler(console_handler)

    def debug(self, message: str, ex: Exception=None):

        function_name = self.function_name_from_trace()

        if ex is not None:

            ex_info = self.extract_exception_info(ex=ex)

            message = " ".join([message, ex_info])

            self.logger.debug(message)

        else:

            message = f"{function_name}: {message}"

            self.logger.debug(message)


    def info(self, message: str, ex: Exception=None):

        function_name = self.function_name_from_trace()

        if ex is not None:

            ex_info = self.extract_exception_info(ex=ex)

            message = " ".join([message, ex_info])

            self.logger.info(message)

        else:

            message = f"{function_name}: {message}"

            self.logger.info(message)

    def warning(self, message: str, ex: Exception=None):

        function_name = self.function_name_from_trace()

        if ex is not None:

            ex_info = self.extract_exception_info(ex=ex)

            message = " ".join([message, ex_info])

            self.logger.warning(message)

        else:

            message = f"{function_name}: {message}"

            self.logger.warning(message)

    def error(self, message: str, ex: Exception=None):

        function_name = self.function_name_from_trace()

        if ex is not None:

            ex_info = self.extract_exception_info(ex=ex)

            message = " ".join([message, ex_info])

            self.logger.error(message)

        else:

            message = f"{function_name}: {message}"

            self.logger.error(message)

    def critical(self, message: str, ex=None):

        function_name = self.function_name_from_trace()

        if ex is not None:

            ex_info = self.extract_exception_info(ex=ex)

            message = " ".join([message, ex_info])

            self.logger.critical(message)

        else:

            message = f"{function_name}: {message}"

            self.logger.critical(message)

    def function_name_from_trace(self):

        try:
            stack_trace = inspect.stack()

            level = stack_trace[-2]

            function_name = level.function.strip()

            return function_name

        except Exception:

            return str()

    def extract_exception_info(self, ex: Exception) -> str:

        try:

            filename, line, func, text = traceback.extract_tb(ex.__traceback__)[-1]

            ex_info = f"Exception: {repr(ex)}: {filename}, line {line}, {func}, {text}"

            return ex_info

        except Exception:

            return str()
 