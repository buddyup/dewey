import pickle

from clint import resources

VALID_PLATFORMS = ["Windows", "MacOSX", "Linux"]


class DeweyCommand(object):

    def __init__(self):
        resources.init('GreenKahuna', 'dewey')
        brain_pickle = resources.user.read('config.py')
        self.brain = pickle.load(brain_pickle)

    def save(self):
        resources.user.read('config.py', pickle.dump(self.brain))

    def set_platform(self, platform):
        assert platform in VALID_PLATFORMS
        self.platform = platform

    def run_pre(self, *args, **kwargs):
        if not self.platform:
            raise OSError("echo 'Dewey doesn't know your operating system. Sorry!'")
        if self.platform == "Windows":
            try:
                ret = self.pre_windows(*args, **kwargs)
                if ret:
                    return ret
            except:
                pass
            return ""
        elif self.platform == "MacOSX":
            try:
                ret = self.pre_macosx(*args, **kwargs)
                if ret:
                    return ret
            except:
                pass
            return ""
        elif self.platform == "Linux":
            try:
                ret = self.pre_unix(*args, **kwargs)
                if ret:
                    return ret
            except:
                pass
            return ""
        else:
            raise OSError("echo 'Dewey doesn't know how to run pre for %s'" % self.platform)

    def pre_default(self, *args, **kwargs):
        raise NotImplementedError("Pre-command not written!")

    def pre_windows(self, *args, **kwargs):
        """Returns a string to execute on windows"""
        return self.pre_all(self, *args, **kwargs)

    def pre_macosx(self, *args, **kwargs):
        """Returns a string to execute on Mac OS X"""
        return self.pre_all(self, *args, **kwargs)

    def pre_unix(self, *args, **kwargs):
        """Returns a string to execute on unix"""
        return self.pre_all(self, *args, **kwargs)

    def run_command(self, *args, **kwargs):
        """Runs the body of the command (should not have current shell side effects.)"""
        pass

    def run_post(self, *args, **kwargs):
        if not self.platform:
            raise OSError("echo 'Dewey doesn't know your operating system. Sorry!'")
        if self.platform == "Windows":
            try:
                ret = self.post_windows(*args, **kwargs)
                if ret:
                    return ret
            except:
                pass
            return ""
        elif self.platform == "MacOSX":
            try:
                ret = self.post_macosx(*args, **kwargs)
                if ret:
                    return ret
            except:
                pass
            return ""
        elif self.platform == "Linux":
            try:
                ret = self.post_unix(*args, **kwargs)
                if ret:
                    return ret
            except:
                pass
            return ""
        else:
            raise OSError("echo 'Dewey doesn't know how to run post for %s'" % self.platform)

    def post_default(self, *args, **kwargs):
        raise NotImplementedError("Post-command not written!")

    def post_windows(self, *args, **kwargs):
        """Returns a string to execute on windows"""
        return self.post_all(self, *args, **kwargs)

    def post_macosx(self, *args, **kwargs):
        """Returns a string to execute on Mac OS X"""
        return self.post_all(self, *args, **kwargs)

    def post_unix(self, *args, **kwargs):
        """Returns a string to execute on unix"""
        return self.post_all(self, *args, **kwargs)