import numpy as np

# Tommy Trojan center point
center_lat = 34.020586907680844
center_lon = -118.28544299106726

# Spirograph parameters
R = 90  # Radius of the fixed circle
r = 36  # Radius of the moving circle
a = 44  # Distance from the moving circle's center to the drawing point
n = 10

#range for the Spirograph curve (can't do for loops that have step vallues of decimal in python so just using np list like this)
t = np.arange(0, n * np.pi, 0.01)

#do the given calc for all in list
x = (R + r) * np.cos((r / R) * t) - a * np.cos((1 + r / R) * t)
y = (R + r) * np.sin((r / R) * t) - a * np.sin((1 + r / R) * t)

#latitude and longitude offseting and approx conversion
lat_offset = y / 110540 
lon_offset = x / (111320 * np.cos(center_lat * np.pi / 180))

# Calculate actual latitude and longitude for all in list
lat = center_lat + lat_offset
lon = center_lon + lon_offset

spirograph_coords = np.column_stack((lat, lon))

#top of kml
kml_content = """<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
<Document>
    <name>Spirograph Curve</name>
    <Placemark>
        <name>Spirograph Curve Points</name>
        <LineString>
            <extrude>1</extrude>
            <tessellate>1</tessellate>
            <coordinates>\n"""

#key: switching lon and lat ordering
kml_content += "\n".join(f"{lon},{lat},0" for lat, lon in spirograph_coords)

# end of KML content
kml_content += """
            </coordinates>
        </LineString>
    </Placemark>
</Document>
</kml>"""


# Save the KML content to a file
with open('spiro.kml', 'w') as file:
    file.write(kml_content)