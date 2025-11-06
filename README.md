# 🐍 Python Project Setup Guide

Welcome to this Python project!  
This guide will help you set up a clean and isolated development environment using Python's built-in `venv`.

---

## 📋 Table of Contents

- [Requirements](#-requirements)
- [Quick Start](#-quick-start)
- [Virtual Environment Setup](#-virtual-environment-setup)
- [Installing Dependencies](#-installing-dependencies)
- [Running the Project](#-running-the-project)
- [Development Workflow](#-development-workflow)
- [Troubleshooting](#-troubleshooting)
- [Additional Resources](#-additional-resources)

---

## 🔧 Requirements

- **Python 3.3+** (Recommended: Python 3.8 or newer)
- **pip** (Python package installer)
- A terminal or command prompt
- Git (optional, for version control)

---

## 🚀 Quick Start

```bash
# Clone the repository (if applicable)
git clone <repository-url>
cd <project-directory>

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # On macOS/Linux
# or
venv\Scripts\activate  # On Windows

# Install dependencies
pip install -r requirements.txt

# Run the project
python main.py  # Adjust based on your entry point
```

---

## 🌱 Virtual Environment Setup

### 1. Check Your Python Version

First, verify that you have Python installed:

```bash
python3 --version
# or on Windows
python --version
```

You should see output like `Python 3.x.x`. If not, [download Python](https://www.python.org/downloads/).

### 2. Create a Virtual Environment

Navigate to your project directory and create a virtual environment:

```bash
# On macOS/Linux
# -m venv 表示使用 Python 的 venv 模块来创建一个虚拟环境（virtual environment）。
python3 -m venv venv

# On Windows
python -m venv venv
```

This creates a `venv` directory containing an isolated Python environment.

### 3. Activate the Virtual Environment

**macOS/Linux:**
```bash
source venv/bin/activate
```

**Windows (Command Prompt):**
```cmd
venv\Scripts\activate
```

**Windows (PowerShell):**
```powershell
venv\Scripts\Activate.ps1
```

> **Note:** If you encounter a PowerShell execution policy error, run:
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```

When activated, you'll see `(venv)` prefix in your terminal prompt.

### 4. Deactivate the Virtual Environment

When you're done working, deactivate the environment:

```bash
deactivate
```

---

## 📦 Installing Dependencies

### Install from requirements.txt

If the project has a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### Install Individual Packages

To install specific packages:

```bash
pip install <package-name>

# Examples:
pip install "fastapi[all]"
pip install uvicorn[standard]
pip install requests
```

### Upgrade pip (Recommended)

Keep pip up to date:

```bash
pip install --upgrade pip
```

---

## 🏃 Running the Project

Adjust the following commands based on your project structure:

```bash
# For a FastAPI application
uvicorn main:app --reload

# For a standard Python script
python main.py

# For a Flask application
flask run

# For a Django application
python manage.py runserver
```

---

## 💻 Development Workflow

### 1. Save Your Dependencies

After installing new packages, update `requirements.txt`:

```bash
pip freeze > requirements.txt
```

### 2. Check Installed Packages

View all installed packages:

```bash
pip list
```

### 3. Uninstall Packages

Remove packages you no longer need:

```bash
pip uninstall <package-name>
```

### 4. Create a .gitignore File

Prevent committing unnecessary files:

```gitignore
# Virtual Environment
venv/
env/
ENV/

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python

# IDE
.vscode/
.idea/
*.swp
*.swo

# Environment variables
.env
.env.local

# OS
.DS_Store
Thumbs.db
```

---

## 🔍 Troubleshooting

### Virtual Environment Not Activating

- **Windows PowerShell:** Check execution policy (see activation section)
- **Path Issues:** Ensure you're in the correct directory
- **Permissions:** Run terminal as administrator if needed

### Package Installation Fails

```bash
# Try upgrading pip first
pip install --upgrade pip

# Use --user flag if permission denied
pip install --user <package-name>

# Clear pip cache
pip cache purge
```

### Python Version Conflicts

```bash
# Use specific Python version
python3.9 -m venv venv
python3.10 -m venv venv
```

### "Command not found" Errors

- Ensure Python is in your system PATH
- Try using `python` instead of `python3` (or vice versa)
- Reinstall Python and check "Add to PATH" during installation

---

## 📚 Additional Resources

- [Python Official Documentation](https://docs.python.org/3/)
- [pip Documentation](https://pip.pypa.io/en/stable/)
- [Virtual Environments Guide](https://docs.python.org/3/tutorial/venv.html)
- [Python Package Index (PyPI)](https://pypi.org/)

---

## 📝 License

[Specify your license here]

## 🤝 Contributing

[Add contribution guidelines if applicable]

## 📧 Contact

[Add contact information or links]

---

**Happy Coding! 🎉**
