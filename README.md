If you first load the surface20.vtk file into Paraview it will give you a variable wind range from 0 to 20 m/sec.
Then start a python programmable filter window, and cut-and-paste the contents of the python file (paraview_prog_filter_10.py) into that window.
You should then be able to selct from the fields Lawson, Davenport, NEN8100, which will show the previous variable wind velocity colourmap,
in bands or categories according to each wind comfort standard
