print('-'*70)

import pandas as pd
import numpy as np
import pickle
from tensorflow.keras.models import load_model

initial_info = '''
                  -------------------------------------------------------
                  #--> import pkg:  import pycpep as pc
                  #--> get info:    pc.prediction.info()
                  #--> get help:    pc.prediction.help()
                  more details: https://github.com/nirmalparmarphd/PyCpep
                  -------------------------------------------------------'''
print(initial_info)  
class prediction():    
  def __init__(self,Ref,Sam):
    if 0 < Ref <= 1 and 0 < Sam <= 1:   
      self.Ref = Ref
      self.Sam = Sam
      model = load_model('micro_dsc_dl.h5')
      with open('scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)
      vol_rel = (self.Ref*self.Ref)/self.Sam
      data = [self.Ref, self.Sam, vol_rel]
      data = pd.DataFrame([data])
      data_ = scaler.transform(data)
      pred = model.predict(data_)
      pred_ = np.round(((pred*100)-100).astype(np.float64),1)
      
      print('-'*70)
      print('Reference amount : ', Ref)
      print('Sample amount : ', Sam)
      
      if abs(pred_) <= 1.5:
        print('Heat capacity measurement deviation prediction (%): ', pred_)
        print('''COMMENT(s):
              You are Awesome!! The predicted deviation is below 1%!
              The combination of the sample and the reference amount is appropriate.
              NOTE:
              Consider 0.8~ml as standard amount to avoid any deviation in the measurement.''')
      else:
        print('Heat capacity measurement deviation prediction (%): ', pred_)
        print('''COMMENT(s): 
              The combination of the sample and the reference amount is NOT appropriate.
              NOTE:
              Consider 0.8~ml as standard amount to avoid any deviation in the measurement.
              ''')
      print('-'*70)
    else:
      print(''' ERROR! --> Entered value of of the reference or/and the standard amount is NOT appropriate.

              # NOTE: enter the sample and reference material amount as mentioned below
                ## Full cell:               1.0 
                ## Two Third full cell:     0.66
                ## One half full cell:      0.5
                ## One third full cell:     0.33
    ''')    

  def info():
      information ='''
        * This is a Deep learning (DL) ANN model to predict a deviation due to an inappropriate amount combination of the sample and a reference material in a batch cell of Tian-Calvet micro-DSC.

        * This ANN model predicts the possible deviation that may arise in the heat capacity measurement experiment due to in appropriate combination of the sample and the reference material amount!

        --> ANN Model accuracy on the test data is 99.82 [%] <--
        
        * more details: https://github.com/nirmalparmarphd/PyCpep'''
      print(information)

  def help():
      help_info = '''
        # prediction of error/deviation in the heat capacity measurement
        # use: prediction = dsc_error_model(Reference amount, Sample amount)
        # NOTE: enter the sample and reference material amount as mentioned below
            ## Full cell:               1.0 
            ## Two Third full cell:     0.66
            ## One half full cell:      0.5
            ## One third full cell:     0.33

        ### MINIMUM WORKING EXAMPLE ###

        # import module
        >>> import pycpep as pc

        # defining values
        >>> Reference_amount = 1
        >>> Sample_amount = 1

        # prediction of deviation in heat capacity measurement
        >>> error_pred = pc.prediction(Reference_amount,Sample_amount)
            '''  
      print(help_info)

