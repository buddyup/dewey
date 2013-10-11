from .base import DeweyCommand

class Command(DeweyCommand):

    def pre_windows(self, *args, **kwargs):
        pass

    def pre_macosx(self, *args, **kwargs):
        return "workon %s" % kwargs["<project_name>"]

    def pre_unix(self, *args, **kwargs):
        return "workon %s" % kwargs["<project_name>"]

    def run_command(self, *args, **kwargs):
        pass

    def post_windows(self, *args, **kwargs):
        pass

    def post_macosx(self, *args, **kwargs):
        pass

    def post_unix(self, *args, **kwargs):
        pass
