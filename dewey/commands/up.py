import sys
import subprocess
from clint.textui import puts, indent, colored

from .base import DeweyCommand
from dewey.util import suppress_stdout_stderr



class Command(DeweyCommand):

    def pre_default(self, *args, **kwargs):
        # return "npm run watch"
        pass


    def run_command(self, *args, **kwargs):
        try:
            ps = subprocess.Popen(
                "gulp dev",
                close_fds=True, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )
            while ps.poll() is None:
                line = ps.stdout.readline()
                sys.stdout.write(line)
                sys.stdout.flush()
        except KeyboardInterrupt:
            print "\n\nShutting down."


    def run_command_oliver(self, *args, **kwargs):
        try:
            ps = subprocess.Popen(
                "npm run watch",
                close_fds=True, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )
            while ps.poll() is None:
                line = ps.stdout.readline()
                if "bundle is now VALID" in line:
                    print "Bundling done.  Launching browser."
                    subprocess.check_output("open http://localhost:8080", shell=True,)
                sys.stdout.write(line)
                sys.stdout.flush()
        except KeyboardInterrupt:
            print "\n\nShutting down."

    def post_default(self, *args, **kwargs):
        pass
