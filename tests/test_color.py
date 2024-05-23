import json
from importlib import import_module

import pytest

from src.color import Color, from_rgb


def get_data() -> dict[str, any]:
    with open("tests/data.json", "r") as f:
        return json.load(f)


def get_name_rgb(color):
    return color["name"], color["decimal"]


@pytest.mark.parametrize(
    "color_name, rgb_tuple",
    list(map(get_name_rgb, get_data()["colors"])),
)
def test_common_colors(color_name: str, rgb_tuple):
    module = import_module("src.color.defined")
    color: Color = getattr(module, color_name.capitalize())
    result: Color = from_rgb(*rgb_tuple)
    assert color.tuple() == result.tuple()
