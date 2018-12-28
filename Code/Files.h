//turn doubles into strings without the trailling zeros
std::string to_string(double x) {

    std::string temp = std::to_string(x);
    temp.erase ( temp.find_last_not_of('0') + 1, std::string::npos );
    if(*temp.rbegin() == '.') temp = temp + '0';
    return temp;

}

//turn ints into strings
std::string to_string(int x) { return std::to_string(x);}




//tag to append to filenames to indicate parameters
std::string SetName() {

    using namespace Parameters;

    return "q" + to_string(fnRate) + "p" + to_string(fpRate) + "Gammap" + to_string(gammap) + "Gamman" + to_string(gamman) + "N"
	+ std::to_string(N) + "n" + std::to_string(n) + "FIn" + std::to_string(FIn) + "Number" + std::to_string(int(MaxRuns * Number)) + "R" + to_string(R)
	+ "nd" + std::to_string(nd) +"Alpha"+ to_string(alpha) +"AvgDeg"+std::to_string(avgdeg)
        + MortalityCondition + Topology + "SingleSeed" + std::to_string(SingleSeed)
	+ NetworkType + "PeakAge" + to_string(PeakAge) + "pA" + to_string(p_assortativity);

}

//tag to append to filenames to indicate parameters
std::string SetRawName(int NNodes = Parameters::N) {

    using namespace Parameters;

    return "Gammap" + to_string(gammap) + "Gamman" + to_string(gamman) + "N"
	+ std::to_string(NNodes)  + "Number" + std::to_string(int(Number)) + "R" + to_string(R)
	+ "nd" + std::to_string(nd) +"Alpha"+ to_string(alpha) +"AvgDeg"+std::to_string(avgdeg) + MortalityCondition + Topology + "SingleSeed" + std::to_string(SingleSeed) + NetworkType + "pA" + to_string(p_assortativity);

}


//set the folder to output Data to
std::string SetFolder() {
	
    if (Parameters::Folder == "Local")
	return "Data/";
    else
	return "../scratch/RawData/" + Parameters::Folder + "/";
	
}

//folder for temporary raw Data
std::string TempFolder() {

    if (Parameters::Folder == "Local")
	return "Data/";
    else
	return "../scratch/TempData/" + Parameters::Folder + "/";

}

//check if a file exists
inline bool FileExists (const std::string& name) {
    std::ifstream f(name.c_str());
    return f.good();
}

