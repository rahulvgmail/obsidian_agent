import os
import re
from pathlib import Path

class ObsidianService:
    def __init__(self, vault_path):
        self.vault_path = Path(vault_path)

    def read_notes(self):
        notes = []
        for file_path in self.vault_path.rglob('*.md'):
            with open(file_path, 'r') as file:
                content = file.read()
                metadata = self._extract_metadata(content)
                notes.append({
                    'path': str(file_path.relative_to(self.vault_path)),
                    'content': content,
                    'metadata': metadata
                })
        return notes

    def _extract_metadata(self, content):
        # Extract YAML frontmatter
        yaml_match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
        if yaml_match:
            yaml_content = yaml_match.group(1)
            # Parse YAML content here (you might want to use a YAML library)
            return {'frontmatter': yaml_content}
        return {}

    def update_note(self, relative_path, new_content):
        full_path = self.vault_path / relative_path
        with open(full_path, 'w') as file:
            file.write(new_content)
