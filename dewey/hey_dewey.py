#! /usr/bin/env python
"""Dewey, our friendly CLI friend!

Usage:
  dewey status
  dewey hi
  dewey --pre
  dewey --post

Options:
  -h --help     Show this screen.
  --version     Show version.
  --pre         Output the pre-command scripts.
  --post        Output the post-command scripts.

"""
from docopt import docopt
from dewey import VERSION

def main():
    arguments = docopt(__doc__, version='Dewey %s' % VERSION)

    # print(arguments)
    if arguments["hi"]:
        print "Oh, hello."

    if arguments["status"]:
        print "I'm fine, how are you?"

if __name__ == '__main__':
    main()