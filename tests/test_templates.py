"""
Unit tests for GlassForge templates.

Tests cover template rendering, file extensions, and output validity
for all supported framework types.
"""

import unittest
import sys
import os
import re

# Add parent directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from glassforge.engine import GlassForgeEngine
from glassforge.templates import (
    get_template,
    CSSTemplate,
    ReactTemplate,
    VueTemplate,
    SvelteTemplate,
    HTMLTemplate,
)


class TestBaseTemplate(unittest.TestCase):
    """Tests for the base template interface."""

    def test_get_template_css(self):
        """Test getting CSS template."""
        template = get_template("css")
        self.assertIsInstance(template, CSSTemplate)

    def test_get_template_react(self):
        """Test getting React template."""
        template = get_template("react")
        self.assertIsInstance(template, ReactTemplate)

    def test_get_template_vue(self):
        """Test getting Vue template."""
        template = get_template("vue")
        self.assertIsInstance(template, VueTemplate)

    def test_get_template_svelte(self):
        """Test getting Svelte template."""
        template = get_template("svelte")
        self.assertIsInstance(template, SvelteTemplate)

    def test_get_template_html(self):
        """Test getting HTML template."""
        template = get_template("html")
        self.assertIsInstance(template, HTMLTemplate)

    def test_get_template_invalid(self):
        """Test that invalid template type raises ValueError."""
        with self.assertRaises(ValueError):
            get_template("invalid")

    def test_get_template_case_insensitive(self):
        """Test that template type is case-insensitive."""
        template = get_template("CSS")
        self.assertIsInstance(template, CSSTemplate)
        template = get_template("React")
        self.assertIsInstance(template, ReactTemplate)


class TestCSSTemplate(unittest.TestCase):
    """Tests for the CSS template."""

    def setUp(self):
        self.engine = GlassForgeEngine()
        self.engine.configure(theme="crystal")
        self.template = CSSTemplate()

    def test_render_returns_string(self):
        """Test that render returns a non-empty string."""
        result = self.template.render(self.engine.get_config())
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)

    def test_render_contains_css_variables(self):
        """Test that rendered CSS contains custom properties."""
        result = self.template.render(self.engine.get_config())
        self.assertIn(":root", result)
        self.assertIn("--glass-blur", result)
        self.assertIn("--glass-opacity", result)

    def test_render_contains_base_class(self):
        """Test that rendered CSS contains the base class."""
        result = self.template.render(self.engine.get_config())
        self.assertIn(".liquid-glass", result)
        self.assertIn("backdrop-filter", result)
        self.assertIn("box-shadow", result)

    def test_render_contains_hover(self):
        """Test that rendered CSS contains hover styles."""
        result = self.template.render(self.engine.get_config())
        self.assertIn(".liquid-glass:hover", result)

    def test_render_contains_animations(self):
        """Test that rendered CSS contains animation keyframes."""
        result = self.template.render(self.engine.get_config())
        self.assertIn("@keyframes glassShimmer", result)
        self.assertIn("@keyframes glassGlow", result)

    def test_render_contains_dark_mode(self):
        """Test that rendered CSS contains dark mode rules."""
        result = self.template.render(self.engine.get_config())
        self.assertIn("@media (prefers-color-scheme: dark)", result)

    def test_render_contains_modifiers(self):
        """Test that rendered CSS contains modifier classes."""
        result = self.template.render(self.engine.get_config())
        self.assertIn("liquid-glass--intense", result)
        self.assertIn("liquid-glass--subtle", result)
        self.assertIn("liquid-glass--card", result)
        self.assertIn("liquid-glass--button", result)

    def test_file_extension(self):
        """Test file extension."""
        self.assertEqual(self.template.file_extension(), ".css")

    def test_description(self):
        """Test description."""
        self.assertIsInstance(self.template.description(), str)
        self.assertTrue(len(self.template.description()) > 0)

    def test_default_filename(self):
        """Test default filename."""
        self.assertEqual(self.template.default_filename(), "liquid-glass.css")


class TestReactTemplate(unittest.TestCase):
    """Tests for the React template."""

    def setUp(self):
        self.engine = GlassForgeEngine()
        self.engine.configure(theme="aurora")
        self.template = ReactTemplate()

    def test_render_returns_string(self):
        """Test that render returns a non-empty string."""
        result = self.template.render(self.engine.get_config())
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)

    def test_render_contains_component(self):
        """Test that rendered code contains React component."""
        result = self.template.render(self.engine.get_config())
        self.assertIn("LiquidGlass", result)
        self.assertIn("React.FC", result)
        self.assertIn("export default", result)

    def test_render_contains_props_interface(self):
        """Test that rendered code contains TypeScript interface."""
        result = self.template.render(self.engine.get_config())
        self.assertIn("interface LiquidGlassProps", result)
        self.assertIn("children", result)
        self.assertIn("blur", result)
        self.assertIn("opacity", result)

    def test_render_contains_backdrop_filter(self):
        """Test that rendered code contains backdrop-filter."""
        result = self.template.render(self.engine.get_config())
        self.assertIn("backdropFilter", result)

    def test_file_extension(self):
        """Test file extension."""
        self.assertEqual(self.template.file_extension(), ".tsx")


