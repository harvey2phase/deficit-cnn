#ifndef SAVEDATA_H
#define SAVEDATA_H



void OutputDataFile::SaveData(std::vector<DeficitVal> &DeficitsValues) {

    std::ios::sync_with_stdio(false);
	
    for(const auto &x: DeficitsValues) {
	
        DeficitsOut << x.age << "\t" << x.id << "\t" << x.d << "\n";
    		    
    }

    DeficitsValues.clear();

};


void OutputDeathAges(const std::vector<double> &DeathAges, int OriginalN) {

    std::string name = TempFolder() + "RawDeathAgeData" + "ID" + std::to_string(Parameters::TaskID) + SetRawName(OriginalN);
    std::ofstream Output;
    Output.open(name.c_str());

    for(double x: DeathAges) Output << x << "\n";

    Output.close();
    
}




#endif
