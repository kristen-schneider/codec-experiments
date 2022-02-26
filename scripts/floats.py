import sys

column_file = sys.argv[1]
block_size = int(sys.argv[2])


def main():
    all_blocks = make_blocks(column_file)
    print(len(all_blocks))


def make_blocks(column_file):
    all_blocks = []
    i = 0

    f = open(column_file, 'r')
    for row in f:
        single_block = []
        if i < block_size:
            single_block.append(float(row))
            i += 1
        elif i == block_size:
            all_blocks.append(single_block)
            i = 0
        # last block
    if len(single_block) > 0:
        all_blocks.append(single_block)

    return all_blocks


if __name__ == "__main__":
    main()
