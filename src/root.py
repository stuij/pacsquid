# Text blatently stolen from Luke Gorrie's Common Lisp root stuff in Slitch,
# slightly adapted for Python of course:
#
# This package implements a convenient security loophole: it allows
# you to become root temporarily, whenever you please.
#
# WARNING: Only use this package if you understand how it works,
# and/or don't mind users of your machine becoming root at will! To
# understand how it works, refer to Stevens' _Advanced Programming in
# the Unix Environment_, or ask your local Unix guru.
#
# To setup:
#
#
#   Add the following line to your init file:
#     import root
#     root.condescend()
#
#   Make your 'python' process setuid-root:
#     which python # as the right user for your virtual environmnet
#     sudo chown root <python path>
#     sudo chmod u+s <python path>
#
# Now your program will start as root, but quickly switch to your
# real user. Whenever you want to run some code as root, you need
# only write:
#  with root():
#      ...naughty code...
#
# You can test by writing:
# print os.geteuid()
# with root.as_root():
#     print os.geteuid()
#
# which should return:
# <your-real-uid> 
# 0

import os
import sys

# root
def condescend():
    os.setreuid(0, os.getuid())

class as_root:
    def __enter__(self):
        self.old_euid = os.geteuid()
        os.setreuid(0, 0)
    
    def __exit__(self, type, value, traceback):
        os.setreuid(0, self.old_euid)
