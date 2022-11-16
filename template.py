import os
from pathlib import Path
import logging

logging.basicConfig(
    level = logging.INFO,
    format = "[%(asctime)s: %(levelname)s]: %(message)s"
    )

while True:
    project_name = input("Enter project name: ")
    if project_name != '':
        break
    
logging.info(f'Creating project by name: {project_name}')

# list of files
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"tests/__init__.py",
    f"src/unit/__init__.py",
    f"src/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "pyproject.toml",
    "setup.cfg",
    "tox.ini",
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating file directory at {filedir} for file: {filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
        logging.info(f"Created a new {filename} at path: {filepath}")
    else:
        logging.info(f"File is already exists at {filepath}")
    