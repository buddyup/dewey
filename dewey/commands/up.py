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
        ps = subprocess.Popen(
            "npm run watch",
            close_fds=True, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        while ps.poll() is None:
            out = ps.stdout.read(1)
            sys.stdout.write(out)
            sys.stdout.flush()
            if "bundle is now VALID" in out:
                subprocess.call("open http://localhost:8080", shell=True,)

    def post_default(self, *args, **kwargs):
        pass
