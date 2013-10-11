#! /usr/bin/env python
"""Dewey, our friendly CLI friend!

Usage:
  dewey status
  dewey hi

Options:
  -h --help     Show this screen.
  --version     Show version.

Hidden commands for scripts:
  --pre         Output the pre-command scripts for execution.
  --post        Output the post-command scripts for execution.

"""
import sys
from docopt import docopt

from dewey import VERSION


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

    arguments = docopt(__doc__, version='Dewey %s' % VERSION)

    
    for arg_name, value in arguments.iteritems():
        if value == True:
            try:
                command_module = __import__("dewey.commands.%s" % arg_name, fromlist=['Command']) 
                cmd = getattr(command_module, 'Command')()
                cmd.set_platform(platform)
                if run_pre:
                    cmd.run_pre(**arguments)
                elif run_post:
                    cmd.run_post(**arguments)
                else:
                    cmd.run_command(**arguments)
            except:
                print "Unable to find a command module for %s" % arg_name

if __name__ == '__main__':
    main()