import typer
import os
from pathlib import Path
from dotenv import load_dotenv
from .agents.orchestrator import DevMateOrchestrator

load_dotenv()

app = typer.Typer(help="DevMate: AI Developer Agent")

@app.command()
def init():
    """Initialize DevMate in the current directory."""
    print("DevMate initialized in current directory.")

@app.command()
def do(task: str):
    """Execute a development task."""
    cwd = os.getcwd()
    orchestrator = DevMateOrchestrator(cwd)
    orchestrator.run(task)

@app.command()
def chat():
    """Interactive chat mode (Placeholder)."""
    print("Chat mode coming soon!")

if __name__ == "__main__":
    app()
