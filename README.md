# ry16_transcon heatmap generator
This is set of python scripts to render an interactive heatmap from the gpx files located in `data_files`.

  1. `python gpx2csv.py` to parse all the gpx files into [ry16_transcon.csv](ry16_transcon.csv).

  2. `python csv2js.py`  creates the file [data.js](data.js), which is defines the variable `points` used by the main html file.

