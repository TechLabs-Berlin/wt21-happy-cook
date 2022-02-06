import numpy as np
import pandas as pd
def difficulty_filter(difficulty):
    
    if difficulty == 'Easy':
        results=data[data['Difficulty']=='Easy']
    elif difficulty == 'Medium':    
        results=data[data['Difficulty']=='Medium']
    elif difficulty == 'Difficult':  
        results=data[data['Difficulty']=='Difficult']
    else:
        results=None
       
    return results
