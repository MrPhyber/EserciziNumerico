set term png
set output "wilkinson_norms.png"

set yrange[0:*]

plot "fort.1" title "Norma 1" with lines, \
     "fort.2" title "Norma 2" with lines, \
     "fort.3" title "Norma ∞" with lines
