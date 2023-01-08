# PyCpep
Prediction in the isobaric heat capacity measurement (at 298~K) deviation due to improper amount of the sample or/and calibration standard in Tian-Calvet microDSC

> Estimated ANN Model prediction accuracy over the test data is '99.83[%]' and R2-score 99.39

# Direction
1. Open terminal and install the PyCpep package by the following pip command.
```
pip install pycpep
```
2. To check a pkg download and a pkg importing for the setup. Python 3.8 or higher version is required.
```
$ python

>>> import pycpep as pc

----------------------------------------------------------------------
Depended packages imported successfully.

                  -------------------------------------------------------
                  #--> import pkg:    import pycpep as pc
                  #--> load locally:  pc.pkg.load()
                  #--> get info:      pc.pkg.info()
                  #--> get help:      pc.pkg.help()
                  #--> use MWE.py to check minimum working example.

                  more details: https://github.com/nirmalparmarphd/PyCpep
                  -------------------------------------------------------
                  
```
3. Download pkg dependencies and ANN model locally for the prediction in the current working directory.

```
>>> pc.pkg.load()

----------------------------------------------------------------------
Directory 'dir_pycpep' created
Downloaded PyCpep in current directory.
```

4. Navigate to 'dir_pycpep' to fine the minimum working example (MWE.py) and run in with the python to predict the deviation in heat capacity measurement.

Minimum Working Example

```python:
# to load pkg
import pycpep as pc

# to check pkg is loaded
pc.pkg()

#   to download pkg and its dependencies locally 
##  pc.pkg.load() #NOTE: only use to download!

# to get quick info on pkg
pc.pkg.info()

# to get quick help on use
pc.pkg.help()

# NOTE: enter the sample and reference material amount as mentioned below
    ## Full cell:               1.0     [0.80 to 1.00 ml]
    ## Two Third full cell:     0.66    [0.40 to 0.80 ml]
    ## One half full cell:      0.5     [0.26 to 0.40 ml]
    ## One third full cell:     0.33    [0.10 to 0.26 ml]
# prediction of the deviation in heat capacity measurement

R = 1 # Reference amount
S = 1 # Sample amount
pc.pkg.prediction(R,S)

```
Example output of the prediction shown in the MWE.py
```
1/1 [==============================] - 0s 494ms/step
----------------------------------------------------------------------
Reference amount :  1
Sample amount :  1
Heat capacity measurement deviation prediction (%):  [[-0.1]]
COMMENT(s):
              You are Awesome!! The predicted deviation is below 1%!
              The combination of the sample and the reference amount is appropriate.
              NOTE:
              Consider 0.8~ml as standard amount to avoid any deviation in the measurement.
----------------------------------------------------------------------
```