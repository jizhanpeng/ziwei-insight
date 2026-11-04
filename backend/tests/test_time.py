import pytest

from app.domain.chart.time import hour_to_index


@pytest.mark.parametrize(
    ("hour", "expected"),
    [
        (0, 0),   # 早子
        (1, 1),   # 丑
        (2, 1),
        (3, 2),   # 寅
        (4, 2),
        (5, 3),   # 卯
        (6, 3),
        (7, 4),   # 辰
        (8, 4),
        (9, 5),   # 巳
        (10, 5),
        (11, 6),  # 午
        (12, 6),
        (13, 7),  # 未
        (14, 7),
        (15, 8),  # 申
        (16, 8),
        (17, 9),  # 酉
        (18, 9),
        (19, 10), # 戌
        (20, 10),
        (21, 11), # 亥
        (22, 11),
        (23, 12), # 晚子
    ],
)
def test_hour_to_index(hour: int, expected: int) -> None:
    assert hour_to_index(hour) == expected


def test_hour_to_index_rejects_out_of_range() -> None:
    with pytest.raises(ValueError, match="hour"):
        hour_to_index(24)
