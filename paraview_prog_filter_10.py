# paraview load vtk slice data
# results must be height z=1.5m
# cell data to point data filter
# use calculator magU = mag(U)
# select programmable filter...
# (paste this code into it)
# set legend blue to red rainbow
# set legend range (0 to 4)

print('hello')

import numpy as np

npts = inputs[0].GetNumberOfPoints()
magU = inputs[0].PointData["magU"]

# weibull constants
Pdir = 12.0  # probability of this wind direction (say 12%)
wbk  = 2.0   # shape factor
wbc  = 6.0   # scale factor
loc  = 1.0   # location
terr = 0.6   # 0.58 <<<<<<<<< terrain correction factor
uref = 5.0   # ref velocity (uref) at ref height (zref)
tiny = 0.01  # to prevent div0 error

# New array for output
pointArray0 = np.empty(npts,dtype=np.float64) # copy magU
pointArray1 = np.empty(npts,dtype=np.float64) # NEN 8100
pointArray2 = np.empty(npts,dtype=np.float64) # Lawson LDDC
pointArray3 = np.empty(npts,dtype=np.float64) # Davenport

#---copy magU into output arrays
for i in range(npts):
    pointArray0[i] = magU[i]
output.PointData.append(pointArray0,"magU")


#---LAWSON LDDC standard (London Docklands Development Corporation)
for i in range(npts):
    waf = terr*(magU[i]/uref)
    if waf < tiny:  waf = tiny
    prob4  = Pdir*math.exp( -((( (4.0/waf)-loc)/wbc)**wbk) ) # 4m/sec
    prob6  = Pdir*math.exp( -((( (6.0/waf)-loc)/wbc)**wbk) ) # 6m/sec
    prob8  = Pdir*math.exp( -((( (8.0/waf)-loc)/wbc)**wbk) ) # 8m/sec
    prob10 = Pdir*math.exp( -((((10.0/waf)-loc)/wbc)**wbk) ) # 10m/sec
    if   prob4  <  5.0 :  pointArray2[i] = 0.0 # blue (sitting)
    elif prob6  <  5.0 :  pointArray2[i] = 1.0 # cyan (standing)
    elif prob8  <  5.0 :  pointArray2[i] = 2.0 # green (strolling)
    elif prob10 <  5.0 :  pointArray2[i] = 3.0 # yellow (business walking/cycling)
    elif prob10 >= 5.0 :  pointArray2[i] = 4.0 # red (uncomfortable)
output.PointData.append(pointArray2,"LawsonLDDC")


#---NEN8100 standard
for i in range(npts):
    waf = terr*(magU[i]/uref)
    if waf < tiny:  waf = tiny
    prob5 = Pdir*math.exp(-((((5.0/waf)-loc)/wbc)**wbk))
    if   prob5 <   2.5 :  pointArray1[i] = 0.0 # blue (sitting long)
    elif prob5 <   5.0 :  pointArray1[i] = 1.0 # cyan (sitting short)
    elif prob5 <  10.0 :  pointArray1[i] = 2.0 # green (walk leisurely)
    elif prob5 <  20.0 :  pointArray1[i] = 3.0 # yellow (walk fast)
    elif prob5 >= 20.0 :  pointArray1[i] = 4.0 # red (uncomfortable)
output.PointData.append(pointArray1,"NEN8100")


#---DAVENPORT standard
for i in range(npts):
    waf = terr*(magU[i]/uref)
    if waf < tiny: waf = tiny
    prob3p6  = Pdir*math.exp( -((( (3.6/waf)-loc)/wbc)**wbk) ) #4m/sec
    prob5p3  = Pdir*math.exp( -((( (5.3/waf)-loc)/wbc)**wbk) ) #6m/sec
    prob7p6  = Pdir*math.exp( -((( (7.6/waf)-loc)/wbc)**wbk) ) #8m/sec
    prob9p8  = Pdir*math.exp( -((( (9.8/waf)-loc)/wbc)**wbk) ) #10m/sec
    prob15p1 = Pdir*math.exp( -((((15.1/waf)-loc)/wbc)**wbk) ) #10m/sec
    if   prob3p6  <  1.5:  pointArray3[i] = 0.0 # dark blue (sitting long)
    elif prob5p3  <  1.5:  pointArray3[i] = 0.5 # medium blue (standing short)
    elif prob7p6  <  1.5:  pointArray3[i] = 1.0 # light blue (walking leisurely)
    elif prob9p8  <  1.5:  pointArray3[i] = 2.0 # green (walking fast)
    elif prob9p8  >= 1.5:  pointArray3[i] = 3.0 # yellow (uncomfortable)
    if   prob15p1 >= 0.01: pointArray3[i] = 4.0 # red (dangerous)
output.PointData.append(pointArray3,"Davenport")



