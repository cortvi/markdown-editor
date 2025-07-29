"""
Theme management for the markdown editor application.
"""

from PyQt6.QtCore import QObject, pyqtSignal
from typing import Dict, Any


class ThemeManager(QObject):
    """
    Manages themes and styling for the application.
    """
    
    theme_changed = pyqtSignal(str)  # theme name
    
    def __init__(self):
        """Initialize the theme manager."""
        super().__init__()
        self.current_theme = "light"
        self._themes = {
            "light": self._get_light_theme(),
            "dark": self._get_dark_theme()
        }
    
    def _get_light_theme(self) -> Dict[str, Any]:
        """Get light theme configuration."""
        return {
            "name": "Light",
            "stylesheet": """
                QMainWindow {
                    background-color: #ffffff;
                    color: #212529;
                }
                
                QMenuBar {
                    background-color: #f8f9fa;
                    border-bottom: 1px solid #dee2e6;
                    padding: 4px;
                    color: #212529;
                }
                
                QMenuBar::item {
                    background-color: transparent;
                    padding: 4px 8px;
                    border-radius: 3px;
                    margin: 2px;
                }
                
                QMenuBar::item:selected {
                    background-color: #e9ecef;
                }
                
                QMenu {
                    background-color: #ffffff;
                    border: 1px solid #dee2e6;
                    border-radius: 4px;
                    padding: 4px;
                }
                
                QMenu::item {
                    padding: 6px 12px;
                    border-radius: 3px;
                }
                
                QMenu::item:selected {
                    background-color: #e9ecef;
                }
                
                QMenu::separator {
                    height: 1px;
                    background-color: #dee2e6;
                    margin: 4px;
                }
                
                QStatusBar {
                    background-color: #f8f9fa;
                    border-top: 1px solid #dee2e6;
                    color: #6c757d;
                }
                
                QToolBar {
                    background-color: #f8f9fa;
                    border: none;
                    spacing: 2px;
                    padding: 4px;
                }
                
                QToolButton {
                    background-color: transparent;
                    border: 1px solid transparent;
                    border-radius: 3px;
                    padding: 6px;
                    margin: 1px;
                    font-weight: bold;
                    min-width: 20px;
                    min-height: 20px;
                }
                
                QToolButton:hover {
                    background-color: #e9ecef;
                    border-color: #adb5bd;
                }
                
                QToolButton:pressed, QToolButton:checked {
                    background-color: #dee2e6;
                    border-color: #6c757d;
                }
                
                QTabWidget::pane {
                    border: 1px solid #dee2e6;
                    background-color: #ffffff;
                }
                
                QTabBar::tab {
                    background-color: #f8f9fa;
                    border: 1px solid #dee2e6;
                    border-bottom: none;
                    padding: 8px 16px;
                    margin-right: 2px;
                }
                
                QTabBar::tab:selected {
                    background-color: #ffffff;
                    border-bottom: 1px solid #ffffff;
                }
                
                QTabBar::tab:hover {
                    background-color: #e9ecef;
                }
                
                QTextEdit, QPlainTextEdit {
                    background-color: #ffffff;
                    border: 1px solid #dee2e6;
                    border-radius: 4px;
                    padding: 8px;
                    font-family: "Consolas", "Monaco", "Courier New", monospace;
                    line-height: 1.4;
                }
                
                QTextEdit:focus, QPlainTextEdit:focus {
                    border-color: #0d6efd;
                    outline: none;
                }
                
                QComboBox, QSpinBox {
                    background-color: #ffffff;
                    border: 1px solid #ced4da;
                    border-radius: 3px;
                    padding: 4px 8px;
                    min-width: 80px;
                }
                
                QComboBox:hover, QSpinBox:hover {
                    border-color: #adb5bd;
                }
                
                QComboBox:focus, QSpinBox:focus {
                    border-color: #0d6efd;
                    outline: none;
                }
                
                QComboBox::drop-down {
                    border: none;
                    width: 20px;
                }
                
                QComboBox::down-arrow {
                    image: none;
                    border-left: 4px solid transparent;
                    border-right: 4px solid transparent;
                    border-top: 4px solid #6c757d;
                    margin-top: 2px;
                }
                
                QSplitter::handle {
                    background-color: #dee2e6;
                }
                
                QSplitter::handle:horizontal {
                    width: 3px;
                }
                
                QSplitter::handle:vertical {
                    height: 3px;
                }
                
                QFrame[frameShape="4"] {
                    border: none;
                    border-top: 1px solid #dee2e6;
                }
                
                QProgressBar {
                    border: 1px solid #dee2e6;
                    border-radius: 3px;
                    text-align: center;
                    background-color: #f8f9fa;
                }
                
                QProgressBar::chunk {
                    background-color: #0d6efd;
                    border-radius: 2px;
                }
                
                QScrollBar:vertical {
                    background-color: #f8f9fa;
                    width: 12px;
                    border: none;
                }
                
                QScrollBar::handle:vertical {
                    background-color: #ced4da;
                    border-radius: 6px;
                    min-height: 20px;
                    margin: 0px 2px;
                }
                
                QScrollBar::handle:vertical:hover {
                    background-color: #adb5bd;
                }
                
                QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                    height: 0px;
                }
                
                QScrollBar:horizontal {
                    background-color: #f8f9fa;
                    height: 12px;
                    border: none;
                }
                
                QScrollBar::handle:horizontal {
                    background-color: #ced4da;
                    border-radius: 6px;
                    min-width: 20px;
                    margin: 2px 0px;
                }
                
                QScrollBar::handle:horizontal:hover {
                    background-color: #adb5bd;
                }
                
                QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
                    width: 0px;
                }
            """,
            "colors": {
                "background": "#ffffff",
                "text": "#212529",
                "accent": "#0d6efd",
                "border": "#dee2e6",
                "hover": "#e9ecef"
            }
        }
    
    def _get_dark_theme(self) -> Dict[str, Any]:
        """Get dark theme configuration."""
        return {
            "name": "Dark",
            "stylesheet": """
                QMainWindow {
                    background-color: #212529;
                    color: #f8f9fa;
                }
                
                QMenuBar {
                    background-color: #343a40;
                    border-bottom: 1px solid #495057;
                    padding: 4px;
                    color: #f8f9fa;
                }
                
                QMenuBar::item {
                    background-color: transparent;
                    padding: 4px 8px;
                    border-radius: 3px;
                    margin: 2px;
                }
                
                QMenuBar::item:selected {
                    background-color: #495057;
                }
                
                QMenu {
                    background-color: #343a40;
                    border: 1px solid #495057;
                    border-radius: 4px;
                    padding: 4px;
                    color: #f8f9fa;
                }
                
                QMenu::item {
                    padding: 6px 12px;
                    border-radius: 3px;
                }
                
                QMenu::item:selected {
                    background-color: #495057;
                }
                
                QMenu::separator {
                    height: 1px;
                    background-color: #495057;
                    margin: 4px;
                }
                
                QStatusBar {
                    background-color: #343a40;
                    border-top: 1px solid #495057;
                    color: #adb5bd;
                }
                
                QToolBar {
                    background-color: #343a40;
                    border: none;
                    spacing: 2px;
                    padding: 4px;
                }
                
                QToolButton {
                    background-color: transparent;
                    border: 1px solid transparent;
                    border-radius: 3px;
                    padding: 6px;
                    margin: 1px;
                    font-weight: bold;
                    min-width: 20px;
                    min-height: 20px;
                    color: #f8f9fa;
                }
                
                QToolButton:hover {
                    background-color: #495057;
                    border-color: #6c757d;
                }
                
                QToolButton:pressed, QToolButton:checked {
                    background-color: #6c757d;
                    border-color: #adb5bd;
                }
                
                QTabWidget::pane {
                    border: 1px solid #495057;
                    background-color: #212529;
                }
                
                QTabBar::tab {
                    background-color: #343a40;
                    border: 1px solid #495057;
                    border-bottom: none;
                    padding: 8px 16px;
                    margin-right: 2px;
                    color: #f8f9fa;
                }
                
                QTabBar::tab:selected {
                    background-color: #212529;
                    border-bottom: 1px solid #212529;
                }
                
                QTabBar::tab:hover {
                    background-color: #495057;
                }
                
                QTextEdit, QPlainTextEdit {
                    background-color: #2d3338;
                    border: 1px solid #495057;
                    border-radius: 4px;
                    padding: 8px;
                    font-family: "Consolas", "Monaco", "Courier New", monospace;
                    line-height: 1.4;
                    color: #f8f9fa;
                }
                
                QTextEdit:focus, QPlainTextEdit:focus {
                    border-color: #0d6efd;
                    outline: none;
                }
                
                QComboBox, QSpinBox {
                    background-color: #343a40;
                    border: 1px solid #495057;
                    border-radius: 3px;
                    padding: 4px 8px;
                    min-width: 80px;
                    color: #f8f9fa;
                }
                
                QComboBox:hover, QSpinBox:hover {
                    border-color: #6c757d;
                }
                
                QComboBox:focus, QSpinBox:focus {
                    border-color: #0d6efd;
                    outline: none;
                }
                
                QComboBox::drop-down {
                    border: none;
                    width: 20px;
                }
                
                QComboBox::down-arrow {
                    image: none;
                    border-left: 4px solid transparent;
                    border-right: 4px solid transparent;
                    border-top: 4px solid #adb5bd;
                    margin-top: 2px;
                }
                
                QSplitter::handle {
                    background-color: #495057;
                }
                
                QSplitter::handle:horizontal {
                    width: 3px;
                }
                
                QSplitter::handle:vertical {
                    height: 3px;
                }
                
                QFrame[frameShape="4"] {
                    border: none;
                    border-top: 1px solid #495057;
                }
                
                QProgressBar {
                    border: 1px solid #495057;
                    border-radius: 3px;
                    text-align: center;
                    background-color: #343a40;
                    color: #f8f9fa;
                }
                
                QProgressBar::chunk {
                    background-color: #0d6efd;
                    border-radius: 2px;
                }
                
                QScrollBar:vertical {
                    background-color: #343a40;
                    width: 12px;
                    border: none;
                }
                
                QScrollBar::handle:vertical {
                    background-color: #6c757d;
                    border-radius: 6px;
                    min-height: 20px;
                    margin: 0px 2px;
                }
                
                QScrollBar::handle:vertical:hover {
                    background-color: #adb5bd;
                }
                
                QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                    height: 0px;
                }
                
                QScrollBar:horizontal {
                    background-color: #343a40;
                    height: 12px;
                    border: none;
                }
                
                QScrollBar::handle:horizontal {
                    background-color: #6c757d;
                    border-radius: 6px;
                    min-width: 20px;
                    margin: 2px 0px;
                }
                
                QScrollBar::handle:horizontal:hover {
                    background-color: #adb5bd;
                }
                
                QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
                    width: 0px;
                }
            """,
            "colors": {
                "background": "#212529",
                "text": "#f8f9fa",
                "accent": "#0d6efd",
                "border": "#495057",
                "hover": "#495057"
            }
        }
    
    def get_available_themes(self) -> list:
        """Get list of available theme names."""
        return list(self._themes.keys())
    
    def get_current_theme(self) -> str:
        """Get the current theme name."""
        return self.current_theme
    
    def set_theme(self, theme_name: str) -> bool:
        """
        Set the current theme.
        
        Args:
            theme_name: Name of the theme to set
            
        Returns:
            True if theme was set successfully
        """
        if theme_name in self._themes:
            self.current_theme = theme_name
            self.theme_changed.emit(theme_name)
            return True
        return False
    
    def get_theme_stylesheet(self, theme_name: str = None) -> str:
        """
        Get the stylesheet for a theme.
        
        Args:
            theme_name: Name of the theme (current theme if None)
            
        Returns:
            CSS stylesheet string
        """
        theme_name = theme_name or self.current_theme
        if theme_name in self._themes:
            return self._themes[theme_name]["stylesheet"]
        return ""
    
    def get_theme_colors(self, theme_name: str = None) -> Dict[str, str]:
        """
        Get the color palette for a theme.
        
        Args:
            theme_name: Name of the theme (current theme if None)
            
        Returns:
            Dictionary of color values
        """
        theme_name = theme_name or self.current_theme
        if theme_name in self._themes:
            return self._themes[theme_name]["colors"]
        return {}
    
    def add_custom_theme(self, name: str, config: Dict[str, Any]) -> bool:
        """
        Add a custom theme.
        
        Args:
            name: Name of the custom theme
            config: Theme configuration dictionary
            
        Returns:
            True if theme was added successfully
        """
        if "stylesheet" in config and "colors" in config:
            self._themes[name] = config
            return True
        return False