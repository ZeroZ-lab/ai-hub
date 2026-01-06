import subprocess
from .context import ProjectContext

class ShellRunner:
    def __init__(self, context: ProjectContext):
        self.context = context

    def run_command(self, command: str, timeout: int = 30) -> str:
        """Run a shell command in the project directory."""
        try:
            # Security check
            # For "rm -rf" etc. simple explicit blocks could be added here.
            
            result = subprocess.run(
                command,
                shell=True,
                cwd=str(self.context.work_dir),
                capture_output=True,
                text=True,
                timeout=timeout
            )
            
            output = result.stdout
            if result.stderr:
                output += f"\nSTDERR:\n{result.stderr}"
                
            if result.returncode != 0:
                output += f"\n[Exit Code {result.returncode}]"
                
            return output.strip()
        except subprocess.TimeoutExpired:
            return f"Error: Command timed out after {timeout} seconds."
        except Exception as e:
            return f"Error executing command: {e}"
