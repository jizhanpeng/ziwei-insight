"""出生时间到排盘时辰索引的转换。

iztro-py 用 0-12 表示时辰：
0=早子（00:00-00:59）
1=丑（01:00-02:59）
2=寅（03:00-04:59）
...
11=亥（21:00-22:59）
12=晚子（23:00-23:59）
"""


def hour_to_index(hour: int) -> int:
    """把 24 小时制的整点转换成 iztro 时辰索引。

    分钟不影响时辰索引：01:00 和 01:59 都属于丑时。
    23 点单独处理为“晚子”，0 点处理为“早子”。
    """
    if not 0 <= hour <= 23:
        raise ValueError(f"hour must be between 0 and 23, got {hour}")

    if hour == 23:
        return 12

    return (hour + 1) // 2
