#import config.main_setup
from config.main_setup import exe_name, ws_data, run_dir, data_dir
from preprocessing.grid_class import grids, build_grids

#testing
import matplotlib.pyplot as plt

grids = build_grids(ws_data, run_dir, data_dir)




#testing -----------
arr = grids.corr
arr2 = grids.arr
plt.imshow(arr2)
plt.imshow(arr - arr2)
grids.idomain.data
grids.idomain.arr()


def plot_diff(plot_arr):

    diff = np.subtract(arr.astype(np.int16), plot_arr.astype(np.int16))

    fig, ax = plt.subplots(1, 3, figsize=(10, 5))
    ax[0].imshow(arr, cmap='gray')
    ax[0].set_title('Original Image')
    ax[1].imshow(plot_arr, cmap='gray')
    ax[1].set_title('Test')
    ax[2].imshow(diff, cmap = 'gray')
    ax[2].set_title('Difference (Original - Test)')
    plt.show()