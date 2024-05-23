from typing import Self, overload
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
    def alpha(self) -> float | None:
        return self._alpha


@overload
def rgb(
    r: int,
    g: int,
    b: int,
    *,
    alpha: float | None = None,
) -> Color:
    """Constructs and returns a `Color` with rgb tuple."""
    return Color(r, g, b, alpha=alpha)


@overload
def rgb(hex: str) -> Color:
    """Constructs and returns a `Color` with hex string."""
    r, g, b = hex2rgb(hex)
    return Color(r, g, b, alpha=None)
