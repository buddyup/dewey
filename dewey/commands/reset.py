import subprocess
from clint.textui import puts, indent, colored

from .base import DeweyCommand
from dewey.util import suppress_stdout_stderr



class Command(DeweyCommand):

    def pre_default(self, *args, **kwargs):
        pass

    def run_command(self, *args, **kwargs):
        subprocess.call("npm install", cwd="app", shell=True)
        subprocess.call("bower install", cwd="app", shell=True)
        subprocess.call("ionic state reset", cwd="app/native/ionic", shell=True)
        subprocess.call("ionic resources", cwd="app/native/ionic", shell=True)

    def post_default(self, *args, **kwargs):
        pass
