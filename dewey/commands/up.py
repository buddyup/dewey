import subprocess
from clint.textui import puts, indent, colored

from .base import DeweyCommand
from dewey.util import suppress_stdout_stderr



class Command(DeweyCommand):

    def pre_default(self, *args, **kwargs):
        # return "npm run watch"
        pass

    def run_command(self, *args, **kwargs):
        output = subprocess.call("open http://localhost:8080", shell=True,)
        output = subprocess.call("npm run watch", shell=True,)

    def post_default(self, *args, **kwargs):
        pass
