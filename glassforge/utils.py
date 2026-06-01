"""
Utility functions for GlassForge CLI.

Provides color manipulation, file output helpers, and validation utilities.
All implementations use only Python standard library.
"""

import os
import re
import json
import webbrowser
import tempfile
from typing import Tuple, Optional, Dict, Any


# ---------------------------------------------------------------------------
# Color utilities
# ---------------------------------------------------------------------------

def hex_to_rgb(hex_color: str) -> Tuple[int, int, int]:
    """Convert a hex color string to an (R, G, B) tuple.

    Supports both 3-digit (#RGB) and 6-digit (#RRGGBB) formats.

    Args:
        hex_color: Hex color string, with or without leading '#'.

    Returns:
        Tuple of (red, green, blue) integers (0-255).

    Raises:
        ValueError: If the hex string is invalid.
    """
    hex_color = hex_color.strip().lstrip("#")

    if len(hex_color) == 3:
        hex_color = "".join(c * 2 for c in hex_color)
    elif len(hex_color) != 6:
        raise ValueError(
            f"Invalid hex color: '{hex_color}'. Expected 3 or 6 hex digits."
        )

    try:
        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)
    except ValueError:
        raise ValueError(f"Invalid hex color: '{hex_color}'. Not valid hex digits.")

    return (r, g, b)


def rgb_to_hex(r: int, g: int, b: int) -> str:
    """Convert (R, G, B) integers to a hex color string.

    Args:
        r: Red component (0-255).
        g: Green component (0-255).
        b: Blue component (0-255).

    Returns:
        Hex color string like '#RRGGBB'.
    """
    return f"#{r:02x}{g:02x}{b:02x}"


def rgb_to_hsl(r: int, g: int, b: int) -> Tuple[float, float, float]:
    """Convert RGB to HSL (Hue, Saturation, Lightness).

    Args:
        r: Red (0-255).
        g: Green (0-255).
        b: Blue (0-255).

    Returns:
        Tuple of (hue 0-360, saturation 0-100, lightness 0-100).
    """
    r_norm = r / 255.0
    g_norm = g / 255.0
    b_norm = b / 255.0

    c_max = max(r_norm, g_norm, b_norm)
    c_min = min(r_norm, g_norm, b_norm)
    delta = c_max - c_min

    # Lightness
    l = (c_max + c_min) / 2.0

    # Saturation
    if delta == 0:
        s = 0.0
    else:
        s = delta / (1.0 - abs(2.0 * l - 1.0)) if (1.0 - abs(2.0 * l - 1.0)) != 0 else 0.0

    # Hue
    if delta == 0:
        h = 0.0
    elif c_max == r_norm:
        h = 60.0 * (((g_norm - b_norm) / delta) % 6)
    elif c_max == g_norm:
        h = 60.0 * (((b_norm - r_norm) / delta) + 2)
    else:
        h = 60.0 * (((r_norm - g_norm) / delta) + 4)

    return (round(h, 2), round(s * 100, 2), round(l * 100, 2))


def adjust_lightness(hex_color: str, amount: float) -> str:
    """Adjust the lightness of a hex color.

    Args:
        hex_color: Hex color string.
        amount: Amount to adjust lightness (-100 to +100).

    Returns:
        Adjusted hex color string.
    """
    r, g, b = hex_to_rgb(hex_color)
    h, s, l = rgb_to_hsl(r, g, b)
    l = max(0, min(100, l + amount))
    return hsl_to_hex(h, s, l)


def hsl_to_hex(h: float, s: float, l: float) -> str:
    """Convert HSL to hex color string.

    Args:
        h: Hue (0-360).
        s: Saturation (0-100).
        l: Lightness (0-100).

    Returns:
        Hex color string.
    """
    s_norm = s / 100.0
    l_norm = l / 100.0

    c = (1.0 - abs(2.0 * l_norm - 1.0)) * s_norm
    x = c * (1.0 - abs((h / 60.0) % 2 - 1.0))
    m = l_norm - c / 2.0

    if h < 60:
        r1, g1, b1 = c, x, 0
    elif h < 120:
        r1, g1, b1 = x, c, 0
    elif h < 180:
        r1, g1, b1 = 0, c, x
    elif h < 240:
        r1, g1, b1 = 0, x, c
    elif h < 300:
        r1, g1, b1 = x, 0, c
    else:
        r1, g1, b1 = c, 0, x

    r = round((r1 + m) * 255)
    g = round((g1 + m) * 255)
    b = round((b1 + m) * 255)

    return rgb_to_hex(r, g, b)


