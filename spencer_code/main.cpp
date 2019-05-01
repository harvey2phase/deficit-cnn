#include <iostream>
#include <vector>
#include <random>
#include <cmath>
#include <cstdlib>
#include <fstream>
#include <string>
#include <assert.h>
#include <algorithm>
#include <unordered_map>
#include <utility>

#include <boost/config.hpp>
#include <boost/graph/adjacency_list.hpp>
#include <boost/graph/connected_components.hpp>

std::mt19937 g1(1); //Random number generator, mersenne twister
std::uniform_real_distribution<double> RNG(0.0,1.0); 

#include "Parameters.h"
#include "Files.h"
#include "DeficitType.h"
#include "Node.h"
#include "DataFile.h" 
#include "OutputDataFile.h" 
#include "SaveData.h"
#include "2Dvector.h"
#include "RandomNetwork.h" 
#include "tree.h" 
#include "GillespieTree.h"
#include "UpdateNode.h"
#include "MortalityNodes.h"
#include "ScaleFreeNetworkTree.h" 
#include "MortalityRules.h"
#include "OutputNetwork.h"
#include "AssortativeMixing.h"
#include "SmallWorld.h"
#include "SetUpNetwork.h"

int main(int argc, char *argv[]) {

    using namespace Parameters; // Using the parameters from cmd line
    SetParameters(argc, argv); // Set initial parameters from command line
    SetSimulate();
    std::cout << "Parameters Loaded" << std::endl;


    // Network
    // some network types remove unconnected nodes, lowering N.
    // Original N will not change
    const int OriginalN = N;
    std::vector<Node> Network;
    std::vector<int> MortalityNodes(nd);


    // Hold all death ages found
    std::vector<double> DeathAges; DeathAges.reserve(Parameters::Number);


    // Holds the time of change, id of the node, and state of the node d
    std::vector<DeficitVal> DeficitsValues;
    if (SimulateVar::MortalityOnly_bool == false)
        DeficitsValues.reserve(N * 1000);


    // Data file to save intermediate Data
    OutputDataFile File(OriginalN);
    if (SimulateVar::MortalityOnly_bool == false) File.Open(); 


    // set up network, if single topology set up network before the simulation
    if(Topology == "Single") {
        g1.seed(Parameters::SingleSeed);
        SetUpNetwork(Network, MortalityNodes, OriginalN);
        std::cout << "Single Network Created" << std::endl;
    }


    // loop through runs to average data
    for (int run = 1; run <= Number; run++) {

        // Set current seed
        if(run == 1) g1.seed(RealSeed); 

        // Set up network for every seed if not single topology 
        if(Topology != "Single") 
            SetUpNetwork(Network, MortalityNodes, OriginalN);

        EventTree<double> tree(N, 1.0); 
        // sum of rates
        double TotalRate = N; 
        // current Time (unscaled age)
        double Time = 0; 

        // evolve in time until Mortality occurs	
        while(true) {
            // Find rate to be performed
            int Index = FindRate(tree, TotalRate);
            // perform rate and increase time
            UpdateNode(Network[Index], Time, TotalRate, DeficitsValues); 
            // update the local frailty after the node is modified
            UpdateLocalFrailty(Network, Network[Index]); 
            // calculate new rates for the node and its neighbours
            CalculateRates(Network, Network[Index], tree, Index, TotalRate); 

            // evaluate mortality
            if(Mortality(Network, MortalityNodes) == 1) break;    
        }

        // ensure something has happened
        // assert(DeficitsValues.size() > 0);

        // record death age data
        DeathAges.push_back(Time);

        // Reset Rates and fraility if it is single topology
        if(Topology == "Single")
            for (auto &x: Network) x.Reset();  

        // Save interediate Data every 1000 individuals
        if(SimulateVar::MortalityOnly_bool == false && run%1000 == 0 ) { 
            // possibly change the 1000 (depends on memory restrictions)
            File.SaveData(DeficitsValues); 

        }

        if (run%1000 == 0)
            std::cout << "Run " << run << std::endl;


    }

    std::cout << "Outputing final data" << std::endl;

    // Save and output final bit of raw Data
    if (SimulateVar::MortalityOnly_bool == false) {
        File.SaveData(DeficitsValues);
        File.FlushDataFile(DeficitsValues);
    }

    OutputDeathAges(DeathAges, OriginalN);
    std::cout << "Finished" << std::endl;

}

