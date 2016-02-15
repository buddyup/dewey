from .base import DeweyCommand


class Command(DeweyCommand):

    def pre_default(self, *args, **kwargs):
        pass

    def run_command(self, *args, **kwargs):
        print("pip install git+https://git@github.com/buddyup/dewey.git#egg=dewey --upgrade")

    def post_default(self, *args, **kwargs):
        pass
