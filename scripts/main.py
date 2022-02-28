import sys
import generate_blocks
import compress_blocks

data_file = sys.argv[1]
block_size = int(sys.argv[2])
data_type = int(sys.argv[3])
codec = sys.argv[4]

def main():
    if data_type == 1:
        print("\tIntegers...")
        blocks = generate_blocks.make_blocks(data_file, data_type, block_size)
        compressed_block = compress_blocks.compress_blocks(blocks, data_type, codec)
        print("\t", sys.getsizeof(compressed_block))
    elif data_type == 2:
        print("\tFloats...")
        blocks = generate_blocks.make_blocks(data_file, data_type, block_size)
        compressed_block = compress_blocks.compress_blocks(blocks, data_type, codec)
        print("\t", sys.getsizeof(compressed_block))
    elif data_type == 3:
        print("\tStrings...")
        blocks = generate_blocks.make_blocks(data_file, data_type, block_size)
        compressed_block = compress_blocks.compress_blocks(blocks, data_type, codec)
        print("\t", sys.getsizeof(compressed_block))
    else:
        print('This data type is not supported. RIP.\n')
        return -1

if __name__ == '__main__':
    main()