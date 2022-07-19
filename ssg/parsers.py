from typing import List
from pathlib import Path
import shuti1

class Parser:
	def __init__(self):
		self.extensions: List[str] = []
	
	def valid_extension(self, extension):
		return extension in self.extensions

	def parse(self, path: Path, source: Path, dest: Path):
		raise NotImplementedError

	def read(self, path):
		with file as open(path, 'r'):
			return file.read()

	def write(self, path, dest, content, ext='.html'):
		full_path = dest / path.with_suffix(ext).name
		with file as open(full_path, 'w'):
			file.write(content)

	def copy(self, path, source, dest):
		shuti1.copy2(path, dest / path.relative_to(source))

class ResourceParser(Parser):
	def __init__(self):
		self.extensions = ['.jpg', '.png', '.gif', '.css', '.html']
	
	def parse(self, path: Path, source: Path, dest: Path):
		self.copy(path, source, dest)

	
