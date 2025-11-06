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
```

You should see output like `Python 3.x.x`. If not, [download Python](https://www.python.org/downloads/).

### 2. Create a Virtual Environment

Navigate to your project directory and create a virtual environment:

```bash
# On macOS/Linux
# -m venv 表示使用 Python 的 venv 模块来创建一个虚拟环境（virtual environment）。
python3 -m venv venv
```

This creates a `venv` directory containing an isolated Python environment.

### 3. Activate the Virtual Environment

**macOS/Linux:**
```bash
source venv/bin/activate
```

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

## ⚡ FastAPI 核心组件

**Starlette：高性能 ASGI 框架**  
FastAPI 基于 Starlette，因此同时继承了 Starlette 提供的异步请求处理、WebSocket 支持、中间件系统和依赖注入等特性。要自定义更底层的行为（例如挂载额外的 ASGI 应用或编写自定义中间件），可以直接使用 FastAPI 实例的 `.add_middleware()`、`.mount()` 等方法，它们与 Starlette 保持兼容。

**Pydantic：飞快的数据校验与序列化**  
FastAPI 中的请求体、查询参数和响应模型均由 Pydantic 驱动。通过声明 `BaseModel` 子类，你可以让 FastAPI 自动完成类型转换、默认值填充和输入校验，并在响应时生成结构化数据。例如：

```python
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    tags: list[str] = []


@app.post("/items")
async def create_item(item: Item):
    return item  # FastAPI 自动使用 Pydantic 序列化响应
```

> 提示：当你的模型或验证逻辑更复杂时，可以利用 Pydantic 的校验器（`@field_validator`）或模型配置（`model_config`）来精细控制输入输出格式。

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
```

---

## 🔍 Troubleshooting

### Virtual Environment Not Activating

- **Path Issues:** Ensure you're in the correct directory
- **Permissions:** Use `sudo` for commands that require elevated rights

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
- If using the official installer, add the Python binary to your shell profile (`~/.zshrc`, `~/.bashrc`, etc.)

---

## 📚 Additional Resources

- [Python Official Documentation](https://docs.python.org/3/)
- [pip Documentation](https://pip.pypa.io/en/stable/)
- [Virtual Environments Guide](https://docs.python.org/3/tutorial/venv.html)
- [Python Package Index (PyPI)](https://pypi.org/)

---


**Happy Coding! 🎉**
