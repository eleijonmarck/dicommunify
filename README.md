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

* preprocess data with datapreprocessing notebook
* makes it into
    * body
    * head-neck
    * ..

#### installation of tensorflow and running any model

* Follow the instructions for installation of the tensorflow environment from here [docker installation](https://docs.docker.com/engine/installation/#supported-platforms)
* command line ```docker run -it -p 8888:8888 tensorflow/tensorflow```
* upload the image_classification notebook
* all models will be stored inside models folder

## TODO

[x] create dataset with samples and labels (x,y)

[x] train a model for classifying at least with > 80 % accuracy and more precision than recall