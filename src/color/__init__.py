"""Convert into RGB color.
"""

# from .color import hsl as hsl
from .color import Color as Color
from .color import rgb as rgb

__all__ = (
    "Color",
    "rgb",
    "hsl",
)
