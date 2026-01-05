#!/usr/bin/env python3
"""Validate Module 05 projects can import correctly."""

import sys
import importlib.util
from pathlib import Path


def test_import(project_name: str, module_path: Path) -> bool:
    """Test if a module can be imported."""
    print(f"\n{'='*60}")
    print(f"Testing {project_name}")
    print(f"{'='*60}")

    spec = importlib.util.spec_from_file_location("test_module", module_path)
    if spec is None or spec.loader is None:
        print(f"❌ Failed to load spec for {module_path}")
        return False

    try:
        module = importlib.util.module_from_spec(spec)
        sys.modules["test_module"] = module
        spec.loader.exec_module(module)
        print(f"✅ Successfully imported {module_path.name}")
        return True
    except Exception as e:
        print(f"❌ Import failed: {e}")
        import traceback
        traceback.print_exc()
        return False
    finally:
        if "test_module" in sys.modules:
            del sys.modules["test_module"]


def main():
    """Main validation function."""
    base_dir = Path(__file__).parent / "projects"

    projects = [
        ("project_01_mcp_note_server", ["solution/server.py", "solution/agent.py", "solution/main.py"]),
        ("project_02_mcp_filesystem_agent", ["solution/agent.py", "solution/main.py"]),
        ("project_03_mcp_git_inspector", ["solution/agent.py", "solution/main.py"]),
        ("project_04_mcp_sqlite_analyst", ["solution/agent.py", "solution/main.py"]),
    ]

    results = []

    for project_name, files in projects:
        project_path = base_dir / project_name

        # Add project to sys.path temporarily
        sys.path.insert(0, str(project_path))

        project_results = []
        for file_path in files:
            full_path = project_path / file_path
            if not full_path.exists():
                print(f"❌ File not found: {full_path}")
                project_results.append(False)
                continue

            success = test_import(f"{project_name}/{file_path}", full_path)
            project_results.append(success)

        # Remove from sys.path
        sys.path.pop(0)

        results.append((project_name, all(project_results)))

    print(f"\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")

    for project_name, success in results:
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{status}: {project_name}")

    all_passed = all(success for _, success in results)

    if all_passed:
        print(f"\n✅ All projects validated successfully!")
        return 0
    else:
        print(f"\n❌ Some projects failed validation")
        return 1


if __name__ == "__main__":
    sys.exit(main())
