# Trail_Features_Buffer.py
#
# Import modules
import arcpy

# Create a list of feature classes to Buffer
bufferList = [arcpy.GetParameterAsText(0), arcpy.GetParameterAsText(1)]

# Initialize a new Python list of feature classes to be Unionized together
unionList = []

# Set Buffer parameters around Park Trails and Trail Points.
distanceField = "1000 meters"
sideType = "FULL"
endType = "ROUND"
dissolveType = "ALL"

for fc in bufferList:
    # Buffer each feature class and dissolve any overlapping polygons.
    arcpy.Buffer_analysis(fc, fc + "dynamicBuffer", distanceField, sideType, endType, dissolveType)
    # Add each buffer feature class to a list of feature classes to Union.
    unionList.append(fc + "dynamicBuffer")

# Union the buffered feature classes
arcpy.Union_analysis(unionList, arcpy.GetParameterAsText(2))

