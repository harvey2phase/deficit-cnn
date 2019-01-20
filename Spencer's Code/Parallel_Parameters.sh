number=100000 # number of runs
R=3.0 #3.0 #$( echo "0.5 + 2.5 + 2" | bc -l ) #gamma+/gamma-
gammap=7.5 #damage rate constant
gamman=6.5 #6.5 #repair rate constant
N=10000 #network size
nd=2 #number of mortality nodes
alpha=2.27 #scale free exponent
avgdeg=4 #average degree(must be even)
Mortality="AND" #mortality condition
Topology="Single" #network topology, single creates one network for all runs, otherwise creates a new network for each run with a different seed 
Folder="Dec15"
NetworkType="ScaleFree"
SingleSeed=1
pA=0.0

make

TaskID=0

for SingleSeed in 1
do
    for NetworkType in "Random" "SmallWorld"
    do
	for gammap in 3.75 7.5 15.0
	do

	    for k in `seq -f "%.0f" 1 10`
	    do
		sleep 1s
		./SedScript.sh $number $R $gammap $gamman $N $nd $alpha $avgdeg $Mortality $Topology $Folder $NetworkType $TaskID $SingleSeed $pA
		chmod 761 runAcenet${TaskID}.sh
		sbatch runAcenet${TaskID}.sh
		#echo $TaskID
		TaskID=$(( TaskID + 1 ))
	    done
	done
    done
done

gammap=7.5 #damage rate constant
avgdeg=4
alpha=2.27
pA=0.0



for SingleSeed in 1
do
    for NetworkType in "Random" "SmallWorld"
    do
	for avgdeg in 2 4 8
	do
	    for k in `seq -f "%.0f" 1 10`
	    do
		sleep 1s
		./SedScript.sh $number $R $gammap $gamman $N $nd $alpha $avgdeg $Mortality $Topology $Folder $NetworkType $TaskID $SingleSeed $pA
		chmod 761 runAcenet${TaskID}.sh
		sbatch runAcenet${TaskID}.sh
		#echo $TaskID
		TaskID=$(( TaskID + 1 ))
	    done
	done
    done
done


gammap=7.5 #damage rate constant
avgdeg=4
alpha=2.27
pA=0.0


for SingleSeed in 1
do
    for NetworkType in "ScaleFree"
    do
	for pA in 0.0 0.99
	do
	    for alpha in 2.1 2.27 2.5
	    do
		for k in `seq -f "%.0f" 1 10`
		do
		    sleep 1s
		    ./SedScript.sh $number $R $gammap $gamman $N $nd $alpha $avgdeg $Mortality $Topology $Folder $NetworkType $TaskID $SingleSeed $pA
		    chmod 761 runAcenet${TaskID}.sh
		    sbatch runAcenet${TaskID}.sh
		    #echo $TaskID
		    TaskID=$(( TaskID + 1 ))
		done
	    done
	done
    done
done
		  
gammap=7.5 #damage rate constant
avgdeg=4
alpha=2.27
pA=0.0

for SingleSeed in 1
do
    for NetworkType in "ScaleFree"
    do
	for pA in 0.0 0.99
	do
	    for gammap in 3.75 7.5 15.0
	    do
		for k in `seq -f "%.0f" 1 10`
		do
		    sleep 1s
		    ./SedScript.sh $number $R $gammap $gamman $N $nd $alpha $avgdeg $Mortality $Topology $Folder $NetworkType $TaskID $SingleSeed $pA
		    chmod 761 runAcenet${TaskID}.sh
		    sbatch runAcenet${TaskID}.sh
		    #echo $TaskID
		    TaskID=$(( TaskID + 1 ))
		done
	    done
	done
    done
done

gammap=7.5 #damage rate constant
avgdeg=4
alpha=2.27
pA=0.0

for SingleSeed in 1
do
    for NetworkType in "ScaleFree"
    do
	for pA in 0.0 0.99
	do
	    for avgdeg in 2 4 8
	    do
		for k in `seq -f "%.0f" 1 10`
		do
		    sleep 1s
		    ./SedScript.sh $number $R $gammap $gamman $N $nd $alpha $avgdeg $Mortality $Topology $Folder $NetworkType $TaskID $SingleSeed $pA
		    chmod 761 runAcenet${TaskID}.sh
		    sbatch runAcenet${TaskID}.sh
		    #echo $TaskID
		    TaskID=$(( TaskID + 1 ))
		done
	    done
	done
    done
done
