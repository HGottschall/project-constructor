from typing import TypeVar, Any, TypeGuard, Dict, List
from src.shared.utils.ErrorMessages.errors_level import AlertLevel

from src.shared.utils.ErrorMessages.custom_errors import (
    display_error_message,
)

K = TypeVar("K")
V = TypeVar("V")
T = TypeVar("T")


class DataValidatorType:
    @staticmethod
    def is_dict_of(
        value: Any, key_type: type[K], value_type: type[V]
    ) -> TypeGuard[Dict[K, V]]:
        if not isinstance(value, dict):
            return False
        return all(
            isinstance(k, key_type) and isinstance(v, value_type)
            for k, v in value.items()
        )

    @staticmethod
    def is_list_of(value: Any, type_: type[T]) -> TypeGuard[List[T]]:
        if not isinstance(value, list):
            return False
        return all(isinstance(item, type_) for item in value)

    @staticmethod
    def is_instance_of(value: Any, type_: Any) -> TypeGuard[Any]:
        if type_ in (dict, list):
            display_error_message(
                AlertLevel.CRITICAL,
                "is_instance_of is not recommended for dictionaries or lists. Use is_dict_of or is_list_of",
            )

        if isinstance(value, type_):
            return True
        return False

    @staticmethod
    def is_empty(value: Any) -> TypeGuard[Any]:
        if value is None or value == "":
            return True
        return False
