import subprocess
from clint.textui import puts, indent, colored

from .base import DeweyCommand
from dewey.util import suppress_stdout_stderr


class Command(DeweyCommand):

    def pre_default(self, *args, **kwargs):
        return "bash <(curl -s https://raw.githubusercontent.com/buddyup/dev-setup/master/setup.sh)"

    def run_command(self, *args, **kwargs):
        pass

    def post_default(self, *args, **kwargs):
        pass
