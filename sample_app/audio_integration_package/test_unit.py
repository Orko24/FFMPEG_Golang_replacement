from vertical_integration_API import *

def list_printer(lst):

    for x in lst:
        print("\n")
        print(x)

    return


directory_path = "C:\\Users\\Owner\\Desktop\\adamas_local_copy\\adamas_cloud\\mid_file_processing_test"

files = file_generator(directory_path).file_list_addresses()


list_printer(files)
