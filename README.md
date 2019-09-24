# Accelerometer-Based Gait Recognition
Senior Year capstone research project (MQP)\
**Goal**: Analyze gait patterns and Build a machine learning/deep learning system to identify subjects based on their gait\
**Stretch Goals**: Apply learned model and Build a mobile application that pops up "Hello [User]" once if it recogizes gait of the person on the phone\
**Development Status**: Currently an early stage project. Expected to complete by March 2020.

## Motivation

>Highest queen of state, Great Juno, comes. I know her by her gait.\
>The Tempest (Act 4, Scene 1)

Human **gait** refers to locomotion achieved through the movement of human limbs. Successful attempts for gait analysis using videos have been made. However, gait analysis by accelerometers is relatively under-researched and the good implementations of the working models are not only very rare to find but also extremely limited on the type of sensor.\
\
The purpose of this project is both to make an open-sourced implementation of gait analysis based on **mobile phone** accelerometers and potentially gyroscopes.


## Methodologies

Various analysis methodologies from a myriad of published research papers will be visited and applied as it is or in a combination of some form. Good tested combinations of methodologies will be noted with their respective performances.
All approaches will be implemented in PythonP

Dataset: Raw Time series data of 424,400 'Walking' data points. (Credited down below)\
Data Description: User_id | Movement_class | Time_stamp | X-acceleration | Y-acceleration | Z-acceleration)

<img src="https://github.com/tharminhtet/Accelerometer-Based-Gait-Recognition/blob/master/images/sample%20data.png" height="400" width="700">

**Figure: Plot of 100 continuous datapoints**

#### Average Cycle detection + Discrete fourier Transform + Euclidean distance (will be updated)

## Authors
* **Thar Min Htet**

## Credits
Special thanks to Professor.Emmanuel Agu for advising this project\
DATASET: [WISDM](http://www.cis.fordham.edu/wisdm/dataset.php | width=100)


### Reference
1. [Accelerometer-Based Gait Analysis, A survey](https://pdfs.semanticscholar.org/509a/4845cf3348837b4a2c0bbf19109449afa39f.pdf)
2. [Eigensteps: A giant leap for gait recognition](https://www.researchgate.net/publication/224151313_Eigensteps_A_giant_leap_for_gait_recognition)
3. [CyclePro: A Robust Framework for Domain-Agnostic Gait Cycle Detection](http://epsl.eecs.wsu.edu/wp-content/uploads/2015/03/08616844.pdf)
