# copy_funcs
A python script for extracting specific functions and classes from one .py file and saving them in a new one. Useful when there are certain parts of a private repository that you'd like to share, without sharing the rest. 

Example usage:
to_public("private_module.py", ["useful_function", "useful_class"], "../public_repo/public_script.py")
