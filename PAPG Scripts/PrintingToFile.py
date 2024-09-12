import arcpy
import os
arcpy.env.overwriteOutput = True

arcpy.env.workspace = "D:\Classes\OnGeo\papg\papg424\PetersBrett\CourseData\GrandTeton.gdb"

# Use the ListFeatureClasses function to return a list of all fc's in the gdb:
fcList = arcpy.ListFeatureClasses()

# Write name of each fc in the text file:
txtFile = open(r"D:\Classes\OnGeo\papg\papg424\PetersBrett\Results\FeatureClassList.txt", "w")
for fc in fcList:
    print(fc)
    txtFile.write(fc)
    txtFile.write(os.linesep)
txtFile.close()

print('done')
