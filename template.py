import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)


project_name='edaproject'

list_of_files=[
    # ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/componennts/__init__py",
    f"src/{project_name}/componennts/data_ingestion.py",
    f"src/{project_name}/componennts/data_transformation.py",
    f"src/{project_name}/componennts/model_trainer.py",
    f"src/{project_name}/componennts/data_monitering.py",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/pipelines/training_pipeline.py",
    f"src/{project_name}/pipelines/prediction_pipeline.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utils.py",
    "app.py",
    "Dockerfile",
    "requirments.txt",
    "setup.py"

]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    
    else:
        logging.info(f"{filename} is already exists")