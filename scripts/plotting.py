import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import random
import numpy as np

import sys

io_file = sys.argv[1]
col_num = 1

def main():
    col_data = group_by_column(col_num)
    plot_by_column(col_data, col_num)

def plot_by_column(col_data, col_num):
    plt.figure(figsize=(20,10))
    color_dict = {'bz2':'red','gzip':'gold', 'zlib':'forestgreen',
              'fastpfor128':'dodgerblue', 'fpzip':'hotpink',
              'zfpy':'black','pyzfp':'saddlebrown'}
    codecs = [d[0] for d in col_data]
    data_types = [d[1] for d in col_data]
    noise = 0.1 * np.random.randn(len(data_types))

    sizes = [d[2] for d in col_data]
    colors = [color_dict[c] for c in codecs]

    plt.scatter(data_types+noise, sizes, c=colors, alpha=0.8, linewidths=20)
    plt.title("COLUMN: " + str(col_num) + " (chromosomes)", fontsize=40)
    plt.xlabel("Data Type", fontsize=20)
    plt.xticks(np.array([1,2,3]), ['integer','float','string'], fontsize=20)
    plt.xlim([0.5, 3.5])
    plt.ylabel("Compressed Size (bytes)", fontsize=20)
    plt.ylim([100000, 200000])
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




    # codec_dict = dict.fromkeys(codecs)
    # for d in col_data:
    #     codec = d[0]
    #     data_type = d[1]
    #     size = d[2]
    #     try: codec_dict[codec].append([data_type,size])




def group_by_column(col_num):
    col_data = []
    f = open(io_file, 'r')
    header = ''
    for line in f:
        if header == '': header = line
        else:
            curr_exp = []
            A = line.strip().split(',')
            col = int(A[0])
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