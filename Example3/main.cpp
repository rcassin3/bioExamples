#include <iostream>
#include "NumericalIntegration.h"

int main() {
  // you can adjust the values a = 0, b = 3.141592645, and n = 1000 as required
    double x1 = 0;
    double x2 = 3.141592645;
    int slices = 1000;
	NumericalIntegration Area1("Trapezoidal", x1, x2, slices);
	NumericalIntegration Area2("Simpson_1_3", x1, x2, slices);
	NumericalIntegration Area3("Simpson_3_8", x1, x2, slices);
	double area = 0;
    
	std::cout.precision(8);
    
    std::cout << "Trapezoidal rule:" << std::endl;
    if (!(Area1.GetErrorStatus())) {
		area = Area1.GetAreaUnderCurve();
		std::cout << "The area under the curve = " << area << " and the accuracy = " << Area1.DetermineAccuracy(area) << std::endl;
	} 

    
	std::cout << "Simpson's 1/3 rule:" << std::endl;
	if (!(Area2.GetErrorStatus())) {
		area = Area2.GetAreaUnderCurve();
		std::cout << "The area under the curve = " << area << " and the accuracy = " << A+rea2.DetermineAccuracy(area) << std::endl;
	}

    
	std::cout << "Simpson's 3/8 rule:" << std::endl;
	if (!(Area3.GetErrorStatus())) {
		area = Area3.GetAreaUnderCurve();
		std::cout << "The area under the curve = " << area << " and the accuracy = " << Area3.DetermineAccuracy(area) << std::endl;
	}
    return 0;
}


 