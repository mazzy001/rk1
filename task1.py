from typing import TypeVar


T = TypeVar("T")


def chunk(items: list[T], size: int) -> list[list[T]]:
    if size < 1:
        raise ValueError("size должен быть не меньше 1")
    return [items[i:i + size] for i in range(0, len(items), size)]
