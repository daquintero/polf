# PORF

Parse OpenRoad Files - A Python Pandas-based report file (RPT) parser for Openlane OpenROAD Static Timing Analysis (STA) output files. 



## Examples

Basic Usage

```python
import porf

parse_file = porf.OpenSTAParser(file_address="./docs/examples/25-rcx_sta.rpt")
parse_run = porf.RunAnalyser(run_directory="./docs/examples/")
```

## Installation

### Quick Start

Install via `pip`

```bash
$ pip install porf
```

Then you can:

```python
import porf
```

Local development install for most recent version. Contributions very welcome.
```bash
$ git clone https://github.com/daquintero/porf.git
$ cd qups
$ pip install -e .[develop]
```
