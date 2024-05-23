import re


def hex2rgb(hex: str) -> tuple[int, int, int]:
    """Converts a hex string into a RGB tuple. Raise ValueError if hex is valid color string.

    Args:
        hex: A hex string. e.g. #fffff

    Returns:
        Tuple of RGB in form of [int, int, int].

    >>> hex2rgb("#ffffff")  # (255, 255, 255)
    """
    pattern = re.compile("#(?P<r>[0-9a-f]{2})(?P<g>[0-9a-f]{2})(?P<b>[0-9a-f]{2})", re.IGNORECASE)
    if (match := pattern.match(hex)) is None:
        raise ValueError("{hex} is not a valid hex color string".format(hex))
    else:
        r, g, b = match.groups()
        r, g, b = int(r, 16), int(g, 16), int(b, 16)
        return r, g, b


def hsl2rgb(hue: int, saturation: float, lightness: float) -> tuple[int, int, int]:
    """Converts HSL color values into RGB values."""
    hue = hue % 360
    if hue < 0:
        hue += 360

    saturation /= 100
    lightness /= 100

    def f(n) -> float:
        k = (n + hue / 30) % 12
        a = saturation * min(lightness, 1 - lightness)
        return lightness - a * max(-1, min(k - 3, 9 - k, 1))

    return f(0), f(8), f(4)
