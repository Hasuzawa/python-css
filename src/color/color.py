from .conversion import hex2rgb


class Color:

    def __init__(self, r: int, g: int, b: int, *, alpha: float | None = None):
        self._r = r
        self._g = g
        self._b = b
        self._alpha = alpha

    @property
    def r(self) -> int:
        return self._r

    @property
    def g(self) -> int:
        return self._g

    @property
    def b(self) -> int:
        return self._b

    @property
    def opacity(self) -> float | None:
        return self._alpha

    @property
    def alpha(self) -> float | None:
        return self._alpha

    def tuple(self) -> tuple[int, int, int]:
        """A tuple of 3 int of RGB values.

        Returns:
            A RGB tuple.
        """
        return self.r, self.g, self.b

    def hex(self, capitalized: bool = False) -> str:
        r = hex(self._r).lstrip("0x")
        g = hex(self._g).lstrip("0x")
        b = hex(self._b).lstrip("0x")
        s = "#{r}{g}{b}".format(r=r, g=g, b=b)
        if capitalized:
            return s.upper()
        return s


def from_rgb(
    r: int,
    g: int,
    b: int,
    *,
    alpha: float | None = None,
) -> Color:
    """Constructs and returns a `Color` with rgb values.

    Args:
            r: Red value of RGB.
            g: Green value of RGB.
            b: Blue value of RGB.

    Returns:
            A RGB color.
    """
    return Color(r, g, b, alpha=alpha)


def from_hex(hex: str) -> Color:
    """Constructs and returns a `Color` with hex string.

    Args:
            hex: A hex string, e.g. #0d1a3f.

    Returns:
            A RGB color.
    """
    r, g, b = hex2rgb(hex)
    return Color(r, g, b, alpha=None)
