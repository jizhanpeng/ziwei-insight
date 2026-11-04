import pytest
from iztro_py import astro


@pytest.fixture(scope="module")
def chart():
    """同一份测试数据只排一次盘，供本文件所有用例复用。"""
    return astro.by_solar("1991-8-15", 1, "男", "zh-CN")


def test_chinese_date(chart) -> None:
    assert chart.chinese_date == "辛未 丙申 丁巳 辛丑"


def test_palace_count(chart) -> None:
    assert len(chart.palaces) == 12


def test_soul_palace(chart) -> None:
    assert chart.get_soul_palace().translate_name() == "命宫"


def test_five_elements_class(chart) -> None:
    assert chart.five_elements_class == "金四局"
