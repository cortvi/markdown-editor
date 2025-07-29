"""
Main application window for the markdown editor.
"""

import os
from pathlib import Path
from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QMenuBar, QMenu,
    QStatusBar, QToolBar, QFileDialog, QMessageBox, QApplication,
    QSplashScreen, QLabel, QProgressBar, QAction, QActionGroup
)
from PyQt6.QtCore import Qt, pyqtSignal, QTimer, QThread, pyqtSlot, QSettings
from PyQt6.QtGui import QKeySequence, QIcon, QPixmap, QFont, QAction

from .editor_widget import MarkdownEditorWidget
from ..core.file_manager import FileManager
from ..core.markdown_processor import MarkdownProcessor


class MainWindow(QMainWindow):
    """
    Main application window for the markdown editor.
    """
    
    def __init__(self):
        """Initialize the main window."""
        super().__init__()
        
        # Initialize core components
        self.markdown_processor = MarkdownProcessor()
        self.file_manager = FileManager()
        
        # Settings
        self.settings = QSettings('MarkdownEditor', 'MainWindow')
        
        # State
        self.is_fullscreen = False
        
        self._setup_ui()
        self._setup_connections()
        self._setup_shortcuts()
        self._restore_settings()
        
        # Initialize with empty document
        self.editor.set_markdown_processor(self.markdown_processor)
        self._update_window_title()
    
    def _setup_ui(self):
        """Setup the user interface."""
        # Set window properties
        self.setWindowTitle("Markdown Editor")
        self.setMinimumSize(800, 600)
        self.resize(1200, 800)
        
        # Create central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Main layout
        layout = QVBoxLayout(central_widget)
        layout.setContentsMargins(0, 0, 0, 0)
        
        # Create editor widget
        self.editor = MarkdownEditorWidget()
        layout.addWidget(self.editor)
        
        # Setup menu bar
        self._create_menu_bar()
        
        # Setup status bar
        self._create_status_bar()
        
        # Apply initial styling
        self._apply_styling()
    
    def _create_menu_bar(self):
        """Create the menu bar."""
        menubar = self.menuBar()
        
        # File menu
        file_menu = menubar.addMenu("File")
        
        self.new_action = QAction("New", self)
        self.new_action.setShortcut(QKeySequence.StandardKey.New)
        self.new_action.setStatusTip("Create a new document")
        file_menu.addAction(self.new_action)
        
        self.open_action = QAction("Open...", self)
        self.open_action.setShortcut(QKeySequence.StandardKey.Open)
        self.open_action.setStatusTip("Open an existing document")
        file_menu.addAction(self.open_action)
        
        # Recent files submenu
        self.recent_menu = file_menu.addMenu("Recent Files")
        self._update_recent_files_menu()
        
        file_menu.addSeparator()
        
        self.save_action = QAction("Save", self)
        self.save_action.setShortcut(QKeySequence.StandardKey.Save)
        self.save_action.setStatusTip("Save the current document")
        file_menu.addAction(self.save_action)
        
        self.save_as_action = QAction("Save As...", self)
        self.save_as_action.setShortcut(QKeySequence.StandardKey.SaveAs)
        self.save_as_action.setStatusTip("Save the document with a new name")
        file_menu.addAction(self.save_as_action)
        
        file_menu.addSeparator()
        
        self.export_html_action = QAction("Export as HTML...", self)
        self.export_html_action.setStatusTip("Export document as HTML")
        file_menu.addAction(self.export_html_action)
        
        self.export_pdf_action = QAction("Export as PDF...", self)
        self.export_pdf_action.setStatusTip("Export document as PDF")
        file_menu.addAction(self.export_pdf_action)
        
        file_menu.addSeparator()
        
        self.quit_action = QAction("Quit", self)
        self.quit_action.setShortcut(QKeySequence.StandardKey.Quit)
        self.quit_action.setStatusTip("Exit the application")
        file_menu.addAction(self.quit_action)
        
        # Edit menu
        edit_menu = menubar.addMenu("Edit")
        
        self.undo_action = QAction("Undo", self)
        self.undo_action.setShortcut(QKeySequence.StandardKey.Undo)
        edit_menu.addAction(self.undo_action)
        
        self.redo_action = QAction("Redo", self)
        self.redo_action.setShortcut(QKeySequence.StandardKey.Redo)
        edit_menu.addAction(self.redo_action)
        
        edit_menu.addSeparator()
        
        self.cut_action = QAction("Cut", self)
        self.cut_action.setShortcut(QKeySequence.StandardKey.Cut)
        edit_menu.addAction(self.cut_action)
        
        self.copy_action = QAction("Copy", self)
        self.copy_action.setShortcut(QKeySequence.StandardKey.Copy)
        edit_menu.addAction(self.copy_action)
        
        self.paste_action = QAction("Paste", self)
        self.paste_action.setShortcut(QKeySequence.StandardKey.Paste)
        edit_menu.addAction(self.paste_action)
        
        edit_menu.addSeparator()
        
        self.select_all_action = QAction("Select All", self)
        self.select_all_action.setShortcut(QKeySequence.StandardKey.SelectAll)
        edit_menu.addAction(self.select_all_action)
        
        self.find_action = QAction("Find...", self)
        self.find_action.setShortcut(QKeySequence.StandardKey.Find)
        edit_menu.addAction(self.find_action)
        
        self.replace_action = QAction("Replace...", self)
        self.replace_action.setShortcut(QKeySequence.StandardKey.Replace)
        edit_menu.addAction(self.replace_action)
        
        # View menu
        view_menu = menubar.addMenu("View")
        
        self.toggle_preview_action = QAction("Toggle Preview", self)
        self.toggle_preview_action.setShortcut("F5")
        self.toggle_preview_action.setCheckable(True)
        self.toggle_preview_action.setChecked(True)
        view_menu.addAction(self.toggle_preview_action)
        
        self.fullscreen_action = QAction("Toggle Fullscreen", self)
        self.fullscreen_action.setShortcut("F11")
        view_menu.addAction(self.fullscreen_action)
        
        view_menu.addSeparator()
        
        # Theme submenu
        theme_menu = view_menu.addMenu("Theme")
        self.theme_group = QActionGroup(self)
        
        self.light_theme_action = QAction("Light", self)
        self.light_theme_action.setCheckable(True)
        self.light_theme_action.setChecked(True)
        self.theme_group.addAction(self.light_theme_action)
        theme_menu.addAction(self.light_theme_action)
        
        self.dark_theme_action = QAction("Dark", self)
        self.dark_theme_action.setCheckable(True)
        self.theme_group.addAction(self.dark_theme_action)
        theme_menu.addAction(self.dark_theme_action)
        
        # Format menu
        format_menu = menubar.addMenu("Format")
        
        self.bold_menu_action = QAction("Bold", self)
        self.bold_menu_action.setShortcut(QKeySequence.StandardKey.Bold)
        format_menu.addAction(self.bold_menu_action)
        
        self.italic_menu_action = QAction("Italic", self)
        self.italic_menu_action.setShortcut(QKeySequence.StandardKey.Italic)
        format_menu.addAction(self.italic_menu_action)
        
        format_menu.addSeparator()
        
        # Header submenu
        header_menu = format_menu.addMenu("Headers")
        for i in range(1, 7):
            action = QAction(f"Header {i}", self)
            action.setShortcut(f"Ctrl+{i}")
            action.setData(i)
            header_menu.addAction(action)
        
        format_menu.addSeparator()
        
        self.bullet_list_action = QAction("Bullet List", self)
        format_menu.addAction(self.bullet_list_action)
        
        self.numbered_list_action = QAction("Numbered List", self)
        format_menu.addAction(self.numbered_list_action)
        
        # Tools menu
        tools_menu = menubar.addMenu("Tools")
        
        self.word_count_action = QAction("Word Count", self)
        tools_menu.addAction(self.word_count_action)
        
        self.table_generator_action = QAction("Insert Table...", self)
        tools_menu.addAction(self.table_generator_action)
        
        tools_menu.addSeparator()
        
        self.preferences_action = QAction("Preferences...", self)
        tools_menu.addAction(self.preferences_action)
        
        # Help menu
        help_menu = menubar.addMenu("Help")
        
        self.about_action = QAction("About", self)
        help_menu.addAction(self.about_action)
        
        self.markdown_help_action = QAction("Markdown Help", self)
        help_menu.addAction(self.markdown_help_action)
    
    def _create_status_bar(self):
        """Create the status bar."""
        self.status_bar = self.statusBar()
        
        # File info label
        self.file_info_label = QLabel("Untitled")
        self.status_bar.addWidget(self.file_info_label)
        
        # Progress bar for operations
        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)
        self.progress_bar.setMaximumWidth(200)
        self.status_bar.addPermanentWidget(self.progress_bar)
        
        # Encoding label
        self.encoding_label = QLabel("UTF-8")
        self.status_bar.addPermanentWidget(self.encoding_label)
        
        # Show ready message
        self.status_bar.showMessage("Ready", 2000)
    
    def _setup_connections(self):
        """Setup signal connections."""
        # File operations
        self.new_action.triggered.connect(self._new_file)
        self.open_action.triggered.connect(self._open_file)
        self.save_action.triggered.connect(self._save_file)
        self.save_as_action.triggered.connect(self._save_file_as)
        self.export_html_action.triggered.connect(self._export_html)
        self.export_pdf_action.triggered.connect(self._export_pdf)
        self.quit_action.triggered.connect(self._quit_application)
        
        # Edit operations
        self.undo_action.triggered.connect(self._undo)
        self.redo_action.triggered.connect(self._redo)
        self.cut_action.triggered.connect(self._cut)
        self.copy_action.triggered.connect(self._copy)
        self.paste_action.triggered.connect(self._paste)
        self.select_all_action.triggered.connect(self._select_all)
        self.find_action.triggered.connect(self._find)
        self.replace_action.triggered.connect(self._replace)
        
        # View operations
        self.toggle_preview_action.triggered.connect(self._toggle_preview)
        self.fullscreen_action.triggered.connect(self._toggle_fullscreen)
        self.light_theme_action.triggered.connect(lambda: self._change_theme("light"))
        self.dark_theme_action.triggered.connect(lambda: self._change_theme("dark"))
        
        # Format operations
        self.bold_menu_action.triggered.connect(self._format_bold)
        self.italic_menu_action.triggered.connect(self._format_italic)
        
        # Tools operations
        self.word_count_action.triggered.connect(self._show_word_count)
        self.table_generator_action.triggered.connect(self._insert_table)
        self.preferences_action.triggered.connect(self._show_preferences)
        
        # Help operations
        self.about_action.triggered.connect(self._show_about)
        self.markdown_help_action.triggered.connect(self._show_markdown_help)
        
        # File manager connections
        self.file_manager.file_opened.connect(self._on_file_opened)
        self.file_manager.file_saved.connect(self._on_file_saved)
        self.file_manager.file_created.connect(self._on_file_created)
        self.file_manager.recent_files_updated.connect(self._update_recent_files_menu)
        
        # Editor connections
        self.editor.content_changed.connect(self._on_content_changed)
        self.editor.cursor_position_changed.connect(self._on_cursor_position_changed)
    
    def _setup_shortcuts(self):
        """Setup additional keyboard shortcuts."""
        # Additional shortcuts can be added here
        pass
    
    def _apply_styling(self):
        """Apply styling to the application."""
        # Set application style
        self.setStyleSheet("""
            QMainWindow {
                background-color: #ffffff;
            }
            
            QMenuBar {
                background-color: #f8f9fa;
                border-bottom: 1px solid #dee2e6;
                padding: 4px;
            }
            
            QMenuBar::item {
                background-color: transparent;
                padding: 4px 8px;
                border-radius: 3px;
            }
            
            QMenuBar::item:selected {
                background-color: #e9ecef;
            }
            
            QStatusBar {
                background-color: #f8f9fa;
                border-top: 1px solid #dee2e6;
            }
            
            QToolBar {
                background-color: #f8f9fa;
                border: none;
                spacing: 3px;
                padding: 4px;
            }
            
            QToolButton {
                background-color: transparent;
                border: 1px solid transparent;
                border-radius: 3px;
                padding: 4px;
                margin: 1px;
            }
            
            QToolButton:hover {
                background-color: #e9ecef;
                border-color: #adb5bd;
            }
            
            QToolButton:pressed, QToolButton:checked {
                background-color: #dee2e6;
                border-color: #6c757d;
            }
        """)
    
    def _restore_settings(self):
        """Restore application settings."""
        # Restore window geometry
        if self.settings.contains("geometry"):
            self.restoreGeometry(self.settings.value("geometry"))
        
        # Restore theme
        theme = self.settings.value("theme", "light")
        if theme == "dark":
            self.dark_theme_action.setChecked(True)
            self._change_theme("dark")
        
        # Restore preview visibility
        preview_visible = self.settings.value("preview_visible", True, type=bool)
        self.toggle_preview_action.setChecked(preview_visible)
        if not preview_visible:
            self.editor.toggle_preview()
    
    def _save_settings(self):
        """Save application settings."""
        self.settings.setValue("geometry", self.saveGeometry())
        
        theme = "dark" if self.dark_theme_action.isChecked() else "light"
        self.settings.setValue("theme", theme)
        
        self.settings.setValue("preview_visible", self.toggle_preview_action.isChecked())
    
    # File operations
    def _new_file(self):
        """Create a new file."""
        if self._check_unsaved_changes():
            self.file_manager.new_file()
            self.editor.clear_content()
            self._update_window_title()
            self.status_bar.showMessage("New document created", 2000)
    
    def _open_file(self):
        """Open a file."""
        if not self._check_unsaved_changes():
            return
        
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Open Markdown File",
            "",
            "Markdown Files (*.md *.markdown *.mdown *.mkd *.mkdn);;All Files (*)"
        )
        
        if file_path:
            success, content = self.file_manager.open_file(file_path)
            if success:
                self.editor.set_content(content)
                self._update_window_title()
                self.status_bar.showMessage(f"Opened: {os.path.basename(file_path)}", 2000)
            else:
                QMessageBox.warning(self, "Error", f"Failed to open file:\n{content}")
    
    def _save_file(self):
        """Save the current file."""
        content = self.editor.get_content()
        
        if self.file_manager.get_current_file():
            success, result = self.file_manager.save_file(content)
            if success:
                self._update_window_title()
                self.status_bar.showMessage(f"Saved: {os.path.basename(result)}", 2000)
            else:
                QMessageBox.warning(self, "Error", f"Failed to save file:\n{result}")
        else:
            self._save_file_as()
    
    def _save_file_as(self):
        """Save the file with a new name."""
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save Markdown File",
            "untitled.md",
            "Markdown Files (*.md);;All Files (*)"
        )
        
        if file_path:
            content = self.editor.get_content()
            success, result = self.file_manager.save_file(content, file_path)
            if success:
                self._update_window_title()
                self.status_bar.showMessage(f"Saved: {os.path.basename(result)}", 2000)
            else:
                QMessageBox.warning(self, "Error", f"Failed to save file:\n{result}")
    
    def _export_html(self):
        """Export as HTML."""
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Export as HTML",
            "document.html",
            "HTML Files (*.html);;All Files (*)"
        )
        
        if file_path:
            try:
                content = self.editor.get_content()
                html = self.markdown_processor.markdown_to_html(content)
                
                # Create complete HTML document
                full_html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Exported Document</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }}
        /* Add more CSS styling here */
    </style>
