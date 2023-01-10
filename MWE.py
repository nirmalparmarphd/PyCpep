# to load pkg
from PyCpep import pycpep as pc

# to check pkg is loaded
pc.pkg()

# to download pkg and its dependencies locally 
# pc.pkg.load() #NOTE: only use to download!

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
