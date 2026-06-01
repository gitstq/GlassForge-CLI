"""
CLI entry point for GlassForge CLI.

Provides command-line interface for generating liquid glass CSS code
across multiple framework outputs. Uses argparse for zero-dependency
command-line parsing.
"""

import argparse
import sys
import os

from . import __version__
from .engine import GlassForgeEngine
from .templates import get_template
from .themes.presets import get_preset_names, get_preset, list_presets
from .utils import write_output, open_in_browser, validate_hex_color


# ---------------------------------------------------------------------------
# Command handlers
# ---------------------------------------------------------------------------

def cmd_generate(args):
    """Handle the 'generate' subcommand.

    Generates liquid glass effect code for the specified framework type.

    Args:
        args: Parsed argparse namespace with generate options.
    """
    try:
        # Initialize engine
        engine = GlassForgeEngine()

        # Configure engine with theme and overrides
        config = engine.configure(
            theme=args.theme,
            blur=args.blur,
            opacity=args.opacity,
            color=args.color,
            border_radius=args.border_radius,
            gloss=args.gloss,
        )

        # Get the appropriate template
        template = get_template(args.type)

        # Render output
        output = template.render(config)

        # Determine output path
        output_path = args.output
        if output_path is None:
            output_path = template.default_filename()

        # Write output
        result = write_output(output, output_path)

        if result == "<stdout>":
            pass  # Already printed
        else:
            print(f"Generated: {result} ({template.description()})")

    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


def cmd_preview(args):
    """Handle the 'preview' subcommand.

    Opens a browser preview of the liquid glass effect using the
    specified theme.

    Args:
        args: Parsed argparse namespace with preview options.
    """
    try:
        engine = GlassForgeEngine()

        config = engine.configure(
            theme=args.theme,
            blur=args.blur,
            opacity=args.opacity,
            color=args.color,
            border_radius=args.border_radius,
            gloss=args.gloss,
        )

        # Always use HTML template for preview
        template = get_template("html")
        html_content = template.render(config)

        # Optionally write to file
        if args.output:
            write_output(html_content, args.output)
            print(f"Preview saved to: {args.output}")

        # Open in browser
        success = open_in_browser(html_content)
        if success:
            print(f"Preview opened in browser (theme: {config.get('name', args.theme)})")
        else:
            print("Warning: Could not open browser. Use --output to save the HTML file.", file=sys.stderr)
            # Fall back to printing the path
            if not args.output:
                print("Tip: Use --output <file.html> to save the preview file.", file=sys.stderr)

    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


def cmd_themes(args):
    """Handle the 'themes' subcommand.

    Lists all available themes or shows details for a specific theme.

    Args:
        args: Parsed argparse namespace with themes options.
    """
    if args.show:
        # Show detailed info for a specific theme
        try:
            preset = get_preset(args.show)
            print(f"Theme: {preset['name']} ({preset['name_zh']})")
            print(f"  Description: {preset['description']}")
            print(f"  Description (zh): {preset['description_zh']}")
            print(f"  Primary Color:    {preset['primary_color']}")
            print(f"  Secondary Color:  {preset.get('secondary_color', 'N/A')}")
            print(f"  Blur:             {preset['blur']}px")
            print(f"  Opacity:          {preset['opacity']}")
            print(f"  Saturate:         {preset['saturate']}")
            print(f"  Border Radius:    {preset['border_radius']}px")
            print(f"  Gloss:            {preset['gloss']}")
            print(f"  Text Color:       {preset['text_color']}")
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        # List all themes
        names = get_preset_names()
        print("Available themes:")
        print()
        for name in names:
            preset = get_preset(name)
            print(f"  {name:<10} {preset['name_zh']:<6} - {preset['description']}")
        print()
        print(f"Total: {len(names)} themes")


