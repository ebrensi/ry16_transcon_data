#! usr/bin/env python

import csv


with open("ry16_transcon.csv", "r") as f:
    reader = csv.reader(f)
    points_list = list(reader)

points = [[float(point[1]), float(point[2])] for point in points_list]

with open("data.js", "w") as jsdatafile:
    jsdatafile.write("data = {};".format(points))
