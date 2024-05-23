"""Convert into RGB color.
"""

from . import defined as defined
from .color import Color as Color
from .color import from_hex as from_hex
from .color import from_rgb as from_rgb

__all__ = (
    "Color",
    "rgb",
    "hsl",
)
