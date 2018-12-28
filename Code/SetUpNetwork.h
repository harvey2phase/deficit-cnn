/*

Set up the network as Random, smallworld or scalefree.
Modify assortativity if needed.
N can change if nodes are removed when making the network connected, but Original N stays fixed.
Mortality Nodes are also set.
The degrees and average nearest neighbour degree of each node in the network are outputted.

*/



std::vector<Node> CheckConnected(const std::vector<Node> &Network) {


    
    //find connected components
    using namespace boost;
    
    typedef adjacency_list <vecS, vecS, undirectedS> Graph;
	    
    Graph G;

    for(const auto &v: Network) {

	for(auto x: v.Neighbours) {
	    
	    //if(G.has_edge(v.id, Network[x].id))
	    auto res = add_edge(v.id, Network[x].id, G);
	    //if (std::get<1>(res)==false) std::cout << "refused" << std::endl;
	}
	    
    }
	    
    
    std::vector<int> component(num_vertices(G));
    int num = connected_components(G, &component[0]);
    
    std::vector<std::tuple<Node, int>> Network_Components; Network_Components.reserve(Parameters::N);
    

    std::vector<int> component_sizes(num,0);
    for (int i = 0; i < component.size(); i++) {

	Network_Components.emplace_back(Network[i], component[i]);

	component_sizes[component[i]]++;
	

    }


    auto iteratorMax = std::max_element(component_sizes.begin(), component_sizes.end());
    
    int giantCom = *iteratorMax;
    int indexMax = iteratorMax - component_sizes.begin();
    
    auto remove = std::remove_if(Network_Components.begin(), Network_Components.end(), [&](const std::tuple<Node, int> &x) {return std::get<1>(x) != indexMax;} );

    Network_Components.erase(remove, Network_Components.end());

    std::cout << giantCom << std::endl;
    
    /*if (Network_Components.size() == 1) {
	for(auto &x: component_sizes) {
	    std::cout << x << ",";
	}
	std::cout << "\n\n\n\n";
    }*/
	
    
    //std::cout << "Total number of components: " << num << std::endl;

    std::vector<Node> Network_GiantComponent; Network_GiantComponent.reserve(giantCom);//(giantCom);
    for(int i = 0; i < giantCom; i++) Network_GiantComponent.emplace_back(std::get<0>(Network_Components[i]));

    //for(auto x: Network_GiantComponent) std::cout << x.id << std::endl;

    //new network size
    Parameters::N = giantCom; 
   
    //fix ids
    std::unordered_map<int,int> map;

    
    for(int i = 0; i < Parameters::N; i++) {
	map.emplace(Network_GiantComponent[i].id, i); //map for neighbours
	//std::cout << Network_GiantComponent[i].id << "\t" << i << std::endl;
	Network_GiantComponent[i].id = i; //change for new order
	
	
    }

    
    //change neighbours using the map
    for(int i = 0; i < Parameters::N; i++) {
	
	for (int &x: Network_GiantComponent[i].Neighbours) x = map[x];
	
    }


    //shouldnt be changed because disconnected..
    for(int i = 0; i < Parameters::N; i++) {
	assert(Network_GiantComponent[i].k == Network_GiantComponent[i].Neighbours.size());
    }
    
    //shouldnt be changed because disconnected
    for(auto x: Network_GiantComponent) {

	for(auto y: x.Neighbours){

	    assert(y < Parameters::N);
	    
	}

    }
    
    return Network_GiantComponent;
    
}


// remove from network if no connections
void RemoveZeros(std::vector<Node> &Network) {
   
    auto remove = std::remove_if(Network.begin(), Network.end(), [](const Node x) {return x.k==0;} );
 
    Network.erase(remove, Network.end());
     
    Parameters::N = Network.size();
     
    //fix ids
    std::unordered_map<int,int> map;
     
    for(int i = 0; i < Parameters::N; i++) {
	map.emplace(Network[i].id,i);
	Network[i].id = i;
    }
         
    for(int i = 0; i < Parameters::N; i++) {
        
	for (auto &x: Network[i].Neighbours) x = map[x];

    }


}



void SetUpNetwork(std::vector<Node> &Network, std::vector<int> &MortalityNodes, int OriginalN) {

    using namespace Parameters;
    
    if(NetworkType == "Random") Network = RandomNetworkFast(double(OriginalN),avgdeg/double(OriginalN));
    
    else if(NetworkType == "SmallWorld") Network = SmallWorld(OriginalN, avgdeg, 0.05);
    
    else if (NetworkType == "ScaleFree") Network = ScaleFreeNetwork(N,avgdeg/2,avgdeg/2+2,alpha); 

    RemoveZeros(Network);
    
    if (fabs(p_assortativity) > 0) {
	
	ChangeAssortivity(Network);
	
	if (Topology == "Single")
	    std::cout << "Assortative network made" << std::endl;
	
    }

    Network = CheckConnected(Network);
	
    for (auto &x: Network) x.Set_knn(Network);
	
    MortalityNodes = FindMortalityNodes(Network);
    
    OutputNetworkDegrees(Network, OriginalN);

    //OutputNetworkStructure(Network, MortalityNodes,OriginalN); //output adjacency matrix

}
