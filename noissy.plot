set term postscript eps color 30
set key outside Right
set size 4, 3
set output "noisy_channel.eps"
set pointsize 2
plot \
"noissy0.50_0.98_0.99.data" using 2:1 with points title "0.50 0.98 0.99", \
exp(-x*0.005) with lines title "0.50 0.98 0.99 esperado"
