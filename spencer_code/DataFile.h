//set the names of these here so only this part needs to be changed if the names need to be changed
class DataFile {

public:

    DataFile(int NNodes = Parameters::N) {
	
	DeathAgesName = TempFolder() + "RawDeathAges" + "ID" + std::to_string(Parameters::TaskID) + SetRawName(NNodes);
	DeficitsName = TempFolder() + "RawDeficits" + "ID" + std::to_string(Parameters::TaskID) + SetRawName(NNodes);

	
    };
    
    std::string DeathAgesName; 
    std::string DeficitsName;

};

