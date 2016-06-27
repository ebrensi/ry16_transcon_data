#! usr/bin/env python

# parse GIS points from gpx files and store them as CSV file with timestamps

import gpxpy
import os
import logging

# 617317129.gpx, 617330020.gpx, 617332984.gpx don't parse
"""
Warning: mysql_fetch_assoc() expects parameter 1 to be resource, boolean given in /www/raceshape/shape/strava.export.php on line 179
{"error":"Strava not available"}
"""

data_file_path = "./data_files/"

logging.basicConfig(
    format='%(levelname)s:%(message)s',
    level=logging.INFO)

unparsed = []

gpx_files = [fname for fname in os.listdir(data_file_path)
             if fname.endswith(".gpx")]

with open("ry16_transcon.csv", "w") as outfile:
    for fname in gpx_files:
        with open(data_file_path + fname, "r") as file:
            data = file.read()

        try:
            activity = gpxpy.parse(data)

        except:
            logging.info('problem parsing %s', fname)
            unparsed.append(fname)

        else:
            for track in activity.tracks:
                for segment in track.segments:
                    for point in segment.points:
                        outfile.write("{},{},{}\n"
                                      .format(point.time,
                                              point.latitude,
                                              point.longitude))

            logging.info('Parsed %s', fname)

logging.info("problems with %s", unparsed)
