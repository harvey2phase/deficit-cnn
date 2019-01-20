

//performs damage/repair on the node "NodeIndex"
//and increments event time
void UpdateNode(Node &X, double &Time, double TotalRate, std::vector<DeficitVal> &DeficitsValues) {

    //perform event
    Time += TimeToEvent(TotalRate);
    X.d = (X.d + 1)%2; //0->1, 1->0

    if (SimulateVar::MortalityOnly_bool == false)
	DeficitsValues.emplace_back(Time, X.id, X.d);

}

//update local frailty of a node after updating it
void UpdateLocalFrailty(std::vector<Node> &Network, Node &X) {

	double sum = 0;

	//update neighbours
	for(auto i: X.Neighbours) {

		sum += Network[i].d; 
		if(X.d == 0) Network[i].f -= 1.0/Network[i].k;
		if(X.d == 1) Network[i].f += 1.0/Network[i].k;

	} 

	//update this node
	X.f = sum/X.k;

}
