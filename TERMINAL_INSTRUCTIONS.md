# Markdown Editor - Terminal Instructions

## 🖥️ How to Run the Markdown Editor from Terminal

This guide covers running the Markdown Editor application from the terminal/command line on Windows, macOS, and Linux.

---

## 📋 Prerequisites

### 1. Python Installation
- **Python 3.8 or later** is required
- Verify installation:
  ```bash
  python --version
  # or
  python3 --version
  ```

### 2. pip Package Manager
- Usually comes with Python
- Verify:
  ```bash
  pip --version
  ```

---

## 🚀 Quick Start (Any Operating System)

### 1. Download/Clone the Project
```bash
# If using git
git clone <repository-url>
cd markdown-editor

# If downloaded as ZIP
cd path/to/extracted/markdown-editor
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Application
```bash
python main.py
```

---

## 🪟 Windows Instructions

### Option 1: Command Prompt
```cmd
# Open Command Prompt (Win+R, type "cmd")
cd C:\path\to\markdown-editor
pip install -r requirements.txt
python main.py
```

### Option 2: PowerShell
```powershell
# Open PowerShell (Win+X, select "PowerShell")
cd C:\path\to\markdown-editor
pip install -r requirements.txt
python main.py
```

### Option 3: Windows Batch File (Easiest)
```cmd
# Double-click run_markdown_editor.bat
# OR from command line:
run_markdown_editor.bat
```

### Windows-Specific Commands
```cmd
# Check Python installation
where python
python --version

# Install dependencies with user permissions
pip install --user -r requirements.txt

# Run with specific file
python main.py "C:\Users\YourName\Documents\document.md"

# Alternative Python command
py main.py
```

---

## 🍎 macOS Instructions

### Option 1: Terminal
```bash
# Open Terminal (Cmd+Space, type "Terminal")
cd /path/to/markdown-editor
pip3 install -r requirements.txt
python3 main.py
```

### Option 2: Using Homebrew Python
```bash
# If you have Homebrew Python
cd /path/to/markdown-editor
pip install -r requirements.txt
python main.py
```

### macOS-Specific Commands
```bash
# Check Python installation
which python3
python3 --version

# Install dependencies for user
pip3 install --user -r requirements.txt

# Run with specific file
python3 main.py ~/Documents/document.md

# Make executable (optional)
chmod +x main.py
./main.py
```

---

## 🐧 Linux Instructions

### Ubuntu/Debian
```bash
# Install Python and pip if needed
sudo apt update
sudo apt install python3 python3-pip

# Navigate to project
cd /path/to/markdown-editor

# Install dependencies
pip3 install -r requirements.txt

# Run application
python3 main.py
```

### CentOS/RHEL/Fedora
```bash
# Install Python and pip if needed
sudo dnf install python3 python3-pip  # Fedora
sudo yum install python3 python3-pip  # CentOS/RHEL

# Navigate and run
cd /path/to/markdown-editor
pip3 install -r requirements.txt
python3 main.py
```

### Arch Linux
```bash
# Install Python if needed
sudo pacman -S python python-pip

# Navigate and run
cd /path/to/markdown-editor
pip install -r requirements.txt
python main.py
```

---

## 🎯 Running with Files

### Open Specific File
```bash
# Basic syntax
python main.py /path/to/your/document.md

# Examples:
python main.py test_sample.md
python main.py ~/Documents/notes.md
python main.py "C:\Users\Name\Documents\file with spaces.md"
```

### Multiple Ways to Launch
```bash
# Method 1: Direct execution
python main.py

# Method 2: Module execution
python -m src.markdown_editor.app

# Method 3: After package installation
pip install -e .
markdown-editor

# Method 4: With Python path
PYTHONPATH=src python -m markdown_editor.app
```

---

## 🔧 Installation Methods

### Method 1: Basic Installation
```bash
cd markdown-editor
pip install -r requirements.txt
python main.py
```

### Method 2: Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv markdown_env

# Activate (Linux/macOS)
source markdown_env/bin/activate

# Activate (Windows)
markdown_env\Scripts\activate

# Install and run
pip install -r requirements.txt
python main.py

# Deactivate when done
deactivate
```

### Method 3: Package Installation
```bash
# Install as editable package
pip install -e .

# Run from anywhere
markdown-editor

# Or with file
markdown-editor document.md
```

