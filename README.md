# ML in prod
Production ready project to solve classification task from Kaggle Dataset "[Heart Disease Cleveland UCI](https://www.kaggle.com/datasets/cherngs/heart-disease-cleveland-uci)"

## Python version 
Python >= 3.6

## Installation
#### Pyenv
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
#### Conda
```bash
conda create -n venv python=3.6 anaconda
source activate venv
conda install --file requirements.txt
```

## Usage
### Train
```bash
python ml_project/train.py
```
Also you can change configurations when run the script. For example:
```bash
python train.py pipeline=custom_pipeline.yaml
python train.py checkpoint_file=/home/username/location_to_save_model/
```
Or use multirun option:
```bash
python train.py --multirun pipeline=custom_pipeline.yaml,pipeline.yaml
python train.py --multirun metrics=f1.yaml,roc_auc.yaml,accuracy.yaml
```

### Inference
```bash
python ml_project/predict.py 'checkpoint_file=full_path_to_the_checkpoint' \ 
    'csv_output=specified_output_dir csv_filename=output_csv_filename' 
```
Example:
```bash
python ml_project/predict.py \ 
    'checkpoint_file=/home/user/homework1/ml_project/LR.pkl' \ 
    'csv_filename=output.csv'
```
Project Organization
------------
    ├── LICENSE
    ├── README.md                   <- The top-level README for developers using this project.
    ├── data                        <- The data sets for modeling.
    ├── notebooks                   <- Jupyter notebooks
    ├── requirements.txt            <- The requirements file for reproducing the analysis environment, e.g.
    │                                   generated with `pip freeze > requirements.txt`
    ├── requirements-dev.txt        <- The requirements with packages for development & testing
    │
    ├── ml_project                  <- Source code for use in this project.
    │   ├── config                  <- Config files
    │   │   ├── data         
    │   │   ├── metrics    
    │   │   ├── pipeline           
    │   │   ├── train.yaml         
    │   │   ├── predict.yaml         
    │   │   └── logger.yaml
    │   │ 
    │   ├── data                    <- Folder for dataset
    │   │   └── heart_cleveland_upload.csv
    │   │
    │   ├── predictor               <- Main codebase
    │   │   ├── data     
    │   │   │    └── data.py    
    │   │   ├── engine     
    │   │   │    └── trainer.py   
    │   │   ├── metrics     
    │   │   │    └── metrics.py 
    │   │   ├── pipeline     
    │   │   │    └── pipeline.py        
    │   │   ├── models     
    │   │   │    └── models.py          
    │   │   └── utils     
    │   │        └── utils.py 
    │   │
    │   ├── entities                <- Dataclasses for config validation
    │   │   └── config.py
    │   │
    │   ├── train.py       <- Train pipeline main script
    │   └── predict.py   <- Inference pipeline main script
    │
    ├── tests                       <- Tests for pipelines and functions
    ├── setup.cfg                   <- Store pytest configurations
    └── setup.py                    <- Makes project pip installable (pip install -e .) so src can be imported
--------

### Config supports
The project supports DataClass as HydraConfig or just yaml config files.