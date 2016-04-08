import subprocess
from clint.textui import puts, indent, colored

from .base import DeweyCommand
from dewey.util import suppress_stdout_stderr



class Command(DeweyCommand):

    def pre_default(self, *args, **kwargs):
        pass

    def run_command(self, *args, **kwargs):
        output = subprocess.check_output("adb devices -l", shell=True, )
        if "device usb" not in output:
            print "No android device connected via USB or in Genymotion.  Stopping."
            self.run_android = False
        else:
            self.run_android = True


    def post_default(self, *args, **kwargs):
        if self.run_android:
            return "npm run android"