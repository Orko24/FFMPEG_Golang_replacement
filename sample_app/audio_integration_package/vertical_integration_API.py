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

# class file_address_generator(object):

#     def __init__(self, file):
#         self.file = file
    


class file_generator(object):

    def __init__(self,directory):

        self.directory = directory

    def files(self):

        file_list = os.listdir(self.directory)
        return file_list
    
    def file_list_addresses(self):

        file_list = self.files()

        full_directory = list(map(lambda x: os.path.join(self.directory, x), file_list))

        return full_directory

class MP3_merge_software_activation(object):

    def __init__(self):

        self.MP3CAT_command = "go install github.com/dmulholl/mp3cat@latest"
        self.MP3WRAP_command = ""



        

        
        

    


