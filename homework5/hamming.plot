set terminal postscript eps enhanced color font 'Helvetica,40'
set output 'error_correction.eps'
set size 4, 4
set xlabel 'Text Errors probability'
set ylabel 'Words sended'
plot "output.dat" using 1:2 with lines lw 10 title 'Sended without errors',\
 "output.dat" using 1:3 with lines lw 10 title 'Error finded and fixed',\
 "output.dat" using 1:4 with lines lw 10 title 'Error not finded or not fixed'

