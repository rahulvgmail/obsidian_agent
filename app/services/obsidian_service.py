import os
import re
from pathlib import Path

class ObsidianService:
    def __init__(self, vault_path):
        self.vault_path = Path(vault_path)

    def read_notes(self):
        notes = []
        for file_path in self.vault_path.rglob('*.md'):
            try:
                with open(file_path, 'r') as file:
                    content = file.read()
                    metadata = self._extract_metadata(content)
                    notes.append({
                        'path': str(file_path.relative_to(self.vault_path)),
                        'content': content,
                        'metadata': metadata
                    })
            except IOError as e:
                print(f"Error reading file {file_path}: {str(e)}")
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
        try:
            with open(full_path, 'w') as file:
                file.write(new_content)
        except IOError as e:
            raise RuntimeError(f"Failed to update note {relative_path}: {str(e)}")

    def create_note(self, relative_path, content):
        full_path = self.vault_path / relative_path
        if full_path.exists():
            raise ValueError(f"Note {relative_path} already exists")
        try:
            full_path.parent.mkdir(parents=True, exist_ok=True)
            with open(full_path, 'w') as file:
                file.write(content)
        except IOError as e:
            raise RuntimeError(f"Failed to create note {relative_path}: {str(e)}")
