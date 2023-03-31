import os
import rpt_parser

example_file_address = os.path.dirname(rpt_parser.__file__) + "/../tests/25-rcx_sta.rpt"

a = rpt_parser.ParserRPT(
    file_address=example_file_address,
)
