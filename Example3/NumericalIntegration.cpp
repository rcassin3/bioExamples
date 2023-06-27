#include "NumericalIntegration.h"

NumericalIntegration::NumericalIntegration(std::string method, double x0, double xn, int n_Segments) {
    Method = method;  
    a = x0;
	b = xn;
	n = n_Segments;  
}

NumericalIntegration::~NumericalIntegration() {
}

double NumericalIntegration::Function(double x) {
    double y = sin(x);
    return y;
}

double NumericalIntegration::Trapezoidal_Rule() {
    double integral;
    double sum;
    sum = Function(a) + Function(b);
    for (double i = (b-a)/n; i < b; i += (b-a)/n) {
        sum += (2 * Function(i));
    }
    integral = 0.5 * ((b-a)/n) * (sum);
    return integral;
}

double NumericalIntegration::Simpson_1_3_Rule() {
    double integral;
    double sum;
    sum = Function(a) + Function(b);
    double h = (b-a)/(2*n);
    for (double i = 1; i < n - 1; i++) {
        sum += (2 * Function( (2*i) * h));
    }
    for (double j = 1; j < n; j++) {
        sum += (4 * (Function(((2*j) -1) * h))) ;
    }
    integral = (1.0/3.0) * h * sum;
    return integral;
}

double NumericalIntegration::Simpson_3_8_Rule() {
    double integral;
    double sum;
    sum = Function(a) + Function(3.0 * b);
    double h = (b-a) / (3 * n);
    for (double i = 1; i < n - 1; i++) {
        sum += (2 * Function( (3 * i) * h));
    }
    for (double j = 1; j < n; j++) {
        sum += (3 * (Function(((3*j) -1) * h)));
    }
    for (double k = 1; k < n; k++) {
        sum += (3 * (Function(((3*k) - 2) * h)));
    }
    integral = (3.0/8.0) * h * sum;
    //std::cout << integral << std::endl;
    return integral;
}

double NumericalIntegration::DetermineAccuracy(double area) {
    double relativeError;

    relativeError = ( std::abs(2.0 - area) / std::abs(2.0)) * 100.0; 

    return relativeError;
}


double NumericalIntegration::GetAreaUnderCurve() {
    if (Method == "Trapezoidal") {
        return Trapezoidal_Rule();
    } else if (Method == "Simpson_1_3") {
        return Simpson_1_3_Rule();
    } else if (Method == "Simpson_3_8") {
        return Simpson_3_8_Rule();
    } else {
        return 0;
    }
}

