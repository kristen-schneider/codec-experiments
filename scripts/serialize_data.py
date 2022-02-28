import struct

def serialize_list(in_list, compression_data_type):
    s_bitstring = b''
    s_value = None
     
    # serialize a list of data depending on its data type
    if compression_data_type == 1:
        s_value = serialize_int_data(in_list)
    elif compression_data_type == 2: 
        s_value = serialize_float_data(in_list)
    elif compression_data_type == 3 or compression_data_type == 4:
        s_value = serialize_string_data(in_list)
    else: print('cannot detect data_type')
    
    try:
        s_bitstring += s_value
    except TypeError:
        print('cannot concat s_value to bitstring')
   
    return s_bitstring


def serialize_int_data(in_list):
    s_ints = b''
    for i in in_list:
        try:
            s_value = i.to_bytes(4, byteorder='big', signed=True)
        # numpy data is not integer
        except AttributeError: 
            print('Attribute error, likely numpy data input.')
            s_value = i.tobytes(order='C')
        except OverflowError:
            print('Overflow error.')
            return -1
        s_ints += s_value
    return s_ints


def serialize_float_data(in_list):
    s_floats = b''
    for i in in_list:
        s_value = bytearray(struct.pack("f", i))
        s_floats += s_value
    return s_floats


def serialize_string_data(in_list):
    s_strings = b''
    for i in in_list:
        try:
            s_value = bytes(i, 'utf-8')
            if len(s_value) > 1:
                s_value = b'\0'+s_value+b'\0'
        except TypeError: return -1
        s_strings += s_value
    return s_strings
