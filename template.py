# script to create the repo template for the project

import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# define the project name
project_name = 'chicken_disease_detection'

# define the list of files to be created
list_of_files = [
    ".github/workflows/.gitkeep",
    "research/trials.ipynb",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "environment.yaml",
    "templates/index.html",
    "Makefile",
]

# create the files
for file in list_of_files:
    file = Path(file)
    filedir, filename = os.path.split(file)

    if filedir != '':
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir}")
    
    if (not os.path.exists(file)) or (os.path.getsize(file) == 0):
        with open(file, 'w') as f:
            logging.info(f"Created empty file: {file}")
    else:
        logging.info(f"File already exists: {file}")

