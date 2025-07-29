# Markdown Editor - User Guide

Welcome to the Markdown Editor User Guide! This comprehensive guide will help you make the most of your markdown editing experience.

## Table of Contents

1. [Getting Started](#getting-started)
2. [Interface Overview](#interface-overview)
3. [Editing Modes](#editing-modes)
4. [Formatting Text](#formatting-text)
5. [File Management](#file-management)
6. [Customization](#customization)
7. [Tips and Tricks](#tips-and-tricks)
8. [Troubleshooting](#troubleshooting)

## Getting Started

### First Launch

When you first launch Markdown Editor, you'll see:
- A clean interface with a toolbar at the top
- Two tabs: "Rich Text" and "Markdown" for different editing modes
- A live preview pane on the right side
- A status bar showing cursor position and word count

### Creating Your First Document

1. Start typing in the Rich Text tab for WYSIWYG editing
2. Use the toolbar buttons for formatting
3. Watch the live preview update automatically
4. Save your work with Ctrl+S

## Interface Overview

### Menu Bar

**File Menu**
- New (Ctrl+N): Create a new document
- Open (Ctrl+O): Open an existing markdown file
- Recent Files: Quick access to recently opened files
- Save (Ctrl+S): Save the current document
- Save As (Ctrl+Shift+S): Save with a new name
- Export as HTML: Export your document as an HTML file
- Export as PDF: Export as PDF (future feature)

**Edit Menu**
- Undo/Redo: Standard text editing operations
- Cut/Copy/Paste: Clipboard operations
- Select All: Select entire document
- Find/Replace: Search and replace text (future feature)

**View Menu**
- Toggle Preview (F5): Show/hide the preview pane
- Toggle Fullscreen (F11): Enter distraction-free mode
- Theme: Switch between light and dark themes

**Format Menu**
- Bold/Italic: Text formatting options
- Headers: Quick access to header levels (H1-H6)
- Lists: Create bullet or numbered lists

**Tools Menu**
- Word Count: Display document statistics
- Insert Table: Add tables to your document (future feature)
- Preferences: Customize application settings (future feature)

**Help Menu**
- About: Application information
- Markdown Help: Quick reference for markdown syntax

### Toolbar

The toolbar provides quick access to common formatting options:

- **Font Controls**: Font family and size selection
- **Text Formatting**: Bold (B), Italic (I), Underline (U)
- **Headers**: Dropdown to select header levels
- **Lists**: Bullet and numbered list buttons
- **Links**: Insert links and images
- **Code**: Inline code and code blocks
- **Quote**: Block quote formatting

### Status Bar

The status bar displays:
- Current file name and path
- Cursor position (line and column)
- Word and character count
- File encoding (UTF-8)

## Editing Modes

### Rich Text Mode

The Rich Text tab provides a WYSIWYG (What You See Is What You Get) editing experience:

- **Visual formatting**: See headers, bold, italic text as you type
- **Toolbar integration**: Use buttons to apply formatting
- **Font controls**: Change font family and size
- **Direct formatting**: Select text and apply formatting directly

**Best for**: Users who prefer visual editing and are new to markdown.

### Markdown Mode

The Markdown tab shows raw markdown syntax:

- **Syntax highlighting**: Code is highlighted for readability
- **Direct markdown**: Type markdown syntax directly
- **Monospace font**: Uses a coding font for better readability
- **Quick formatting**: Use toolbar to insert markdown syntax

**Best for**: Experienced markdown users and those who want full control over syntax.

### Live Preview

The preview pane shows how your document will look when rendered:

- **Real-time updates**: Changes appear instantly
- **Styled output**: Clean, readable formatting
- **Scroll synchronization**: Preview follows your editing position
- **Print-ready**: Shows exactly how exports will appear

## Formatting Text

### Basic Formatting

**Bold Text**
- Rich Text: Select text and click B button or Ctrl+B
- Markdown: Surround text with `**bold**` or `__bold__`

**Italic Text**
- Rich Text: Select text and click I button or Ctrl+I
- Markdown: Surround text with `*italic*` or `_italic_`

**Underline**
- Rich Text: Select text and click U button or Ctrl+U
- Markdown: Use `<u>underline</u>` HTML tags

### Headers

Create headers for document structure:

**Using Toolbar**
1. Place cursor at the beginning of a line
2. Select header level from dropdown
3. Type your header text

**Using Markdown**
```markdown
# Header 1
## Header 2
### Header 3
#### Header 4
##### Header 5
###### Header 6
```

**Keyboard Shortcuts**
- Ctrl+1 through Ctrl+6 for headers H1-H6

### Lists

**Bullet Lists**
- Rich Text: Click bullet list button
- Markdown: Start lines with `-`, `*`, or `+`

```markdown
- First item
- Second item
  - Sub-item
  - Another sub-item
```

**Numbered Lists**
- Rich Text: Click numbered list button
- Markdown: Start lines with numbers

```markdown
1. First item
2. Second item
   1. Sub-item
   2. Another sub-item
```

### Links and Images

**Links**
- Rich Text: Click Link button, enter URL and text
- Markdown: `[Link text](URL)`

**Images**
- Rich Text: Click Image button, enter image URL and alt text
- Markdown: `![Alt text](image URL)`

### Code

**Inline Code**
- Rich Text: Select text and click Code button
- Markdown: Surround with backticks `` `code` ``

**Code Blocks**
- Rich Text: Click Code Block button
- Markdown: Use triple backticks

```markdown
```python
def hello_world():
    print("Hello, World!")
```
```

### Block Quotes

**Creating Quotes**
- Rich Text: Click Quote button
- Markdown: Start lines with `>`

```markdown
> This is a block quote.
> It can span multiple lines.
```

### Tables

Tables can be created using markdown syntax:

```markdown
| Header 1 | Header 2 | Header 3 |
|----------|----------|----------|
| Cell 1   | Cell 2   | Cell 3   |
| Cell 4   | Cell 5   | Cell 6   |
```

### Task Lists

Create interactive checklists:

```markdown
- [x] Completed task
- [ ] Incomplete task
- [ ] Another task
```

## File Management

### Creating Files

1. **New Document**: File → New or Ctrl+N
2. **Start typing**: Begin with your content
3. **Save when ready**: Ctrl+S to save

### Opening Files

1. **Open Dialog**: File → Open or Ctrl+O
2. **Recent Files**: File → Recent Files for quick access
3. **Command Line**: Launch with `python main.py filename.md`

### Saving Files

**Save (Ctrl+S)**
- Saves to current file location
- Prompts for location if new file

**Save As (Ctrl+Shift+S)**
- Always prompts for new location
- Useful for creating copies

**Auto-Save**
- Automatically saves temporary copies
- Prevents data loss from crashes
- Saved to `~/.markdown_editor/autosave/`

### File Types

**Supported Extensions**
- `.md` - Standard markdown files
- `.markdown` - Alternative markdown extension
- `.mdown`, `.mkd`, `.mkdn` - Other markdown variations

**Export Formats**
- HTML: Styled web page output
- PDF: Coming in future updates

## Customization

### Themes

**Switching Themes**
1. View → Theme → Light/Dark
2. Theme persists between sessions
3. Applied instantly to entire interface

**Theme Features**
- Light theme: Clean, bright interface
- Dark theme: Easy on eyes for low-light editing
- Consistent styling across all components

### Settings

Application settings are automatically saved:
- Window size and position
- Theme preference
- Preview pane visibility
- Recent files list

### Font Preferences

**Rich Text Editor**
- Change font family using toolbar dropdown
- Adjust font size with spinbox
- Settings apply to current session

**Markdown Editor**
- Uses monospace font for better code readability
- Font size can be adjusted in toolbar

## Tips and Tricks

### Productivity Tips

1. **Use Keyboard Shortcuts**: Learn common shortcuts for faster editing
2. **Split-Screen**: Keep preview open while editing
3. **Recent Files**: Use File → Recent Files for quick access
4. **Headers**: Use headers to structure long documents
5. **Auto-Save**: Don't worry about losing work - auto-save has you covered

### Markdown Best Practices

1. **Consistent Styling**: Use the same syntax throughout
2. **Line Breaks**: Leave blank lines between sections
3. **Headers**: Use logical header hierarchy (H1 → H2 → H3)
4. **Links**: Use descriptive link text
5. **Images**: Always include alt text for accessibility

### Workflow Suggestions

**For Beginners**
1. Start with Rich Text mode
2. Use toolbar for formatting
3. Check preview frequently
4. Switch to Markdown mode to learn syntax

**For Advanced Users**
1. Work primarily in Markdown mode
2. Use keyboard shortcuts extensively
3. Learn extended markdown syntax
4. Customize themes and settings

### Performance Tips

1. **Large Files**: Use Markdown mode for better performance with large documents
2. **Auto-Save**: Longer intervals for large files
3. **Preview**: Toggle off preview for very large documents
4. **Memory**: Restart application occasionally for best performance

## Troubleshooting

### Common Issues

**Application Won't Start**
- Check Python version (3.8+ required)
- Verify all dependencies are installed
- Run `pip install -r requirements.txt`

**Formatting Not Working**
- Ensure you're in the correct editing mode
- Check if text is selected for formatting
- Try switching between Rich Text and Markdown modes

**Preview Not Updating**
- Check if preview pane is visible (F5 to toggle)
- Try typing in the other editing mode
- Restart application if problem persists

**File Won't Open**
- Verify file exists and is readable
- Check file extension is supported (.md, .markdown, etc.)
- Ensure file isn't corrupted

**Slow Performance**
- Close and reopen large files
- Restart the application
- Switch to Markdown mode for large documents
- Check available system memory

### Getting Help

1. **Built-in Help**: Help → Markdown Help for syntax reference
2. **Documentation**: Check docs/ folder for detailed guides
3. **Community**: Report issues on the project repository
4. **Debug**: Check console output for error messages

### Error Recovery

**Lost Changes**
- Check auto-save folder: `~/.markdown_editor/autosave/`
- Look for `*_autosave.md` files
- Recent changes may be recoverable

**Corrupted Files**
- Open in text editor to check content
- Copy content to new file in Markdown Editor
- Report corruption issues to developers

---

**Need More Help?** Check the project documentation or create an issue on the repository for additional support.