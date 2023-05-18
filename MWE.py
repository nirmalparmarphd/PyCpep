
# to load pkg
from PyCpep import DeviationPredictor

deviation = DeviationPredictor()

# help
help(deviation)

# info
deviation.info()

# Minimum working example download for a quick start
deviation.load_locally()

# deviation prediction
R = 1 # Reference amount
S = 1 # Sample amount
deviation.deviation_prediction(R,S)

# NOTE: enter the sample and reference material amount as mentioned below
    ## Full cell:               1.0     [0.80 to 1.00 ml]
    ## Two Third full cell:     0.66    [0.40 to 0.80 ml]
    ## One half full cell:      0.5     [0.26 to 0.40 ml]
    ## One third full cell:     0.33    [0.10 to 0.26 ml]
# prediction of the deviation in heat capacity measurement


