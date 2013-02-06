FILE="noissy"
MAXWORDLEN=50
SENDREPETITIONS=1000

ZEROPROB="0.50 0.70 0.90"
ZEROSEND="0.80"
ONESEND="0.99"

for zp in $ZEROPROB
do
    GNUPLOT_FILE="noissy_"$zp".plot"
    > $GNUPLOT_FILE
    echo set term postscript eps color 30 >> $GNUPLOT_FILE
    echo set key outside Right >> $GNUPLOT_FILE
    echo set size 4, 3 >> $GNUPLOT_FILE
    echo set output \""noissy_"$zp".eps"\" >> $GNUPLOT_FILE
    echo set pointsize 3 >> $GNUPLOT_FILE
    echo plot \\ >> $GNUPLOT_FILE
    for zs in $ZEROSEND
    do
        for os in $ONESEND
	do
	    python canales.py $FILE$zp\_$zs\_$os".data" $MAXWORDLEN $SENDREPETITIONS $zp $zs $os
	    echo python canales.py $FILE$zp\_$zs\_$os".data" $MAXWORDLEN $SENDREPETITIONS $zp $zs $os
	    echo \"$FILE$zp\_$zs\_$os".data"\" using 2:1 with points title \"$zp $zs $os\", \\ >> $GNUPLOT_FILE
	    echo \"$FILE$zp\_$zs\_$os".data"\" using 3 with lines title \"Mean\", \\ >> $GNUPLOT_FILE
	    echo \"$FILE$zp\_$zs\_$os".data"\" using 4 with impulses title \"Standard deviation\" >> $GNUPLOT_FILE
	done
    done
done
gnuplot *.plot
rm *.plot
rm *.data