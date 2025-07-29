"""
File management functionality for the markdown editor.
"""

import os
import json
from pathlib import Path
from typing import List, Optional, Tuple
from PyQt6.QtCore import QObject, pyqtSignal, QTimer, QSettings


class FileManager(QObject):
    """
    Handles file operations for the markdown editor.
    """
    
    # Signals
    file_opened = pyqtSignal(str, str)  # filepath, content
    file_saved = pyqtSignal(str)  # filepath
    file_created = pyqtSignal()
    recent_files_updated = pyqtSignal(list)  # list of recent files
    
    def __init__(self):
        """Initialize the file manager."""
        super().__init__()
        
        self.current_file = None
        self.content_modified = False
        self.auto_save_timer = QTimer()
        self.auto_save_timer.timeout.connect(self._auto_save)
        self.auto_save_timer.setSingleShot(True)
        self.auto_save_interval = 30000  # 30 seconds
        
        # Settings for persistent data
        self.settings = QSettings('MarkdownEditor', 'FileManager')
        
        # Auto-save content (temporary storage)
        self.auto_save_content = ""
        self.auto_save_filepath = ""
    
    def new_file(self) -> None:
        """Create a new file."""
        self.current_file = None
        self.content_modified = False
        self.auto_save_content = ""
        self.auto_save_filepath = ""
        self.file_created.emit()
    
    def open_file(self, filepath: str) -> Tuple[bool, str]:
        """
        Open a markdown file.
        
        Args:
            filepath: Path to the file to open
            
        Returns:
            Tuple of (success, content_or_error_message)
        """
        try:
            # Validate file exists
            if not os.path.exists(filepath):
                return False, f"File not found: {filepath}"
            
            # Check if it's a markdown file
            if not self._is_markdown_file(filepath):
                return False, f"Not a markdown file: {filepath}"
            
            # Read file content
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
            
            self.current_file = filepath
            self.content_modified = False
            self.auto_save_content = content
            self.auto_save_filepath = filepath
            
            # Add to recent files
            self._add_to_recent_files(filepath)
            
            # Emit signal
            self.file_opened.emit(filepath, content)
            
            return True, content
            
        except Exception as e:
            return False, f"Error opening file: {str(e)}"
    
    def save_file(self, content: str, filepath: Optional[str] = None) -> Tuple[bool, str]:
        """
        Save content to a file.
        
        Args:
            content: Content to save
            filepath: Path to save to (if None, uses current file)
            
        Returns:
            Tuple of (success, filepath_or_error_message)
        """
        try:
            # Determine filepath
            save_path = filepath or self.current_file
            
            if not save_path:
                return False, "No file path specified"
            
            # Ensure directory exists
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            
            # Write file
            with open(save_path, 'w', encoding='utf-8') as file:
                file.write(content)
            
            self.current_file = save_path
            self.content_modified = False
            self.auto_save_content = content
            self.auto_save_filepath = save_path
            
            # Add to recent files
            self._add_to_recent_files(save_path)
            
            # Emit signal
            self.file_saved.emit(save_path)
            
            return True, save_path
            
        except Exception as e:
            return False, f"Error saving file: {str(e)}"
    
    def set_content_modified(self, modified: bool = True) -> None:
        """
        Mark content as modified and start auto-save timer.
        
        Args:
            modified: Whether content is modified
        """
        self.content_modified = modified
        
        if modified and self.auto_save_interval > 0:
            self.auto_save_timer.start(self.auto_save_interval)
    
    def set_auto_save_content(self, content: str) -> None:
        """
        Set content for auto-save.
        
        Args:
            content: Content to auto-save
        """
        self.auto_save_content = content
        if self.current_file:
            self.auto_save_filepath = self.current_file
    
    def _auto_save(self) -> None:
        """Auto-save content to temporary location."""
        if self.auto_save_content and self.content_modified:
            try:
                # Create auto-save directory
                auto_save_dir = Path.home() / '.markdown_editor' / 'autosave'
                auto_save_dir.mkdir(parents=True, exist_ok=True)
                
                # Generate auto-save filename
                if self.current_file:
                    base_name = Path(self.current_file).stem
                    auto_save_file = auto_save_dir / f"{base_name}_autosave.md"
                else:
                    auto_save_file = auto_save_dir / "untitled_autosave.md"
                
                # Save content
                with open(auto_save_file, 'w', encoding='utf-8') as file:
                    file.write(self.auto_save_content)
                
            except Exception:
                # Silently fail auto-save to not interrupt user experience
                pass
    
    def get_recent_files(self) -> List[str]:
        """
        Get list of recent files.
        
        Returns:
            List of recent file paths
        """
        recent_files = self.settings.value('recent_files', [])
        if isinstance(recent_files, str):
            recent_files = [recent_files]
        elif recent_files is None:
            recent_files = []
        
        # Filter out non-existent files
        existing_files = [f for f in recent_files if os.path.exists(f)]
        
        # Update settings if list changed
        if len(existing_files) != len(recent_files):
            self.settings.setValue('recent_files', existing_files)
        
        return existing_files
    
    def _add_to_recent_files(self, filepath: str) -> None:
        """
        Add file to recent files list.
        
        Args:
            filepath: File path to add
        """
        recent_files = self.get_recent_files()
        
        # Remove if already exists
        if filepath in recent_files:
            recent_files.remove(filepath)
        
        # Add to beginning
        recent_files.insert(0, filepath)
        
        # Limit to 10 recent files
        recent_files = recent_files[:10]
        
        # Save to settings
        self.settings.setValue('recent_files', recent_files)
        
        # Emit signal
        self.recent_files_updated.emit(recent_files)
    
    def clear_recent_files(self) -> None:
        """Clear the recent files list."""
        self.settings.setValue('recent_files', [])
        self.recent_files_updated.emit([])
    
    def _is_markdown_file(self, filepath: str) -> bool:
        """
        Check if file is a markdown file.
        
        Args:
            filepath: File path to check
            
        Returns:
            True if it's a markdown file
        """
        markdown_extensions = {'.md', '.markdown', '.mdown', '.mkd', '.mkdn', '.mdx'}
        return Path(filepath).suffix.lower() in markdown_extensions
    
    def get_current_file(self) -> Optional[str]:
        """Get the current file path."""
        return self.current_file
    
    def is_modified(self) -> bool:
        """Check if content is modified."""
        return self.content_modified
    
    def get_file_info(self) -> dict:
        """
        Get information about the current file.
        
        Returns:
            Dictionary with file information
        """
        if not self.current_file:
            return {
                'name': 'Untitled',
                'path': None,
                'size': 0,
                'modified': self.content_modified
            }
        
        try:
            stat = os.stat(self.current_file)
            return {
                'name': os.path.basename(self.current_file),
                'path': self.current_file,
                'size': stat.st_size,
                'modified': self.content_modified,
                'last_modified': stat.st_mtime
            }
        except Exception:
            return {
                'name': os.path.basename(self.current_file) if self.current_file else 'Untitled',
                'path': self.current_file,
                'size': 0,
                'modified': self.content_modified
            }