# Accelerometer-Based Gait Recognition
Senior Year capstone research project (MQP)\
**Goal**: Analyze gait patterns and Build a machine learning/deep learning system to identify subjects based on their gait\
**Stretch Goals**: Apply learned model and Build a mobile application that pops up "Hello [User]" once if it recogizes gait of the person on the phone

## Motivation

>Highest queen of state, Great Juno, comes. I know her by her gait.\
>The Tempest (Act 4, Scene 1)

Human **gait** refers to locomotion achieved through the movement of human limbs. Successful attempts for gait analysis using videos have been made. However, gait analysis by accelerometers is relatively under-researched and the good implementations of the working models are not only very rare to find but also extremely limited on the type of sensor.\
\
The purpose of this project is both to make an open-sourced implementation of gait analysis based on **mobile phone** accelerometers and potentially gyroscopes.


## Methodologies

Various analysis methodologies from a myriad of published research papers will be visited and applied as it is or in a combination of some form. Good tested combinations of methodologies will be noted with their respective performances.

Dataset: Raw Time series data of 424,400 'Walking' data points. (Credited down below)

#### Average Cycle detection + Discrete fourier Transform + Euclidean distance

## Authors
* **Thar Min Htet**

## Credits
Special thanks to Professor.Emmanuel Agu for advising this project\
DATASET: [WISDM](http://www.cis.fordham.edu/wisdm/dataset.php)


### Reference
1. Accelerometer-Based Gait Analysis, A survey
2. Eigensteps: A giant leap for gait recognition
3. CyclePro: A Robust Framework for Domain-Agnostic Gait Cycle Detection
