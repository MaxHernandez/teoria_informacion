
GNUPLOT_FILE="noissy.plot"
FILE="noissy"
MAXWORDLEN=50
SENDREPETITIONS=1000

ZEROPROB="0.50"
ZEROSEND="0.98"
ONESEND="0.99"
#ZEROPROB="0.60 0.78 0.9"
#ZEROSEND="0.90 0.95 0.99"
#ONESEND="0.90 0.97 0.99"

> $GNUPLOT_FILE
echo set term postscript eps color 30 >> $GNUPLOT_FILE
echo set key outside Right >> $GNUPLOT_FILE
echo set size 4, 3 >> $GNUPLOT_FILE
echo set output \"noisy_channel.eps\" >> $GNUPLOT_FILE
echo set pointsize 2 >> $GNUPLOT_FILE
echo plot \\ >> $GNUPLOT_FILE

for zp in $ZEROPROB
do
    for zs in $ZEROSEND
    do
        for os in $ONESEND
	do
	    python canales.py $FILE$zp\_$zs\_$os".data" $MAXWORDLEN $SENDREPETITIONS $zp $zs $os
	    echo python canales.py $FILE$zp\_$zs\_$os".data" $MAXWORDLEN $SENDREPETITIONS $zp $zs $os
	    echo \"$FILE$zp\_$zs\_$os".data"\" using 2:1 with points title \"$zp $zs $os\", \\ >> $GNUPLOT_FILE
	    echo exp\(-x*\( \($zp*\(1-$zs\)\)+\(\(1-$zp\)*\(1-$os\)\) \)\)  with lines title \"$zp $zs $os esperado\", \\ >> $GNUPLOT_FILE
	done
    done
done
