import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PyCpep import DeviationPredictor

# initializing
deviation = DeviationPredictor()


deviation.info()

deviation.load_locally()

R = 1 # Reference amount
S = 1 # Sample amount
deviation.deviation_prediction(R,S)