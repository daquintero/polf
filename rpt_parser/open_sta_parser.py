import pandas as pd


class OpenSTAParser:
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
            file_address="25-rcx_sta.rpt",
    ):
        self.file_address = file_address

        # Internal
        self.file_lines_raw = None
        self.file_lines_raw = None
        self.file_lines_data = None
        self.propagation_delay = {}
        self.meta_data = pd.DataFrame()

        # Full file configuration operations
        self.read_file_meta_data()
        self.extract_frame_meta_data()

        # Main Flow
        self.frame_timing_data = {}
        for frame_id in range(self.maximum_frame_amount):
            self.frame_timing_data[frame_id] = self.extract_timing_data(frame_id=frame_id)
            if len(self.start_point_name.values) > frame_id:
                # TODO bit hackish and unconvincing
                frame_net_in = self.start_point_name.values[frame_id][0]
                frame_net_out = self.end_point_name.values[frame_id][0]
                propagation_delay = self.calculate_propagation_delay(net_name_in=frame_net_in,
                                                                     net_name_out=frame_net_out,
                                                                     timing_data=self.frame_timing_data[frame_id])

                self.propagation_delay[frame_id] = propagation_delay

    def read_file_meta_data(self):
        self.file = open(self.file_address, "r")
        self.file_lines_raw = self.file.readlines()
        self.file_lines_data = pd.DataFrame({"lines": self.file_lines_raw})
        self.configure_frame_id()
        self.configure_timing_data_rows()

    def configure_frame_id(self):
        self.file_lines_data["delimiters_line"] = self.file_lines_data.lines.str.contains("==========")
        self.file_lines_data["timing_data_line"] = self.file_lines_data.lines.str.contains("---------")
        frame_data = []
        frame_id_counter = 0
        parity_counter = 1
        row = 0
        for delimiter in self.file_lines_data["delimiters_line"]:
            if (delimiter):
                if (parity_counter % 2):
                    frame_id_counter += 1
                    parity_counter = 0
                else:
                    parity_counter += 1
            frame_data.append(frame_id_counter - 1)
            row += 1
        self.file_lines_data["frame_id"] = frame_data
        self.maximum_frame_amount = frame_id_counter

    def configure_timing_data_rows(self):
        self.frame_meta_data = {}
        for frame in range(self.maximum_frame_amount):
            timing_rows_index = self.file_lines_data.index[
                self.file_lines_data['timing_data_line'] & (self.file_lines_data['frame_id'] == frame)].tolist()
            if len(timing_rows_index) >= 1:

                self.frame_meta_data[frame] = {
                    "start_index": timing_rows_index[0],
                    "end_index": timing_rows_index[-1],
                    "start_rows_skip": timing_rows_index[0] + 1,
                    "end_rows_skip": len(self.file_lines_data) - timing_rows_index[-1],
                }
            else:
                self.frame_meta_data[frame] = {
                    "start_index": 0,
                    "end_index": 0,
                    "start_rows_skip": 0,
                    "end_rows_skip": 0,
                }
        return self.frame_meta_data

    def extract_frame_meta_data(self):
        # Extract Frame Metadata, note that these operations can be performed dataset wise.
        self.file_lines_data["start_point_line"] = self.file_lines_data.lines.str.contains("Startpoint")
        self.file_lines_data["end_point_line"] = self.file_lines_data.lines.str.contains("Endpoint")
        self.file_lines_data["path_group_line"] = self.file_lines_data.lines.str.contains("Path Group")
        self.file_lines_data["path_type_line"] = self.file_lines_data.lines.str.contains("Path Type")

        self.start_point_name = self.file_lines_data.lines[self.file_lines_data.start_point_line].str.extract(
            r'((?<=Startpoint:\s).*?(?=\s\())')
        self.end_point_name = self.file_lines_data.lines[self.file_lines_data.end_point_line].str.extract(
            r'((?<=Endpoint:\s).*?(?=\s\())')
        self.path_group_name = self.file_lines_data.lines[self.file_lines_data.path_group_line].str.extract(
            r'((?<=Path Group:\s).*)')
        self.path_type_name = self.file_lines_data.lines[self.file_lines_data.path_type_line].str.extract(
            r'((?<=Path Type:\s).*)')
        self.timing_data_start = self.file_lines_data.lines[self.file_lines_data.path_type_line].str.extract(
            r'((?<=Path Type:\s).*)')

    def extract_timing_data(self, frame_id=0):
        timing_data = pd.read_fwf(self.file_address,
                                  colspecs=[(0, 6), (6, 14), (14, 22), (22, 30), (30, 38), (38, 40), (40, 100)],
                                  skiprows=self.frame_meta_data[frame_id]["start_rows_skip"],
                                  skipfooter=self.frame_meta_data[frame_id]["end_rows_skip"],
                                  names=["Fanout", "Cap", "Slew", "Delay", "Time", "Direction", "Description"])
        timing_data["net_type"] = timing_data["Description"].str.extract(r'\(([^()]+)\)')
        timing_data["net_name"] = timing_data["Description"].str.extract(r'(.*?)\s?\(.*?\)')
        return timing_data

    def calculate_propagation_delay(self,
                          net_name_in="in",
                          net_name_out="out",
                          timing_data=None,
                          ):
        if (len(timing_data[(timing_data.net_name == net_name_in) & (timing_data.net_type == "in")]) > 0) \
                and (len(timing_data[(timing_data.net_name == net_name_out) & (timing_data.net_type == "out")]) > 0):
            output_net_datafame = timing_data[(timing_data.net_type == "out")].copy().add_suffix("_out").reset_index()
            input_net_datafame = timing_data[(timing_data.net_type == "in")].copy().add_suffix("_in").reset_index()
            propagation_delay_dataframe = output_net_datafame.merge(input_net_datafame, left_index=True, right_index=True)
            propagation_delay_dataframe["propagation_delay"] = pd.to_numeric(output_net_datafame.iloc[:].Time_out.values) \
                - pd.to_numeric(input_net_datafame.iloc[:].Time_in.values)
            return propagation_delay_dataframe

        # return pd.to_numeric(timing_data[timing_data.net == net_out].Time) - pd.to_numeric(timing_data[timing_data.net == net_in].Time)
