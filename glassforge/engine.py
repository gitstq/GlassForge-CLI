"""
Core engine for GlassForge CLI.

Generates liquid glass CSS effects based on theme presets and user parameters.
The engine produces raw CSS configuration data that templates consume.
"""

from typing import Dict, Any, Optional

from .themes.presets import get_preset, merge_preset_with_overrides
from .utils import (
    hex_to_rgba,
    validate_blur,
    validate_opacity,
    validate_border_radius,
    validate_gloss,
    validate_hex_color,
    adjust_lightness,
)


class GlassForgeEngine:
    """Core engine for generating liquid glass CSS configurations.

    This engine computes all CSS property values needed for the liquid glass
    effect, including backdrop filters, shadows, borders, and animations.
    It does not produce framework-specific code directly; instead, it
    provides a configuration dictionary that templates render into output.
    """

    def __init__(self):
        self._config: Optional[Dict[str, Any]] = None

    def configure(
        self,
        theme: str = "crystal",
        blur: Optional[int] = None,
        opacity: Optional[float] = None,
        color: Optional[str] = None,
        border_radius: Optional[int] = None,
        gloss: Optional[float] = None,
    ) -> Dict[str, Any]:
        """Configure the engine with a theme preset and optional overrides.

        Args:
            theme: Name of the theme preset to use.
            blur: Override blur value (0-50 pixels).
            opacity: Override opacity value (0.0-1.0).
            color: Override primary color (hex string).
            border_radius: Override border radius (0-100 pixels).
            gloss: Override gloss intensity (0.0-1.0).

        Returns:
            Complete configuration dictionary for the glass effect.

        Raises:
            ValueError: If theme name is unknown or color is invalid.
        """
        # Load preset
        preset = get_preset(theme)

        # Validate overrides before merging
        if blur is not None:
            blur = validate_blur(blur)
        if opacity is not None:
            opacity = validate_opacity(opacity)
        if color is not None:
            if not validate_hex_color(color):
                raise ValueError(
                    f"Invalid color '{color}'. Must be a valid hex color "
                    "(e.g., '#ff0000' or 'ff0000')."
                )
            color = color.lstrip("#")
            color = f"#{color}"
        if border_radius is not None:
            border_radius = validate_border_radius(border_radius)
        if gloss is not None:
            gloss = validate_gloss(gloss)

        # Merge overrides with preset
        config = merge_preset_with_overrides(
            preset,
            blur=blur,
            opacity=opacity,
            color=color,
            border_radius=border_radius,
            gloss=gloss,
        )

        # Recompute derived values based on merged config
        self._config = self._compute_derived_values(config)
        return self._config

    def _compute_derived_values(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """Compute all derived CSS values from the base configuration.

        This method generates all the CSS property values needed for the
        liquid glass effect, including shadows, borders, gradients, and
        animation keyframes.

        Args:
            config: Base configuration dictionary.

        Returns:
            Enhanced configuration dictionary with all derived values.
        """
        primary = config["primary_color"]
        secondary = config.get("secondary_color", primary)
        opacity = config["opacity"]
        blur = config["blur"]
        gloss = config["gloss"]
        border_radius = config["border_radius"]
        saturate = config.get("saturate", 1.8)
        shadow_color = config.get("shadow_color", "rgba(0, 0, 0, 0.1)")
        border_color = config.get("border_color", "rgba(255, 255, 255, 0.3)")

        # Compute gradient colors based on primary color and opacity
        gradient_start = hex_to_rgba(primary, min(opacity + 0.05, 0.4))
        gradient_end = hex_to_rgba(primary, max(opacity - 0.1, 0.02))

        # Compute multi-layer box shadows for depth and gloss
        gloss_alpha = gloss * 0.15
        gloss_color = hex_to_rgba(primary, gloss_alpha)
        lighter_gloss = hex_to_rgba(
            adjust_lightness(primary, 30), gloss_alpha * 0.5
        )

        # Outer shadow for depth
        outer_shadow = (
            f"0 8px 32px {shadow_color}, "
            f"0 2px 8px {hex_to_rgba(primary, 0.05)}"
        )

        # Inner shadow for glass depth
        inner_shadow = (
            f"inset 0 1px 1px {gloss_color}, "
            f"inset 0 -1px 1px {lighter_gloss}"
        )

        # Combined shadow
        box_shadow = f"{outer_shadow}, {inner_shadow}"

        # Border with highlight effect
        border = f"1px solid {border_color}"

        # Backdrop filter
        backdrop_filter = f"blur({blur}px) saturate({saturate})"

        # Webkit prefix for Safari compatibility
        webkit_backdrop_filter = f"blur({blur}px) saturate({saturate})"

        # Background gradient simulating light refraction
        background = (
            f"linear-gradient("
            f"135deg, "
            f"{gradient_start} 0%, "
            f"{gradient_end} 50%, "
            f"{hex_to_rgba(secondary, opacity * 0.3)} 100%"
            f")"
        )

        # Hover effect values
        hover_box_shadow = box_shadow.replace(
            shadow_color,
            hex_to_rgba(primary, 0.2),
        )
        hover_background = (
            f"linear-gradient("
            f"135deg, "
            f"{hex_to_rgba(primary, min(opacity + 0.1, 0.5))} 0%, "
            f"{hex_to_rgba(primary, opacity)} 50%, "
            f"{hex_to_rgba(secondary, opacity * 0.5)} 100%"
            f")"
        )

        # Animation for shimmer effect
        shimmer_gradient_start = hex_to_rgba(primary, 0.0)
        shimmer_gradient_mid = hex_to_rgba(primary, gloss * 0.3)
        shimmer_gradient_end = hex_to_rgba(primary, 0.0)

        # Light mode / dark mode adaptive values
        light_mode_overlay = hex_to_rgba("#ffffff", 0.05)
        dark_mode_overlay = hex_to_rgba("#000000", 0.1)

        # Build the full config
        derived = {
            **config,
            "gradient_start": gradient_start,
            "gradient_end": gradient_end,
            "outer_shadow": outer_shadow,
            "inner_shadow": inner_shadow,
            "box_shadow": box_shadow,
            "hover_box_shadow": hover_box_shadow,
            "border": border,
            "backdrop_filter": backdrop_filter,
            "webkit_backdrop_filter": webkit_backdrop_filter,
            "background": background,
            "hover_background": hover_background,
            "shimmer_start": shimmer_gradient_start,
            "shimmer_mid": shimmer_gradient_mid,
            "shimmer_end": shimmer_gradient_end,
            "light_mode_overlay": light_mode_overlay,
            "dark_mode_overlay": dark_mode_overlay,
            "hover_scale": config.get("hover_scale", 1.02),
        }

        return derived

    def get_config(self) -> Dict[str, Any]:
        """Get the current configuration.

        Returns:
            Current configuration dictionary.

        Raises:
            RuntimeError: If configure() has not been called yet.
        """
        if self._config is None:
            raise RuntimeError(
                "Engine not configured. Call configure() first."
            )
        return dict(self._config)

    def get_css_properties(self) -> Dict[str, str]:
        """Get a flat dictionary of CSS property name to value.

        This is useful for template rendering where each CSS property
        is needed individually.

        Returns:
            Dictionary mapping CSS property names to their values.
        """
        config = self.get_config()
        return {
            "backdrop-filter": config["backdrop_filter"],
            "-webkit-backdrop-filter": config["webkit_backdrop_filter"],
            "background": config["background"],
            "border": config["border"],
            "border-radius": f"{config['border_radius']}px",
            "box-shadow": config["box_shadow"],
            "color": config["text_color"],
            "transition": "all 0.3s ease",
        }

    def get_hover_properties(self) -> Dict[str, str]:
        """Get CSS properties for the hover state.

        Returns:
            Dictionary mapping CSS property names to hover values.
        """
        config = self.get_config()
        return {
            "background": config["hover_background"],
            "box-shadow": config["hover_box_shadow"],
            "transform": f"scale({config['hover_scale']})",
        }

    def get_css_variables(self) -> Dict[str, str]:
        """Get CSS custom properties for the glass effect.

        Returns:
            Dictionary mapping CSS variable names to their values.
        """
        config = self.get_config()
        return {
            "--glass-blur": f"{config['blur']}px",
            "--glass-opacity": str(config["opacity"]),
            "--glass-saturate": str(config["saturate"]),
            "--glass-border-radius": f"{config['border_radius']}px",
            "--glass-primary": config["primary_color"],
            "--glass-secondary": config.get("secondary_color", config["primary_color"]),
            "--glass-text-color": config["text_color"],
            "--glass-background": config["background"],
            "--glass-border": config["border"],
            "--glass-box-shadow": config["box_shadow"],
            "--glass-backdrop-filter": config["backdrop_filter"],
            "--glass-hover-scale": str(config["hover_scale"]),
            "--glass-gloss": str(config["gloss"]),
        }

    def get_animation_css(self) -> str:
        """Generate CSS keyframes for the shimmer animation.

        Returns:
            CSS string with @keyframes rule for the glass shimmer effect.
        """
        config = self.get_config()
        return (
            "@keyframes glassShimmer {\n"
            "  0% {\n"
            "    background-position: -200% center;\n"
            "  }\n"
            "  100% {\n"
            "    background-position: 200% center;\n"
            "  }\n"
            "}\n"
            "\n"
            "@keyframes glassGlow {\n"
            "  0%, 100% {\n"
            f"    box-shadow: {config['box_shadow']};\n"
            "  }\n"
            "  50% {\n"
            f"    box-shadow: {config['hover_box_shadow']};\n"
            "  }\n"
            "}\n"
        )

    def get_dark_mode_css(self) -> str:
        """Generate CSS for dark mode adaptation.

        Returns:
            CSS string with @media (prefers-color-scheme: dark) rules.
        """
        config = self.get_config()
        return (
            "@media (prefers-color-scheme: dark) {\n"
            "  .liquid-glass {\n"
            f"    background: {config['dark_mode_overlay']};\n"
            "    color: #e0e0e0;\n"
            "  }\n"
            "}\n"
        )
