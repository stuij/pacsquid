import fcntl
import os
import root
import struct
import subprocess

root.condescend()

# ping server
TUNSETIFF = 0x400454ca
TUNSETOWNER = TUNSETIFF + 2
IFF_TUN = 0x0001
IFF_TAP = 0x0002
IFF_NO_PI = 0x1000

TUNMODE = IFF_TUN

def ping_server():
    with open('/dev/net/tun', 'r+b') as f:
        ifs = fcntl.ioctl(f, TUNSETIFF, 
                          struct.pack("16sH", "tun0", TUNMODE | IFF_NO_PI))
        # Optionally, we want it be accessed by the normal user.
        # fcntl.ioctl(tun, TUNSETOWNER, 1000)

        # Bring it up and assign addresses.
        subprocess.check_call('ifconfig tun0 192.168.125.3 pointopoint '
                              '192.168.125.4 up', shell=True)
    
        while True:
            packet = bytearray(os.read(f.fileno(), 1500))
            packet[12:16], packet[16:20] = packet[16:20], packet[12:16]    
            os.write(f.fileno(), ''.join(map(chr, packet)))

def run_ping_server():
    with root.as_root():
        ping_server()
