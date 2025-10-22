#ifndef MATRIX_H
#define MATRIX_H

#include <vector>
using namespace std;

class Matrix {
public:
    vector<vector<int>> data;
    int rows;
    int columns;

    Matrix(int row=0,int column=0);
    Matrix operator+(const Matrix& b);
    Matrix operator*(const Matrix& b);
};

#endif
