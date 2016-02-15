from .base import DeweyCommand


class Command(DeweyCommand):

    def pre_default(self, *args, **kwargs):
        pass

    def run_command(self, *args, **kwargs):
        return "docker-compose --project-name bu up"

    def post_default(self, *args, **kwargs):
        pass
