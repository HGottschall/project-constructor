import time
from typing import Any, Callable
import psutil


def timer(func: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(
            f"Tempo de execução de {func.__name__}: {round(end_time - start_time, 2)}"
        )
        return result

    return wrapper


def cpu_usage(func: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        before = psutil.cpu_percent(interval=None)
        result = func(*args, **kwargs)
        after = psutil.cpu_percent(interval=None)
        print(f"Uso da CPU antes da execução de {func.__name__}: {before}%")
        print(f"Uso da CPU após a execução de {func.__name__}: {after}%")
        return result

    return wrapper


def ram_memory_usage(func: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        before = psutil.virtual_memory().used
        result = func(*args, **kwargs)
        after = psutil.virtual_memory().used
        print(f"Uso de memória antes da execução: {before}")
        print(f"Uso de memória após a execução: {after}")
        return result

    return wrapper
