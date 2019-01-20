#include <vector>


//Time to an event given the rates
double TimeToEvent(double TotalRate) {
    
    using namespace Parameters;
    return -1.0/TotalRate * log(RNG(g1));

}


//repair rate given parameters and local frailty
double DamageRate(double f) {

    using namespace Parameters;
    return exp(gammap * f);

}


//Damage rate given parameters and local frailty
double RepairRate(double f) {

    using namespace Parameters;
    return 1/R * exp(-gamman * f);

}

//calculate and set the rate of a node and all of its neighbours, as well as the
//cumulative rate
void CalculateRates(std::vector<Node> &Network, Node &X, EventTree<double> &tree, int j, double &TotalRate) {

    for(int i: X.Neighbours) {

	//remove current from total rate
        TotalRate -= Network[i].Rate;

        //update rates on the network
        if(Network[i].d == 0) Network[i].Rate = DamageRate(Network[i].f); 
        else if(Network[i].d == 1) Network[i].Rate = RepairRate(Network[i].f); 

        //update rates on the tree
        tree.Update(i, Network[i].Rate);

        //update new total rate
        TotalRate += Network[i].Rate;
	//std::cout << i << "\t" << Network[i].id << "\t" << j << "\t" << Network[j].id << std::endl;
	/*if( i == X.id)
	  std::cout << Network[i].k << "\t" << Network[X.id].k << std::endl;*/
	//assert(i != X.id);

    }


    //update the X node
    TotalRate -= X.Rate;
    if(X.d == 0) X.Rate = DamageRate(X.f); 
    else if(X.d == 1) X.Rate = RepairRate(X.f); 

    tree.Update(j, Network[j].Rate);

    TotalRate += X.Rate;

}


//finds rate and returns index of rate to be performed
int FindRate(EventTree<double> &tree, double TotalRate) {

    double val = TotalRate * RNG(g1) ; //temp

    int i = tree.Search(val);
    assert(i < Parameters::N);
    
    return i;

}




