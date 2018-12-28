#ifndef PARAMETERS_H
#define PARAMETERS_H


//All global parameters used.
//Initialized with cmdline arguments by SetParameters(argc, argv)
namespace Parameters {
	
    //Variable parameters
    double R; //Ratio of damage to repair
    int N; //Number of nodes in the network
    double gammap; //Damage rate constant
    double gamman; //repair rate constant
    int n; //number of frailty indicies
    int FIn; //number of nodes per frailty Index
    int nd; //Number of mortality nodes
    int Number; //Number of runs per job 
    double alpha; //scale free distribution exponent
    int avgdeg; //average node degree 
    std::string MortalityCondition; //"OR" or "AND"
    std::string Topology; //"Random" sampled topology or "Single" for all runs
    std::string Folder; //Acenet or local
    std::string NetworkType; //"Random" or "ScaleFree"
    int TaskID; //ID used for many simulaneous jobs
    int SingleSeed; //Seed used to make the single topology
    double PeakAge;
    int RealSeed; //Seed used
    int AnalysisFI; //which FI out of n are we using for the main analysis.
    double p_assortativity;
    double fpRate; //False positive rate, sets a lower limit on fi distributions
    double fnRate; //False negative rate, sets a upper limit on fi distributions
    int FIclass; // 0 is high, 1 is low, and 2 is combined
    int BinaryMortalityTime; //mortality in this number of years is 1
    
    //other parameters, not in the name (i.e. not going to be varied much/often/together)
    double FrailtyIncrement; //Increment of frailty used for calculation of average entropies
    int AgeIncrement = 5; //Increment of frailty used for calculation of average entropies

    int NumberOfBootstraps = 0; //Number of bootstrap samples for entropy errorbars
    int MaxRuns = 1;

    int IFIbins;
    
}	


//get parameters from cmd line and set them
void SetParameters(int argc, char *argv[]) {

	using namespace Parameters;

	Number = atoi(argv[1]); std::cout << "Number: " << Number;
	R = atof(argv[2]); std::cout << ", R: " << R;
	gammap = atof(argv[3]); std::cout << ", gammap: " << gammap;
	gamman = atof(argv[4]); std::cout << ", gamman: " << gamman;
	N = atoi(argv[5]); std::cout << ", N: " << N;
	nd = atoi(argv[6]); std::cout << ", nd: " << nd;
	alpha = atof(argv[7]); std::cout << ", alpha: " << alpha;
	avgdeg = atoi(argv[8]); std::cout << ", avgdeg: " << avgdeg;
	MortalityCondition = argv[9]; std::cout << ", MortalityCondition: " << MortalityCondition;
	Topology = argv[10]; std::cout << ", Topology: " << Topology;
	Folder = argv[11]; 
	NetworkType = argv[12]; std::cout << ", NetworkType: " << NetworkType;
	TaskID = atoi(argv[13]); std::cout << ", TaskID: " << TaskID;
	SingleSeed = atoi(argv[14]);  std::cout << ", SingleSeed: " << SingleSeed;
        p_assortativity = atof(argv[15]);  std::cout << ", p_assortativity: " << p_assortativity;


	FrailtyIncrement = 1.0/FIn;
   
	std::cout << std::endl;
	std::cout << std::endl;
	

	std::ifstream SeedFile;
	SeedFile.open("SeedFile");
	int lineCounter = 0;
	int Seed;
	SeedFile >> Seed;
	while(lineCounter < TaskID) {

	    SeedFile >> Seed;
	    lineCounter++;
	    
	}
	
	std::cout << "Seed: " << Seed << std::endl;
	RealSeed = Seed;

	SeedFile.close();
	
	
}



