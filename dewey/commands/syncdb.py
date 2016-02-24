import subprocess
from clint.textui import puts, indent, colored

from .base import DeweyCommand
from dewey.util import suppress_stdout_stderr



class Command(DeweyCommand):

    def pre_default(self, *args, **kwargs):
        return 'docker-compose --project-name bu run db bash -c "createdb -h db -U postgres buddyup"'

    def run_command(self, *args, **kwargs):
        pass

    def post_default(self, *args, **kwargs):
        return 'docker-compose --project-name bu run web bash -c "cd api; python3 manage.py migrate"'
