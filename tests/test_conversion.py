import json

import pytest

from src.color.conversion import hex2rgb, hsl2rgb


def get_data() -> dict[str, any]:
    with open("tests/data.json", "r") as f:
        return json.load(f)


@pytest.fixture
def data() -> dict[str, any]:
    return get_data()


def get_hex_decimal(color):
    return color["hex"], color["decimal"]


@pytest.mark.parametrize(
    "input, output",
    list(map(get_hex_decimal, get_data()["colors"])),
)
def test_hex2rgb(input, output):
    result = hex2rgb(input)
    assert result == tuple(output)


def get_hsl_data():
    with open("tests/hsl_color.json", "r") as f:
        return json.load(f)


def get_hsl_decimal(color):
    return color["hsl"], color["rgb"]


@pytest.mark.parametrize("input, output", list(map(get_hsl_decimal, get_hsl_data()["colors"])))
def test_hsl2rgb(input, output):
    print(input, output)
    result = hsl2rgb(*input)
    assert result == tuple(output)
