from pathlib import Path
from rich.console import Console
from rich.panel import Panel

from ..core.context import ProjectContext
from ..core.files import FileManager
from ..core.shell import ShellRunner

from .planner import PlannerAgent
from .engineer import EngineerAgent

console = Console()

class DevMateOrchestrator:
    def __init__(self, project_root: str):
        path = Path(project_root).resolve()
        self.context = ProjectContext(project_root=path, work_dir=path)
        
        # Tools
        self.files = FileManager(self.context)
        self.shell = ShellRunner(self.context)
        
        # Agents
        self.planner = PlannerAgent()
        self.engineer = EngineerAgent(self.files, self.shell)

    def run(self, task: str):
        console.print(Panel(f"[bold blue]DevMate Task:[/bold blue] {task}"))
        
        # 1. Perception
        tree = self.files.list_files()
        console.print(f"[dim]Project Structure loaded ({len(tree.splitlines())} lines)[/dim]")
        
        # 2. Planning
        console.print("[bold yellow]🤖 [Planner] Thinking...[/bold yellow]")
        plan_data = self.planner.create_plan(task, tree)
        
        if "plan" not in plan_data:
            console.print("[red]Failed to generate plan.[/red]")
            return
            
        console.print(f"[dim]Thought: {plan_data.get('thought')}[/dim]")
        console.print("[bold green]📋 Plan Generated:[/bold green]")
        for i, step in enumerate(plan_data["plan"]):
            console.print(f"  {i+1}. {step}")
            
        # 3. Execution
        for i, step in enumerate(plan_data["plan"]):
            console.print(f"\n[bold cyan]▶️  Executing Step {i+1}: {step}[/bold cyan]")
            result = self.engineer.execute_step(step)
            console.print(f"[dim]Result: {result}[/dim]")
            
        console.print("\n[bold green]✅ Task Completed![/bold green]")
