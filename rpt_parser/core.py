class ParserRPT:
    """

    Methodology:
    1. Read metadata on the type of file and run this is.
    2. Identify the boundary lines of the table data through regex matching.
    3. Read in table data of the timing performance.
    4. Understand the relevant timing and data parameters.
    5. Extract the relevant timing and data parameters from the
    """
    def __init__(
            self,
            file_address="",
    ):
        self.file_address = file_address
        self.read_file()

    def read_file(self):
        self.file = open(self.file_address, "r")
        # self.file_text = self.file.read()
        self.file_lines = self.file.readlines()
        print(self.file_lines)
