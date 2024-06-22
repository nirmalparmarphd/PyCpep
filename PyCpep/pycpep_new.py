import os
import shutil
import joblib
import pandas as pd
import numpy as np
import tensorflow as tf
from git import Repo

class DeviationPredictor:
    """
    DeviationPredictor is a class from the PyCpep package to predict a deviation in the heat capacity measurement (at 298 K)
    due to the improper amount of the sample or/and calibration standard in Tian-Calvet microDSC. PyCpep package works on a
    well-trained artificial neural network (ANN) model.
    
    Usage:
    ```
    from pycpep import DeviationPredictor
    deviation = DeviationPredictor()
    help(deviation)
    deviation.info()
    deviation.load_locally()
    deviation.deviation_prediction(Ref, Sam)
    ```
    
    More details: https://github.com/nirmalparmarphd/PyCpep
    """
    
    def __init__(self):
        print("Imported DeviationPredictor successfully.")
        self.amount_info_msg = """
        ERROR! --> Entered value of the reference or/and the standard amount is NOT appropriate.

        # NOTE: enter the sample and reference material amount as mentioned below

        ## Full cell:               1.0     [0.80 to 1.00 ml]
        ## Two Third full cell:     0.66    [0.40 to 0.80 ml]
        ## One half full cell:      0.5     [0.26 to 0.40 ml]
        ## One third full cell:     0.33    [0.10 to 0.26 ml] 

        For more information please check https://github.com/nirmalparmarphd/PyCpep.
        """
        self.information = """
        * This is a Deep learning (DL) ANN model to predict a deviation due to an inappropriate amount combination of the sample and a reference material in a batch cell of Tian-Calvet micro-DSC.

        * This ANN model predicts the possible deviation that may arise in the heat capacity measurement experiment due to inappropriate combination of the sample and the reference material amount!

        --> ANN Model accuracy on the test data is 99.83 [%] <--

        * More details: https://github.com/nirmalparmarphd/PyCpep
        """

    def load_locally(self):
        """
        Load the ANN model locally by downloading the minimum working example (.py) for a quick start.

        Usage:
        ```
        from pycpep import DeviationPredictor
        deviation = DeviationPredictor()
        deviation.load_locally()
        ```
        """
        url_mwe = 'https://github.com/nirmalparmarphd/PyCpep/'
        cwd = os.getcwd()
        directory = 'pkg_pycpep'
        path = os.path.join(cwd, directory)
        self.path = path

        if not os.path.exists(path):
            os.mkdir(path)
            print(f"Directory '{directory}' created")
            Repo.clone_from(url_mwe, directory)
            print(f'Downloaded the latest trained neural network model from the PyCpep package source successfully at: {path}')
        else:
            print(f"Directory '{directory}' already exists!")
        
        # Cleaning unnecessary files
        self._clean_directory(path)

    def _clean_directory(self, path):
        """Clean up unnecessary files in the directory."""
        files_to_remove = [
            "setup.py",
            "PyCpep/__init__.py",
            "PyCpep/pycpep.py",
            "PyCpep/setup.cfg"
        ]
        for file in files_to_remove:
            file_path = os.path.join(path, file)
            if os.path.exists(file_path):
                os.remove(file_path)

        cache_dir = os.path.join(path, "PyCpep/__pycache__")
        if os.path.exists(cache_dir):
            shutil.rmtree(cache_dir, ignore_errors=True)

    def deviation_prediction(self, Ref: float, Sam: float, scaler_pkl="scaler.pkl", mdl_h5="model.h5"):
        """
        Predict the possible deviation in the heat capacity measurement as a function of the sample and the reference material amount.

        Usage:
        ```
        from pycpep import DeviationPredictor
        deviation = DeviationPredictor()
        deviation.deviation_prediction(Ref, Sam)
        ```

        Args:
            Ref (float): Reference material amount.
            Sam (float): Sample material amount.
            scaler_pkl (str): Path to the scaler file.
            mdl_h5 (str): Path to the ANN model file.

        Returns:
            dict: Prediction results including the reference amount, sample amount, and predicted deviation.
        """
        self.scaler_pkl = scaler_pkl
        self.mdl_h5 = mdl_h5
        self.Ref = Ref
        self.Sam = Sam

        if not (0 < Ref <= 1 and 0 < Sam <= 1):
            return {"error": f"[Ref: {self.Ref}, Sam: {self.Sam}]: Please enter the correct amount of the sample and the reference material.\n {self.amount_info_msg}"}

        # Load scaler
        scaler = joblib.load(os.path.join(self.path, f"PyCpep/mdl/{self.scaler_pkl}"))
        
        # Load ANN model
        model = tf.keras.models.load_model(os.path.join(self.path, f"PyCpep/mdl/{self.mdl_h5}"))
        
        # Calculate vol-rel
        vol_rel = (Ref * Ref) / Sam
        data = pd.DataFrame([[Ref, Sam, vol_rel]])
        
        # Scale data
        data_ = scaler.transform(data)
        
        # Predict from ANN model
        pred = model.predict(data_)
        pred_ = np.round(((pred * 100) - 100).astype(np.float64), 2)
        
        result = {
            "Reference amount": Ref,
            "Sample amount": Sam,
            "Predicted deviation (%)": pred_.item(),
            "Comment": self._get_comment(pred_)
        }
        return result

    def _get_comment(self, pred):
        """Generate comment based on prediction result."""
        if abs(pred) <= 1.5:
            return "You are Awesome!! The predicted deviation is below 1%! The combination of the sample and the reference amount is appropriate."
        else:
            return "The combination of the sample and the reference amount is NOT appropriate. Consider 0.8~ml as standard amount to avoid any deviation in the measurement."

    def info(self):
        """
        Get a quick info on module usage.

        Usage:
        ```
        from pycpep import DeviationPredictor
        deviation = DeviationPredictor()
        deviation.info()
        ```
        """
        return self.information
