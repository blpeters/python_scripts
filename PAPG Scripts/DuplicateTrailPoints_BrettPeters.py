## Name: DuplicateTrailPoints.py ##
# Description: Create 3 empty Feature Classes
# using the Trail_Points layer as a template
# for the purpose of testing out new data

## Section 1. ##
# Import system modules
import arcpy
arcpy.env.overwriteOutput = True

## Section 2. ##
# Set workspace
arcpy.env.workspace = r"D:\Classes\OnGeo\papg\papg424\PetersBrett\CourseData\GrandTeton.gdb"

## Section 3. ##
# Use the Describe function to get a SpatialReference object
# Set parameters for the CreateFeatureclass_management function
spatial_reference = arcpy.Describe("Trail_Points").spatialReference
out_path = arcpy.env.workspace
geometry_type = "POINT"
template = "Trail_Points"
has_m = "DISABLED"
has_z = "DISABLED"

## Section 4. ##
# Set up while loop
n = 1
while n < 4:
    out_name = "out{0}".format(n)
    ## Section 5. ##
    # Execute CreateFeatureclass_management and update
    arcpy.CreateFeatureclass_management(out_path, out_name, geometry_type, template, has_m, has_z, spatial_reference)
    print(f"FeatureClass {n} creation complete.")
    n += 1

## Section 6. ##
# Print a final message
print("Script complete")
