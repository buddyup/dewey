import subprocess
from clint.textui import puts, indent, colored

from .base import DeweyCommand
from dewey.util import suppress_stdout_stderr



class Command(DeweyCommand):

    def pre_default(self, *args, **kwargs):
        pass

    def run_command(self, *args, **kwargs):
        subprocess.check_call("ionic state reset", cwd="app/native/ionic",
            shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def post_default(self, *args, **kwargs):
        pass
