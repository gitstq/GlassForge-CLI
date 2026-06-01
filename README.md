# GlassForge CLI

A zero-dependency terminal CLI tool for generating Apple Liquid Glass UI effect CSS code.

## Features

- **6 Preset Themes**: Crystal, Aurora, Ocean, Lava, Mint, Sunset
- **5 Output Formats**: CSS, React (TypeScript), Vue 3 (SFC), Svelte, HTML
- **Fully Customizable**: Blur, opacity, color, border-radius, gloss intensity
- **Zero Dependencies**: Uses only Python standard library
- **Dark Mode**: Automatic dark/light mode adaptation
- **Animations**: Shimmer and glow effects built-in

## Installation

```bash
pip install .
```

## Quick Start

```bash
# Generate CSS with default crystal theme
glassforge generate --type css

# Generate React component with aurora theme
glassforge generate --type react --theme aurora

# Preview in browser
glassforge preview --theme sunset

# List all themes
glassforge themes --list

# Show theme details
glassforge themes --show ocean

# Initialize a Vue component
glassforge init --type vue --theme mint
```

## Commands

### `glassforge generate`

Generate liquid glass effect code.

| Option | Short | Description | Default |
|--------|-------|-------------|---------|
| `--type` | `-t` | Output type: css, react, vue, svelte, html | css |
| `--theme` | | Theme preset name | crystal |
| `--blur` | `-b` | Blur intensity (0-50px) | theme default |
| `--opacity` | `-o` | Background opacity (0.0-1.0) | theme default |
| `--color` | `-c` | Primary color (hex) | theme default |
| `--border-radius` | `-r` | Border radius (0-100px) | theme default |
| `--gloss` | `-g` | Gloss intensity (0.0-1.0) | theme default |
| `--output` | | Output file path | auto |

### `glassforge preview`

Open a browser preview of the liquid glass effect.

### `glassforge themes`

List or show theme presets.

### `glassforge init`

Initialize a project with liquid glass component files.

## License

MIT
