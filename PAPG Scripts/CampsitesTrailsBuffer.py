# CampsitesTrailsBuffer.py
import arcpy
# Set geoprocessing environments
arcpy.env.workspace = "D:\Classes\OnGeo\papg\papg424\PetersBrett\CourseData\GrandTeton.gdb"
# Allow for overwriting
arcpy.env.overwriteOutput = True
# Create list of feature classes from GrandTeton.gdb
fcList = arcpy.ListFeatureClasses()
# Create a for loop to buffer Campsites and Trails
bufferList = []
for fc in fcList:
    if fc == "Backcountry_Camping_Areas":
       arcpy.Buffer_analysis(fc, fc + "Buffer", "100 meters")
       bufferList.append(fc + " Buffer")

# Summarize the results of the geoprocessing
for item in bufferList:
    print(f"\n We have produced: {item}")

