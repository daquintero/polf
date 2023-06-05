import os
import porf

example_file_address = os.path.dirname(porf.__file__) + "/../tests/25-rcx_sta.rpt"

test = porf.OpenSTAParser(
    file_address=example_file_address,
)

print(test.file_lines_data)
