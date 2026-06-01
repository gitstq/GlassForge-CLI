"""
Unit tests for the GlassForge engine.

Tests cover engine configuration, CSS property generation,
derived value computation, and edge cases.
"""

import unittest
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from glassforge.engine import GlassForgeEngine
from glassforge.utils import (
    hex_to_rgb,
    rgb_to_hex,
    hex_to_rgba,
    validate_hex_color,
    validate_blur,
    validate_opacity,
    validate_border_radius,
    validate_gloss,
    adjust_lightness,
    rgb_to_hsl,
    hsl_to_hex,
)


class TestColorUtils(unittest.TestCase):
    """Tests for color utility functions."""

    def test_hex_to_rgb_6digit(self):
        """Test 6-digit hex to RGB conversion."""
        self.assertEqual(hex_to_rgb("#ff0000"), (255, 0, 0))
        self.assertEqual(hex_to_rgb("#00ff00"), (0, 255, 0))
        self.assertEqual(hex_to_rgb("#0000ff"), (0, 0, 255))
        self.assertEqual(hex_to_rgb("ffffff"), (255, 255, 255))

    def test_hex_to_rgb_3digit(self):
        """Test 3-digit hex to RGB conversion."""
        self.assertEqual(hex_to_rgb("#f00"), (255, 0, 0))
        self.assertEqual(hex_to_rgb("#0f0"), (0, 255, 0))
        self.assertEqual(hex_to_rgb("#abc"), (170, 187, 204))

    def test_hex_to_rgb_invalid(self):
        """Test invalid hex color raises ValueError."""
        with self.assertRaises(ValueError):
            hex_to_rgb("#gg0000")
        with self.assertRaises(ValueError):
            hex_to_rgb("#ff")
        with self.assertRaises(ValueError):
            hex_to_rgb("#ffff")

    def test_rgb_to_hex(self):
        """Test RGB to hex conversion."""
        self.assertEqual(rgb_to_hex(255, 0, 0), "#ff0000")
        self.assertEqual(rgb_to_hex(0, 255, 0), "#00ff00")
        self.assertEqual(rgb_to_hex(0, 0, 255), "#0000ff")
        self.assertEqual(rgb_to_hex(170, 187, 204), "#aabbcc")

    def test_hex_to_rgba(self):
        """Test hex to rgba string conversion."""
        result = hex_to_rgba("#ff0000", 0.5)
        self.assertEqual(result, "rgba(255, 0, 0, 0.5)")
        result = hex_to_rgba("#000000", 0.0)
        self.assertEqual(result, "rgba(0, 0, 0, 0.0)")
        result = hex_to_rgba("#ffffff", 1.0)
        self.assertEqual(result, "rgba(255, 255, 255, 1.0)")

    def test_validate_hex_color(self):
        """Test hex color validation."""
        self.assertTrue(validate_hex_color("#ff0000"))
        self.assertTrue(validate_hex_color("ff0000"))
        self.assertTrue(validate_hex_color("#f00"))
        self.assertTrue(validate_hex_color("ABC"))
        self.assertFalse(validate_hex_color("#gg0000"))
        self.assertFalse(validate_hex_color("ff"))
        self.assertFalse(validate_hex_color(""))

    def test_rgb_to_hsl(self):
        """Test RGB to HSL conversion."""
        # Pure red
        h, s, l = rgb_to_hsl(255, 0, 0)
        self.assertEqual(h, 0.0)
        self.assertEqual(s, 100.0)
        self.assertEqual(l, 50.0)

        # Pure white
        h, s, l = rgb_to_hsl(255, 255, 255)
        self.assertEqual(s, 0.0)
        self.assertEqual(l, 100.0)

        # Pure black
        h, s, l = rgb_to_hsl(0, 0, 0)
        self.assertEqual(s, 0.0)
        self.assertEqual(l, 0.0)

    def test_hsl_to_hex(self):
        """Test HSL to hex conversion."""
        self.assertEqual(hsl_to_hex(0, 100, 50), "#ff0000")
        self.assertEqual(hsl_to_hex(120, 100, 50), "#00ff00")
        self.assertEqual(hsl_to_hex(240, 100, 50), "#0000ff")

    def test_adjust_lightness(self):
        """Test lightness adjustment."""
        result = adjust_lightness("#808080", 20)
        r, g, b = hex_to_rgb(result)
        self.assertTrue(r > 128)  # Should be lighter

        result = adjust_lightness("#808080", -20)
        r, g, b = hex_to_rgb(result)
        self.assertTrue(r < 128)  # Should be darker


