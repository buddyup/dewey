from .base import DeweyCommand

class Command(DeweyCommand):

    def pre_default(self, *args, **kwargs):
        # return "cd ~/buddyup/oliver"
        return "workon buddyup-core"

    def run_command(self, *args, **kwargs):
        pass

    def post_default(self, *args, **kwargs):
        return "cd ~/buddyup/core"
