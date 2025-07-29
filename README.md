# Markdown Editor

A modern, sophisticated Python application that functions as a markdown text processor with WYSIWYG interface and real-time preview capabilities.

![Markdown Editor](https://img.shields.io/badge/Python-3.8+-blue.svg)
![PyQt6](https://img.shields.io/badge/PyQt6-6.6+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## Features

### 🎨 Modern Interface
- **Clean, professional UI** with contemporary styling
- **Dual editing modes**: Rich text (WYSIWYG) and raw markdown
- **Live preview** with real-time rendering
- **Split-pane layout** for editing and preview side-by-side
- **Dark and light themes** for comfortable editing

### 📝 Rich Text Editing
- **WYSIWYG editor** with intuitive formatting controls
- **Comprehensive toolbar** with font controls, formatting options
- **Header styles** (H1-H6) with visual hierarchy
- **Text formatting**: Bold, italic, underline
- **Lists**: Bullet points and numbered lists
- **Links and images** insertion
- **Code blocks** with syntax highlighting
- **Block quotes** for emphasized content

### 📁 File Management
- **Create, open, save** markdown files
- **Recent files** menu with quick access
- **Auto-save** functionality to prevent data loss
- **Export to HTML** with styled output
- **Cross-platform** file handling

### ⚡ Advanced Features
- **Real-time markdown processing** with extensions
- **Syntax highlighting** in code blocks
- **Table support** for structured data
- **Task lists** with checkboxes
- **Metadata extraction** from front matter
- **Word count** and document statistics
- **Keyboard shortcuts** for efficient editing

## Installation

### Prerequisites
- Python 3.8 or later
- pip package manager

### Install Dependencies

```bash
# Clone or download the repository
cd markdown-editor

# Install required packages
pip install -r requirements.txt
```

### Dependencies
- **PyQt6** (≥6.6.0) - Modern GUI framework
- **markdown** (≥3.5.1) - Core markdown processing
- **pymdown-extensions** (≥10.4) - Extended markdown features
- **Pygments** (≥2.17.2) - Syntax highlighting
- **QDarkStyle** (≥3.2.3) - Dark theme support

## Usage

### Running the Application

```bash
# Run from the root directory
python main.py

# Or run the module directly
python -m src.markdown_editor.app

# Open a specific file
python main.py document.md
```

### Basic Workflow

1. **Create a new document** (Ctrl+N) or open existing (Ctrl+O)
2. **Choose editing mode**: Rich text for WYSIWYG or Markdown for raw editing
3. **Format your content** using the toolbar or keyboard shortcuts
4. **Preview in real-time** in the right pane
5. **Save your work** (Ctrl+S) or export to HTML

### Keyboard Shortcuts

| Action | Shortcut |
|--------|----------|
| New File | Ctrl+N |
| Open File | Ctrl+O |
| Save File | Ctrl+S |
| Save As | Ctrl+Shift+S |
| Bold | Ctrl+B |
| Italic | Ctrl+I |
| Underline | Ctrl+U |
| Find | Ctrl+F |
| Replace | Ctrl+H |
| Toggle Preview | F5 |
| Fullscreen | F11 |
| Headers | Ctrl+1-6 |
| Quit | Ctrl+Q |

## Project Structure

```
markdown-editor/
├── src/
│   └── markdown_editor/
│       ├── __init__.py          # Package initialization
│       ├── app.py               # Main application entry point
│       ├── core/                # Core functionality
│       │   ├── __init__.py
│       │   ├── markdown_processor.py  # Markdown processing
│       │   └── file_manager.py        # File operations
│       ├── ui/                  # User interface components
│       │   ├── __init__.py
│       │   ├── main_window.py   # Main application window
│       │   └── editor_widget.py # Rich text editor widget
│       └── utils/               # Utility functions
│           ├── __init__.py
│           └── themes.py        # Theme management
├── assets/                      # Resources (future use)
├── docs/                       # Documentation
├── tests/                      # Unit tests (future)
├── requirements.txt            # Python dependencies
├── main.py                     # Application entry point
└── README.md                   # This file
```

## Architecture

### Core Components

1. **MarkdownProcessor**: Handles conversion between markdown and HTML using the `markdown` library with extensions for enhanced features.

2. **FileManager**: Manages file operations including open, save, auto-save, and recent files tracking.

3. **MarkdownEditorWidget**: The main editing interface with rich text and raw markdown modes, plus live preview.

4. **MainWindow**: Application window with menu system, toolbar, and status bar integration.

5. **ThemeManager**: Handles light/dark themes and custom styling.

### Design Principles

- **Separation of Concerns**: Clear separation between UI, business logic, and file handling
- **Signal-Slot Architecture**: PyQt6 signals for loose coupling between components
- **Extensible Design**: Plugin-ready architecture for future enhancements
- **Error Handling**: Comprehensive error handling with user feedback
- **Settings Persistence**: User preferences saved between sessions

## Customization

### Themes

The application supports light and dark themes. You can extend themes by modifying `src/markdown_editor/utils/themes.py`:

```python
# Add custom theme
theme_manager = ThemeManager()
custom_theme = {
    "stylesheet": "/* Your CSS here */",
    "colors": {
        "background": "#color",
        "text": "#color",
        # ... more colors
    }
}
theme_manager.add_custom_theme("custom", custom_theme)
```

### Markdown Extensions

Extend markdown processing by modifying the extensions list in `MarkdownProcessor`:

```python
self.extensions = [
    'markdown.extensions.extra',
    'your.custom.extension',
    # ... more extensions
]
```

## Contributing

We welcome contributions! Please feel free to:

1. **Report bugs** by creating issues
2. **Suggest features** for enhancement
3. **Submit pull requests** with improvements
4. **Improve documentation** and examples

### Development Setup

```bash
# Clone the repository
git clone <repository-url>
cd markdown-editor

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

## Troubleshooting

### Common Issues

1. **Import Errors**: Ensure all dependencies are installed with `pip install -r requirements.txt`

2. **Font Issues**: The application uses system fonts. If fonts appear incorrect, check your system font installation.

3. **Theme Problems**: If themes don't apply correctly, try restarting the application.

4. **File Permission Errors**: Ensure you have read/write permissions for the files and directories you're working with.

### Getting Help

- Check the built-in help: Help → Markdown Help
- Review the documentation in the `docs/` directory
- Create an issue for bugs or feature requests

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- **PyQt6** for the excellent GUI framework
- **Python-Markdown** for robust markdown processing
- **PyMdown Extensions** for enhanced markdown features
- **Pygments** for syntax highlighting capabilities

## Future Enhancements

- [ ] Plugin system for custom extensions
- [ ] PDF export functionality
- [ ] Collaborative editing features
- [ ] Custom CSS themes
- [ ] Table editor dialog
- [ ] Find and replace functionality
- [ ] Spell check integration
- [ ] Document outline/table of contents
- [ ] Live word count in status bar
- [ ] Distraction-free writing mode

---

**Markdown Editor** - Bringing modern word processing experience to markdown editing.