def cmd_init(args):
    """Handle the 'init' subcommand.

    Initializes a project by generating liquid glass component files
    for the specified framework.

    Args:
        args: Parsed argparse namespace with init options.
    """
    try:
        engine = GlassForgeEngine()

        config = engine.configure(
            theme=args.theme,
            blur=args.blur,
            opacity=args.opacity,
            color=args.color,
            border_radius=args.border_radius,
            gloss=args.gloss,
        )

        framework = args.type.lower()
        template = get_template(framework)
        content = template.render(config)

        # Determine filename based on framework
        ext = template.file_extension()
        if framework == "css":
            filename = f"liquid-glass{ext}"
        elif framework == "react":
            filename = f"LiquidGlass{ext}"
        elif framework == "vue":
            filename = f"LiquidGlass{ext}"
        elif framework == "svelte":
            filename = f"LiquidGlass{ext}"
        elif framework == "html":
            filename = f"liquid-glass-demo{ext}"
        else:
            filename = f"liquid-glass{ext}"

        output_path = args.output or filename
        result = write_output(content, output_path)

        if result != "<stdout>":
            print(f"Initialized: {result}")
            print(f"  Framework: {framework}")
            print(f"  Theme:     {config.get('name', args.theme)}")
            print()
            print("Next steps:")
            if framework == "css":
                print(f"  1. Import '{filename}' in your HTML or CSS bundle")
                print("  2. Add class 'liquid-glass' to any element")
            elif framework == "react":
                print(f"  1. Import the component: import LiquidGlass from './{filename}'")
                print("  2. Use it: <LiquidGlass>Your content</LiquidGlass>")
            elif framework == "vue":
                print(f"  1. Import the component: import LiquidGlass from './{filename}'")
                print("  2. Use it: <LiquidGlass>Your content</LiquidGlass>")
            elif framework == "svelte":
                print(f"  1. Import the component: import LiquidGlass from './{filename}'")
                print("  2. Use it: <LiquidGlass>Your content</LiquidGlass>")
            elif framework == "html":
                print(f"  1. Open '{filename}' in your browser")
                print("  2. Copy the CSS and HTML patterns into your project")

    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


