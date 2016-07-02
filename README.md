# ry16_transcon heatmap generator
This is a python Flask app running at http://ry16-transcon-data.herokuapp.com that displays a heatmap of the points contained in gpx files in this repo. Flask isn't really ncessary for this app, as the data all come from [data.js](./static/data.js). If new gps files are added we update `data.js` with:

  1. `python gpx2csv.py` to parse all the gpx files into [ry16_transcon.csv](ry16_transcon.csv).

  2. `python csv2js.py`  creates the file [data.js](./static/data.js), which defines the variable `points` used by the main html file.


