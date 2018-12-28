//makes network more assortative
//controled by p, smaller p -> most assortative, and larger # of iterations
//from Brunet Sokolov 2004 PRE
void ChangeAssortivity(std::vector<Node> &Network) {

    using Parameters::N;

    bool disassortative;
    if(Parameters::p_assortativity > 0)
	disassortative = false;
    else if(Parameters::p_assortativity < 0) {
	disassortative = true;
    }
    
    double p = fabs(Parameters::p_assortativity);
    std::vector<int> ids(4);
    int tempId;
    
    for(int inum = 0; inum < N * N; inum++) {
	//std::cout << inum << "\n";
	//find random unique ids
	while(true) {
	    
	    ids[0] = RNG(g1) * N; //random node
	    assert(Network[ids[0]].k > 0);
	    tempId = Network[ids[0]].k * RNG(g1); 
	    ids[1] = Network[ids[0]].Neighbours[tempId]; //random node its attached to
	    assert(Network[ids[1]].k > 0);

	    while (true) {
		ids[2] = RNG(g1) * N;
		if(ids[2] != ids[0] && ids[2] != ids[1])
		    break;
	    }
	    assert(Network[ids[2]].k > 0 && ids[2] != ids[0] && ids[2] != ids[1]);
	    tempId = Network[ids[2]].k * RNG(g1); 
	    ids[3] = Network[ids[2]].Neighbours[tempId];
	    assert(Network[ids[3]].k > 0);

	    auto tempIds = ids;
	    std::sort(tempIds.begin(), tempIds.end());
	    int count = 0;
	    int past = -1;
	    for(int x: tempIds) {
		if(x != past ) {
		    count++;
		    past = x;
		}
	    }
	    
	    if(count == 4) break;
		
	}



	//remove first link
	auto id1 = std::find( (Network[ids[0]].Neighbours).begin(), (Network[ids[0]].Neighbours).end(), ids[1]);
	assert(id1 != Network[ids[0]].Neighbours.end());
	Network[ids[0]].Neighbours.erase(id1);
	Network[ids[0]].k--;
	
	auto id0 = std::find(Network[ids[1]].Neighbours.begin(), Network[ids[1]].Neighbours.end(), ids[0]);
	assert(id0 != Network[ids[1]].Neighbours.end());
	Network[ids[1]].Neighbours.erase(id0);
	Network[ids[1]].k--;

	
	//remove second link
	auto id3 = std::find(Network[ids[2]].Neighbours.begin(), Network[ids[2]].Neighbours.end(), ids[3]);
	assert(id3 != Network[ids[2]].Neighbours.end());
	Network[ids[2]].Neighbours.erase(id3);
	Network[ids[2]].k--;
	
	auto id2 = std::find(Network[ids[3]].Neighbours.begin(), Network[ids[3]].Neighbours.end(), ids[2]);
	assert(id2 != Network[ids[3]].Neighbours.end());
	Network[ids[3]].Neighbours.erase(id2);
	Network[ids[3]].k--;

	
	
	if (RNG(g1) < p) {
	    
	    std::sort(ids.begin(), ids.end(), [&](int x, int y){ //sort ascending
		    return Network[x].k < Network[y].k;  
		}); 

	    if (disassortative == false) {
		Network[ids[0]].ConnectNode(Network[ids[1]]); //make assortative
		Network[ids[2]].ConnectNode(Network[ids[3]]);
	    }
	    else {
		Network[ids[0]].ConnectNode(Network[ids[3]]);
		Network[ids[1]].ConnectNode(Network[ids[2]]);
	    }
	}

	//randomly rewire
	else {

	    std::shuffle(ids.begin(), ids.end(), g1);

	    Network[ids[0]].ConnectNode(Network[ids[1]]);
	    Network[ids[2]].ConnectNode(Network[ids[3]]);
		
	}

    }


}
