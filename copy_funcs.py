import re

def to_public(private_file, blocks_to_copy, public_file):

    block_indices = {}
    blocks = {}
    previous_block = 0
    file_to_create = []

    with open(private_file, "r") as file:
        file_lines = file.read().split("\n")

    n_lines = len(file_lines)

    print("About to analyse a python file with %s lines" % n_lines)

    for i, line in enumerate(file_lines):
        # For the purpose of defining blocks of code, ignore whitespace, comments, and imports
        if len(line) == 0 or line.startswith("#"):
            ignore_line = True
        elif line.split(" ")[0] in ["from", "import"]:
            file_to_create.append(line)
            ignore_line = True
        else:
            ignore_line = False

        leading_tabs = (len(line) - len(line.lstrip(" "))) // 4

        # Identify the start of blocks, ie functions and classes and get their first and last lines
        if leading_tabs == 0 and not ignore_line:
            try:
                block_indices[block_name] = [previous_block, i]
            except UnboundLocalError:
                pass
            block_name = re.split(" |\(", line)[1]

            previous_block = i

    # For each identified block, obtain its contents from the indices stored
    for (block_name, indices) in block_indices.items():
        block_contents = "\n".join(file_lines[indices[0]: indices[1]])
        blocks[block_name] = block_contents

    # Turns input into a list if only one is passed in
    if type(blocks_to_copy) != list:
        blocks_to_copy = [blocks_to_copy]

    # Append the requested blocks to the file which will be written, with whitespace after imports
    file_to_create.append("")
    for block_name in blocks_to_copy:
        file_to_create.append(blocks[block_name])
        pass

    # Adds each separate entry in the file_to_create as a new line
    file_to_create = "\n".join(file_to_create)

    with open(public_file, "w+") as file:
        file.write(file_to_create)

    return

if __name__ == "__main__":
    
    # Example usage:
    #to_public("private_module.py", ["useful_function", "useful_class"], "../public_repo/public_script.py")
