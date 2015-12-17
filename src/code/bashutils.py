import subprocess

def line_count(inputFile):
    bashcommand="wc -l "+inputFile
    output = subprocess.check_output(['bash','-c', bashcommand])
    print output.split(' ')[0]

def egrep(inputFile,pattern):
    print('hello!')

def execute(inputCommand):
    bashcommand=inputCommand
    print bashcommand
    output = subprocess.check_output(['bash','-c', bashcommand])
    return output