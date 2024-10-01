import arcpy

# Set the workspace
arcpy.env.workspace = "path/to/your/data"

# Read the shapefiles
national_parks = "D:\Enviormental Geomactics\GEO115 Programming in GIS\Week 6_5\CLAB_CA_2023-09-08\CLAB_CA_2023-09-08.shp"


# Set the workspace
arcpy.env.workspace = ""D:\Enviormental Geomactics\GEO115 Programming in GIS\Week 6_5""

# Read the shapefiles
national_parks = "D:\Enviormental Geomactics\GEO115 Programming in GIS\Week 6_5\CLAB_CA_2023-09-08\CLAB_CA_2023-09-08.shp"
ecozone = "D:\Enviormental Geomactics\GEO115 Programming in GIS\Week5\ecozone_shp\Ecozones\ecozones.shp"

# Set the workspace
arcpy.env.workspace = ""path/to/your/data""

# Read the shapefiles
national_parks = "D:\Enviormental Geomactics\GEO115 Programming in GIS\Week 6_5\CLAB_CA_2023-09-08\CLAB_CA_2023-09-08.shp"
ecozone = "D:\Enviormental Geomactics\GEO115 Programming in GIS\Week5\ecozone_shp\Ecozones\ecozones.shp"

# Set the workspace
arcpy.env.workspace = ""D:\Enviormental Geomactics\GEO115 Programming in GIS\Week 6_5""

# Read the shapefiles
national_parks = "D:\Enviormental Geomactics\GEO115 Programming in GIS\Week 6_5\CLAB_CA_2023-09-08\CLAB_CA_2023-09-08.shp"

# Set the workspace
arcpy.env.workspace = "D:\Enviormental Geomactics\GEO115 Programming in GIS\Week 6_5"

# Read the shapefiles
national_parks = "D:\Enviormental Geomactics\GEO115 Programming in GIS\Week 6_5\CLAB_CA_2023-09-08\CLAB_CA_2023-09-08.shp"

ecozone = "D:\Enviormental Geomactics\GEO115 Programming in GIS\Week5\ecozone_shp\Ecozones\ecozones.shp"

# Define the input and intersect feature classes
input_fc = "D:\Enviormental Geomactics\GEO115 Programming in GIS\Week 6_5\CLAB_CA_2023-09-08\CLAB_CA_2023-09-08.shp"
intersect_fc = "D:\Enviormental Geomactics\GEO115 Programming in GIS\Week5\ecozone_shp\Ecozones\ecozones.shp"
output_fc = "output_intersect.shp"

# Perform the intersection
arcpy.analysis.Intersect({input_fc, intersect_fc}, output_fc)
print("Intersection query completed.")

# Perform the intersection
arcpy.analysis.Intersect({"D:\Enviormental Geomactics\GEO115 Programming in GIS\Week 6_5\CLAB_CA_2023-09-08\CLAB_CA_2023-09-08.shp" , "D:\Enviormental Geomactics\GEO115 Programming in GIS\Week5\ecozone_shp\Ecozones\ecozones.shp"}, "output_fc2" , "ALL")
print("Intersection query completed.")

# Set the workspace from directory
arcpy.env.workspace = "D:\Enviormental Geomactics\GEO115 Programming in GIS\Week 6_5"

arcpy.analysis.Intersect(["D:\Enviormental Geomactics\GEO115 Programming in GIS\Week 6_5\CLAB_CA_2023-09-08\CLAB_CA_2023-09-08.shp","D:\Enviormental Geomactics\GEO115 Programming in GIS\Week5\ecozone_shp\Ecozones\ecozones.shp"], "output_fc2","ALL")
print("Intersection query completed.")

# Set the workspace
arcpy.env.workspace = "D:/Enviormental Geomactics/GEO115 Programming in GIS/Week 6_5"

# Define the input feature class and buffer distance
input_fc = "D:/Enviormental Geomactics/GEO115 Programming in GIS/Week 6_5/CLAB_CA_2023-09-08/CLAB_CA_2023-09-08.shp"
buffer_fc = "national_parks_buffer.shp"
wetlands_fc = "C:/Users/ASUS/Downloads/WETLAND/Non_Sensitive.gdb/WETLAND"



# Select Ontario national parks
sql_query = "CPC_CODE = 'ON'"
arcpy.management.MakeFeatureLayer(input_fc, "national_parks_layer", sql_query)

# Create a 20km buffer around the selected national parks
buffer_distance = "20000 Meters"
arcpy.analysis.Buffer("national_parks_layer", buffer_fc, buffer_distance)


# Select wetlands within the buffer zone
arcpy.management.MakeFeatureLayer(wetlands_fc, "wetlands_layer")
arcpy.management.SelectLayerByLocation("wetlands_layer", "WITHIN", buffer_fc, selection_type="NEW_SELECTION")


# Select wetlands within the buffer zone
arcpy.management.MakeFeatureLayer(wetlands_fc, "wetlands_layer")
arcpy.management.SelectLayerByLocation("wetlands_layer", "WITHIN", buffer_fc, selection_type="NEW_SELECTION")


# Export the selected wetlands to a new feature class
output_wetlands = "wetlands_within_20km.shp"
arcpy.management.CopyFeatures("wetlands_layer", output_wetlands)
print("SQL query and spatial selection completed.")



