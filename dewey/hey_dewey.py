#! /usr/bin/env python
"""Dewey, our friendly CLI friend!

Usage:
  dewey workon <project_name>
  dewey (checkout | co) <branch_name>
  dewey (new-branch | nb) <branch_name>
  dewey hi

Options:
  -h --help     Show this screen.
  --version     Show version.

Hidden commands for scripts:
  --pre         Output the pre-command scripts for execution.
  --post        Output the post-command scripts for execution.

"""
import os
import sys
from docopt import docopt

from dewey import VERSION


class suppress_stdout_stderr(object):
    """
    Via http://stackoverflow.com/questions/11130156/suppress-stdout-stderr-print-from-python-functions
    A context manager for doing a "deep suppression" of stdout and stderr in
    Python, i.e. will suppress all print, even if the print originates in a
    compiled C/Fortran sub-function.
       This will not suppress raised exceptions, since exceptions are printed
    to stderr just before a script exits, and after the context manager has
    exited (at least, I think that is why it lets exceptions through).
    """
    def __init__(self):
        # Open a pair of null files
        self.null_fds = [os.open(os.devnull, os.O_RDWR) for x in range(2)]
        # Save the actual stdout (1) and stderr (2) file descriptors.
        self.save_fds = (os.dup(1), os.dup(2))

    def __enter__(self):
        # Assign the null pointers to stdout and stderr.
        os.dup2(self.null_fds[0], 1)
        os.dup2(self.null_fds[1], 2)

    def __exit__(self, *_):
        # Re-assign the real stdout/stderr back to (1) and (2)
        os.dup2(self.save_fds[0], 1)
        os.dup2(self.save_fds[1], 2)
        # Close the null files
        os.close(self.null_fds[0])
        os.close(self.null_fds[1])

def main():
    # Handle pre/post handlers
    run_pre = False
    run_post = False
    if "--pre" in sys.argv:
        run_pre = True
        sys.argv.remove("--pre")
    if "--post" in sys.argv:
        run_post = True
        sys.argv.remove("--post")

    # Platform detection
    platform = None
    if sys.platform == "win32":
        platform = "Windows"
    elif sys.platform == "darwin":
        platform = "MacOSX"
    elif sys.platform == "linux2":
        platform = "Linux"

    arguments = {}
    if run_pre or run_post:
        with suppress_stdout_stderr():
            try:
                arguments = docopt(__doc__, version='Dewey %s' % VERSION)
            except:
                pass
    else:
        arguments = docopt(__doc__, version='Dewey %s' % VERSION)
    
    for arg_name, value in arguments.iteritems():
        if value == True:
            arg_name = arg_name.replace("-", "_")
            try:
                command_module = __import__("dewey.commands.%s" % arg_name, fromlist=['Command']) 
                cmd = getattr(command_module, 'Command')()
                cmd.set_platform(platform)
                if run_pre:
                    print cmd.run_pre(**arguments)
                elif run_post:
                    print cmd.run_post(**arguments)
                else:
                    cmd.run_command(**arguments)
            except:
                print "Unable to find a command module for %s" % arg_name

if __name__ == '__main__':
    main()