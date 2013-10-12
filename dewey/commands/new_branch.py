from .base import DeweyCommand

class Command(DeweyCommand):

    def pre_default(self, *args, **kwargs):
        pass

    def run_command(self, *args, **kwargs):
        branch_name = kwargs["<branch_name>"]
        # Checkout master, check if it's behind, ask to pull
        # Start a new branch called feature/foo 
        #   (parse out feature/ if it's in the branch name)
        # Set remote origin
        # Push it to github
        pass

    def post_default(self, *args, **kwargs):
        # Check out branch
        pass
