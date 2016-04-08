import subprocess
from .base import DeweyCommand


class Command(DeweyCommand):

    def pre_default(self, *args, **kwargs):
        return "echo 'Upgrading dewey...'"

    def run_command(self, *args, **kwargs):
        try:
            output = subprocess.check_output("pip install git+https://git@github.com/buddyup/dewey.git#egg=dewey --upgrade", shell=True, )
        except subprocess.CalledProcessError as grepexc:                                                                                                   
            print("Error upgrading dewey. \n%s" % (grepexc.output,))

    def post_default(self, *args, **kwargs):
        pass
