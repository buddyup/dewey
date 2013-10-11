from .base import DeweyCommand

class Command(DeweyCommand):

    def pre_windows(self, *args, **kwargs):
        pass

    def pre_macosx(self, *args, **kwargs):
        pass

    def pre_unix(self, *args, **kwargs):
        pass

    def run_command(self, *args, **kwargs):
        print "Oh, hello."

    def post_windows(self, *args, **kwargs):
        pass

    def post_macosx(self, *args, **kwargs):
        pass

    def post_unix(self, *args, **kwargs):
        pass
