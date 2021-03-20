#!/usr/bin/python3
import pyperclip
import sys
import subprocess
ch = sys.argv[1]

pastePath = '/home/tubbadu/code/GitHub/CustomBindKeys/bind_paste.py'

def spawn_program_and_die(program, exit_code=0): #copiata lol
    """
    Start an external program and exit the script 
    with the specified return code.

    Takes the parameter program, which is a list 
    that corresponds to the argv of your command.
    """
    # Start the external program
    subprocess.Popen(program)
    # We have started the program, and can suspend this interpreter
    sys.exit(exit_code)

pyperclip.copy(ch)
spawn_program_and_die(['python3', pastePath, ch])