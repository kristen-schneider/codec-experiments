def make_block(column, block_size):
    single_block = []
    r = 0
    while(r < block_size):
        for r in column:
            single_block.append(r)

    return single_block




