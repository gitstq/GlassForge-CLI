"""
Theme presets for GlassForge CLI.

Each preset defines a unique visual configuration for the liquid glass effect,
including colors, blur levels, opacity, and other visual parameters.
"""

from typing import Dict, Any


# ---------------------------------------------------------------------------
# Preset theme definitions
# ---------------------------------------------------------------------------

PRESETS: Dict[str, Dict[str, Any]] = {
    "crystal": {
        "name": "Crystal",
        "name_zh": "水晶",
        "description": "Transparent and clear with white highlights",
        "description_zh": "透明清亮，白色高光",
        "primary_color": "#ffffff",
        "secondary_color": "#e8f4fd",
        "gradient_start": "rgba(255, 255, 255, 0.25)",
        "gradient_end": "rgba(255, 255, 255, 0.05)",
        "border_color": "rgba(255, 255, 255, 0.3)",
        "shadow_color": "rgba(0, 0, 0, 0.1)",
        "text_color": "#1a1a2e",
        "blur": 20,
        "opacity": 0.2,
        "saturate": 1.8,
        "border_radius": 24,
        "gloss": 0.8,
        "background_gradient": "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
        "hover_scale": 1.02,
    },
    "aurora": {
        "name": "Aurora",
        "name_zh": "极光",
        "description": "Blue-green gradient with a dreamy feel",
        "description_zh": "蓝绿渐变，梦幻感",
        "primary_color": "#00d2ff",
        "secondary_color": "#7b2ff7",
        "gradient_start": "rgba(0, 210, 255, 0.2)",
        "gradient_end": "rgba(123, 47, 247, 0.08)",
        "border_color": "rgba(0, 210, 255, 0.25)",
        "shadow_color": "rgba(0, 100, 200, 0.15)",
        "text_color": "#e0f7ff",
        "blur": 24,
        "opacity": 0.25,
        "saturate": 2.0,
        "border_radius": 28,
        "gloss": 0.7,
        "background_gradient": "linear-gradient(135deg, #0c0e23 0%, #1a1a4e 50%, #0d2137 100%)",
        "hover_scale": 1.03,
    },
    "ocean": {
        "name": "Ocean",
        "name_zh": "深海",
        "description": "Deep blue gradient, calm and steady",
        "description_zh": "深蓝渐变，沉稳",
        "primary_color": "#0066cc",
        "secondary_color": "#003366",
        "gradient_start": "rgba(0, 102, 204, 0.2)",
        "gradient_end": "rgba(0, 51, 102, 0.08)",
        "border_color": "rgba(0, 150, 255, 0.2)",
        "shadow_color": "rgba(0, 50, 150, 0.2)",
        "text_color": "#c8e6ff",
        "blur": 18,
        "opacity": 0.3,
        "saturate": 1.5,
        "border_radius": 20,
        "gloss": 0.5,
        "background_gradient": "linear-gradient(135deg, #001a33 0%, #003366 50%, #001a33 100%)",
        "hover_scale": 1.02,
    },
    "lava": {
        "name": "Lava",
        "name_zh": "熔岩",
        "description": "Red-orange gradient, passionate and intense",
        "description_zh": "红橙渐变，热烈",
        "primary_color": "#ff4500",
        "secondary_color": "#ff8c00",
        "gradient_start": "rgba(255, 69, 0, 0.2)",
        "gradient_end": "rgba(255, 140, 0, 0.08)",
        "border_color": "rgba(255, 100, 0, 0.3)",
        "shadow_color": "rgba(200, 50, 0, 0.2)",
        "text_color": "#fff0e0",
        "blur": 16,
        "opacity": 0.25,
        "saturate": 2.2,
        "border_radius": 22,
        "gloss": 0.9,
        "background_gradient": "linear-gradient(135deg, #1a0000 0%, #330000 50%, #1a0a00 100%)",
        "hover_scale": 1.03,
    },
    "mint": {
        "name": "Mint",
        "name_zh": "薄荷",
        "description": "Fresh green, soft and gentle",
        "description_zh": "绿色清新，柔和",
        "primary_color": "#00e676",
        "secondary_color": "#00c853",
        "gradient_start": "rgba(0, 230, 118, 0.18)",
        "gradient_end": "rgba(0, 200, 83, 0.06)",
        "border_color": "rgba(0, 230, 118, 0.2)",
        "shadow_color": "rgba(0, 150, 80, 0.15)",
        "text_color": "#e0fff0",
        "blur": 22,
        "opacity": 0.2,
        "saturate": 1.6,
        "border_radius": 26,
        "gloss": 0.6,
        "background_gradient": "linear-gradient(135deg, #0a1a0a 0%, #0d2818 50%, #0a1a10 100%)",
        "hover_scale": 1.02,
    },
    "sunset": {
        "name": "Sunset",
        "name_zh": "日落",
        "description": "Orange-purple gradient, warm and cozy",
        "description_zh": "橙紫渐变，温暖",
        "primary_color": "#ff6b35",
        "secondary_color": "#9b59b6",
        "gradient_start": "rgba(255, 107, 53, 0.2)",
        "gradient_end": "rgba(155, 89, 182, 0.08)",
        "border_color": "rgba(255, 130, 80, 0.25)",
        "shadow_color": "rgba(150, 50, 100, 0.15)",
        "text_color": "#fff0e8",
        "blur": 20,
        "opacity": 0.22,
        "saturate": 1.9,
        "border_radius": 24,
        "gloss": 0.75,
        "background_gradient": "linear-gradient(135deg, #1a0a1e 0%, #2d1b3d 50%, #1a0e0a 100%)",
        "hover_scale": 1.02,
    },
}


def get_preset(name: str) -> Dict[str, Any]:
    """Get a theme preset by name.

    Args:
        name: Preset name (case-insensitive).

    Returns:
        Preset configuration dictionary.

    Raises:
        ValueError: If the preset name is not found.
    """
    name_lower = name.lower()
    if name_lower not in PRESETS:
        available = ", ".join(sorted(PRESETS.keys()))
        raise ValueError(
            f"Unknown theme '{name}'. Available themes: {available}"
        )
    return dict(PRESETS[name_lower])  # Return a copy


def list_presets() -> Dict[str, Dict[str, Any]]:
    """List all available theme presets.

    Returns:
        Dictionary of all preset names to their configurations.
    """
    return dict(PRESETS)


def get_preset_names() -> list:
    """Get a sorted list of all preset names.

    Returns:
        Sorted list of preset name strings.
    """
    return sorted(PRESETS.keys())


def merge_preset_with_overrides(
    preset: Dict[str, Any],
    blur: int = None,
    opacity: float = None,
    color: str = None,
    border_radius: int = None,
    gloss: float = None,
) -> Dict[str, Any]:
    """Merge a preset configuration with user-provided overrides.

    User overrides take precedence over preset defaults.

    Args:
        preset: Base preset configuration dictionary.
        blur: Override blur value (pixels).
        opacity: Override opacity value (0.0-1.0).
        color: Override primary color (hex string).
        border_radius: Override border radius (pixels).
        gloss: Override gloss intensity (0.0-1.0).

    Returns:
        Merged configuration dictionary.
    """
    merged = dict(preset)

    if blur is not None:
        merged["blur"] = blur
    if opacity is not None:
        merged["opacity"] = opacity
    if color is not None:
        merged["primary_color"] = color
    if border_radius is not None:
        merged["border_radius"] = border_radius
    if gloss is not None:
        merged["gloss"] = gloss

    return merged
