import glob
import os


class RunAnalyser:
    """
    This class aims to list and perform analysis on all the relevant files in a particular run between all the corners.
    """

    def __init__(
            self,
            run_directory=None,
    ):
        self.run_directory = run_directory

        # Internal
        self.all_rpt_files_list = None
        self.timing_sta_files_list = None
        self.power_sta_files_list = None

        self.get_all_rpt_files()

    def get_all_rpt_files(self):
        self.all_rpt_files_list = []
        self.timing_sta_files_list = []
        self.power_sta_files_list = []
        PATH = os.path.dirname(os.getcwd())
        for x in os.walk(PATH):
            for file_path in glob.glob(os.path.join(x[0], '*.rpt')):
                self.all_rpt_files_list.append(file_path)
                if file_path.endswith(("sta.rpt", "sta.min.rpt", "sta.max.rpt",)):
                    self.timing_sta_files_list.append(file_path)
                if file_path.endswith(("power.rpt")):
                    self.power_sta_files_list.append(file_path)

    def extract_metrics_timing(self):
        """
        For every file in the sta timing file, extract the propagation delay and save the file meta data into a dicitonary.
        """
        self.timing_metrics_list = []
        for file in self.timing_sta_files_list:
            print(file)
            file_directory_data = os.path.normpath(file).split(os.path.sep)
            timing_data = OpenSTAParser(file_address=file)
            metrics = {
                "file_name": file_directory_data[-1],
                "flow_step_name": file_directory_data[-2],
                "propagation_delay": timing_data.propagation_delay,
            }
            self.timing_metrics_list.append(metrics)
        return self.timing_metrics_list

    def extract_metrics_power(self):
        pass