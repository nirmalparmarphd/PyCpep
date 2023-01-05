# microDSC_error_prediction_ANN
Prediction in the isobaric heat capacity measurement (at 298~K) deviation due to improper amount of the sample or/and calibration standard in Tian-Calvet microDSC

> Estimated ANN Model prediction accuracy over the test data is '99.52[%]'

![Deep Neural Network Architecture used in the present case](dsc_ann.png)

# Direction
Use python file 'mwe.py' file to predict the error in heat capacity measurement

**OR**

Minimum Working Example

```python:
# prediction of error/deviation in the heat capacity measurement
# use: prediction = dsc_error_model(Reference amount, Sample amount)
# NOTE: enter the sample and reference material amount as mentioned below
    ## Full cell:               1.0 
    ## Two Third full cell:     0.66
    ## One half full cell:      0.5
    ## One third full cell:     0.33


### MINIMUM WORKING EXAMPLE ###

# import module
import pycpep as pc

# defining values
Reference_amount = 1
Sample_amount = 1

# prediction of deviation in heat capacity measurement
error_pred = pc.dev_pred(Reference_amount,Sample_amount)

# for help
pc.dev_pred.help()

# for info of model
pc.dev_pred.info()
```

The example output

```
1/1 [==============================] - 0s 392ms/step
----------------------------------------------------------------------
Reference amount :  1
Sample amount :  1
Heat capacity measurement deviation prediction (%):  [[-0.1]]
COMMENT(s):
            The predicted deviation is below 1%!
            The combination of the sample and the reference amount is appropriate.
            NOTE:
            Consider 0.8~ml as standard amount to avoid any deviation in the measurement.
----------------------------------------------------------------------
```