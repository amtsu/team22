import sys
import os
MODULE_PATH = os.path.dirname(os.path.abspath(__file__))
if(MODULE_PATH) not in sys.path: 
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))