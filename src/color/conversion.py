import re


def hex2rgb(hex: str) -> tuple[int, int, int]:
    """Converts a hex string into a RGB tuple. Case is ignored when handling the string.

    Args:
        hex: A hex string. e.g. #fffff

    Returns:
        Tuple of RGB in form of (int, int, int).

    Raises:
        ValueError: The hex string is invalid.

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
    """Converts HSL color values into a RGB tuple.

    Args:
        hue: The hue of a HSL color, in angle.
        saturation: The saturation of a HSL color. Should be between 0 and 1.
        lightness: The lightness of a HSL color. Should be between 0 and 1.

    Returns:
        A Tuple of RGB in form of (int, int, int).

    >>> hsl2rgb(180, 1.0, 0.5)  # (0, 255, 255)

    Algorithm given by CSS Color Module Level 3.

    See more:
        https://www.w3.org/TR/css-color-3/#hsl-color
    """
    hue = hue % 360
    if hue < 0:
        hue += 360

    def f(n) -> float:
        k = (n + hue / 30) % 12
        a = saturation * min(lightness, 1 - lightness)
        return lightness - a * max(-1, min(k - 3, 9 - k, 1))

    cap = 255

    def normalize(x: float) -> int:
        return round(cap * x)

    return tuple(map(normalize, (f(0), f(8), f(4))))
