
namespace Vector2D {



template <typename T>
class vector {

public:

	vector(int SizeX, int SizeY, T Default = 0) : SizeX(SizeX), SizeY(SizeY), Contents(SizeX*SizeY, Default) {};

	//set up indicies to access elements as if it were a vector<vector>>
    inline T &operator()(int i, int j) {

    	return Contents[i*SizeY + j];

    }

    int size() {

	return SizeX * SizeY;

    }	

    std::vector<T> Contents;

    int SizeX, SizeY;

};





}

