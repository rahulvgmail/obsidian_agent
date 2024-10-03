import os
import pathlib

def get_icloud_directory():
    """
    Returns the path to the iCloud Drive directory.
    """
    home = pathlib.Path.home()
    icloud_dir = home / "Library" / "Mobile Documents" / "com~apple~CloudDocs"
    return icloud_dir

def read_md_file(filename):
    """
    Reads a Markdown file from the iCloud Drive directory.
    
    :param filename: Name of the file to read (including .md extension)
    :return: Content of the file as a string
    """
    icloud_dir = get_icloud_directory()
    file_path = icloud_dir / filename
    
    if not file_path.exists():
        raise FileNotFoundError(f"The file {filename} does not exist in your iCloud Drive.")
    
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    return content

def write_md_file(filename, content):
    """
    Writes content to a Markdown file in the iCloud Drive directory.
    
    :param filename: Name of the file to write (including .md extension)
    :param content: Content to write to the file
    """
    icloud_dir = get_icloud_directory()
    file_path = icloud_dir / filename
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def list_md_files():
    """
    Lists all Markdown files in the iCloud Drive directory.
    
    :return: List of Markdown filenames
    """
    icloud_dir = get_icloud_directory()
    md_files = [f.name for f in icloud_dir.glob("*.md")]
    return md_files
