# Markdown Editor - Windows Setup & Usage Guide

## 🪟 Complete Windows Installation and Usage Instructions

### Prerequisites

1. **Python 3.8 or Later**
   - Download from [python.org](https://www.python.org/downloads/windows/)
   - ⚠️ **IMPORTANT:** During installation, check "Add Python to PATH"
   - Verify installation by opening Command Prompt and typing: `python --version`

2. **Command Prompt or PowerShell**
   - Built into Windows
   - Access via: Start Menu → "cmd" or "PowerShell"

---

## 📥 Installation Instructions

### Step 1: Download the Project

```cmd
# If you have git installed
git clone <repository-url>
cd markdown-editor

# OR download ZIP and extract, then:
cd path\to\extracted\markdown-editor
```

### Step 2: Install Dependencies

**Option A: Using pip (Recommended)**
```cmd
# Install all required packages
pip install -r requirements.txt
```

**Option B: Manual Installation**
```cmd
pip install PyQt6>=6.6.0
pip install markdown>=3.5.1
pip install pymdown-extensions>=10.4
pip install Pygments>=2.17.2
pip install QDarkStyle>=3.2.3
```

### Step 3: Verify Installation

```cmd
python -c "import PyQt6, markdown, pymdownx; print('✅ All dependencies installed successfully!')"
```

---

## 🚀 Running the Application

### Method 1: Direct Execution (Recommended)

```cmd
# Navigate to the project directory
cd path\to\markdown-editor

# Run the application
python main.py
```

### Method 2: With a File

```cmd
# Open the app with a specific markdown file
python main.py path\to\your\document.md

# Example:
python main.py test_sample.md
```

### Method 3: Run as Module

```cmd
python -m src.markdown_editor.app
```

### Method 4: Install as Package

```cmd
# Install the app as a Python package
pip install -e .

# Then run from anywhere
markdown-editor
```

---

## 🎯 Quick Start Guide

### First Launch

1. **Open Command Prompt**
   - Press `Windows Key + R`
   - Type `cmd` and press Enter

2. **Navigate to Project**
   ```cmd
   cd C:\path\to\markdown-editor
   ```

3. **Launch Application**
   ```cmd
   python main.py
   ```

4. **Start Editing**
   - The app will open with a clean interface
   - Choose "Rich Text" tab for WYSIWYG editing
   - Or "Markdown" tab for syntax editing
   - See live preview on the right

### Basic Workflow

1. **Create New Document:** `Ctrl+N` or File → New
2. **Open Existing File:** `Ctrl+O` or File → Open
3. **Save Your Work:** `Ctrl+S` or File → Save
4. **Format Text:** Use toolbar or keyboard shortcuts
5. **Export:** File → Export as HTML

---

## 🔧 Troubleshooting

### Common Windows Issues

**"Python is not recognized as an internal or external command"**
```cmd
# Solution: Add Python to PATH
# 1. Find Python installation (usually C:\Python3x\ or C:\Users\Username\AppData\Local\Programs\Python\)
# 2. Add to Windows PATH environment variable
# 3. Restart Command Prompt

# Quick test:
where python
```

**"No module named 'PyQt6'"**
```cmd
# Solution: Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# If still failing, try:
pip install PyQt6 --force-reinstall
```

**"Permission denied" errors**
```cmd
# Solution: Run as administrator or use --user flag
pip install --user -r requirements.txt
```

**App window appears but is blank**
```cmd
# Solution: Graphics driver issue, try:
python main.py --platform windows
```

### Performance on Windows

**For Better Performance:**
- Close other applications
- Use SSD if available
- Ensure at least 4GB RAM available
- Use dark theme for less eye strain

**File Paths:**
- Use forward slashes or escaped backslashes in file paths
- Example: `C:/Users/Username/Documents/file.md`
- Or: `C:\\Users\\Username\\Documents\\file.md`

---

## 📂 Windows File Management

### Default Save Locations

**Documents Folder:**
```cmd
C:\Users\%USERNAME%\Documents
```

**Auto-save Location:**
```cmd
C:\Users\%USERNAME%\.markdown_editor\autosave\
```

### File Associations (Optional)

To open .md files directly with Markdown Editor:

1. Right-click any `.md` file
2. Choose "Open with" → "Choose another app"
3. Browse to your Python installation
4. Add command line: `python "C:\path\to\markdown-editor\main.py"`

---

## ⌨️ Windows-Specific Shortcuts

| Action | Windows Shortcut |
|--------|------------------|
| New File | `Ctrl+N` |
| Open File | `Ctrl+O` |
| Save | `Ctrl+S` |
| Save As | `Ctrl+Shift+S` |
| Bold | `Ctrl+B` |
| Italic | `Ctrl+I` |
| Underline | `Ctrl+U` |
| Find | `Ctrl+F` |
| Fullscreen | `F11` |
| Toggle Preview | `F5` |
| Close App | `Alt+F4` or `Ctrl+Q` |

---

## 🖱️ Windows UI Features

### Window Management
- **Minimize:** Click `-` button or `Windows+Down`
- **Maximize:** Click `□` button or `Windows+Up`
- **Close:** Click `×` button or `Alt+F4`
- **Snap to Side:** `Windows+Left/Right`

### Theme Selection
- **Light Theme:** Default Windows-friendly appearance
- **Dark Theme:** Better for low-light environments
- Switch via: View → Theme → Light/Dark

---

## 📋 Complete Example Session

```cmd
# 1. Open Command Prompt
Windows Key + R → type "cmd" → Enter

# 2. Navigate to project
cd C:\Users\YourName\Downloads\markdown-editor

# 3. Install dependencies (first time only)
pip install -r requirements.txt

# 4. Launch application
python main.py

# 5. Optional: Open with sample file
python main.py test_sample.md
```

---

## 🔄 Updating the Application

```cmd
# If installed via git
git pull origin main
pip install -r requirements.txt

# If downloaded as ZIP
# Download new version and extract
# Copy your documents to new folder
# Install dependencies again
```

---

## 💡 Windows Tips & Best Practices

### File Organization
```
📁 Documents\
  📁 Markdown Projects\
    📁 Project 1\
      📄 notes.md
      📄 readme.md
    📁 Project 2\
      📄 documentation.md
```

### Backup Strategy
- Save frequently (`Ctrl+S`)
- Use auto-save feature (enabled by default)
- Export important documents as HTML
- Keep backups in cloud storage (OneDrive, Google Drive)

### Performance Tips
- Close preview pane for large documents (`F5`)
- Use Markdown mode for better performance
- Restart app periodically for optimal performance
- Keep Windows updated for best compatibility

---

## 🆘 Getting Help

### Built-in Help
- **Markdown Syntax:** Help → Markdown Help
- **About:** Help → About

### External Resources
- **Windows Command Prompt Guide:** [Microsoft Docs](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/windows-commands)
- **Python on Windows:** [Python.org Windows FAQ](https://docs.python.org/3/faq/windows.html)

### Support
- Check `README.md` for general information
- Review `docs\USER_GUIDE.md` for detailed usage
- Report issues on the project repository

---

## ✅ Verification Checklist

Before using the app, ensure:

- [ ] Python 3.8+ installed and in PATH
- [ ] All dependencies installed (`pip install -r requirements.txt`)
- [ ] Application launches without errors (`python main.py`)
- [ ] Can create and save documents
- [ ] Preview pane displays formatted content
- [ ] Toolbar formatting works
- [ ] Can switch between Rich Text and Markdown modes

---

**🎉 You're ready to use Markdown Editor on Windows!**

**Quick Start Command:**
```cmd
cd path\to\markdown-editor && python main.py
```