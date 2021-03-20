#!/usr/bin/python3
# funziona !
# cmd: python3 "/home/tubbadu/code/GitHub/CustomBindKeys/CustomBindKeys.py" §

import pyperclip
import sys
import subprocess
ch = sys.argv[1]

pastePath = '/home/tubbadu/code/GitHub/CustomBindKeys/CustomBindKeys_paste.py'

def spawn_program_and_die(program, exit_code=0): #copiata lol
	subprocess.Popen(program)
	sys.exit(exit_code)

pyperclip.copy(ch)
spawn_program_and_die(['python3', pastePath, ch])

