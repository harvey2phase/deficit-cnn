std::vector<Node> SmallWorld(int N, int avg, double pRewire) {

    
    std::vector<Node> Network;
    Network.reserve(N+1);

    for(int i = 0; i < N; i++) {

	Network.emplace_back(i);

    }

    //create regular ring network
    std::vector<std::tuple<int,int>> connections_list; connections_list.reserve(4*N);
    Vector2D::vector<double> connections(N,N);
    for(int i = 0; i < N; i++) {
	
	for(int j = i+1; j < N; j++) {
	    
	    int distance = (j - i) % (N - 1 - avg/2);
	    
	    if (distance <= avg/2 && distance > 0 && i != j) {

		assert(i != j);
		Network[i].ConnectNode(Network[j]);
		connections_list.emplace_back(i,j);

		connections(i,j) = 1;
		connections(j,i) = 1;
		
	    }
	    
	}
	
    }


    //randomly reqire
    
    for(const auto &x: connections_list) {

	int i = std::get<0>(x);
	int j = std::get<1>(x);
	
	if(RNG(g1) < pRewire) {

	    //remove link
	    auto id1 = std::find( (Network[i].Neighbours).begin(), (Network[i].Neighbours).end(), j);
	    assert(id1 != Network[i].Neighbours.end());
	    Network[i].Neighbours.erase(id1);
	    Network[i].k--;
	
	    auto id0 = std::find(Network[j].Neighbours.begin(), Network[j].Neighbours.end(), i);
	    assert(id0 != Network[j].Neighbours.end());
	    Network[j].Neighbours.erase(id0);
	    Network[j].k--;

	    //add new random link
	    int k;
	    while(true) {

		k = floor(RNG(g1) * N);

		if(connections(i,k) == 0 && connections(k,i) == 0 && k != i && i != j)
		    break;
		
	    }

	    assert(i != k);
	    
	    Network[i].ConnectNode(Network[k]);

	    connections(i,k) = 1;
	    connections(k,i) = 1;
	    connections(i,j) = 0;
	    connections(j,i) = 0;
		    
	}
	    
    }

    return Network;

}

