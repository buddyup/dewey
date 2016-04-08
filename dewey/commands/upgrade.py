import subprocess
from .base import DeweyCommand
from dewey.util import suppress_stdout_stderr

class Command(DeweyCommand):

    def pre_default(self, *args, **kwargs):
        pass

    def run_command(self, *args, **kwargs):
        print "Upgrading dewey...",
        with suppress_stdout_stderr():
            try:
                output = subprocess.check_output("pip install git+https://git@github.com/buddyup/dewey.git#egg=dewey --upgrade", shell=True, )
                print(" complete.")
            except subprocess.CalledProcessError as grepexc:                                                                                                   
                print("problem!\nError upgrading dewey. \n%s" % (grepexc.output,))


    def post_default(self, *args, **kwargs):
        pass
