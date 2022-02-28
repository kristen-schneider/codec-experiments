import sys

def make_blocks(column_file, data_type, block_size):
    if data_type == 1:
        all_blocks = int_blocks(column_file, block_size)
    elif data_type == 2:
        all_blocks = float_blocks(column_file, block_size)
    elif data_type == 3:
        all_blocks = string_blocks(column_file, block_size)
    else:
        print('invalid data type.')
        return -1

    return all_blocks


def int_blocks(column_file, block_size):
    all_blocks = []
    i = 0

    f = open(column_file, 'r')
    single_block = []
    for row in f:
        if i < block_size:
            try:
                single_block.append(int(row))
            except ValueError:
                if row == 'X': single_block.apppend(23)
                if row == 'Y': single_block.append(24)
                else: print(row)
            i += 1
        elif i == block_size:
            all_blocks.append(single_block)
            single_block = []
            i = 0
        # last block
    if len(single_block) > 0:
        all_blocks.append(single_block)

    f.close()
    return all_blocks

def float_blocks(column_file, block_size):
    all_blocks = []
    i = 0

    f = open(column_file, 'r')
    single_block = []
    for row in f:
        if i < block_size:
            single_block.append(float(row))
            i += 1
        elif i == block_size:
            all_blocks.append(single_block)
            single_block = []
            i = 0
        # last block
    if len(single_block) > 0:
        all_blocks.append(single_block)

    f.close()
    return all_blocks

def string_blocks(column_file, block_size):
    all_blocks = []
    i = 0

    f = open(column_file, 'r')
    single_block = []
    for row in f:
        if i < block_size:
            single_block.append(str(row))
            i += 1
        elif i == block_size:
            all_blocks.append(single_block)
            single_block = []
            i = 0
        # last block
    if len(single_block) > 0:
        all_blocks.append(single_block)

    f.close()
    return all_blocks
