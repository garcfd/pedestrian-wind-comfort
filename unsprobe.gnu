
# Optional: set labels
set xlabel 'Index'
set ylabel 'Value'
set grid
set key top right
set xrange [0:81]


# cfd normalised by wind speed at height 15.9m (0.03)
plot 'unsprobe.dat' using 1:($2/(0.03)) w lp title 'cfd',\
     'exptwest.dat' using 1:2           w lp title 'expt'


pause -1  # wait for keypress
