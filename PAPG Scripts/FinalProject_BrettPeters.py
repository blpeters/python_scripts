# FinalProjectScript.py

import arcpy

arcpy.env.workspace = "D:\Classes\OnGeo\papg\papg424\PetersBrett\FinalProject\FinalProject.gdb"
arcpy.env.overwriteOutput = True

# Get endangered/threatened species habitat Feature Class input:
species_fc = arcpy.GetParameterAsText(0)
spatial_ref_species = arcpy.Describe(species_fc).spatialReference

# Get current wildfires Feature Class input:
fire_fc = arcpy.GetParameterAsText(1)

# Create a feature data set in the project gdb to add all individual species FCs. Match original species fc spatial ref.
arcpy.CreateFeatureDataset_management(arcpy.env.workspace, 'IndividualSpeciesHabitats', spatial_ref_species)

# Split the species FCs into individual FCs for each species on the common name attribute (2 owl species in my example).
arcpy.SplitByAttributes_analysis(species_fc, 'IndividualSpeciesHabitats', 'comname')
habitats = arcpy.ListFeatureClasses(feature_dataset='IndividualSpeciesHabitats')


# For each species FC, intersect with the wildfires to determine areas of overlap and add point at each location.
for habitat in habitats:
    inFeatures = [habitat, fire_fc]
    intersectOutput = habitat + "_FireImpacts"
    joinAttr = "NO_FID"
    outputType = "point"
    arcpy.Intersect_analysis(inFeatures, intersectOutput, join_attributes=joinAttr, output_type=outputType)

