"""ECU44291 self-check. Run with:  uv run python check_setup.py

Prints PASS or FAIL for each item. Every FAIL says what to do.
Belongs at the root of the student template repository.
"""
import importlib
import shutil
import subprocess
import sys
from pathlib import Path

results = []


def check(name, ok, fix=""):
    results.append((name, ok, fix))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + ("" if ok else f"  ->  {fix}"))


def run(cmd):
    try:
        out = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
        return out.returncode == 0, out.stdout.strip()
    except (OSError, subprocess.TimeoutExpired):
        return False, ""


# 1. Python version
v = sys.version_info
check(f"Python {v.major}.{v.minor}.{v.micro}", (v.major, v.minor) >= (3, 11),
      "run 'uv sync' and then 'uv run python check_setup.py' so uv's Python is used")

# 2. Running inside the project's virtual environment
check("running inside .venv", ".venv" in sys.prefix,
      "run this as 'uv run python check_setup.py', not plain 'python'")

# 3. Packages
for pkg in ("numpy", "scipy", "matplotlib", "pytest"):
    try:
        mod = importlib.import_module(pkg)
        check(f"{pkg} {getattr(mod, '__version__', '')}".strip(), True)
    except ImportError:
        check(pkg, False, "run 'uv sync' in the project folder")

# 4. git installed and configured
check("git installed", shutil.which("git") is not None,
      "install Git for Windows, or 'xcode-select --install' on a Mac")
ok, name = run(["git", "config", "user.name"])
check("git user.name set", ok and bool(name),
      "git config --global user.name \"Your Name\"")
ok, email = run(["git", "config", "user.email"])
check("git user.email set", ok and bool(email),
      "git config --global user.email \"you@tcd.ie\"")

# 5. This folder is a repository with a remote
ok, _ = run(["git", "rev-parse", "--is-inside-work-tree"])
check("inside a git repository", ok, "clone your repository and run this from inside it")
ok, remote = run(["git", "remote", "get-url", "origin"])
check("remote 'origin' set", ok and "github.com" in remote,
      "clone from GitHub rather than copying files")

# 6. Not inside a synced folder
here = str(Path.cwd()).lower()
synced = any(s in here for s in ("onedrive", "icloud", "dropbox"))
check("not inside OneDrive/iCloud/Dropbox", not synced,
      "move the repository to a plain local folder such as ~/code/")

# 7. Copilot: cannot be checked from Python; remind
print("[NOTE] Copilot: allowed except during M1 Part A. See section D of the checklist for how to disable it.")

n_fail = sum(1 for _, ok, _ in results if not ok)
print()
print("All checks passed. You are set up." if n_fail == 0 else f"{n_fail} item(s) to fix. Bring any you cannot fix to the Week 2 office hours.")
sys.exit(1 if n_fail else 0)
