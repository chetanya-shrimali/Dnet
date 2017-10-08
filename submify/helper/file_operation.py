import os


def file_rename(file_desc, name):
    """Function to chnage the filename
    to desired file name
    :par file_desc : File descriptor
    :par name : Name to which we change
    """
    if os.path.exists(file_desc):
        os.rename(file_desc, name)
