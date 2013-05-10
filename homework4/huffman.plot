set terminal postscript eps enhanced color font 'Helvetica,40'
set output 'huffman_encode_time.eps'
set size 4, 4
set xlabel 'Text length'
set ylabel 'Time (s)'
plot "output_graphs.dat" using 1:2 with lines lw 10 title 'Esp distribution', "output_graphs.dat" using 1:3 with lines lw 10 title 'Uniform distribuiton'
      
set output 'huffman_decode_time.eps'
set xlabel 'Text length'
set ylabel 'Time (s)'
plot "output_graphs.dat" using 1:4 with lines lw 10 title 'Esp distribution', "output_graphs.dat" using 1:5 with lines lw 10 title 'Uniform distribuiton'

set output 'huffman_memory.eps'
set xlabel 'Text length'
set ylabel 'Memory (bits)'
plot "output_graphs.dat" using 1:6 with lines lw 10 title 'Esp distribution', "output_graphs.dat" using 1:7 with lines lw 10 title 'Uniform distribuiton'

set output 'huffman_compression_ratio.eps'
set xlabel 'Text length'
set ylabel 'Compression ratio (compressed + memory to decode on file / original)'
plot "output_graphs.dat" using 1:8 with lines lw 10 title 'Esp distribution', "output_graphs.dat" using 1:9 with lines lw 10 title 'Uniform distribuiton'
