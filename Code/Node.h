#include <vector>


class Node {

public:

    Node(int id) : d(0), id(id), k(0), f(0), Rate(1), knn(0) {

	    Neighbours.reserve(Parameters::avgdeg + 5); //reserve just a bit more than average
		
	};

	void ConnectNode(Node &X){ //connect two nodes

	    assert(X.id != id);
	   
	    X.Neighbours.push_back(id); //add this node as a neighbour of X
	    Neighbours.push_back(X.id); //add X as a neighbour of this node

	    k = Neighbours.size();
	    X.k += 1;

	};

    	void RemoveConnection(Node &X){ //connect two nodes

	    assert(X.id != id);

	    auto idX = std::find( Neighbours.begin(), Neighbours.end(), X.id);
	    assert(idX != Neighbours.end());
	    Neighbours.erase(idX);
	    k--;
	    

	    auto id_cur = std::find(X.Neighbours.begin(), X.Neighbours.end(), id);
	    assert(id_cur != X.Neighbours.end());
	    X.Neighbours.erase(id_cur);
	    X.k--;
	    

	};

	void Reset() { //reset network for single topology runs

		Rate = 1;
		d = 0;
		f = 0;

	};

    
    void Set_knn(const std::vector<Node> &Network) {

	assert(k != 0);
	
	knn = 0.0;
	for(auto x: Neighbours) knn += Network[x].k;

	knn = knn/double(k);

    }
	
    std::vector<int> Neighbours; //list of neighbour ids
    int d, id, k; //d deficit, id node number, k number of neighbours
    double f, Rate; //local frailty, rate
    double knn; //average nearest neighbour degree
    
};


