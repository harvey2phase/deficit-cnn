
//find node to attach given connectivity
int FindNode(EventTree<double> &tree) {

    double val = tree.TotalSum * RNG(g1);

    return  tree.Search(val);

}




//create a scale free network from the BA algorithm
std::vector<Node> ScaleFreeNetwork(int N, int m, int m0, double alpha) {
    
    std::vector<Node> Network;
    Network.reserve(N+1); 
    EventTree<double> tree(N, 0);

    //set up initial nodes
    Network.emplace_back(0);
    double lambda = (alpha-3) * m;
    double SumOfDegrees = 0;

    for(int i = 1; i < m0; i++) {

        Network.emplace_back(i);
        for(int j = 0; j < i; j++) {

            Network[i].ConnectNode(Network[j]);
            tree.Update(i,Network[i].k + lambda);
            tree.Update(j,Network[j].k + lambda);

        }

    }

    std::vector<int> ConnectTo(m,0);

    //create other nodes
    for(int i = m0; i < N; i++) {
        
        for(int j = 0; j < m; j++) {

            int newConnection = FindNode(tree);
	    while(std::find(ConnectTo.begin(), ConnectTo.end(), newConnection) != ConnectTo.end()) {
	        newConnection = FindNode(tree);
		}

	    ConnectTo[j] = newConnection;
	    
        }

        Network.emplace_back(i);
        for(auto x: ConnectTo) {
            Network[i].ConnectNode(Network[x]);
            tree.Update(i,Network[i].k + lambda);
            tree.Update(x,Network[x].k + lambda);
        }

    }

    return Network;

}


/*
//create a scale free network from the BA algorithm
auto ScaleFreeNetwork_Links(int N, int m, int m0, double alpha) {

    std::vector<std::vector<int>> Links; Links.reserve(m * N);
    
    std::vector<Node> Network;
    Network.reserve(N+1); 
    EventTree<double> tree(N, 0);

    //set up initial nodes
    Network.emplace_back(0);
    double lambda = (alpha-3) * m;
    double SumOfDegrees = 0;

    for(int i = 1; i < m0; i++) {

        Network.emplace_back(i);
        for(int j = 0; j < i; j++) {

            Network[i].ConnectNode(Network[j]);
	    Links.emplace_back({i,j});
            tree.Update(i,Network[i].k + lambda);
            tree.Update(j,Network[j].k + lambda);

        }

    }

    std::vector<int> ConnectTo(m,0);

    //create other nodes
    for(int i = m0; i < N; i++) {
        
        for(int j = 0; j < m; j++) {

            int newConnection = FindNode(tree);
	    while(std::find(ConnectTo.begin(), ConnectTo.end(), newConnection) != ConnectTo.end()) {
	        newConnection = FindNode(tree);
		}

	    ConnectTo[j] = newConnection;
	    
        }

        Network.emplace_back(i);
        for(auto x: ConnectTo) {
            Network[i].ConnectNode(Network[x]);
	    Links.emplace_back({i,x.id});
            tree.Update(i,Network[i].k + lambda);
            tree.Update(x,Network[x].k + lambda);
        }

    }

    return std::make_tuple(Network,Links);

}
*/