# ---------------------------------------------------------------------------
# Argument parser setup
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    """Build the main argument parser with all subcommands.

    Returns:
        Configured ArgumentParser instance.
    """
    parser = argparse.ArgumentParser(
        prog="glassforge",
        description=(
            "GlassForge CLI - Generate Apple Liquid Glass UI CSS code.\n\n"
            "A zero-dependency terminal tool for creating beautiful liquid glass\n"
            "effects with support for CSS, React, Vue, Svelte, and HTML output."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  glassforge generate --type css --theme aurora\n"
            "  glassforge generate --type react --theme crystal --blur 30\n"
            "  glassforge preview --theme sunset\n"
            "  glassforge themes --list\n"
            "  glassforge themes --show ocean\n"
            "  glassforge init --type vue --theme mint\n"
        ),
    )

    parser.add_argument(
        "-V", "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )

    subparsers = parser.add_subparsers(
        dest="command",
        help="Available commands",
    )

    # ---- generate subcommand ----
    gen_parser = subparsers.add_parser(
        "generate",
        help="Generate liquid glass effect code",
        description="Generate liquid glass CSS/component code for the specified framework.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    gen_parser.add_argument(
        "--type", "-t",
        type=str,
        choices=["css", "react", "vue", "svelte", "html"],
        default="css",
        help="Output type (default: css)",
    )
    gen_parser.add_argument(
        "--theme",
        type=str,
        default="crystal",
        help="Theme preset name (default: crystal)",
    )
    gen_parser.add_argument(
        "--blur", "-b",
        type=int,
        default=None,
        help="Blur intensity in pixels (0-50, overrides theme default)",
    )
    gen_parser.add_argument(
        "--opacity", "-o",
        type=float,
        default=None,
        help="Background opacity (0.0-1.0, overrides theme default)",
    )
    gen_parser.add_argument(
        "--color", "-c",
        type=str,
        default=None,
        help="Primary color in hex format (e.g., '#ff0000', overrides theme default)",
    )
    gen_parser.add_argument(
        "--border-radius", "-r",
        type=int,
        default=None,
        help="Border radius in pixels (0-100, overrides theme default)",
    )
    gen_parser.add_argument(
        "--gloss", "-g",
        type=float,
        default=None,
        help="Gloss intensity (0.0-1.0, overrides theme default)",
    )
    gen_parser.add_argument(
        "--output",
        type=str,
        default=None,
        help="Output file path (default: auto-generated filename)",
    )

    # ---- preview subcommand ----
    prev_parser = subparsers.add_parser(
        "preview",
        help="Open a browser preview of the liquid glass effect",
        description="Generate and open an HTML preview in your default browser.",
    )

    prev_parser.add_argument(
        "--theme",
        type=str,
        default="crystal",
        help="Theme preset name (default: crystal)",
    )
    prev_parser.add_argument(
        "--blur", "-b",
        type=int,
        default=None,
        help="Blur intensity in pixels (0-50)",
    )
    prev_parser.add_argument(
        "--opacity", "-o",
        type=float,
        default=None,
        help="Background opacity (0.0-1.0)",
    )
    prev_parser.add_argument(
        "--color", "-c",
        type=str,
        default=None,
        help="Primary color in hex format",
    )
    prev_parser.add_argument(
        "--border-radius", "-r",
        type=int,
        default=None,
        help="Border radius in pixels (0-100)",
    )
    prev_parser.add_argument(
        "--gloss", "-g",
        type=float,
        default=None,
        help="Gloss intensity (0.0-1.0)",
    )
    prev_parser.add_argument(
        "--output",
        type=str,
        default=None,
        help="Also save the preview HTML to this file path",
    )

    # ---- themes subcommand ----
    themes_parser = subparsers.add_parser(
        "themes",
        help="List or show theme presets",
        description="List all available theme presets or show details for a specific theme.",
    )

    themes_group = themes_parser.add_mutually_exclusive_group(required=True)
    themes_group.add_argument(
        "--list", "-l",
        action="store_true",
        help="List all available theme presets",
    )
    themes_group.add_argument(
        "--show", "-s",
        type=str,
        metavar="NAME",
        help="Show detailed configuration for a theme",
    )

    # ---- init subcommand ----
    init_parser = subparsers.add_parser(
        "init",
        help="Initialize a liquid glass component file",
        description="Generate a liquid glass component file for the specified framework.",
    )

    init_parser.add_argument(
        "--type", "-t",
        type=str,
        choices=["css", "react", "vue", "svelte", "html"],
        default="css",
        help="Framework type (default: css)",
    )
    init_parser.add_argument(
        "--theme",
        type=str,
        default="crystal",
        help="Theme preset name (default: crystal)",
    )
    init_parser.add_argument(
        "--blur", "-b",
        type=int,
        default=None,
        help="Blur intensity in pixels (0-50)",
    )
    init_parser.add_argument(
        "--opacity", "-o",
        type=float,
        default=None,
        help="Background opacity (0.0-1.0)",
    )
    init_parser.add_argument(
        "--color", "-c",
        type=str,
        default=None,
        help="Primary color in hex format",
    )
    init_parser.add_argument(
        "--border-radius", "-r",
        type=int,
        default=None,
        help="Border radius in pixels (0-100)",
    )
    init_parser.add_argument(
        "--gloss", "-g",
        type=float,
        default=None,
        help="Gloss intensity (0.0-1.0)",
    )
    init_parser.add_argument(
        "--output",
        type=str,
        default=None,
        help="Output file path (default: auto-generated filename)",
    )

    return parser


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------

def main(argv=None):
    """Main entry point for the GlassForge CLI.

    Args:
        argv: Command-line arguments (defaults to sys.argv[1:]).
    """
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command is None:
        parser.print_help()
        sys.exit(0)

    # Dispatch to the appropriate command handler
    handlers = {
        "generate": cmd_generate,
        "preview": cmd_preview,
        "themes": cmd_themes,
        "init": cmd_init,
    }

    handler = handlers.get(args.command)
    if handler:
        handler(args)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
