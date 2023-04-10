#from config.main_setup import ws_data
#sys.path.append('../config')
#from gridit import Grid
from gridit import Grid
import numpy as np
import os

# local
from utils import utils
from preprocessing import boundary
#from skimage import io, morphology
#import numpy as np
"""

"""

# PART 1 - class define
class grids:

    def __init__(self, model_data, run_dir, data_dir):
        self.model_data = model_data
        self.dx = model_data['base']['dx']
        self.dy = model_data['base']['dy']
        self.res = self.dx
        
        #gridit grid object & idomain
        self.grid, self.idomain = boundary.new_boundary(model_data, run_dir)

        top_fn = os.path.join(data_dir, model_data['raster_inputs']['top']['infile'])
        self.top = self.grid.array_from_raster(top_fn).data



        # returns arrays for various inputs
        #self.k33 = self.k33(self.ws_data['raster_inputs']['surf_k'], self.res)


    class k33:
        def __init__(self, data, res):
            self.data = data
            self.in_file = self.data['infile']
            #idomain = 
            #min_val = 
            #drop_cells = 
            #fill_cells = 
        
        def arr(self):
            #arr = grid.mask_from_vector(domain_fn)
            None
            
            #return arr


    

def build_grids(ws_data, run_dir, data_dir):

    return grids(ws_data['model'], run_dir, data_dir)