class TestVueTemplate(unittest.TestCase):
    """Tests for the Vue template."""

    def setUp(self):
        self.engine = GlassForgeEngine()
        self.engine.configure(theme="mint")
        self.template = VueTemplate()

    def test_render_returns_string(self):
        """Test that render returns a non-empty string."""
        result = self.template.render(self.engine.get_config())
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)

    def test_render_contains_sfc_structure(self):
        """Test that rendered code has Vue SFC structure."""
        result = self.template.render(self.engine.get_config())
        self.assertIn("<template>", result)
        self.assertIn("<script setup", result)
        self.assertIn("<style scoped>", result)

    def test_render_contains_slot(self):
        """Test that rendered code contains slot."""
        result = self.template.render(self.engine.get_config())
        self.assertIn("<slot />", result)

    def test_render_contains_props(self):
        """Test that rendered code contains defineProps."""
        result = self.template.render(self.engine.get_config())
        self.assertIn("defineProps", result)

    def test_file_extension(self):
        """Test file extension."""
        self.assertEqual(self.template.file_extension(), ".vue")


class TestSvelteTemplate(unittest.TestCase):
    """Tests for the Svelte template."""

    def setUp(self):
        self.engine = GlassForgeEngine()
        self.engine.configure(theme="sunset")
        self.template = SvelteTemplate()

    def test_render_returns_string(self):
        """Test that render returns a non-empty string."""
        result = self.template.render(self.engine.get_config())
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)

    def test_render_contains_svelte_structure(self):
        """Test that rendered code has Svelte structure."""
        result = self.template.render(self.engine.get_config())
        self.assertIn("<script>", result)
        self.assertIn("<style>", result)
        self.assertIn("export let", result)

    def test_render_contains_slot(self):
        """Test that rendered code contains slot."""
        result = self.template.render(self.engine.get_config())
        self.assertIn("<slot />", result)

    def test_render_contains_dispatch(self):
        """Test that rendered code contains event dispatcher."""
        result = self.template.render(self.engine.get_config())
        self.assertIn("createEventDispatcher", result)

    def test_file_extension(self):
        """Test file extension."""
        self.assertEqual(self.template.file_extension(), ".svelte")


class TestHTMLTemplate(unittest.TestCase):
    """Tests for the HTML template."""

    def setUp(self):
        self.engine = GlassForgeEngine()
        self.engine.configure(theme="ocean")
        self.template = HTMLTemplate()

    def test_render_returns_string(self):
        """Test that render returns a non-empty string."""
        result = self.template.render(self.engine.get_config())
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)

    def test_render_contains_doctype(self):
        """Test that rendered HTML contains DOCTYPE."""
        result = self.template.render(self.engine.get_config())
        self.assertIn("<!DOCTYPE html>", result)

    def test_render_contains_demo_cards(self):
        """Test that rendered HTML contains demo cards."""
        result = self.template.render(self.engine.get_config())
        self.assertIn("demo-card", result)
        self.assertIn("liquid-glass", result)

    def test_render_contains_styles(self):
        """Test that rendered HTML contains embedded styles."""
        result = self.template.render(self.engine.get_config())
        self.assertIn("<style>", result)
        self.assertIn("backdrop-filter", result)

    def test_render_contains_responsive(self):
        """Test that rendered HTML contains responsive styles."""
        result = self.template.render(self.engine.get_config())
        self.assertIn("@media", result)

    def test_file_extension(self):
        """Test file extension."""
        self.assertEqual(self.template.file_extension(), ".html")


class TestAllThemesWithAllTemplates(unittest.TestCase):
    """Cross-product test: all themes x all templates render without error."""

    def test_all_combinations(self):
        """Test that every theme works with every template."""
        themes = ["crystal", "aurora", "ocean", "lava", "mint", "sunset"]
        template_types = ["css", "react", "vue", "svelte", "html"]

        for theme in themes:
            for ttype in template_types:
                with self.subTest(theme=theme, template=ttype):
                    engine = GlassForgeEngine()
                    engine.configure(theme=theme)
                    template = get_template(ttype)
                    result = template.render(engine.get_config())
                    self.assertIsInstance(result, str)
                    self.assertTrue(len(result) > 100)


if __name__ == "__main__":
    unittest.main()