def hex_to_rgba(hex_color: str, alpha: float) -> str:
    """Convert hex color to CSS rgba() string.

    Args:
        hex_color: Hex color string.
        alpha: Opacity value (0.0 to 1.0).

    Returns:
        CSS rgba() string.
    """
    r, g, b = hex_to_rgb(hex_color)
    return f"rgba({r}, {g}, {b}, {alpha})"


def validate_hex_color(color: str) -> bool:
    """Validate a hex color string.

    Args:
        color: String to validate.

    Returns:
        True if valid hex color, False otherwise.
    """
    pattern = r"^#?([0-9a-fA-F]{3}|[0-9a-fA-F]{6})$"
    return bool(re.match(pattern, color.strip()))


# ---------------------------------------------------------------------------
# File output utilities
# ---------------------------------------------------------------------------

def write_output(content: str, output_path: Optional[str] = None) -> str:
    """Write generated content to a file or stdout.

    If output_path is None, returns the content string.
    If output_path is '-', prints to stdout.
    Otherwise writes to the specified file path.

    Args:
        content: The content to output.
        output_path: File path to write to, or None for return.

    Returns:
        The file path written to, or the content itself if no path given.
    """
    if output_path is None:
        return content

    if output_path == "-":
        print(content)
        return "<stdout>"

    # Ensure directory exists
    directory = os.path.dirname(output_path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)

    return output_path


def open_in_browser(html_content: str) -> bool:
    """Open HTML content in the default browser using a temp file.

    Args:
        html_content: Complete HTML string to display.

    Returns:
        True if browser opened successfully, False otherwise.
    """
    try:
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".html", delete=False, encoding="utf-8"
        ) as f:
            f.write(html_content)
            temp_path = f.name

        webbrowser.open(f"file://{temp_path}")
        return True
    except Exception:
        return False


# ---------------------------------------------------------------------------
# Validation utilities
# ---------------------------------------------------------------------------

def validate_blur(value: int) -> int:
    """Validate and clamp blur value to valid range.

    Args:
        value: Blur value in pixels.

    Returns:
        Clamped blur value (0-50).
    """
    return max(0, min(50, value))


def validate_opacity(value: float) -> float:
    """Validate and clamp opacity value to valid range.

    Args:
        value: Opacity value.

    Returns:
        Clamped opacity value (0.0-1.0).
    """
    return max(0.0, min(1.0, round(value, 2)))


def validate_border_radius(value: int) -> int:
    """Validate and clamp border radius value.

    Args:
        value: Border radius in pixels.

    Returns:
        Clamped border radius (0-100).
    """
    return max(0, min(100, value))


def validate_gloss(value: float) -> float:
    """Validate and clamp gloss intensity value.

    Args:
        value: Gloss intensity value.

    Returns:
        Clamped gloss value (0.0-1.0).
    """
    return max(0.0, min(1.0, round(value, 2)))


# ---------------------------------------------------------------------------
# Misc utilities
# ---------------------------------------------------------------------------

def build_css_vars(params: Dict[str, Any]) -> str:
    """Build a CSS custom properties block from a parameter dictionary.

    Args:
        params: Dictionary of CSS variable names to values.

    Returns:
        CSS custom properties string block.
    """
    lines = [":root {"]
    for key, value in params.items():
        css_key = f"--glass-{key}" if not key.startswith("--") else key
        lines.append(f"  {css_key}: {value};")
    lines.append("}")
    return "\n".join(lines)


def indent(text: str, spaces: int = 2) -> str:
    """Indent each line of text by the given number of spaces.

    Args:
        text: Multi-line text string.
        spaces: Number of spaces for indentation.

    Returns:
        Indented text string.
    """
    prefix = " " * spaces
    return "\n".join(prefix + line for line in text.split("\n"))
