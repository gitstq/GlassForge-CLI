"""
Unit tests for the GlassForge CLI.

Tests cover argument parsing, command dispatch, and CLI behavior.
"""

import unittest
import sys
import os
import io
import contextlib

# Add parent directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from glassforge.cli import build_parser, main, cmd_generate, cmd_themes, cmd_init
from glassforge.engine import GlassForgeEngine


class TestArgumentParser(unittest.TestCase):
    """Tests for the CLI argument parser."""

    def setUp(self):
        self.parser = build_parser()

    def test_no_args_shows_help(self):
        """Test that no arguments triggers help (no error)."""
        with contextlib.redirect_stdout(io.StringIO()):
            with contextlib.redirect_stderr(io.StringIO()):
                # Should not raise an exception
                try:
                    self.parser.parse_args([])
                except SystemExit:
                    pass

    def test_version_flag(self):
        """Test that --version works."""
        with self.assertRaises(SystemExit) as cm:
            self.parser.parse_args(["--version"])
        self.assertEqual(cm.exception.code, 0)

    def test_generate_defaults(self):
        """Test generate command with default values."""
        args = self.parser.parse_args(["generate"])
        self.assertEqual(args.command, "generate")
        self.assertEqual(args.type, "css")
        self.assertEqual(args.theme, "crystal")
        self.assertIsNone(args.blur)
        self.assertIsNone(args.opacity)

    def test_generate_with_options(self):
        """Test generate command with all options."""
        args = self.parser.parse_args([
            "generate",
            "--type", "react",
            "--theme", "aurora",
            "--blur", "30",
            "--opacity", "0.5",
            "--color", "#ff0000",
            "--border-radius", "16",
            "--gloss", "0.9",
            "--output", "output.tsx",
        ])
        self.assertEqual(args.type, "react")
        self.assertEqual(args.theme, "aurora")
        self.assertEqual(args.blur, 30)
        self.assertEqual(args.opacity, 0.5)
        self.assertEqual(args.color, "#ff0000")
        self.assertEqual(args.border_radius, 16)
        self.assertEqual(args.gloss, 0.9)
        self.assertEqual(args.output, "output.tsx")

    def test_generate_short_options(self):
        """Test generate command with short option flags."""
        args = self.parser.parse_args([
            "generate",
            "-t", "vue",
            "-b", "20",
            "-o", "0.3",
            "-c", "#00ff00",
            "-r", "12",
            "-g", "0.5",
        ])
        self.assertEqual(args.type, "vue")
        self.assertEqual(args.blur, 20)
        self.assertEqual(args.opacity, 0.3)
        self.assertEqual(args.color, "#00ff00")
        self.assertEqual(args.border_radius, 12)
        self.assertEqual(args.gloss, 0.5)

    def test_preview_command(self):
        """Test preview command parsing."""
        args = self.parser.parse_args(["preview", "--theme", "sunset"])
        self.assertEqual(args.command, "preview")
        self.assertEqual(args.theme, "sunset")

    def test_themes_list(self):
        """Test themes --list command parsing."""
        args = self.parser.parse_args(["themes", "--list"])
        self.assertEqual(args.command, "themes")
        self.assertTrue(args.list)
        self.assertIsNone(args.show)

    def test_themes_show(self):
        """Test themes --show command parsing."""
        args = self.parser.parse_args(["themes", "--show", "ocean"])
        self.assertEqual(args.command, "themes")
        self.assertEqual(args.show, "ocean")

    def test_init_command(self):
        """Test init command parsing."""
        args = self.parser.parse_args(["init", "--type", "svelte", "--theme", "mint"])
        self.assertEqual(args.command, "init")
        self.assertEqual(args.type, "svelte")
        self.assertEqual(args.theme, "mint")

    def test_invalid_type_rejected(self):
        """Test that invalid output type is rejected."""
        with self.assertRaises(SystemExit):
            self.parser.parse_args(["generate", "--type", "angular"])


class TestCommandHandlers(unittest.TestCase):
    """Tests for CLI command handler functions."""

    def test_cmd_themes_list(self):
        """Test themes list command outputs theme names."""
        args = type('Args', (), {'show': None})()
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            cmd_themes(args)
        result = output.getvalue()
        self.assertIn("crystal", result)
        self.assertIn("aurora", result)
        self.assertIn("ocean", result)
        self.assertIn("lava", result)
        self.assertIn("mint", result)
        self.assertIn("sunset", result)

    def test_cmd_themes_show(self):
        """Test themes show command outputs theme details."""
        args = type('Args', (), {'show': 'crystal'})()
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            cmd_themes(args)
        result = output.getvalue()
        self.assertIn("Crystal", result)
        self.assertIn("blur", result.lower())
        self.assertIn("opacity", result.lower())

    def test_cmd_themes_show_invalid(self):
        """Test themes show with invalid name exits with error."""
        args = type('Args', (), {'show': 'nonexistent'})()
        output = io.StringIO()
        with contextlib.redirect_stderr(output):
            with self.assertRaises(SystemExit):
                cmd_themes(args)

    def test_cmd_generate_to_stdout(self):
        """Test generate command outputs to stdout."""
        args = type('Args', (), {
            'type': 'css',
            'theme': 'crystal',
            'blur': None,
            'opacity': None,
            'color': None,
            'border_radius': None,
            'gloss': None,
            'output': '-',
        })()
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            cmd_generate(args)
        result = output.getvalue()
        self.assertIn(".liquid-glass", result)
        self.assertIn("backdrop-filter", result)

    def test_cmd_init(self):
        """Test init command creates file."""
        # Use a temp path
        temp_path = os.path.join(
            os.path.dirname(__file__), "_test_init_output.css"
        )
        try:
            args = type('Args', (), {
                'type': 'css',
                'theme': 'crystal',
                'blur': None,
                'opacity': None,
                'color': None,
                'border_radius': None,
                'gloss': None,
                'output': temp_path,
            })()
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                cmd_init(args)
            result = output.getvalue()
            self.assertIn("Initialized", result)

            # Verify file was created
            self.assertTrue(os.path.exists(temp_path))
            with open(temp_path, "r") as f:
                content = f.read()
            self.assertIn(".liquid-glass", content)
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)


class TestMainEntry(unittest.TestCase):
    """Tests for the main() entry point."""

    def test_main_no_args(self):
        """Test main with no args shows help."""
        with contextlib.redirect_stdout(io.StringIO()):
            with contextlib.redirect_stderr(io.StringIO()):
                try:
                    main([])
                except SystemExit:
                    pass

    def test_main_version(self):
        """Test main with --version."""
        with self.assertRaises(SystemExit) as cm:
            with contextlib.redirect_stdout(io.StringIO()):
                main(["--version"])
        self.assertEqual(cm.exception.code, 0)


if __name__ == "__main__":
    unittest.main()
