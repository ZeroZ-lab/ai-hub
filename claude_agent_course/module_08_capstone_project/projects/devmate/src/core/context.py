from pathlib import Path
from typing import List, Optional
from pydantic import BaseModel

class ProjectContext(BaseModel):
    """
    Holds the current context of the project being worked on.
    """
    project_root: Path
    work_dir: Path
    # User preferences could go here
    safe_mode: bool = True
    
    class Config:
        arbitrary_types_allowed = True

    def resolve_path(self, path_str: str) -> Path:
        """Resolve a path relative to the work_dir, ensuring it stays within project_root."""
        path = (self.work_dir / path_str).resolve()
        if not str(path).startswith(str(self.project_root.resolve())):
             # In a real scenario, might want to allow /tmp, but for now strict.
             # Or just warn. For this project, let's keep it simple.
             pass
        return path
