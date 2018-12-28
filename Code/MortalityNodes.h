//Sort the network to find the nd Mortality Nodes and n frailty nodes
std::vector<int> FindMortalityNodes(std::vector<Node> Network) {

    std::vector<int> MortalityNodes(Parameters::nd);
    
    //sort in descending order
    std::sort(Network.begin(), Network.end(), [](const Node &x, const Node &y){

	    return x.k > y.k;

	});

    int minimumDegree = Network[Network.size() - 1].k;
        
    //set mortality nodes as the largest nd nodes
    for(int i = 0; i < Parameters::nd; i++)
	MortalityNodes[i] = Network[i].id;

    return MortalityNodes;

}



