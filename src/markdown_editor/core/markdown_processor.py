"""
Markdown processing functionality for converting between markdown and HTML.
"""

import markdown
from markdown.extensions import codehilite, tables, toc, fenced_code
from pymdown import superfences, highlight, inlinehilite, magiclink, tasklist
import re
from typing import Dict, Any, Optional


class MarkdownProcessor:
    """
    Handles conversion between markdown text and HTML for rendering.
    """
    
    def __init__(self):
        """Initialize the markdown processor with extensions."""
        self.extensions = [
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
            'markdown.extensions.tables',
            'markdown.extensions.fenced_code',
            'pymdownx.superfences',
            'pymdownx.highlight',
            'pymdownx.inlinehilite',
            'pymdownx.magiclink',
            'pymdownx.tasklist',
            'pymdownx.tilde',
            'pymdownx.caret',
            'pymdownx.mark',
            'pymdownx.keys'
        ]
        
        self.extension_configs = {
            'codehilite': {
                'css_class': 'highlight',
                'use_pygments': True
            },
            'pymdownx.highlight': {
                'css_class': 'highlight',
                'use_pygments': True,
                'auto_title': True
            },
            'pymdownx.superfences': {
                'custom_fences': [
                    {
                        'name': 'mermaid',
                        'class': 'mermaid',
                        'format': self._format_mermaid
                    }
                ]
            },
            'pymdownx.tasklist': {
                'custom_checkbox': True
            }
        }
        
        self.md = markdown.Markdown(
            extensions=self.extensions,
            extension_configs=self.extension_configs
        )
    
    def _format_mermaid(self, source: str, language: str, css_class: str, **kwargs) -> str:
        """Format mermaid diagrams."""
        return f'<div class="mermaid">{source}</div>'
    
    def markdown_to_html(self, markdown_text: str) -> str:
        """
        Convert markdown text to HTML.
        
        Args:
            markdown_text: The markdown content to convert
            
        Returns:
            HTML representation of the markdown
        """
        try:
            # Reset the markdown processor to clear any previous state
            self.md.reset()
            
            # Convert markdown to HTML
            html = self.md.convert(markdown_text)
            
            return html
        except Exception as e:
            return f"<p>Error processing markdown: {str(e)}</p>"
    
    def extract_metadata(self, markdown_text: str) -> Dict[str, Any]:
        """
        Extract metadata from markdown front matter.
        
        Args:
            markdown_text: The markdown content
            
        Returns:
            Dictionary of metadata
        """
        metadata = {}
        
        # Check for YAML front matter
        front_matter_pattern = r'^---\s*\n(.*?)\n---\s*\n'
        match = re.match(front_matter_pattern, markdown_text, re.DOTALL)
        
        if match:
            try:
                import yaml
                metadata = yaml.safe_load(match.group(1))
            except ImportError:
                # If PyYAML is not available, parse basic key-value pairs
                lines = match.group(1).strip().split('\n')
                for line in lines:
                    if ':' in line:
                        key, value = line.split(':', 1)
                        metadata[key.strip()] = value.strip()
        
        return metadata
    
    def get_table_of_contents(self) -> str:
        """
        Get the table of contents from the last processed markdown.
        
        Returns:
            HTML table of contents
        """
        if hasattr(self.md, 'toc'):
            return self.md.toc
        return ""
    
    def html_to_markdown_approximation(self, html: str) -> str:
        """
        Convert basic HTML back to markdown (approximation).
        This is a simple implementation for basic formatting.
        
        Args:
            html: HTML content to convert
            
        Returns:
            Approximate markdown representation
        """
        # Remove HTML tags and convert basic formatting
        # This is a simplified conversion - for production use,
        # consider using html2text library
        
        # Basic replacements
        replacements = [
            (r'<h1[^>]*>(.*?)</h1>', r'# \1'),
            (r'<h2[^>]*>(.*?)</h2>', r'## \1'),
            (r'<h3[^>]*>(.*?)</h3>', r'### \1'),
            (r'<h4[^>]*>(.*?)</h4>', r'#### \1'),
            (r'<h5[^>]*>(.*?)</h5>', r'##### \1'),
            (r'<h6[^>]*>(.*?)</h6>', r'###### \1'),
            (r'<strong[^>]*>(.*?)</strong>', r'**\1**'),
            (r'<b[^>]*>(.*?)</b>', r'**\1**'),
            (r'<em[^>]*>(.*?)</em>', r'*\1*'),
            (r'<i[^>]*>(.*?)</i>', r'*\1*'),
            (r'<code[^>]*>(.*?)</code>', r'`\1`'),
            (r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>', r'[\2](\1)'),
            (r'<img[^>]*src="([^"]*)"[^>]*alt="([^"]*)"[^>]*/?>', r'![\2](\1)'),
            (r'<br[^>]*/?>', r'\n'),
            (r'<p[^>]*>', r'\n'),
            (r'</p>', r'\n'),
            (r'<div[^>]*>', r''),
            (r'</div>', r''),
        ]
        
        text = html
        for pattern, replacement in replacements:
            text = re.sub(pattern, replacement, text, flags=re.IGNORECASE | re.DOTALL)
        
        # Clean up extra whitespace
        text = re.sub(r'\n\s*\n\s*\n', '\n\n', text)
        text = text.strip()
        
        return text