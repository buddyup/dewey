VALID_PLATFORMS = ["Windows", "MacOSX", "Linux"]

class DeweyCommand(object):

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

    def pre_windows(self, *args, **kwargs):
        """Returns a string to execute on windows"""
        pass

    def pre_macosx(self, *args, **kwargs):
        """Returns a string to execute on Mac OS X"""
        pass

    def pre_unix(self, *args, **kwargs):
        """Returns a string to execute on unix"""
        pass

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

    def post_windows(self, *args, **kwargs):
        """Returns a string to execute on windows"""
        pass

    def post_macosx(self, *args, **kwargs):
        """Returns a string to execute on Mac OS X"""
        pass

    def post_unix(self, *args, **kwargs):
        """Returns a string to execute on unix"""
        pass
