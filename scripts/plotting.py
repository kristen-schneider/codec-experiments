import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import random
import numpy as np

import sys

io_file = sys.argv[1]
col_num1 = '2'
col_num2 = '2o'

def main():
    col_data1 = group_by_column(col_num1)
    col_data2 = group_by_column(col_num2)
    plot_by_column(col_data1, col_data2, col_num1)

def plot_by_column(col_data1, col_data2, col_num):
    plt.figure(figsize=(20,10))
    color_dict = {'bz2':'red','gzip':'gold', 'zlib':'forestgreen',
              'fastpfor128':'dodgerblue', 'fpzip':'hotpink',
              'zfpy':'black','pyzfp':'saddlebrown'}

    # NO FLAGS
    codecs1 = [d[0] for d in col_data1]
    data_types1 = [d[1] for d in col_data1]
    noise1 = 0.1 * np.random.randn(len(data_types1))

    sizes1 = [d[2] for d in col_data1]
    colors1 = [color_dict[c] for c in codecs1]

    # FLAGS
    codecs2 = [d[0] for d in col_data2]
    data_types2 = [d[1] for d in col_data2]
    noise2 = 0.1 * np.random.randn(len(data_types2))

    sizes2 = [d[2] for d in col_data2]
    colors2 = [color_dict[c] for c in codecs2]



    plt.scatter(data_types1+noise1, sizes1, c=colors1, alpha=0.8, s=500)
    plt.scatter(data_types2+noise2, sizes2, c=colors2, alpha=0.8, s=500, marker='X')

    plt.title("COLUMN: " + str(col_num) + " (positions)\nwith offset", fontsize=40)
    plt.xlabel("Data Type", fontsize=20)
    plt.xticks(np.array([1,2,3]), ['integer','float','string'], fontsize=20)
    plt.xlim([0.5, 3.5])
    plt.ylabel("Compressed Size (bytes)", fontsize=20)
    plt.ylim([0, 120000000])
    plt.yticks(fontsize=20)

    # Legend
    blue_patch = mpatches.Patch(color='red', label='bz2')
    green_patch = mpatches.Patch(color='gold', label='gzip')
    red_patch = mpatches.Patch(color='forestgreen', label='zlib')
    yellow_patch = mpatches.Patch(color='dodgerblue', label='fastpfor128')
    cyan_patch = mpatches.Patch(color='hotpink', label='fpzip')
    black_patch = mpatches.Patch(color='black', label='zfpy')
    magenta_patch = mpatches.Patch(color='saddlebrown', label='pyzfp')

    plt.legend(loc=[.95, .6], fontsize=20,
               handles=[blue_patch, green_patch, red_patch, yellow_patch, cyan_patch, black_patch, magenta_patch])

    for pos in ['right', 'top']:
        plt.gca().spines[pos].set_visible(False)

    plt.savefig("col"+str(col_num)+".png")




def group_by_column(col_num):
    col_data = []
    f = open(io_file, 'r')
    header = ''
    for line in f:
        if header == '': header = line
        else:
            curr_exp = []
            A = line.strip().split(',')
            col = A[0]
            codec = A[1]
            data_type = int(A[2])
            try:
                size = int(A[3])
            except ValueError:
                size = -1
            except IndexError:
                size = -1

            if col_num == col:
                curr_exp = [codec, data_type, size]
                col_data.append(curr_exp)

    return col_data



if __name__ == '__main__':
    main()