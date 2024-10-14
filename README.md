# MetasurfaceToolbox
Scripts to handle design and layout creation for metasurfaces

1- The first script is a simple, illustrated script to explain the principles of a simple flat metasurface layout generation

2- The second script ('ArbitrarilyCurvedMetasurface_BeamSteering.ipynb') is a script for generating an arbitrarily curved metasurface gds layout, by splitting tasks in z sub tasks to handle storage constraints. The target GDS layout here is a phase profile conformal to a 3D curved curface. The goal of the meatsurace is to achieve 3D beam steering of an incoming pencil beam

3- The thrid script ('CurvedMetasurface_IncidentAngleCorrected_DeformationCorrected_ContinuousSampling.ipynb')  generates a metasurface gds layout. This script generates the flat metasurface layout to write in ebeam if the final target phase profile is a conformal phase profile over a spherical lens of curvature radius 3.21mm. Cells are recommended to be merged before execution


