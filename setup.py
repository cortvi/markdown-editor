#!/usr/bin/env python3
"""
Setup script for Markdown Editor application.
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README for long description
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text(encoding="utf-8") if readme_file.exists() else ""

# Read requirements
requirements_file = Path(__file__).parent / "requirements.txt"
requirements = []
if requirements_file.exists():
    requirements = requirements_file.read_text(encoding="utf-8").strip().split("\n")

setup(
    name="markdown-editor",
    version="1.0.0",
    description="A modern, user-friendly markdown editor with live preview",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Markdown Editor Team",
    author_email="info@markdowneditor.app",
    url="https://github.com/yourusername/markdown-editor",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-qt>=4.0.0",
            "black>=22.0.0",
            "flake8>=4.0.0",
            "mypy>=0.950",
        ]
    },
    entry_points={
        "console_scripts": [
            "markdown-editor=markdown_editor.app:main",
        ],
        "gui_scripts": [
            "markdown-editor-gui=markdown_editor.app:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Text Editors",
        "Topic :: Text Processing :: Markup",
        "Topic :: Software Development :: Documentation",
        "Environment :: X11 Applications :: Qt",
        "Typing :: Typed",
    ],
    keywords="markdown editor wysiwyg preview text processing",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/markdown-editor/issues",
        "Source": "https://github.com/yourusername/markdown-editor",
        "Documentation": "https://github.com/yourusername/markdown-editor/tree/main/docs",
    },
    include_package_data=True,
    zip_safe=False,
)