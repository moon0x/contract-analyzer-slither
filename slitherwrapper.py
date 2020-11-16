import os
import signal
import subprocess
import sys
from subprocess import Popen, PIPE, STDOUT

def get_slither_result(address):
    p = subprocess.Popen(['slither', address], stdout=PIPE, stderr=STDOUT)
    with p.stdout:
        for line in iter(p.stdout.readline, b''):
            print(line)
    p.wait()

get_slither_result(sys.argv[1])
