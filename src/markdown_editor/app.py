"""
Main application entry point for the markdown editor.
"""

import sys
import os
from pathlib import Path
from PyQt6.QtWidgets import QApplication, QSplashScreen, QMessageBox
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QPixmap, QFont, QIcon

# Add the src directory to the Python path for imports
current_dir = Path(__file__).parent
src_dir = current_dir.parent
sys.path.insert(0, str(src_dir))

from markdown_editor.ui.main_window import MainWindow
from markdown_editor import __version__


class MarkdownEditorApp:
    """
    Main application class for the markdown editor.
    """
    
    def __init__(self):
        """Initialize the application."""
        self.app = None
        self.main_window = None
        self.splash = None
    
    def create_application(self):
        """Create the QApplication instance."""
        self.app = QApplication(sys.argv)
        
        # Set application properties
        self.app.setApplicationName("Markdown Editor")
        self.app.setApplicationVersion(__version__)
        self.app.setOrganizationName("Markdown Editor Team")
        self.app.setOrganizationDomain("markdowneditor.app")
        
        # Set application style
        self.app.setStyle('Fusion')
        
        # Set default font
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.app.setFont(font)
        
        return self.app
    
    def show_splash_screen(self):
        """Show splash screen during application startup."""
        # Create a simple splash screen
        splash_pixmap = QPixmap(400, 300)
        splash_pixmap.fill(Qt.GlobalColor.white)
        
        self.splash = QSplashScreen(splash_pixmap)
        self.splash.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.FramelessWindowHint)
        
        # Show splash with message
        self.splash.show()
        self.splash.showMessage(
            f"Markdown Editor {__version__}\nLoading...",
            Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignBottom,
            Qt.GlobalColor.black
        )
        
        # Process events to show splash
        self.app.processEvents()
        
        return self.splash
    
    def create_main_window(self):
        """Create and setup the main window."""
        self.main_window = MainWindow()
        return self.main_window
    
    def handle_command_line_args(self):
        """Handle command line arguments."""
        args = sys.argv[1:]
        
        if args:
            # Try to open the first argument as a file
            file_path = args[0]
            if os.path.exists(file_path) and os.path.isfile(file_path):
                # Open the file after the window is shown
                QTimer.singleShot(100, lambda: self._open_file_delayed(file_path))
    
    def _open_file_delayed(self, file_path):
        """Open a file with a small delay."""
        if self.main_window:
            success, content = self.main_window.file_manager.open_file(file_path)
            if success:
                self.main_window.editor.set_content(content)
                self.main_window._update_window_title()
                self.main_window.status_bar.showMessage(f"Opened: {os.path.basename(file_path)}", 3000)
            else:
                QMessageBox.warning(
                    self.main_window,
                    "Error",
                    f"Failed to open file:\n{content}"
                )
    
    def setup_error_handling(self):
        """Setup global error handling."""
        def handle_exception(exc_type, exc_value, exc_traceback):
            """Handle uncaught exceptions."""
            if issubclass(exc_type, KeyboardInterrupt):
                sys.__excepthook__(exc_type, exc_value, exc_traceback)
                return
            
            error_msg = f"An unexpected error occurred:\n\n{exc_type.__name__}: {exc_value}"
            
            if self.main_window:
                QMessageBox.critical(
                    self.main_window,
                    "Unexpected Error",
                    error_msg
                )
            else:
                print(error_msg, file=sys.stderr)
        
        sys.excepthook = handle_exception
    
    def run(self):
        """Run the application."""
        try:
            # Create application
            app = self.create_application()
            
            # Setup error handling
            self.setup_error_handling()
            
            # Show splash screen
            splash = self.show_splash_screen()
            
            # Simulate loading time
            QTimer.singleShot(1500, lambda: self._finish_startup(splash))
            
            # Start event loop
            return app.exec()
            
        except Exception as e:
            print(f"Failed to start application: {e}", file=sys.stderr)
            return 1
    
    def _finish_startup(self, splash):
        """Finish application startup."""
        # Create main window
        self.create_main_window()
        
        # Handle command line arguments
        self.handle_command_line_args()
        
        # Show main window
        self.main_window.show()
        
        # Close splash screen
        if splash:
            splash.finish(self.main_window)
        
        # Focus the editor
        self.main_window.editor.focus_editor()


def main():
    """Main entry point for the application."""
    # Check Python version
    if sys.version_info < (3, 8):
        print("Python 3.8 or later is required.", file=sys.stderr)
        return 1
    
    # Check for required packages
    try:
        import PyQt6
        import markdown
        import pymdown
    except ImportError as e:
        print(f"Missing required package: {e}", file=sys.stderr)
        print("Please install dependencies: pip install -r requirements.txt", file=sys.stderr)
        return 1
    
    # Create and run application
    app = MarkdownEditorApp()
    return app.run()


if __name__ == "__main__":
    sys.exit(main())