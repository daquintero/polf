import os
import polf

example_file_address = os.path.dirname(polf.__file__) + "/../tests/25-rcx_sta.rpt"

test = polf.OpenSTAParser(
    file_address=example_file_address,
)

print(test.file_lines_data)
