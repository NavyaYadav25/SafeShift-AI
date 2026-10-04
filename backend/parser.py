import re

def parse_stack_trace(stack_trace: str):

    file_name = None
    line_number = None

    file_match = re.search(r'(\w+\.py)', stack_trace)

    line_match = re.search(r'line\s+(\d+)', stack_trace)

    if file_match:
        file_name = file_match.group(1)

    if line_match:
        line_number = int(line_match.group(1))

    return {
        "file_name": file_name,
        "line_number": line_number
    }