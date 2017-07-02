dicommunify
==============================

DICommunify is built for dicom header images in which to translate them from imagery to the approriate DICOM encoding

## Prerequisities

* virtualenv
* python 3.x installed on your computer
* scipy and numpy
* theano / tensorflow and keras
* matplotlib (optional)

### Installation

* pip install -r requirements.txt
* download the [Image_Downscaled](https://www.dropbox.com/home/Analytics/R%C3%B6ntgenklassificering/data?preview=Image_Downscaled.zip) zipfile from Forefront data repo. Ask someone who has access.
        * put the image folder inside [data/raw](data/raw) as in data/raw/Image_Downscaled
* download the csv file which contain the image to label data at [ImageData.csv](https://www.dropbox.com/home/Analytics/R%C3%B6ntgenklassificering/data?preview=ImageData.csv)
* Preprocess the data using datapreprocessing module
* all models will be stored inside models folder

#### isntallatio nof tensorflow and running any model

* Follow the instructions for installation of the tensorflow environment from here [docker installation](https://docs.docker.com/engine/installation/#supported-platforms)
 * run from the command line ```docker run -it -p 8888:8888 tensorflow/tensorflow```
 * upload the image_classification notebook

## TODO

[x] create dataset with samples and labels (x,y)
[x] train a model for classifying at least with > 80 % accuracy and more precision than recall

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.testrun.org


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
