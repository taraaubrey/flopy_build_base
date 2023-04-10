# local
import numpy as np
from gridit import Grid
from skimage import io, morphology
from scipy import ndimage
import os

from utils import utils


# removes boundary single pixels
def remove_pixels(grid, matrix):
    return morphology.binary_closing(grid, matrix)

# fills single pixels at boundary
def fill_pixels(
        grid,
        matrix,
        min_size=1):
    # try and fill with binary opening
    con1 = morphology.binary_opening(grid, matrix)
    diff = np.subtract(grid.astype(np.int16), con1.astype(np.int16))

    # label the added sections
    labels, num_labels = ndimage.label(diff)

    # Find the unique labels and their counts
    unique_labels, counts = np.unique(labels, return_counts=True)

    # Filter out components with only min size pixel
    for label, count in zip(unique_labels, counts):
        if count != min_size:
            diff[labels == label] = False
    
    return grid - diff

# creates and saves a new boundary file
def new_boundary(ws_data,
                 run_dir,
                 remove_matrix = np.ones((2,2)),
                 fill_matrix = np.ones((2,2)),
                 min_size=1):
    
    res = ws_data['base']['dx']
    grid_fn = ws_data['raster_inputs']['surf_idomain']['infile']
    
    grid = Grid.from_vector(grid_fn, res)
    arr_raw = grid.mask_from_vector(grid_fn)
    
    # boundary operations
    arr_chop = remove_pixels(arr_raw, remove_matrix)
    idomain = fill_pixels(arr_chop, fill_matrix, min_size)

    # raster meta data
    kwds = {
        "driver": 'gtiff',
        "width": idomain.shape[1],
        "height": idomain.shape[0],
        "crs": grid.projection,
        "transform": grid.transform,
        "NBITS": "2",
        "dtype": idomain.dtype,
        "nodata": -9999
    }

    # save as a raster
    ras_fn = os.path.join(run_dir,'idomain.tif')
    grid.write_raster(idomain, ras_fn)

    # import new grid from raster
    new_grid = Grid.from_raster(ras_fn)

    return new_grid, idomain