### Method 4: System-wide Installation
```bash
# Install system-wide (not recommended for development)
sudo pip install -r requirements.txt  # Linux/macOS
python main.py
```

---

## 🛠️ Troubleshooting

### Common Issues and Solutions

**"Command not found" or "No such file"**
```bash
# Make sure you're in the right directory
ls -la  # Linux/macOS
dir     # Windows

# Look for main.py
find . -name "main.py"  # Linux/macOS
dir main.py             # Windows
```

**"No module named 'PyQt6'"**
```bash
# Install dependencies
pip install -r requirements.txt

# If that fails, install individually
pip install PyQt6>=6.6.0
pip install markdown>=3.5.1
pip install pymdown-extensions>=10.4
pip install Pygments>=2.17.2
```

**"Permission denied"**
```bash
# Linux/macOS: Use user installation
pip install --user -r requirements.txt

# Or use sudo (not recommended)
sudo pip install -r requirements.txt

# Windows: Run as administrator or use --user
pip install --user -r requirements.txt
```

**"Python not found"**
```bash
# Try alternative commands
python3 main.py  # Linux/macOS
py main.py       # Windows

# Check Python installation
which python     # Linux/macOS
where python     # Windows
```

**GUI doesn't appear**
```bash
# Linux: May need additional packages
sudo apt install python3-pyqt6  # Ubuntu/Debian

# Check display
echo $DISPLAY  # Should show something like :0

# For WSL on Windows
export DISPLAY=localhost:0.0
```

---

## 🎮 Advanced Usage

### Command Line Options
```bash
# Run with specific file
python main.py document.md

# Run with debug output
python main.py --debug  # (if implemented)

# Check version
python -c "import sys; sys.path.insert(0, 'src'); from markdown_editor import __version__; print(__version__)"
```

### Environment Variables
```bash
# Set Python path
export PYTHONPATH="${PYTHONPATH}:$(pwd)/src"
python -m markdown_editor.app

# Set Qt platform (if needed)
export QT_QPA_PLATFORM=xcb  # Linux
python main.py
```

### Development Mode
```bash
# Install in development mode
pip install -e .

# Run tests (if available)
python -m pytest tests/

# Format code (if tools installed)
black src/
flake8 src/
```

---

## 📊 System Requirements

### Minimum Requirements
- **OS**: Windows 10, macOS 10.14, Ubuntu 18.04 (or equivalent)
- **Python**: 3.8+
- **RAM**: 4GB
- **Storage**: 100MB free space
- **Display**: 1024x768 minimum

### Recommended Requirements
- **OS**: Windows 11, macOS 12+, Ubuntu 20.04+
- **Python**: 3.10+
- **RAM**: 8GB+
- **Storage**: 500MB free space
- **Display**: 1920x1080 or higher

---

## ✅ Verification Steps

### 1. Check Installation
```bash
python --version                    # Should be 3.8+
pip list | grep PyQt6              # Should show PyQt6
python -c "import PyQt6; print('OK')"  # Should print OK
```

### 2. Test Application
```bash
python main.py                     # Should open GUI
python main.py test_sample.md      # Should open with sample file
```

### 3. Verify Features
- [ ] Application window opens
- [ ] Can switch between Rich Text and Markdown tabs
- [ ] Live preview updates
- [ ] Can create new document (Ctrl+N)
- [ ] Can save document (Ctrl+S)
- [ ] Toolbar buttons work
- [ ] Can export to HTML

---

## 📝 Quick Reference

### Essential Commands
```bash
# Navigate to project
cd path/to/markdown-editor

# Install dependencies (first time only)
pip install -r requirements.txt

# Run application
python main.py

# Run with file
python main.py your-document.md

# Get help
python main.py --help  # (if implemented)
```

### Keyboard Shortcuts in App
- `Ctrl+N` - New document
- `Ctrl+O` - Open file
- `Ctrl+S` - Save
- `Ctrl+B` - Bold
- `Ctrl+I` - Italic
- `F5` - Toggle preview
- `F11` - Fullscreen

---

## 🆘 Getting Help

If you encounter issues:

1. **Check this guide** for common solutions
2. **Verify Python version**: `python --version`
3. **Check dependencies**: `pip list`
4. **Read error messages** carefully
5. **Check file permissions** and paths
6. **Try virtual environment** if system-wide installation fails

---

**🎉 You're ready to use Markdown Editor!**

**Quick start command:**
```bash
cd markdown-editor && pip install -r requirements.txt && python main.py
```