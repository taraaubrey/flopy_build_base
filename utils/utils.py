
import yaml
from skimage import io, morphology
import numpy as np
from scipy import ndimage
from gridit import Grid
import rasterio as rio



def save_raster(ras, ras_out, ras_meta):
    with rio.open(ras_out, 'w', **ras_meta) as m:
        m.write(ras)
        m.close()