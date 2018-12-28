


/*
Random Network

Create N isolated nodes, and then connect ecah node wit probablilty p
The average degree is pN

*/
std::vector<Node> RandomNetwork(int N, double p) {

    std::vector<Node> Network;
    Network.reserve(N+1);

    for(int i = 0; i < N; i++) {

	Network.emplace_back(i);

    }


    for(int i = 0; i < N; i++) {

	for(int j = i + 1; j < N; j++) {

	    if (RNG(g1) < p && i != j) {

		Network[i].ConnectNode(Network[j]);	

	    }

	}

	if(Network[i].k == 0) Network[i].ConnectNode( Network[int(floor(RNG(g1) * i))] );	


    }

    return Network;

}


std::vector<Node> RandomNetworkFast(int N, double p) {

    std::vector<Node> Network;
    Network.reserve(N+1);

    for(int i = 0; i < N; i++) {

	Network.emplace_back(i);
	
    }
    
    int v = 1;
    int w = -1;
	
    while(v < N) {

	w += 1 + int(floor(log(1 - RNG(g1))/log(1 - p)));

	while(w >= v && v < N) {

	    w = w -v;
	    v += 1;
	}
	
	if(v < N) {

	    Network[v].ConnectNode(Network[w]);

	    
	}
	    
    }

    return Network;

}
