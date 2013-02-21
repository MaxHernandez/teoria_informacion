set terminal postscript eps enhanced color font 'Helvetica,40'
set output 'introduction.eps'
set size 4, 4
set xlabel 'Pattern length'
set ylabel 'Text length'
set zlabel 'time running'
set logscale
splot "time_test.dat" using 1:2:3 with dots title 'Boyer-Moore' , 'time_test.dat' using 1:2:4 with dots title 'Knuth-Morris-Pratt';