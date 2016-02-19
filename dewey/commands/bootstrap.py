import subprocess
from clint.textui import puts, indent, colored

from .base import DeweyCommand
from dewey.util import suppress_stdout_stderr


class Command(DeweyCommand):

    def pre_default(self, *args, **kwargs):
        return ""
        pass

    def run_command(self, *args, **kwargs):
        # # Base OSX Dev
        # output = subprocess.check_output("docker-osx-dev", shell=True, )

        # Dev DNS
        output = subprocess.check_output("docker run -d --name devdns -p 53:53/udp -v /var/run/docker.sock:/var/run/docker.sock ruudud/devdns --restart always", shell=True, )

        # Old image cleanup
        output = subprocess.check_output("docker run -d --name cleanup --restart always -v /var/run/docker.sock:/var/run/docker.sock:rw -v /var/lib/docker:/var/lib/docker:rw meltwater/docker-cleanup:latest ", shell=True, )

        # Get the latest boot2docker
        output = subprocess.check_output("docker-machine upgrade default", shell=True, )

        print("Ready for development")

    def post_default(self, *args, **kwargs):
        return "docker-osx-dev -e .git -e bower_components -e node_modules -e source"