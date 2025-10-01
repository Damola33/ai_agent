import os
def get_files_info(working_dir, dir="."):
    full_path = os.path.join(working_dir, dir)
    if os.path.abspath(dir) != os.path.abspath(working_dir):
        return f'Error: Cannot list "{dir}" as it is outside the permitted woking directory'
    if not os.path.isdir(dir):
        return f'Error: "{dir}" is not a dirtectory'