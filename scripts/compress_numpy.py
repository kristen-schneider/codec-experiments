from pyfastpfor import *
import fpzip
import zfpy
import pyzfp
import sys
import numpy as np


def compress_numpy_array(current_block, codec, data_type):
    """
    compress a serialized bitstring using specified compression method

    INPUT
        compression_method: e.g. gzip, zlib, etc...
        s_bitstring = serialized bitstring from the serialize_data method in serialize_body.py

    OUTPUT
        c_bitstring = compressed bitstring

    """
    # pyFASTPFOR
    if codec in getCodecList():
        compressed_numpy_array = pyfast_compress(current_block, codec)
        compressed_bitstring = compressed_numpy_array.tobytes(order='C')

    # FPZIP
    elif codec == 'fpzip':
        compressed_bitstring = fpzip_compress(current_block)

    # ZFPY
    elif codec == 'zfpy':
        compressed_bitstring = zfpy_compress(current_block, data_type)

    # PYZFP
    elif codec == 'pyzfp':
        compressed_bitstring = pyzfp_compress(current_block, data_type)
    else: return None
    return compressed_bitstring

def pyfast_compress(current_block, codec):
    """
    compresses a single column of data using pyfastpfor codecs
    INPUT
        typed_column = column as proper type (list of ints, rather than strings)
        codec = method of compression for given column (one of the 33 codecs)

    OUTPUT
        compressed_column = compressed data
    """

    # convert input array to numpy array
    numpy_array = np.array(current_block, dtype=np.uint32, order='C')
    np_arr_size = numpy_array.size
    buffer_size = 3 * 32

    # allocate space for compressed data
    comp_arr = np.zeros(np_arr_size + buffer_size, dtype=np.uint32, order='C')

    # get codec method from pyfastpfor and use it for compression
    codec_method = getCodec(codec)
    comp_arr_size = codec_method.encodeArray(numpy_array, np_arr_size, comp_arr, len(comp_arr))

    return comp_arr[0:comp_arr_size]

def fpzip_compress(current_block):
    """
    compresses floats with fpzip codec.
    """
    # converts all data to floats.
    numpy_array = np.array(current_block, dtype=np.float32, order='C')
    try:
        compressed_bitstring = fpzip.compress(numpy_array, precision=0, order='C')
    except fpzip.FpzipWriteError:
        print('try a bigger block size')
        # replace problem value
        #for n in range(len(numpy_array)):
        #    if np.isnan(numpy_array[n]):
        #        numpy_array[n] = numpy_array[n]
        #numpy_array = np.multiply(numpy_array,1)
        #try:
        #    compressed_bitstring = fpzip.compress(numpy_array, precision=0, order='C')
        #except fpzip.FpzipWriteError:
        #    print(numpy_array)
    return compressed_bitstring

def zfpy_compress(current_block, data_type):
    """
    compresses floats and integers with fpzip codec.
    """
    # converts all data to floats (can take in integers, but will convert).
    if data_type == 1:
        numpy_array = np.array(current_block, dtype=np.uintc, order='C')
    elif data_type == 2:
        numpy_array = np.array(current_block, dtype=np.float32, order='C')

    compressed_bitstring = zfpy.compress_numpy(numpy_array)
    return compressed_bitstring

def pyzfp_compress(current_block, data_type):
    """
    """
    if data_type == 1:
        numpy_array = np.array(current_block, dtype=np.uint32, order='C')
    elif data_type == 2:
        numpy_array = np.array(current_block, dtype=np.float32, order='C')
    compressed_bitstring = pyzfp.compress(numpy_array, precision=100, parallel=True)
    return compressed_bitstring

