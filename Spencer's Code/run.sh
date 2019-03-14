number=1000 # number of runs
R=3.0 #Gamma+/Gamma-
gammap=7.5 #damage rate constant
gamman=6.5 #repair rate constant
N=10000 #network size
FIn=32 #number of frailty nodes 
nd=2 #number of mortality nodes
alpha=2.27 #scale free exponent
avgdeg=4 #average degree(must be even for scalefree and smallworld)
Mortality="AND" #mortality condition
Topology="Single" #"Single" #network topology, single creates one network for all runs, otherwise creates a new network for each run with a different seed 
Folder="Local"
NetworkType="ScaleFree"
SingleSeed=1
pA=0.0
make

for k in `seq -f "%.0f" 1 1`
do	
    ./main $number $R $gammap $gamman $N $nd $alpha $avgdeg $Mortality $Topology $Folder $NetworkType $k $SingleSeed $pA
done

