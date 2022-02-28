import gzip
import zlib
import bz2
import sys


def compress_bitstring(serialized_bitstring, codec):
    """
    compress a serialized bitstring using specified compression method

    INPUT
        compression_method: e.g. gzip, zlib, etc...
        s_bitstring = serialized bitstring from the serialize_data method in serialize_body.py

    OUTPUT
        c_bitstring = compressed bitstring

    """

    # GZIP
    if codec == 'gzip':
        compressed_bitstring = gzip_compress(serialized_bitstring, 0) 
        header_size = 10

    # ZLIB
    elif codec == 'zlib':
        compressed_bitstring = zlib_compress(serialized_bitstring)
        header_size = 0

    # BZ2
    elif codec == 'bz2':
        compressed_bitstring = bz2_compress(serialized_bitstring)
        header_size = 4
    else: return None
    return compressed_bitstring[header_size:]

def gzip_compress(s_bitstring, time):
    '''
    uses python_scripts's gzip.compress to compress a serialized bitstring

    INPUT
        s_bitstring = serialized bitstring from the serialize_data method in serialize_body.py
        time = mtime argument for gzip.compress

    OUTPUT
        c_bitstring = compressed bitstring (using python_scripts's gzip.compress() function)

    '''

    compressed_bitstring = gzip.compress(s_bitstring, mtime=time)
    return compressed_bitstring


def zlib_compress(s_bitstring):
    '''
    uses python_scripts's zlib.compress to compress a serialized bitstring

    INPUT
        s_bitstring = serialized bitstring from the serialize_data method in serialize_body.py

    OUTPUT
        c_bitstring = compressed bitstring (using python_scripts's zlib.compress() function)

    '''

    compressed_bitstring = zlib.compress(s_bitstring)
    return compressed_bitstring


def bz2_compress(s_bitstring):
    '''
    uses python_scripts's zlib.compress to compress a serialized bitstring

    INPUT
        s_bitstring = serialized bitstring from the serialize_data method in serialize_body.py

    OUTPUT
        c_bitstring = compressed bitstring (using python_scripts's zlib.compress() function)

    '''

    compressed_bitstring = bz2.compress(s_bitstring)
    return compressed_bitstring

