//output adjacency matrix
void OutputNetworkStructure(std::vector<Node> Network, const std::vector<int> &MortalityNodes, int OriginalN) {

    //create adjacency matrix
    std::vector<std::vector<int>> adjacencyMatrix(Network.size(), std::vector<int>(Network.size(), 0));


    for(auto &x: Network) {

        for(auto &y: x.Neighbours) {

	    
	    adjacencyMatrix[x.id][y] = 1;
 
	}


    }
    

    std::ofstream output;
    std::string name = SetFolder() + "NetworkAdjacencyMatrix" + SetRawName(OriginalN) + ".csv";
    output.open(name.c_str());
   
    for(int i = 0; i < Network.size(); i++) {
	int sum = 0;
        output << adjacencyMatrix[i][0];
	sum += adjacencyMatrix[i][0];
	for(int j = 1; j < Network.size(); j++) {

	    assert(adjacencyMatrix[i][j] == 0 || adjacencyMatrix[i][j] == 1);
	    
	    output << "," << adjacencyMatrix[i][j];
	    sum+=adjacencyMatrix[i][j];
	}
	output << "\n";
	//std::cout << sum << std::endl;

    }
    
    output.close();

    //nearest neighbour data
    name = SetFolder() + "kvskNN" + SetRawName(OriginalN);

    output.open(name.c_str());
   
    for(int i = 0; i < Network.size(); i++) {
	output << Network[i].k << "\t" << Network[i].knn;
	output << "\n";

    }
    
    output.close();

    
    
}


void OutputNetworkDegrees(const std::vector<Node> &Network, int OriginalN, int run = -1) {

    
    std::ofstream output;
    std::string name = SetFolder() + "NetworkDegrees" + SetRawName(OriginalN);

    if (run > -1)
	name += "Run" + std::to_string(run);
    
    output.open(name.c_str());
    
    for(const auto &x: Network) {

	output << x.id << "\t" << x.k << "\t" << x.knn << "\n";

    }

    output.close();

}
