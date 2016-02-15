from .base import DeweyCommand


class Command(DeweyCommand):

    def pre_default(self, *args, **kwargs):
        return "pip install git+https://git@github.com/buddyup/dewey.git#egg=dewey --upgrade"

    def run_command(self, *args, **kwargs):
        print("Upgraded.")

    def post_default(self, *args, **kwargs):
        pass
