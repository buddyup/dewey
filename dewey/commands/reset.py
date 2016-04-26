import os
import subprocess
from clint.textui import puts, indent, colored

from .base import DeweyCommand
from dewey.util import suppress_stdout_stderr



class Command(DeweyCommand):

    def print_section(self, message):
        print("=" * (len(message) + 4))
        print("  %s  " % message)
        print("=" * (len(message) + 4))


    def pre_default(self, *args, **kwargs):
        pass

    def run_command(self, *args, **kwargs):
        print("Resetting libraries and native components")

        self.print_section("Updating global libs")
        subprocess.call("npm install -g ionic", shell=True)

        self.print_section("Clearing NPM and Bower")
        subprocess.call("rm -rf node_modules", cwd="app", shell=True)
        subprocess.call("rm -rf bower_components", cwd="app", shell=True)
        subprocess.call("npm cache clean", cwd="app", shell=True)

        self.print_section("Installing NPM Libraries")
        subprocess.call("npm install", cwd="app", shell=True)

        self.print_section("Installing Bower Libraries")
        subprocess.call("bower install", cwd="app", shell=True)

        self.print_section("Backing up postactivate")
        if not os.path.isfile("postactivate"):
            subprocess.call("cp ~/.virtualenvs/buddyup-core/bin/postactivate postactivate", shell=True)

        self.print_section("Clearing virtualenv")
        subprocess.call("rmvirtualenv buddyup-core", shell=True)
        subprocess.call("mkvirtualenv buddyup-core -p `which python3`", shell=True)

        self.print_section("Setting up postactivate")
        subprocess.call("rm ~/.virtualenvs/buddyup-core/bin/postactivate", shell=True)
        subprocess.call("ln -s postactivate ~/.virtualenvs/buddyup-core/bin/postactivate", shell=True)

        self.print_section("Installing Python Libraries")
        subprocess.call("workon buddyup-core; pip install requirements.txt", shell=True)

        self.print_section("Resetting Ionic App")
        subprocess.call("ionic state reset", cwd="app/native/ionic", shell=True)

        self.print_section("Rebuilding Ionic Splash Resources")
        subprocess.call("ionic resources", cwd="app/native/ionic", shell=True)
        print("Reset complete.")

    def post_default(self, *args, **kwargs):
        return "workon buddyup-core"
