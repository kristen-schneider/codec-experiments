import sys
import integers
import floats
import strings
import compress_gzip

data_file = sys.argv[1]
block_size = sys.argv[2]
data_type = sys.argv[3]
codec = sys.argv[4]

def main():
    if data_type == 1:
        print("Integers...")
        blocks = integers.make_blocks(data_file)
        for b in blocks: print(b)
    elif data_type == 2:
        blocks = floats.make_blocks(data_file)
    elif data_type == 3:
        blocks = strings.make_blocks(data_file)
    else:
        print('This data type is not supported. RIP.\n')
        return -1