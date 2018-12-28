template <typename T>
class EventTree {

public:

    //initialize tree
    EventTree(int N, T InitialRate){

        ntotal = 0;
        offset = 0;
        nevents = N;

        int nround = 1;
        while (nround < nevents) nround *= 2;

        offset = nround - 1; //where propensities start as leaves of tree
        nround = 2*nround - 1;
        ntotal = nround;

        tree.resize(ntotal, InitialRate); //set tree size

        //set rates
        for (int i = offset; i < offset + nevents; i++) tree[i] = InitialRate; 

        //perform initial sum to set up tree structure
        SumTree();


    };


    void OutputRates() {

        for (int i = offset; i < offset + nevents; i++) std::cout << tree[i] << "\n"; 

    };


    //perform initial sum to set up tree structure
    void SumTree() {

        int child1,child2;
        for (int parent = offset-1; parent >= 0; parent--) {
            child1 = 2*parent + 1;
            child2 = 2*parent + 2;
            tree[parent] = tree[child1] + tree[child2];
        }

        TotalSum = tree[0];

    };

    //change the rate of event i to value
    void Update(int i, T value) {

        int parent,sibling;


        tree[offset+i] = value;

        // I walks tree from leaf to root, summing children at each step
        // left child is odd index, right child is even index

        i += offset;
        while (i > 0) {

            if (i % 2) sibling = i + 1;
            else sibling = i - 1;

            parent = (i-1)/2;
            tree[parent] = tree[i] + tree[sibling];
            i = parent;

        }

        TotalSum = tree[0];

    };

    

    int Search(T value) {
        int i,leftchild;

        // I walks tree from root to appropriate leaf
        // value is modified when right branch of tree is traversed

        i = 0;
        while (i < offset) {
            leftchild = 2*i + 1;
            if (value <= tree[leftchild]) i = leftchild;
            else {
                value -= tree[leftchild];
                i = leftchild + 1;
            }
        }     


        return i - offset;
    }


    //reset entire tree to Value
    void ResetTree(T Value) {

        for(auto &x: tree) x = 0;

        //set rates
        for (int i = offset; i < offset + nevents; i++) tree[i] = Value; 

        //perform initial sum to set up tree structure
        SumTree();

    };



    std::vector<T> tree; //tree + propensities
    int nevents; // # of propensities (unrounded)
    int ntotal; // # of propensities (rounded up to power-of-2) + tree          
    int offset; // index where propensities start as leaves of tree
    T TotalSum;

};
