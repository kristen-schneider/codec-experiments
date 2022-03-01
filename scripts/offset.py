def int_blocks(column_file, block_size):
    print("OFFSET")

    all_blocks = []
    i = 0

    f = open(column_file, 'r')
    single_block = []
    for row in f:
        ROW = row.strip()
        if i < block_size:
            try:
                single_block.append(int(ROW))
            except ValueError:
                if ROW == 'X':
                    single_block.append(23)
                elif ROW == 'Y': single_block.append(24)
                elif ROW == 'NA': single_block.append(-1)
                elif ROW == 'true': single_block.append(1)
                elif ROW == 'false': single_block.append(0)
            i += 1
        elif i == block_size:
            ## OFFSET PART ##
            max_val = max(single_block)
            single_block = [(max_val-v) for v in single_block]

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
        ROW = row.strip()
        if i < block_size:
            try: single_block.append(float(ROW))
            except ValueError:
                if ROW == 'X': single_block.append(23.)
                elif ROW == 'Y': single_block.append(24.)
                elif ROW == 'NA': single_block.append(-10.)
                elif ROW == 'true': single_block.append(1.)
                elif ROW == 'false': single_block.append(0.)
            i += 1
        elif i == block_size:
            ## OFFSET PART ##
            max_val = max(single_block)
            single_block = [(max_val - v) for v in single_block]

            all_blocks.append(single_block)
            single_block = []
            i = 0
        # last block
    if len(single_block) > 0:
        all_blocks.append(single_block)

    f.close()
    return all_blocks