import pytest

from task1 import chunk


@pytest.mark.parametrize(
    "items, size, expected",
    [
        ([1, 2, 3, 4], 2, [[1, 2], [3, 4]]),
        ([1, 2, 3, 4, 5], 2, [[1, 2], [3, 4], [5]]),
        ([1, 2], 5, [[1, 2]]),
        ([], 3, []),
        ([1, 2, 3], 1, [[1], [2], [3]]),
    ],
)
def test_chunk(items: list[int], size: int, expected: list[list[int]]) -> None:
    assert chunk(items, size) == expected


@pytest.mark.parametrize("size", [0, -1])
def test_wrong_size(size: int) -> None:
    with pytest.raises(ValueError):
        chunk([1, 2, 3], size)
