#!/usr/bin/env python3
"""
Markdown Editor - Main Entry Point

A modern, user-friendly markdown editor with live preview capabilities.
"""

import sys
import os
from pathlib import Path

# Add src to path
current_dir = Path(__file__).parent
src_dir = current_dir / "src"
sys.path.insert(0, str(src_dir))

from markdown_editor.app import main

if __name__ == "__main__":
    sys.exit(main())