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

* ```brew install pip3```
* ```pip3 install -r requirements.txt```
* ```mkdir -p data/raw```
* download the [Image_Downscaled](https://www.dropbox.com/home/Analytics/R%C3%B6ntgenklassificering/data?preview=Image_Downscaled.zip) zipfile from Forefront data repo. Ask someone who has access.
    * extract the folder to [data/raw](data/raw) so you get ```data/raw/Image_Downscaled```
* download the csv file which contain the image to label data at [ImageData.csv](https://www.dropbox.com/home/Analytics/R%C3%B6ntgenklassificering/data?preview=ImageData.csv)
    * put the csv file into ```data/raw``` so you get ```data/raw/ImageData.csv```

#### data-preprocessing

    * this is to visualize the neural network inside of jupyter notebook
* open Jupyter Notebook by ```jupyter notebook```
* go to ```notebooks/preprocessing.ipynb```
* run through all of the cells and the output will be folders with each class
* makes it into the folder structure
``` yaml
train:
    Body: "images"
    Head-Neck: "images"
    ..: "images"
test:
    Body: "images"
    Head-Neck: "images"
    ..: "images"
```

#### installation of tensorflow and running any model

* for mac install ```brew install gprof2dot```
    * otherwise install from source [graphviz](http://www.graphviz.org/pub/graphviz/CURRENT/graphviz-working.tar.gz)
* open the ```image_classification.ipynb``` notebook
* before running the model, start tensorboard by running:
    * cd to ```notebook``` directory and run 
    * ```tensorboard --logdir summary --port=8008 &```
    * this will give you tensorboard @ localhost:8008
* for running completely new models with tensorboard, just delete the ```summary``` folder
* all models will be stored inside models folder for further evaluation

## TODO

[x] create dataset with samples and labels (x,y)

[x] train a model for classifying at least with > 80 % accuracy and more precision than recall