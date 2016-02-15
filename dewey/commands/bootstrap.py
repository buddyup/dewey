from .base import DeweyCommand


class Command(DeweyCommand):

    def pre_default(self, *args, **kwargs):
        pass

    def run_command(self, *args, **kwargs):
        # Base OSX Dev
        output = subprocess.check_output("docker-osx-dev", shell=True, )

        # Dev DNS
        output = subprocess.check_output("docker run -d --name devdns -p 53:53/udp -v /var/run/docker.sock:/var/run/docker.sock ruudud/devdns --restart always", shell=True, )

        # Old image cleanup
        output = subprocess.check_output("docker run -d --name cleanup -v /var/run/docker.sock:/var/run/docker.sock:rw -v /var/lib/docker:/var/lib/docker:rw meltwater/docker-cleanup:latest ", shell=True, )

        # Get the latest boot2docker
        output = subprocess.check_output("docker-machine upgrade default", shell=True, )

        return "docker-osx-dev -e .git -e bower_components -e node_modules -e source"

        # return "echo 'Ready for development'"

    def post_default(self, *args, **kwargs):
        pass
