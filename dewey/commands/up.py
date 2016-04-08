import subprocess
from clint.textui import puts, indent, colored

from .base import DeweyCommand
from dewey.util import suppress_stdout_stderr



class Command(DeweyCommand):

    def pre_default(self, *args, **kwargs):
        return "npm run watch"

    def run_command(self, *args, **kwargs):
        pass

    def post_default(self, *args, **kwargs):
        pass
        # return "open http://localhost:8080"
