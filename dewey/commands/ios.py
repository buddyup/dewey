import subprocess
from clint.textui import puts, indent, colored

from .base import DeweyCommand
from dewey.util import suppress_stdout_stderr



class Command(DeweyCommand):

    def pre_default(self, *args, **kwargs):
        pass

    def run_command(self, *args, **kwargs):
        print("Building for iOS...")
        subprocess.call("ionic run ios", cwd="app/native/ionic", shell=True)

    def post_default(self, *args, **kwargs):
        pass