//get parameters from cmd line and set them
void SetParametersAnalysis(int argc, char *argv[]) {

	using namespace Parameters;

	Number = atoi(argv[1]); std::cout << "Number: " << Number;
	R = atof(argv[2]); std::cout << ", R: " << R;
	gammap = atof(argv[3]); std::cout << ", gammap: " << gammap;
	gamman = atof(argv[4]); std::cout << ", gamman: " << gamman;
	N = atoi(argv[5]); std::cout << ", N: " << N;
	n = atoi(argv[6]); std::cout << ", n: " << n;
	FIn = atoi(argv[7]); std::cout << ", FIn: " << FIn;
	nd = atoi(argv[8]); std::cout << ", nd: " << nd;
	alpha = atof(argv[9]); std::cout << ", alpha: " << alpha;
	avgdeg = atoi(argv[10]); std::cout << ", avgdeg: " << avgdeg;
	MortalityCondition = argv[11]; std::cout << ", MortalityCondition: " << MortalityCondition;
	Topology = argv[12]; std::cout << ", Topology: " << Topology;
	Folder = argv[13]; 
	NetworkType = argv[14]; std::cout << ", NetworkType: " << NetworkType;
	TaskID = atoi(argv[15]); std::cout << ", Starting TaskID: " << TaskID;
	SingleSeed = atoi(argv[16]);  std::cout << ", SingleSeed: " << SingleSeed;
	fnRate = atof(argv[17]);  std::cout << ", fnRate: " << fnRate;
	fpRate = atof(argv[18]);  std::cout << ", fpRate: " << fpRate;
	PeakAge = atof(argv[19]);  std::cout << ", PeakAge: " << PeakAge;
        p_assortativity = atof(argv[20]);  std::cout << ", p_assortativity: " << p_assortativity;
	FIclass = atoi(argv[21]);  std::cout << ", FIclass: " << FIclass;
	BinaryMortalityTime = atoi(argv[22]);  std::cout << ", BinaryMortalityTime: " << BinaryMortalityTime;
	IFIbins = atoi(argv[23]);  std::cout << ", IFIbins: " << IFIbins;
   
	std::cout << std::endl;
	std::cout << std::endl;
	
	/*
	std::ifstream SeedFile;
	SeedFile.open("SeedFile");
	int lineCounter = 0;
	int Seed;
	SeedFile >> Seed;
	while(lineCounter < TaskID) {

	    SeedFile >> Seed;
	    lineCounter++;
	    
	}
	
	std::cout << "Seed: " << Seed << std::endl;
	RealSeed = Seed;

	SeedFile.close();
	*/
	
}


namespace SimulateVar {

    bool MortalityOnly_bool = false;


}


namespace AnalysisVar {

    bool IFI_bool = false;
    bool Spectrum_bool = false;
    bool knnDamDist_bool = false;
    bool multipleDeficits_bool = false;
    bool IDF_bool = false;
    bool outputDeathAgeDists_bool = false;
    bool outputFrailtyDists_bool = false;
    bool entropyFI_bool = false;
    bool percentile_bool = false;
    bool propDegreeDamaged_bool = false;
    bool timeDamaged_bool = false;
    bool timeDamaged_Distributions_bool = false;
    bool binary_FI_Information_bool = false;
    bool continousFIinformation_bool = false;
    bool fixedGamma0_bool = false;
    bool trajectories_bool = false;

}


void SetAnalysis() {


    std::ifstream File;
    File.open("CommandFile.txt");
    std::string line;

    while(std::getline(File, line)){

	std::cout << line << std::endl;

	if(line == "IFI") AnalysisVar::IFI_bool = true;
	if(line == "Spectrum") AnalysisVar::Spectrum_bool = true;
	if(line == "knnDamDist") AnalysisVar::knnDamDist_bool = true;
	if(line == "multipleDeficits") AnalysisVar::multipleDeficits_bool = true;
	if(line == "IDF") AnalysisVar::IDF_bool = true;
	if(line == "outputDeathAgeDists") AnalysisVar::outputDeathAgeDists_bool = true;
	if(line == "outputFrailtyDists") AnalysisVar::outputFrailtyDists_bool = true;
	if(line == "entropyFI") AnalysisVar::entropyFI_bool = true;
	if(line == "percentile") AnalysisVar::percentile_bool = true;
	if(line == "propDegree") AnalysisVar::propDegreeDamaged_bool = true;
	if(line == "timeDamaged") AnalysisVar::timeDamaged_bool = true;
	if(line == "timeDamagedDistribution") AnalysisVar::timeDamaged_Distributions_bool = true;
	if(line == "binaryFInformation") AnalysisVar::binary_FI_Information_bool = true;
	if(line == "continousFIinformation") AnalysisVar::continousFIinformation_bool = true;
	if(line == "fixedGamma0") AnalysisVar::fixedGamma0_bool = true;
	if(line == "trajectories") AnalysisVar::trajectories_bool = true;
	
    }
		
    File.close();

}


void SetSimulate() {


    std::ifstream File;
    File.open("CommandFile_Simulate.txt");
    std::string line;

    while(std::getline(File, line)){

	std::cout << line << std::endl;

	if(line == "MortalityOnly") SimulateVar::MortalityOnly_bool = true;
	
    }
		
    File.close();

}





#endif
