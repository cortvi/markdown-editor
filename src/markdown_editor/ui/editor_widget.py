"""
Rich text editor widget with WYSIWYG capabilities for markdown editing.
"""

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QToolBar, QToolButton,
    QComboBox, QSpinBox, QColorDialog, QFontComboBox, QSplitter,
    QTabWidget, QPlainTextEdit, QLabel, QFrame
)
from PyQt6.QtCore import Qt, pyqtSignal, QTimer, QUrl
from PyQt6.QtGui import (
    QFont, QTextCursor, QTextCharFormat, QColor, QAction, QIcon,
    QKeySequence, QTextDocument, QTextBlockFormat, QTextListFormat,
    QPixmap, QPainter, QDesktopServices
)
from PyQt6.QtWebEngineWidgets import QWebEngineView
import re
from typing import Optional, Dict, Any


class MarkdownEditorWidget(QWidget):
    """
    Rich text editor widget with WYSIWYG capabilities and live preview.
    """
    
    # Signals
    content_changed = pyqtSignal(str)  # markdown content
    formatting_changed = pyqtSignal()
    cursor_position_changed = pyqtSignal(int, int)  # line, column
    
    def __init__(self, parent=None):
        """Initialize the editor widget."""
        super().__init__(parent)
        
        self.markdown_processor = None  # Will be set by parent
        self.current_content = ""
        self.is_updating = False
        
        # Timer for delayed content processing
        self.update_timer = QTimer()
        self.update_timer.setSingleShot(True)
        self.update_timer.timeout.connect(self._process_content)
        self.update_timer.setInterval(500)  # 500ms delay
        
        self._setup_ui()
        self._setup_connections()
        self._setup_formatting()
    
    def _setup_ui(self):
        """Setup the user interface."""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        
        # Create toolbar
        self.toolbar = self._create_toolbar()
        layout.addWidget(self.toolbar)
        
        # Create splitter for editor and preview
        self.splitter = QSplitter(Qt.Orientation.Horizontal)
        layout.addWidget(self.splitter)
        
        # Create tab widget for different editing modes
        self.tab_widget = QTabWidget()
        
        # Rich text editor tab
        self.rich_editor = QTextEdit()
        self.rich_editor.setAcceptRichText(True)
        self.rich_editor.setPlaceholderText("Start typing your markdown content...")
        self.tab_widget.addTab(self.rich_editor, "Rich Text")
        
        # Raw markdown editor tab
        self.raw_editor = QPlainTextEdit()
        self.raw_editor.setPlaceholderText("Raw markdown content...")
        self.raw_editor.setFont(QFont("Consolas", 10))
        self.tab_widget.addTab(self.raw_editor, "Markdown")
        
        # Add editor to splitter
        self.splitter.addWidget(self.tab_widget)
        
        # Create preview widget
        self.preview = QWebEngineView()
        self.preview.setMinimumWidth(300)
        self.splitter.addWidget(self.preview)
        
        # Set splitter proportions
        self.splitter.setSizes([500, 500])
        
        # Status frame
        self.status_frame = QFrame()
        self.status_frame.setFrameStyle(QFrame.Shape.StyledPanel)
        self.status_frame.setMaximumHeight(25)
        status_layout = QHBoxLayout(self.status_frame)
        status_layout.setContentsMargins(5, 2, 5, 2)
        
        self.cursor_label = QLabel("Line 1, Column 1")
        self.word_count_label = QLabel("Words: 0")
        
        status_layout.addWidget(self.cursor_label)
        status_layout.addStretch()
        status_layout.addWidget(self.word_count_label)
        
        layout.addWidget(self.status_frame)
    
    def _create_toolbar(self) -> QToolBar:
        """Create the formatting toolbar."""
        toolbar = QToolBar()
        toolbar.setMovable(False)
        toolbar.setFloatable(False)
        
        # Font family
        self.font_combo = QFontComboBox()
        self.font_combo.setCurrentFont(QFont("Arial"))
        toolbar.addWidget(self.font_combo)
        
        # Font size
        self.font_size = QSpinBox()
        self.font_size.setRange(8, 72)
        self.font_size.setValue(12)
        self.font_size.setSuffix("pt")
        toolbar.addWidget(self.font_size)
        
        toolbar.addSeparator()
        
        # Bold, Italic, Underline
        self.bold_action = toolbar.addAction("B")
        self.bold_action.setCheckable(True)
        self.bold_action.setShortcut(QKeySequence.StandardKey.Bold)
        self.bold_action.setToolTip("Bold (Ctrl+B)")
        
        self.italic_action = toolbar.addAction("I")
        self.italic_action.setCheckable(True)
        self.italic_action.setShortcut(QKeySequence.StandardKey.Italic)
        self.italic_action.setToolTip("Italic (Ctrl+I)")
        
        self.underline_action = toolbar.addAction("U")
        self.underline_action.setCheckable(True)
        self.underline_action.setShortcut(QKeySequence.StandardKey.Underline)
        self.underline_action.setToolTip("Underline (Ctrl+U)")
        
        toolbar.addSeparator()
        
        # Headers
        self.header_combo = QComboBox()
        self.header_combo.addItems(["Normal", "Header 1", "Header 2", "Header 3", "Header 4", "Header 5", "Header 6"])
        toolbar.addWidget(self.header_combo)
        
        toolbar.addSeparator()
        
        # Lists
        self.bullet_action = toolbar.addAction("• List")
        self.bullet_action.setToolTip("Bullet List")
        
        self.number_action = toolbar.addAction("1. List")
        self.number_action.setToolTip("Numbered List")
        
        toolbar.addSeparator()
        
        # Links and Images
        self.link_action = toolbar.addAction("Link")
        self.link_action.setToolTip("Insert Link")
        
        self.image_action = toolbar.addAction("Image")
        self.image_action.setToolTip("Insert Image")
        
        toolbar.addSeparator()
        
        # Code
        self.code_action = toolbar.addAction("Code")
        self.code_action.setToolTip("Inline Code")
        
        self.code_block_action = toolbar.addAction("Code Block")
        self.code_block_action.setToolTip("Code Block")
        
        toolbar.addSeparator()
        
        # Quote
        self.quote_action = toolbar.addAction("Quote")
        self.quote_action.setToolTip("Block Quote")
        
        return toolbar
    
    def _setup_connections(self):
        """Setup signal connections."""
        # Rich editor connections
        self.rich_editor.textChanged.connect(self._on_rich_text_changed)
        self.rich_editor.cursorPositionChanged.connect(self._on_cursor_changed)
        self.rich_editor.currentCharFormatChanged.connect(self._on_format_changed)
        
        # Raw editor connections
        self.raw_editor.textChanged.connect(self._on_raw_text_changed)
        self.raw_editor.cursorPositionChanged.connect(self._on_cursor_changed)
        
        # Tab change
        self.tab_widget.currentChanged.connect(self._on_tab_changed)
        
        # Toolbar connections
        self.font_combo.currentFontChanged.connect(self._on_font_changed)
        self.font_size.valueChanged.connect(self._on_font_size_changed)
        self.bold_action.triggered.connect(self._on_bold)
        self.italic_action.triggered.connect(self._on_italic)
        self.underline_action.triggered.connect(self._on_underline)
        self.header_combo.currentIndexChanged.connect(self._on_header_changed)
        self.bullet_action.triggered.connect(self._on_bullet_list)
        self.number_action.triggered.connect(self._on_number_list)
        self.link_action.triggered.connect(self._on_insert_link)
        self.image_action.triggered.connect(self._on_insert_image)
        self.code_action.triggered.connect(self._on_inline_code)
        self.code_block_action.triggered.connect(self._on_code_block)
        self.quote_action.triggered.connect(self._on_quote)
    
    def _setup_formatting(self):
        """Setup default formatting."""
        # Set default font for rich editor
        font = QFont("Arial", 12)
        self.rich_editor.setFont(font)
        
        # Set default font for raw editor
        mono_font = QFont("Consolas", 10)
        self.raw_editor.setFont(mono_font)
    
    def _on_rich_text_changed(self):
        """Handle rich text changes."""
        if self.is_updating:
            return
        
        self.is_updating = True
        
        # Convert rich text to markdown
        html = self.rich_editor.toHtml()
        markdown = self._html_to_markdown(html)
        
        # Update raw editor
        self.raw_editor.setPlainText(markdown)
        
        # Update current content
        self.current_content = markdown
        
        # Update preview
        self.update_timer.start()
        
        # Update word count
        self._update_word_count()
        
        # Emit signal
        self.content_changed.emit(markdown)
        
        self.is_updating = False
    
    def _on_raw_text_changed(self):
        """Handle raw text changes."""
        if self.is_updating:
            return
        
        self.is_updating = True
        
        # Get markdown content
        markdown = self.raw_editor.toPlainText()
        
        # Update current content
        self.current_content = markdown
        
        # Update rich editor (simplified - just set as plain text for now)
        # In a production app, you'd want more sophisticated markdown-to-rich-text conversion
        self.rich_editor.setPlainText(markdown)
        
        # Update preview
        self.update_timer.start()
        
        # Update word count
        self._update_word_count()
        
        # Emit signal
        self.content_changed.emit(markdown)
        
        self.is_updating = False
    
    def _on_tab_changed(self, index):
        """Handle tab change between rich and raw editors."""
        if index == 0:  # Rich text tab
            # Sync from raw to rich
            if not self.is_updating:
                markdown = self.raw_editor.toPlainText()
                self.rich_editor.setPlainText(markdown)
        else:  # Raw text tab
            # Sync from rich to raw
            if not self.is_updating:
                html = self.rich_editor.toHtml()
                markdown = self._html_to_markdown(html)
                self.raw_editor.setPlainText(markdown)
    
    def _on_cursor_changed(self):
        """Handle cursor position changes."""
        if self.tab_widget.currentIndex() == 0:  # Rich editor
            cursor = self.rich_editor.textCursor()
            document = self.rich_editor.document()
        else:  # Raw editor
            cursor = self.raw_editor.textCursor()
            document = self.raw_editor.document()
        
        # Calculate line and column
        line = cursor.blockNumber() + 1
        column = cursor.columnNumber() + 1
        
        # Update status
        self.cursor_label.setText(f"Line {line}, Column {column}")
        
        # Emit signal
        self.cursor_position_changed.emit(line, column)
    
    def _on_format_changed(self):
        """Handle format changes in rich editor."""
        if self.is_updating:
            return
        
        cursor = self.rich_editor.textCursor()
        format = cursor.charFormat()
        
        # Update toolbar states
        self.bold_action.setChecked(format.fontWeight() == QFont.Weight.Bold)
        self.italic_action.setChecked(format.fontItalic())
        self.underline_action.setChecked(format.fontUnderline())
        
        # Update font controls
        self.font_combo.setCurrentFont(format.font())
        if format.fontPointSize() > 0:
            self.font_size.setValue(int(format.fontPointSize()))
        
        self.formatting_changed.emit()
    
    def _process_content(self):
        """Process content for preview update."""
        if self.markdown_processor:
            html = self.markdown_processor.markdown_to_html(self.current_content)
            
            # Add CSS styling
            styled_html = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="utf-8">
                <style>
                    body {{
                        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                        line-height: 1.6;
                        color: #333;
                        max-width: 800px;
                        margin: 0 auto;
                        padding: 20px;
                    }}
                    h1, h2, h3, h4, h5, h6 {{
                        color: #2c3e50;
                        margin-top: 24px;
                        margin-bottom: 16px;
                    }}
                    h1 {{ border-bottom: 2px solid #eee; padding-bottom: 10px; }}
                    h2 {{ border-bottom: 1px solid #eee; padding-bottom: 8px; }}
                    code {{
                        background-color: #f4f4f4;
                        padding: 2px 4px;
                        border-radius: 3px;
                        font-family: 'Consolas', 'Monaco', monospace;
                    }}
                    pre {{
                        background-color: #f4f4f4;
                        padding: 16px;
                        border-radius: 6px;
                        overflow-x: auto;
                    }}
                    blockquote {{
                        border-left: 4px solid #ddd;
                        margin: 0;
                        padding-left: 16px;
                        color: #666;
                    }}
                    table {{
                        border-collapse: collapse;
                        width: 100%;
                        margin: 16px 0;
                    }}
                    th, td {{
                        border: 1px solid #ddd;
                        padding: 8px 12px;
                        text-align: left;
                    }}
                    th {{
                        background-color: #f4f4f4;
                        font-weight: bold;
                    }}
                    a {{
                        color: #3498db;
                        text-decoration: none;
                    }}
                    a:hover {{
                        text-decoration: underline;
                    }}
                    img {{
                        max-width: 100%;
                        height: auto;
                    }}
                    ul, ol {{
                        padding-left: 24px;
                    }}
                    li {{
                        margin: 4px 0;
                    }}
                </style>
            </head>
            <body>
                {html}
            </body>
            </html>
            """
            
            self.preview.setHtml(styled_html)
    
    def _update_word_count(self):
        """Update word count in status bar."""
        if self.tab_widget.currentIndex() == 0:
            text = self.rich_editor.toPlainText()
        else:
            text = self.raw_editor.toPlainText()
        
        words = len(text.split()) if text.strip() else 0
        chars = len(text)
        
        self.word_count_label.setText(f"Words: {words} | Characters: {chars}")
    
    def _html_to_markdown(self, html: str) -> str:
        """Convert HTML to markdown (simplified)."""
        if self.markdown_processor:
            return self.markdown_processor.html_to_markdown_approximation(html)
        return html  # Fallback
    
    # Formatting actions
    def _on_font_changed(self, font):
        """Handle font change."""
        if self.tab_widget.currentIndex() == 0:
            cursor = self.rich_editor.textCursor()
            format = cursor.charFormat()
            format.setFont(font)
            cursor.mergeCharFormat(format)
    
    def _on_font_size_changed(self, size):
        """Handle font size change."""
        if self.tab_widget.currentIndex() == 0:
            cursor = self.rich_editor.textCursor()
            format = cursor.charFormat()
            format.setFontPointSize(size)
            cursor.mergeCharFormat(format)
    
    def _on_bold(self):
        """Toggle bold formatting."""
        if self.tab_widget.currentIndex() == 0:
            cursor = self.rich_editor.textCursor()
            format = cursor.charFormat()
            if format.fontWeight() == QFont.Weight.Bold:
                format.setFontWeight(QFont.Weight.Normal)
            else:
                format.setFontWeight(QFont.Weight.Bold)
            cursor.mergeCharFormat(format)
        else:
            self._insert_markdown_formatting("**", "**")
    
    def _on_italic(self):
        """Toggle italic formatting."""
        if self.tab_widget.currentIndex() == 0:
            cursor = self.rich_editor.textCursor()
            format = cursor.charFormat()
            format.setFontItalic(not format.fontItalic())
            cursor.mergeCharFormat(format)
        else:
            self._insert_markdown_formatting("*", "*")
    
    def _on_underline(self):
        """Toggle underline formatting."""
        if self.tab_widget.currentIndex() == 0:
            cursor = self.rich_editor.textCursor()
            format = cursor.charFormat()
            format.setFontUnderline(not format.fontUnderline())
            cursor.mergeCharFormat(format)
        else:
            self._insert_markdown_formatting("<u>", "</u>")
    
    def _on_header_changed(self, index):
        """Handle header level change."""
        if index == 0:  # Normal
            return
        
        header_level = "#" * index
        
        if self.tab_widget.currentIndex() == 0:
            # Rich editor - set block format
            cursor = self.rich_editor.textCursor()
            block_format = QTextBlockFormat()
            char_format = QTextCharFormat()
            
            if index == 1:  # H1
                char_format.setFontPointSize(24)
                char_format.setFontWeight(QFont.Weight.Bold)
            elif index == 2:  # H2
                char_format.setFontPointSize(20)
                char_format.setFontWeight(QFont.Weight.Bold)
            elif index == 3:  # H3
                char_format.setFontPointSize(16)
                char_format.setFontWeight(QFont.Weight.Bold)
            else:
                char_format.setFontPointSize(14)
                char_format.setFontWeight(QFont.Weight.Bold)
            
            cursor.mergeBlockFormat(block_format)
            cursor.mergeCharFormat(char_format)
        else:
            # Raw editor - insert markdown
            cursor = self.raw_editor.textCursor()
            cursor.movePosition(QTextCursor.MoveOperation.StartOfLine)
            cursor.insertText(f"{header_level} ")
    
    def _on_bullet_list(self):
        """Insert bullet list."""
        if self.tab_widget.currentIndex() == 0:
            cursor = self.rich_editor.textCursor()
            list_format = QTextListFormat()
            list_format.setStyle(QTextListFormat.Style.ListDisc)
            cursor.insertList(list_format)
        else:
            self._insert_markdown_at_line_start("- ")
    
    def _on_number_list(self):
        """Insert numbered list."""
        if self.tab_widget.currentIndex() == 0:
            cursor = self.rich_editor.textCursor()
            list_format = QTextListFormat()
            list_format.setStyle(QTextListFormat.Style.ListDecimal)
            cursor.insertList(list_format)
        else:
            self._insert_markdown_at_line_start("1. ")
    
    def _on_insert_link(self):
        """Insert link."""
        self._insert_markdown_formatting("[", "](url)")
    
    def _on_insert_image(self):
        """Insert image."""
        self._insert_markdown_formatting("![", "](image_url)")
    
    def _on_inline_code(self):
        """Insert inline code."""
        self._insert_markdown_formatting("`", "`")
    
    def _on_code_block(self):
        """Insert code block."""
        self._insert_markdown_formatting("```\n", "\n```")
    
    def _on_quote(self):
        """Insert quote."""
        if self.tab_widget.currentIndex() == 1:
            self._insert_markdown_at_line_start("> ")
    
    def _insert_markdown_formatting(self, start: str, end: str):
        """Insert markdown formatting around selection."""
        if self.tab_widget.currentIndex() == 1:  # Raw editor
            cursor = self.raw_editor.textCursor()
            
            if cursor.hasSelection():
                selected_text = cursor.selectedText()
                cursor.insertText(f"{start}{selected_text}{end}")
            else:
                cursor.insertText(f"{start}text{end}")
                # Move cursor back to select "text"
                for _ in range(len(end) + 4):
                    cursor.movePosition(QTextCursor.MoveOperation.Left)
                for _ in range(4):
                    cursor.movePosition(QTextCursor.MoveOperation.Right, QTextCursor.MoveMode.KeepAnchor)
                self.raw_editor.setTextCursor(cursor)
    
    def _insert_markdown_at_line_start(self, text: str):
        """Insert markdown formatting at the start of the current line."""
        if self.tab_widget.currentIndex() == 1:  # Raw editor
            cursor = self.raw_editor.textCursor()
            cursor.movePosition(QTextCursor.MoveOperation.StartOfLine)
            cursor.insertText(text)
    
    # Public methods
    def set_markdown_processor(self, processor):
        """Set the markdown processor."""
        self.markdown_processor = processor
    
    def set_content(self, content: str):
        """Set the editor content."""
        self.is_updating = True
        
        self.current_content = content
        self.raw_editor.setPlainText(content)
        self.rich_editor.setPlainText(content)  # Simplified
        
        self._process_content()
        self._update_word_count()
        
        self.is_updating = False
    
    def get_content(self) -> str:
        """Get the current markdown content."""
        return self.current_content
    
    def clear_content(self):
        """Clear all content."""
        self.set_content("")
    
    def toggle_preview(self):
        """Toggle preview visibility."""
        if self.preview.isVisible():
            self.preview.hide()
        else:
            self.preview.show()
    
    def focus_editor(self):
        """Focus the current editor."""
        if self.tab_widget.currentIndex() == 0:
            self.rich_editor.setFocus()
        else:
            self.raw_editor.setFocus()