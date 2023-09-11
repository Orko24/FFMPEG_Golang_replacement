import subprocess
import os

class command_line_runner(object):

    def __init__(self, cmd):
        self.cmd = cmd

    def run(self):

        process = subprocess.Popen(self.cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)

        for line in process.stdout:
            print(line)

        return


# cmd_golang = "mp3cat merged_audio_1.mp3 merged_audio_2.mp3 merged_audio_3.mp3 -o joined_3.mp3"
# cmd_cpp = "mp3wrap joined_2.mp3 merged_audio_1.mp3 merged_audio_2.mp3 merged_audio_3.mp3"

# command_line_runner(cmd = cmd_golang).run()
# command_line_runner(cmd = cmd_cpp).run()

class file_generator(object):

    def __init__(self,directory):

        self.directory = directory

    