class TestValidationUtils(unittest.TestCase):
    """Tests for validation utility functions."""

    def test_validate_blur(self):
        """Test blur value validation and clamping."""
        self.assertEqual(validate_blur(25), 25)
        self.assertEqual(validate_blur(0), 0)
        self.assertEqual(validate_blur(50), 50)
        self.assertEqual(validate_blur(100), 50)  # Clamped
        self.assertEqual(validate_blur(-10), 0)     # Clamped

    def test_validate_opacity(self):
        """Test opacity value validation and clamping."""
        self.assertEqual(validate_opacity(0.5), 0.5)
        self.assertEqual(validate_opacity(0.0), 0.0)
        self.assertEqual(validate_opacity(1.0), 1.0)
        self.assertEqual(validate_opacity(1.5), 1.0)   # Clamped
        self.assertEqual(validate_opacity(-0.5), 0.0)   # Clamped
        self.assertEqual(validate_opacity(0.123), 0.12) # Rounded

    def test_validate_border_radius(self):
        """Test border radius validation and clamping."""
        self.assertEqual(validate_border_radius(24), 24)
        self.assertEqual(validate_border_radius(0), 0)
        self.assertEqual(validate_border_radius(100), 100)
        self.assertEqual(validate_border_radius(200), 100)  # Clamped
        self.assertEqual(validate_border_radius(-5), 0)       # Clamped

    def test_validate_gloss(self):
        """Test gloss value validation and clamping."""
        self.assertEqual(validate_gloss(0.5), 0.5)
        self.assertEqual(validate_gloss(0.0), 0.0)
        self.assertEqual(validate_gloss(1.0), 1.0)
        self.assertEqual(validate_gloss(2.0), 1.0)   # Clamped
        self.assertEqual(validate_gloss(-0.5), 0.0)   # Clamped


class TestEngine(unittest.TestCase):
    """Tests for the GlassForgeEngine class."""

    def setUp(self):
        """Set up test fixtures."""
        self.engine = GlassForgeEngine()

    def test_configure_default(self):
        """Test engine configuration with default theme."""
        config = self.engine.configure()
        self.assertIsNotNone(config)
        self.assertIn("blur", config)
        self.assertIn("opacity", config)
        self.assertIn("background", config)
        self.assertIn("box_shadow", config)
        self.assertIn("backdrop_filter", config)
        self.assertEqual(config["blur"], 20)  # crystal default

    def test_configure_with_theme(self):
        """Test engine configuration with a specific theme."""
        config = self.engine.configure(theme="aurora")
        self.assertEqual(config["blur"], 24)  # aurora default
        self.assertEqual(config["primary_color"], "#00d2ff")

    def test_configure_with_overrides(self):
        """Test engine configuration with parameter overrides."""
        config = self.engine.configure(
            theme="crystal",
            blur=30,
            opacity=0.5,
            border_radius=16,
        )
        self.assertEqual(config["blur"], 30)
        self.assertEqual(config["opacity"], 0.5)
        self.assertEqual(config["border_radius"], 16)

    def test_configure_invalid_theme(self):
        """Test that invalid theme raises ValueError."""
        with self.assertRaises(ValueError):
            self.engine.configure(theme="nonexistent")

    def test_configure_invalid_color(self):
        """Test that invalid color raises ValueError."""
        with self.assertRaises(ValueError):
            self.engine.configure(color="not-a-color")

    def test_get_config_before_configure(self):
        """Test that get_config raises RuntimeError before configure."""
        engine = GlassForgeEngine()
        with self.assertRaises(RuntimeError):
            engine.get_config()

    def test_get_css_properties(self):
        """Test CSS property generation."""
        self.engine.configure(theme="crystal")
        props = self.engine.get_css_properties()
        self.assertIn("backdrop-filter", props)
        self.assertIn("background", props)
        self.assertIn("border", props)
        self.assertIn("box-shadow", props)
        self.assertIn("color", props)
        self.assertIn("transition", props)

    def test_get_hover_properties(self):
        """Test hover CSS property generation."""
        self.engine.configure(theme="crystal")
        hover_props = self.engine.get_hover_properties()
        self.assertIn("background", hover_props)
        self.assertIn("box-shadow", hover_props)
        self.assertIn("transform", hover_props)

    def test_get_css_variables(self):
        """Test CSS custom properties generation."""
        self.engine.configure(theme="crystal")
        vars_dict = self.engine.get_css_variables()
        self.assertIn("--glass-blur", vars_dict)
        self.assertIn("--glass-opacity", vars_dict)
        self.assertIn("--glass-primary", vars_dict)
        self.assertIn("--glass-background", vars_dict)

    def test_get_animation_css(self):
        """Test animation CSS generation."""
        self.engine.configure(theme="crystal")
        anim_css = self.engine.get_animation_css()
        self.assertIn("@keyframes glassShimmer", anim_css)
        self.assertIn("@keyframes glassGlow", anim_css)

    def test_get_dark_mode_css(self):
        """Test dark mode CSS generation."""
        self.engine.configure(theme="crystal")
        dark_css = self.engine.get_dark_mode_css()
        self.assertIn("@media (prefers-color-scheme: dark)", dark_css)
        self.assertIn(".liquid-glass", dark_css)

    def test_all_themes_configurable(self):
        """Test that all preset themes can be configured without error."""
        themes = ["crystal", "aurora", "ocean", "lava", "mint", "sunset"]
        for theme in themes:
            with self.subTest(theme=theme):
                engine = GlassForgeEngine()
                config = engine.configure(theme=theme)
                self.assertIsNotNone(config)
                self.assertIn("background", config)
                self.assertIn("box_shadow", config)

    def test_derived_values_present(self):
        """Test that all expected derived values are computed."""
        config = self.engine.configure(theme="crystal")
        expected_keys = [
            "background", "box_shadow", "hover_box_shadow",
            "border", "backdrop_filter", "webkit_backdrop_filter",
            "hover_background", "dark_mode_overlay", "light_mode_overlay",
            "shimmer_start", "shimmer_mid", "shimmer_end",
        ]
        for key in expected_keys:
            with self.subTest(key=key):
                self.assertIn(key, config)


if __name__ == "__main__":
    unittest.main()
