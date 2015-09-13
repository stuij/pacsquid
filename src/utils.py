def swap_chunks(array, size):
    for i in xrange(0, len(array), size):
        array[i: i + size] = array[i: i + size][::-1]

def swap_byte_order(array, byte_len):
    if(sys.byteorder == 'little'):
        swap_chunks(array, byte_len)
    
def ntohl(array):
    """In-place swap of 4 bytes from network byte-order to host byte-order."""
    swap_byte_order(array, 4)

def htonl(array):
    """In-place swap of 4 bytes from host byte-order to network byte-order."""
    swap_byte_order(array, 4)
