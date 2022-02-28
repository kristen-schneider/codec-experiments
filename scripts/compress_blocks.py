import serialize_data
import compress

def compress_blocks(blocks, data_type, codec):
    serialized_block = b''

    block_bitstring = b''

    # compress one column at a time
    for block_i in range(len(blocks)):
        # current column info
        curr_block = blocks[block_i]
        curr_block_bitstring = serialize_data.serialize_list(curr_block, data_type)
        curr_compressed_block = compress.compress_bitstring(curr_block_bitstring, codec)
        block_bitstring += curr_compressed_block

    return block_bitstring
