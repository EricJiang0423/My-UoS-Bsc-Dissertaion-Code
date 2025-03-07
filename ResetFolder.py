# This Python file is to clean the temerory files and folders.
# !!!!!!!!!  Use by Caution

import os
# delete datasets, results, tensorboard_log, trained_models
folders_to_delete = ["datasets", "results", "tensorboard_log"]
for folder in folders_to_delete:
    if os.path.exists(folder):
        os.system(f"rmdir /S /Q {folder}")

# delete pycache
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".pyc"):
            os.remove(os.path.join(root, file))

# delete __pycache__
if os.path.exists("__pycache__"):
    os.system("rmdir /S /Q __pycache__")

# delete .ipynb_checkpoints
if os.path.exists(".ipynb_checkpoints"):
    os.system("rmdir /S /Q .ipynb_checkpoints")