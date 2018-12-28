int Mortality(const std::vector<Node> &Network, const std::vector<int> &MortalityNodes) {

	using namespace Parameters;

	if(MortalityCondition == "OR") {


		//OR
		for(int i :  MortalityNodes) {

			if(Network[i].d == 1) return 1;

		}

		return 0;

	}

	else if (MortalityCondition == "AND"){

		//AND
		int sum = 0;
		for(int i : MortalityNodes) {
		
			sum += Network[i].d;

		}

		if(sum == MortalityNodes.size()) return 1;
		else return 0;

	}

	
	assert(false);

}

