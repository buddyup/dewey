import sys
import subprocess
from clint.textui import puts, indent, colored

from .base import DeweyCommand
from dewey.util import suppress_stdout_stderr


class Command(DeweyCommand):

    def pre_default(self, *args, **kwargs):
        pass

    def run_command(self, *args, **kwargs):
        try:
            output = subprocess.check_output("adb devices -l", shell=True, )
            if "device usb" not in output:
                print "No android device connected via USB or in Genymotion.  "
            else:
                print "Device found.  Building...\n"
                subprocess.call("ionic run android", cwd="app/native/ionic", shell=True)
        except KeyboardInterrupt:
            print "\n\nShutting down."

    def post_default(self, *args, **kwargs):
        pass
