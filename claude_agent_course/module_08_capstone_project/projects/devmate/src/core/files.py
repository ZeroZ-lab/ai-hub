import os
import shutil
import pathspec
from pathlib import Path
from typing import List, Union
from rich.console import Console
from .context import ProjectContext

console = Console()

class FileManager:
    def __init__(self, context: ProjectContext):
        self.context = context

    def read_file(self, rel_path: str) -> str:
        """Read content of a file."""
        path = self.context.resolve_path(rel_path)
        if not path.exists():
            return f"Error: File {rel_path} does not exist."
        try:
            return path.read_text(encoding="utf-8")
        except Exception as e:
            return f"Error reading file {rel_path}: {e}"

    def write_file(self, rel_path: str, content: str) -> str:
        """Write content to a file, with backup."""
        path = self.context.resolve_path(rel_path)
        
        # Security check (Simple)
        if self.context.safe_mode:
            console.print(f"[yellow]⚠️  Request to write to: {rel_path}[/yellow]")
            # In a real CLI loop, we might ask for input here, 
            # but for the Agent's tool execution, we assume authorization 
            # or rely on the Orchestrator to ask user beforehand if designed so.
            # For this implementation, we proceed but log it visually.
        
        try:
            # Create backup if exists
            if path.exists():
                backup_path = path.with_suffix(path.suffix + ".bak")
                shutil.copy2(path, backup_path)
            
            # Ensure parent dirs exist
            path.parent.mkdir(parents=True, exist_ok=True)
            
            path.write_text(content, encoding="utf-8")
            return f"Successfully wrote to {rel_path}"
        except Exception as e:
            return f"Error writing file {rel_path}: {e}"

    def list_files(self, max_depth: int = 2) -> str:
        """List files in the project, respecting .gitignore."""
        # Load .gitignore patterns
        patterns = []
        gitignore_path = self.context.project_root / ".gitignore"
        if gitignore_path.exists():
            with open(gitignore_path, "r") as f:
                patterns = f.read().splitlines()
        
        # Add default ignores
        patterns.extend([".git", "__pycache__", ".DS_Store", "*.pyc", "venv", ".env"])
        spec = pathspec.PathSpec.from_lines(pathspec.patterns.gitwildmatch.GitWildMatchPattern, patterns)

        tree_output = []
        root = self.context.project_root
        
        for path in root.rglob("*"):
            rel_path = path.relative_to(root)
            
            # Skip checking directories themselves against gitignore for now needed for recursion logic?
            # pathspec matches files/dirs.
            if spec.match_file(str(rel_path)):
                continue
                
            # Depth check
            depth = len(rel_path.parts)
            if depth > max_depth:
                continue
                
            prefix = "  " * (depth - 1) + ("📂 " if path.is_dir() else "📄 ")
            tree_output.append(f"{prefix}{rel_path.name}")
            
        return "\n".join(tree_output) if tree_output else "(Empty directory)"
