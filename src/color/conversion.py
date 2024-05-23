import re


def hex2rgb(hex: str) -> tuple[int, int, int]:
    """Converts a hex string into a RGB tuple. Raise ValueError if hex is invalid.
    
    Args:
		hex: A hex string. e.g. #fffff
        
    Returns:
		Tuple of RGB in form of [int, int, int].
        
    >>> 
    """
    pattern = re.compile("#(?P<r>[a-f]{2})(?P<g>[a-f]{2})(?P<b>[a-f]{2})", re.IGNORECASE)
    if (match := pattern.match(hex)) is None:
        raise ValueError("")
    else:
        r, g, b = match.groups()
        r, g, b = int(r, 16), int(g, 16), int(b, 16)
        return r, g, b    