</head>
<body>
    {html}
</body>
</html>"""
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(full_html)
                
                self.status_bar.showMessage(f"Exported to HTML: {os.path.basename(file_path)}", 2000)
                
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Failed to export HTML:\n{str(e)}")
    
    def _export_pdf(self):
        """Export as PDF."""
        # This would require additional dependencies like reportlab or weasyprint
        QMessageBox.information(self, "Info", "PDF export functionality would be implemented with additional libraries.")
    
    def _quit_application(self):
        """Quit the application."""
        if self._check_unsaved_changes():
            self._save_settings()
            QApplication.quit()
    
    # Edit operations
    def _undo(self):
        """Undo last action."""
        self.editor.rich_editor.undo()
    
    def _redo(self):
        """Redo last action."""
        self.editor.rich_editor.redo()
    
    def _cut(self):
        """Cut selected text."""
        if self.editor.tab_widget.currentIndex() == 0:
            self.editor.rich_editor.cut()
        else:
            self.editor.raw_editor.cut()
    
    def _copy(self):
        """Copy selected text."""
        if self.editor.tab_widget.currentIndex() == 0:
            self.editor.rich_editor.copy()
        else:
            self.editor.raw_editor.copy()
    
    def _paste(self):
        """Paste text from clipboard."""
        if self.editor.tab_widget.currentIndex() == 0:
            self.editor.rich_editor.paste()
        else:
            self.editor.raw_editor.paste()
    
    def _select_all(self):
        """Select all text."""
        if self.editor.tab_widget.currentIndex() == 0:
            self.editor.rich_editor.selectAll()
        else:
            self.editor.raw_editor.selectAll()
    
    def _find(self):
        """Show find dialog."""
        QMessageBox.information(self, "Info", "Find functionality would be implemented with a custom dialog.")
    
    def _replace(self):
        """Show replace dialog."""
        QMessageBox.information(self, "Info", "Replace functionality would be implemented with a custom dialog.")
    
    # View operations
    def _toggle_preview(self):
        """Toggle preview pane."""
        self.editor.toggle_preview()
    
    def _toggle_fullscreen(self):
        """Toggle fullscreen mode."""
        if self.isFullScreen():
            self.showNormal()
        else:
            self.showFullScreen()
    
    def _change_theme(self, theme):
        """Change application theme."""
        if theme == "dark":
            # Apply dark theme
            self.setStyleSheet("""
                QMainWindow {
                    background-color: #2b2b2b;
                    color: #ffffff;
                }
                /* Add dark theme styles */
            """)
        else:
            # Apply light theme
            self._apply_styling()
    
    # Format operations
    def _format_bold(self):
        """Apply bold formatting."""
        self.editor.bold_action.trigger()
    
    def _format_italic(self):
        """Apply italic formatting."""
        self.editor.italic_action.trigger()
    
    # Tools operations
    def _show_word_count(self):
        """Show word count dialog."""
        content = self.editor.get_content()
        words = len(content.split()) if content.strip() else 0
        chars = len(content)
        chars_no_spaces = len(content.replace(' ', ''))
        
        QMessageBox.information(
            self,
            "Word Count",
            f"Words: {words}\nCharacters: {chars}\nCharacters (no spaces): {chars_no_spaces}"
        )
    
    def _insert_table(self):
        """Insert table dialog."""
        QMessageBox.information(self, "Info", "Table generator would be implemented with a custom dialog.")
    
    def _show_preferences(self):
        """Show preferences dialog."""
        QMessageBox.information(self, "Info", "Preferences dialog would be implemented.")
    
    # Help operations
    def _show_about(self):
        """Show about dialog."""
        QMessageBox.about(
            self,
            "About Markdown Editor",
            "Markdown Editor v1.0.0\n\n"
            "A modern, user-friendly markdown editor with live preview.\n\n"
            "Built with PyQt6 and Python."
        )
    
    def _show_markdown_help(self):
        """Show markdown help."""
        help_text = """
        # Markdown Quick Reference
        
        ## Headers
        # H1
        ## H2
        ### H3
        
        ## Emphasis
        *italic* or _italic_
        **bold** or __bold__
        
        ## Lists
        - Bullet item
        1. Numbered item
        
        ## Links and Images
        [Link text](URL)
        ![Alt text](image URL)
        
        ## Code
        `inline code`
        ```
        code block
        ```
        
        ## Quotes
        > Blockquote
        """
        
        QMessageBox.information(self, "Markdown Help", help_text)
    
    # File manager event handlers
    @pyqtSlot(str, str)
    def _on_file_opened(self, filepath, content):
        """Handle file opened event."""
        self.editor.set_content(content)
        self._update_window_title()
    
    @pyqtSlot(str)
    def _on_file_saved(self, filepath):
        """Handle file saved event."""
        self._update_window_title()
    
    @pyqtSlot()
    def _on_file_created(self):
        """Handle new file created event."""
        self.editor.clear_content()
        self._update_window_title()
    
    # Editor event handlers
    @pyqtSlot(str)
    def _on_content_changed(self, content):
        """Handle content changed event."""
        self.file_manager.set_content_modified(True)
        self.file_manager.set_auto_save_content(content)
        self._update_window_title()
    
    @pyqtSlot(int, int)
    def _on_cursor_position_changed(self, line, column):
        """Handle cursor position changed event."""
        pass  # Already handled by editor status
    
    # Utility methods
    def _update_window_title(self):
        """Update the window title."""
        file_info = self.file_manager.get_file_info()
        title = file_info['name']
        
        if file_info['modified']:
            title += " •"
        
        title += " - Markdown Editor"
        self.setWindowTitle(title)
        
        # Update status bar file info
        if file_info['path']:
            self.file_info_label.setText(f"{file_info['name']} - {file_info['path']}")
        else:
            self.file_info_label.setText(file_info['name'])
    
    def _update_recent_files_menu(self):
        """Update the recent files menu."""
        self.recent_menu.clear()
        
        recent_files = self.file_manager.get_recent_files()
        
        if recent_files:
            for file_path in recent_files:
                action = QAction(os.path.basename(file_path), self)
                action.setData(file_path)
                action.setStatusTip(file_path)
                action.triggered.connect(lambda checked, path=file_path: self._open_recent_file(path))
                self.recent_menu.addAction(action)
            
            self.recent_menu.addSeparator()
            clear_action = QAction("Clear Recent Files", self)
            clear_action.triggered.connect(self.file_manager.clear_recent_files)
            self.recent_menu.addAction(clear_action)
        else:
            no_recent_action = QAction("No recent files", self)
            no_recent_action.setEnabled(False)
            self.recent_menu.addAction(no_recent_action)
    
    def _open_recent_file(self, file_path):
        """Open a recent file."""
        if self._check_unsaved_changes():
            success, content = self.file_manager.open_file(file_path)
            if success:
                self.editor.set_content(content)
                self._update_window_title()
                self.status_bar.showMessage(f"Opened: {os.path.basename(file_path)}", 2000)
            else:
                QMessageBox.warning(self, "Error", f"Failed to open file:\n{content}")
                # Remove from recent files if it no longer exists
                if "not found" in content.lower():
                    recent_files = self.file_manager.get_recent_files()
                    if file_path in recent_files:
                        recent_files.remove(file_path)
                        self.file_manager.settings.setValue('recent_files', recent_files)
                        self._update_recent_files_menu()
    
    def _check_unsaved_changes(self):
        """Check for unsaved changes and prompt user."""
        if self.file_manager.is_modified():
            reply = QMessageBox.question(
                self,
                "Unsaved Changes",
                "You have unsaved changes. Do you want to save them?",
                QMessageBox.StandardButton.Save | 
                QMessageBox.StandardButton.Discard | 
                QMessageBox.StandardButton.Cancel
            )
            
            if reply == QMessageBox.StandardButton.Save:
                self._save_file()
                return True
            elif reply == QMessageBox.StandardButton.Discard:
                return True
            else:  # Cancel
                return False
        
        return True
    
    # Override close event
    def closeEvent(self, event):
        """Handle window close event."""
        if self._check_unsaved_changes():
            self._save_settings()
            event.accept()
        else:
            event.ignore()