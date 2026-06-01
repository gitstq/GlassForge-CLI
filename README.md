<div align="center">

# 🔮 GlassForge-CLI

**轻量级终端液态玻璃UI效果生成引擎 | Lightweight Terminal Liquid Glass UI Effect Generation Engine**

[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-Zero-orange.svg)]()
[![82 Tests](https://img.shields.io/badge/Tests-82%20Passed-brightgreen.svg)]()

**一键生成 Apple 液态玻璃风格 UI 效果代码，支持 CSS / React / Vue / Svelte / HTML 五种输出格式 🚀**

[English](#english) · [简体中文](#简体中文) · [繁體中文](#繁體中文)

</div>

---

## 简体中文

### 🎉 项目介绍

**GlassForge-CLI** 是一款零依赖的终端命令行工具，灵感来源于 Apple 2025 WWDC 发布的「液态玻璃（Liquid Glass）」设计语言。它能一键生成精美的毛玻璃 UI 效果代码，支持 **CSS、React（TypeScript）、Vue 3（SFC）、Svelte、HTML** 五种输出格式，让开发者无需手动编写复杂的 CSS 即可将液态玻璃效果集成到任何项目中。

**🦞 自研差异化亮点：**
- 🔧 **跨框架通用** — 不限于单一框架，一套工具覆盖前端全技术栈
- ⚡ **零外部依赖** — 仅使用 Python 标准库，即装即用，无环境陷阱
- 🎨 **6 套精心调校的预设主题** — 水晶、极光、深海、熔岩、薄荷、日落，开箱即用
- 🖥️ **浏览器实时预览** — 一键在浏览器中查看效果，所见即所得
- 🌙 **暗色/亮色模式自适应** — 自动适配系统主题偏好
- 📦 **项目初始化** — 快速将液态玻璃组件集成到现有项目中

### ✨ 核心特性

- 🎨 **6 套预设主题**：水晶（Crystal）、极光（Aurora）、深海（Ocean）、熔岩（Lava）、薄荷（Mint）、日落（Sunset）
- 📝 **5 种输出格式**：纯 CSS、React TSX 组件、Vue 3 SFC 组件、Svelte 组件、完整 HTML 演示页面
- 🔧 **高度可定制**：模糊度、透明度、主色调、边框圆角、光泽强度均可自定义
- ⚡ **零外部依赖**：仅使用 Python 标准库（argparse、unittest、webbrowser、tempfile 等）
- 🌙 **暗色模式自适应**：通过 `prefers-color-scheme` 自动切换
- ✨ **内置动画效果**：光泽闪烁（Shimmer）和辉光脉冲（Glow Pulse）动画
- 🖥️ **浏览器预览**：一键生成 HTML 并在浏览器中打开预览
- 📦 **项目初始化**：支持快速初始化各框架的液态玻璃组件文件
- 🧪 **82 个单元测试**：完整的测试覆盖，确保代码质量

### 🚀 快速开始

**环境要求：**
- Python 3.8 或更高版本
- pip（Python 包管理器）

**安装步骤：**

```bash
# 克隆仓库
git clone https://github.com/gitstq/GlassForge-CLI.git
cd GlassForge-CLI

# 安装（零外部依赖，即装即用）
pip install .
```

**快速使用：**

```bash
# 使用默认水晶主题生成纯 CSS 代码
glassforge generate --type css

# 使用极光主题生成 React 组件
glassforge generate --type react --theme aurora

# 使用日落主题生成 Vue 组件
glassforge generate --type vue --theme sunset

# 使用薄荷主题生成 Svelte 组件
glassforge generate --type svelte --theme mint

# 生成完整 HTML 演示页面并在浏览器中预览
glassforge preview --theme ocean

# 列出所有可用主题
glassforge themes --list

# 查看主题详细配置
glassforge themes --show aurora

# 初始化项目（将组件文件添加到当前项目）
glassforge init --type react --theme crystal
```

### 📖 详细使用指南

#### `glassforge generate` — 生成液态玻璃效果代码

| 参数 | 简写 | 说明 | 默认值 |
|------|------|------|--------|
| `--type` | `-t` | 输出类型：css、react、vue、svelte、html | css |
| `--theme` | | 预设主题名称 | crystal |
| `--blur` | `-b` | 模糊强度（0-50px） | 主题默认值 |
| `--opacity` | `-o` | 背景透明度（0.0-1.0） | 主题默认值 |
| `--color` | `-c` | 主色调（十六进制颜色值） | 主题默认值 |
| `--border-radius` | `-r` | 边框圆角（0-100px） | 主题默认值 |
| `--gloss` | `-g` | 光泽强度（0.0-1.0） | 主题默认值 |
| `--output` | | 输出文件路径 | 自动生成 |

**自定义示例：**

```bash
# 自定义参数生成
glassforge generate --type css --theme aurora --blur 30 --opacity 0.8 --color "#00ff88" --border-radius 32 --gloss 0.9 --output my-glass.css

# 生成 React 组件到指定文件
glassforge generate --type react --theme sunset --output src/components/LiquidGlass.tsx

# 生成 Vue 组件
glassforge generate --type vue --theme mint --output src/components/LiquidGlass.vue
```

#### `glassforge preview` — 浏览器预览

```bash
# 使用指定主题预览
glassforge preview --theme crystal
glassforge preview --theme aurora
```

#### `glassforge themes` — 主题管理

```bash
# 列出所有主题
glassforge themes --list

# 查看主题详细信息
glassforge themes --show crystal
glassforge themes --show aurora
```

#### `glassforge init` — 项目初始化

```bash
# 初始化 React 项目
glassforge init --type react --theme crystal

# 初始化 Vue 项目
glassforge init --type vue --theme mint

# 初始化 Svelte 项目
glassforge init --type svelte --theme ocean
```

#### 预设主题一览

| 主题 | 英文名 | 风格描述 |
|------|--------|----------|
| 💎 水晶 | Crystal | 透明清亮，白色高光，经典纯净 |
| 🌌 极光 | Aurora | 蓝绿渐变，梦幻迷离，科技感 |
| 🌊 深海 | Ocean | 深蓝渐变，沉稳大气，深邃 |
| 🌋 熔岩 | Lava | 红橙渐变，热烈奔放，活力 |
| 🌿 薄荷 | Mint | 绿色清新，柔和自然，舒适 |
| 🌅 日落 | Sunset | 橙紫渐变，温暖浪漫，优雅 |

### 💡 设计思路与迭代规划

**设计理念：**
GlassForge-CLI 的核心理念是「**让液态玻璃效果触手可及**」。Apple 在 2025 WWDC 上推出的液态玻璃设计语言惊艳了整个设计界，但将其集成到实际项目中需要大量 CSS 调试工作。GlassForge-CLI 通过模板引擎和预设主题系统，将复杂的 CSS 效果封装为简单的 CLI 命令，让任何开发者都能在几秒内获得生产级的液态玻璃 UI 代码。

**技术选型原因：**
- **Python 标准库**：选择零依赖方案确保工具可在任何 Python 环境中即装即用，无需担心版本冲突
- **模板引擎模式**：通过抽象基类 + 具体模板实现的策略模式，轻松扩展新的框架支持
- **CSS 自定义属性**：生成的代码使用 CSS 变量，方便用户在项目中二次定制

**后续迭代计划：**
- [ ] 新增 Figma/Sketch 设计稿导入功能
- [ ] 新增 Tailwind CSS 插件输出
- [ ] 新增 Angular 组件模板
- [ ] 新增自定义主题创建与导出功能
- [ ] 新增在线 Web 版本

### 📦 安装与部署指南

```bash
# 从 PyPI 安装（未来发布后）
pip install glassforge-cli

# 从源码安装
git clone https://github.com/gitstq/GlassForge-CLI.git
cd GlassForge-CLI
pip install .

# 验证安装
glassforge --help
```

**兼容环境：**
- Python 3.8+
- macOS / Linux / Windows
- 所有现代浏览器（backdrop-filter 支持）

### 🤝 贡献指南

欢迎贡献代码！请遵循以下规范：

1. **Fork** 本仓库
2. 创建功能分支：`git checkout -b feat/your-feature`
3. 提交更改：`git commit -m "feat: add your feature"`
4. 推送分支：`git push origin feat/your-feature`
5. 提交 **Pull Request**

**提交规范：** 遵循 Angular Commit Convention
- `feat:` 新增功能
- `fix:` 修复问题
- `docs:` 文档更新
- `refactor:` 代码重构
- `test:` 测试相关
- `chore:` 构建/工具链相关

### 📄 开源协议

本项目基于 [MIT License](LICENSE) 开源。

---

## 繁體中文

### 🎉 專案介紹

**GlassForge-CLI** 是一款零依賴的終端命令列工具，靈感來源於 Apple 2025 WWDC 發布的「液態玻璃（Liquid Glass）」設計語言。它能一鍵生成精美的毛玻璃 UI 效果程式碼，支援 **CSS、React（TypeScript）、Vue 3（SFC）、Svelte、HTML** 五種輸出格式，讓開發者無需手動編寫複雜的 CSS 即可將液態玻璃效果整合到任何專案中。

**🦞 自研差異化亮點：**
- 🔧 **跨框架通用** — 不限於單一框架，一套工具覆蓋前端全技術棧
- ⚡ **零外部依賴** — 僅使用 Python 標準庫，即裝即用，無環境陷阱
- 🎨 **6 套精心調校的預設主題** — 水晶、極光、深海、熔岩、薄荷、日落，開箱即用
- 🖥️ **瀏覽器即時預覽** — 一鍵在瀏覽器中查看效果，所見即所得
- 🌙 **暗色/亮色模式自適應** — 自動適配系統主題偏好
- 📦 **專案初始化** — 快速將液態玻璃元件整合到現有專案中

### ✨ 核心特性

- 🎨 **6 套預設主題**：水晶（Crystal）、極光（Aurora）、深海（Ocean）、熔岩（Lava）、薄荷（Mint）、日落（Sunset）
- 📝 **5 種輸出格式**：純 CSS、React TSX 元件、Vue 3 SFC 元件、Svelte 元件、完整 HTML 演示頁面
- 🔧 **高度可自訂**：模糊度、透明度、主色調、邊框圓角、光澤強度均可自訂
- ⚡ **零外部依賴**：僅使用 Python 標準庫
- 🌙 **暗色模式自適應**：透過 `prefers-color-scheme` 自動切換
- ✨ **內建動畫效果**：光澤閃爍（Shimmer）和輝光脈衝（Glow Pulse）動畫
- 🖥️ **瀏覽器預覽**：一鍵生成 HTML 並在瀏覽器中開啟預覽
- 📦 **專案初始化**：支援快速初始化各框架的液態玻璃元件檔案
- 🧪 **82 個單元測試**：完整的測試覆蓋，確保程式碼品質

### 🚀 快速開始

**環境要求：**
- Python 3.8 或更高版本
- pip（Python 套件管理器）

**安裝步驟：**

```bash
# 克隆倉庫
git clone https://github.com/gitstq/GlassForge-CLI.git
cd GlassForge-CLI

# 安裝（零外部依賴，即裝即用）
pip install .
```

**快速使用：**

```bash
# 使用預設水晶主題生成純 CSS 程式碼
glassforge generate --type css

# 使用極光主題生成 React 元件
glassforge generate --type react --theme aurora

# 使用日落主題生成 Vue 元件
glassforge generate --type vue --theme sunset

# 使用薄荷主題生成 Svelte 元件
glassforge generate --type svelte --theme mint

# 生成完整 HTML 演示頁面並在瀏覽器中預覽
glassforge preview --theme ocean

# 列出所有可用主題
glassforge themes --list

# 查看主題詳細配置
glassforge themes --show aurora

# 初始化專案（將元件檔案新增到當前專案）
glassforge init --type react --theme crystal
```

### 📖 詳細使用指南

#### `glassforge generate` — 生成液態玻璃效果程式碼

| 參數 | 簡寫 | 說明 | 預設值 |
|------|------|------|--------|
| `--type` | `-t` | 輸出類型：css、react、vue、svelte、html | css |
| `--theme` | | 預設主題名稱 | crystal |
| `--blur` | `-b` | 模糊強度（0-50px） | 主題預設值 |
| `--opacity` | `-o` | 背景透明度（0.0-1.0） | 主題預設值 |
| `--color` | `-c` | 主色調（十六進位顏色值） | 主題預設值 |
| `--border-radius` | `-r` | 邊框圓角（0-100px） | 主題預設值 |
| `--gloss` | `-g` | 光澤強度（0.0-1.0） | 主題預設值 |
| `--output` | | 輸出檔案路徑 | 自動生成 |

**自訂範例：**

```bash
# 自訂參數生成
glassforge generate --type css --theme aurora --blur 30 --opacity 0.8 --color "#00ff88" --border-radius 32 --gloss 0.9 --output my-glass.css

# 生成 React 元件到指定檔案
glassforge generate --type react --theme sunset --output src/components/LiquidGlass.tsx

# 生成 Vue 元件
glassforge generate --type vue --theme mint --output src/components/LiquidGlass.vue
```

#### 預設主題一覽

| 主題 | 英文名 | 風格描述 |
|------|--------|----------|
| 💎 水晶 | Crystal | 透明清亮，白色高光，經典純淨 |
| 🌌 極光 | Aurora | 藍綠漸層，夢幻迷離，科技感 |
| 🌊 深海 | Ocean | 深藍漸層，沉穩大氣，深邃 |
| 🌋 熔岩 | Lava | 紅橙漸層，熱烈奔放，活力 |
| 🌿 薄荷 | Mint | 綠色清新，柔和自然，舒適 |
| 🌅 日落 | Sunset | 橙紫漸層，溫暖浪漫，優雅 |

### 💡 設計思路與迭代規劃

**設計理念：**
GlassForge-CLI 的核心理念是「**讓液態玻璃效果觸手可及**」。Apple 在 2025 WWDC 上推出的液態玻璃設計語言驚豔了整個設計界，但將其整合到實際專案中需要大量 CSS 除錯工作。GlassForge-CLI 透過模板引擎和預設主題系統，將複雜的 CSS 效果封裝為簡單的 CLI 命令，讓任何開發者都能在幾秒內獲得生產級的液態玻璃 UI 程式碼。

**後續迭代計畫：**
- [ ] 新增 Figma/Sketch 設計稿匯入功能
- [ ] 新增 Tailwind CSS 插件輸出
- [ ] 新增 Angular 元件模板
- [ ] 新增自訂主題建立與匯出功能
- [ ] 新增線上 Web 版本

### 📦 安裝與部署指南

```bash
# 從原始碼安裝
git clone https://github.com/gitstq/GlassForge-CLI.git
cd GlassForge-CLI
pip install .

# 驗證安裝
glassforge --help
```

**相容環境：**
- Python 3.8+
- macOS / Linux / Windows
- 所有現代瀏覽器（backdrop-filter 支援）

### 🤝 貢獻指南

歡迎貢獻程式碼！請遵循以下規範：

1. **Fork** 本倉庫
2. 建立功能分支：`git checkout -b feat/your-feature`
3. 提交變更：`git commit -m "feat: add your feature"`
4. 推送分支：`git push origin feat/your-feature`
5. 提交 **Pull Request**

### 📄 開源協議

本專案基於 [MIT License](LICENSE) 開源。

---

## English

### 🎉 Project Introduction

**GlassForge-CLI** is a zero-dependency terminal CLI tool inspired by Apple's "Liquid Glass" design language unveiled at WWDC 2025. It generates stunning frosted glass UI effect code with a single command, supporting **CSS, React (TypeScript), Vue 3 (SFC), Svelte, and HTML** output formats. Developers can integrate liquid glass effects into any project without manually writing complex CSS.

**🦞 Key Differentiators:**
- 🔧 **Cross-Framework** — Not limited to a single framework, one tool covers the entire frontend ecosystem
- ⚡ **Zero External Dependencies** — Uses only Python standard library, install and run instantly
- 🎨 **6 Carefully Tuned Preset Themes** — Crystal, Aurora, Ocean, Lava, Mint, Sunset — ready to use out of the box
- 🖥️ **Browser Live Preview** — One-click preview in your browser, WYSIWYG
- 🌙 **Dark/Light Mode Adaptive** — Automatically adapts to system theme preferences
- 📦 **Project Initialization** — Quickly integrate liquid glass components into existing projects

### ✨ Core Features

- 🎨 **6 Preset Themes**: Crystal, Aurora, Ocean, Lava, Mint, Sunset
- 📝 **5 Output Formats**: Pure CSS, React TSX Component, Vue 3 SFC Component, Svelte Component, Full HTML Demo Page
- 🔧 **Highly Customizable**: Blur, opacity, primary color, border-radius, gloss intensity — all configurable
- ⚡ **Zero External Dependencies**: Uses only Python standard library (argparse, unittest, webbrowser, tempfile, etc.)
- 🌙 **Dark Mode Adaptive**: Automatic switching via `prefers-color-scheme`
- ✨ **Built-in Animations**: Shimmer and Glow Pulse effects
- 🖥️ **Browser Preview**: Generate HTML and open in browser with one command
- 📦 **Project Init**: Quick initialization of liquid glass component files for any framework
- 🧪 **82 Unit Tests**: Comprehensive test coverage ensuring code quality

### 🚀 Quick Start

**Prerequisites:**
- Python 3.8 or higher
- pip (Python package manager)

**Installation:**

```bash
# Clone the repository
git clone https://github.com/gitstq/GlassForge-CLI.git
cd GlassForge-CLI

# Install (zero external dependencies, ready to use)
pip install .
```

**Quick Usage:**

```bash
# Generate pure CSS with default crystal theme
glassforge generate --type css

# Generate React component with aurora theme
glassforge generate --type react --theme aurora

# Generate Vue component with sunset theme
glassforge generate --type vue --theme sunset

# Generate Svelte component with mint theme
glassforge generate --type svelte --theme mint

# Generate full HTML demo page and preview in browser
glassforge preview --theme ocean

# List all available themes
glassforge themes --list

# Show theme details
glassforge themes --show aurora

# Initialize project (add component files to current project)
glassforge init --type react --theme crystal
```

### 📖 Detailed Usage Guide

#### `glassforge generate` — Generate Liquid Glass Effect Code

| Option | Short | Description | Default |
|--------|-------|-------------|---------|
| `--type` | `-t` | Output type: css, react, vue, svelte, html | css |
| `--theme` | | Preset theme name | crystal |
| `--blur` | `-b` | Blur intensity (0-50px) | theme default |
| `--opacity` | `-o` | Background opacity (0.0-1.0) | theme default |
| `--color` | `-c` | Primary color (hex value) | theme default |
| `--border-radius` | `-r` | Border radius (0-100px) | theme default |
| `--gloss` | `-g` | Gloss intensity (0.0-1.0) | theme default |
| `--output` | | Output file path | auto-generated |

**Customization Examples:**

```bash
# Generate with custom parameters
glassforge generate --type css --theme aurora --blur 30 --opacity 0.8 --color "#00ff88" --border-radius 32 --gloss 0.9 --output my-glass.css

# Generate React component to specific file
glassforge generate --type react --theme sunset --output src/components/LiquidGlass.tsx

# Generate Vue component
glassforge generate --type vue --theme mint --output src/components/LiquidGlass.vue
```

#### `glassforge preview` — Browser Preview

```bash
# Preview with a specific theme
glassforge preview --theme crystal
glassforge preview --theme aurora
```

#### `glassforge themes` — Theme Management

```bash
# List all themes
glassforge themes --list

# Show theme details
glassforge themes --show crystal
glassforge themes --show aurora
```

#### `glassforge init` — Project Initialization

```bash
# Initialize React project
glassforge init --type react --theme crystal

# Initialize Vue project
glassforge init --type vue --theme mint

# Initialize Svelte project
glassforge init --type svelte --theme ocean
```

#### Theme Gallery

| Theme | Name | Description |
|-------|------|-------------|
| 💎 Crystal | Crystal | Transparent and clear with white highlights, classic and pure |
| 🌌 Aurora | Aurora | Blue-green gradient, dreamy and tech-forward |
| 🌊 Ocean | Ocean | Deep blue gradient, calm and profound |
| 🌋 Lava | Lava | Red-orange gradient, passionate and vibrant |
| 🌿 Mint | Mint | Fresh green, soft and natural |
| 🌅 Sunset | Sunset | Orange-purple gradient, warm and elegant |

### 💡 Design Philosophy & Roadmap

**Design Philosophy:**
GlassForge-CLI's core philosophy is "**Making liquid glass effects accessible to everyone**." Apple's liquid glass design language unveiled at WWDC 2025 captivated the design world, but integrating it into real projects requires extensive CSS debugging. GlassForge-CLI encapsulates complex CSS effects into simple CLI commands through a template engine and preset theme system, enabling any developer to obtain production-ready liquid glass UI code in seconds.

**Technical Choices:**
- **Python Standard Library**: Zero-dependency approach ensures the tool works in any Python environment without version conflicts
- **Template Engine Pattern**: Strategy pattern with abstract base class + concrete templates for easy framework extension
- **CSS Custom Properties**: Generated code uses CSS variables for easy secondary customization

**Roadmap:**
- [ ] Figma/Sketch design import support
- [ ] Tailwind CSS plugin output
- [ ] Angular component template
- [ ] Custom theme creation and export
- [ ] Online Web version

### 📦 Installation & Deployment

```bash
# Install from source
git clone https://github.com/gitstq/GlassForge-CLI.git
cd GlassForge-CLI
pip install .

# Verify installation
glassforge --help
```

**Compatible Environments:**
- Python 3.8+
- macOS / Linux / Windows
- All modern browsers (with backdrop-filter support)

### 🤝 Contributing

Contributions are welcome! Please follow these guidelines:

1. **Fork** this repository
2. Create a feature branch: `git checkout -b feat/your-feature`
3. Commit your changes: `git commit -m "feat: add your feature"`
4. Push to the branch: `git push origin feat/your-feature`
5. Submit a **Pull Request**

**Commit Convention:** Follow Angular Commit Convention
- `feat:` New features
- `fix:` Bug fixes
- `docs:` Documentation updates
- `refactor:` Code refactoring
- `test:` Test-related changes
- `chore:` Build/tooling changes

### 📄 License

This project is licensed under the [MIT License](LICENSE).

---

<div align="center">

**Made with 🦞 by [LobsterBot](https://github.com/gitstq)**

**Inspired by Apple Liquid Glass Design Language**

</div>
