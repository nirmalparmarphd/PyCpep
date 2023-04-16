# [PyCpep](https://pypi.org/project/pycpep/)
[PyCpep](https://pypi.org/project/pycpep/) package predicts the deviation in the isobaric heat capacity measurement (at 298~K) due to the improper amount of the sample or/and calibration standard in Tian-Calvet microDSC. PyCpep package works on the well-trained artificial neural network (ANN) model.

> Estimated PyCpep prediction accuracy over the test data is '99.83[%]' and R2-score 99.4

# Direction
1. Open terminal and install the [PyCpep](https://pypi.org/project/pycpep/) package by the following pip command.
```
pip install pycpep
```
2. To check the pkg download and importing the pkg in python. Python 3.8 or higher version is required.
```
$ python

  ## DeviationPredictor
  DeviationPredictor is a class from PyCpep package to predict a deviation in the heat capacity measurement (at 298~K) due to the improper amount of the sample or/and calibration standard in Tian-Calvet microDSC. PyCpep package works on the well-trained artificial neural network (ANN) model.
  
  ## useage:\n
  ## importing module\n
  from pycpep import DeviationPredictor\n
  deviation = DeviationPredictor(Ref, Sam)
  ## calling help
  help(deviation)
  ## quick info
  deviation.info()
  ## downloading trained model locally
  deviation.load_locally()
  ## deviation prediction
  deviation.deviation_prediction()

  more details: https://github.com/nirmalparmarphd/PyCpep
```

## NOTE: enter the sample and reference material amount as mentioned below

```
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
    Heat capacity measurement deviation prediction (%):  [[0.01]]
    COMMENT(s):
                You are Awesome!! The predicted deviation is below 1%!
                The combination of the sample and the reference amount is appropriate.
                NOTE:
                Consider 0.8~ml as standard amount to avoid any deviation in the measurement.
    ----------------------------------------------------------------------
```
