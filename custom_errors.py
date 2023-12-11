from colorama import Fore, Style
from src.shared.utils.ErrorMessages.errors_level import AlertLevel


def display_error_message(level: AlertLevel, error_message: str) -> None:
    color = {
        AlertLevel.INFO: Fore.BLUE,
        AlertLevel.WARNING: Fore.YELLOW,
        AlertLevel.ERROR: Fore.RED,
        AlertLevel.CRITICAL: Fore.MAGENTA,
    }.get(level, Fore.WHITE)

    print(color + f"{level.name}: {error_message}" + Style.RESET_ALL)


class CustomError(Exception):
    def __init__(self, level: AlertLevel, error_message: str):
        self.level = level
        self.error_message = error_message
        super().__init__(self.error_message)
