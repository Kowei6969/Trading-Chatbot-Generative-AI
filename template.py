#  Automatically create the project folder structure (Can be use in every project)
# Help to save time manually creating folder structure

import os
from pathlib import Path
import logging

# Create logging string   
                    #Create information level log
                    # - save the current timestamp when executing of code
                    # - save the log message
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

list_of_files = [
    "src\__init__.py",
    "src\help.py",
    "src\prompt.py",
    ".env",
    "setup.py",
    "app.py",
    "research\\trials.ipynb",
    "test.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    # Check whether folder directory is not empty
    if filedir != "":
         # Create folder
        os.makedirs(filedir, exist_ok=True)
        # Login in terminal and creating folder directory for the filename
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    # Create file (Check if exists and if size = 0)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else: 
        logging.info(f"{filename} is already exists")

### Execute this code "python template.py" in git.cmd
# from pathlib import Path
# p = "test/t.py"
# Path(p)
# import os
# os.path.split(p)
# ('test', 't.py')
# ^(folder, file)
###