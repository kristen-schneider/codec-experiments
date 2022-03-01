import numpy as np
import compress_numpy

def compress_blocks(blocks, data_type, codec):
    serialized_block = b''

    block_bitstring = b''

    # compress one column at a time
    for block_i in range(len(blocks)):
        # current column info
        curr_block = blocks[block_i]
        curr_compressed_block = compress_numpy.compress_bitstring(curr_block, codec, data_type)
        block_bitstring += curr_compressed_block

    return block_bitstring
