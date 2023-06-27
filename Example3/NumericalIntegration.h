#ifndef NUMERICALINTEGRATION_H_
#define NUMERICALINTEGRATION_H_
#include <string>
#include <iostream>
#include <cmath>

class NumericalIntegration {
	double a = 0;
	double b = 0;
	double* y = NULL;
	double Accuracy;
	bool Error = false;
	int n = 1;
	double Function(double);
	double Trapezoidal_Rule();
	double Simpson_1_3_Rule();
	double Simpson_3_8_Rule();
	std::string Method;
public:
	NumericalIntegration(std::string, double, double, int);
	~NumericalIntegration();
	double GetAreaUnderCurve();   
	double DetermineAccuracy(double);
	bool GetErrorStatus() { return Error; };
};

#endif

