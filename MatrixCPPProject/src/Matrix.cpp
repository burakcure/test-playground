#include "Matrix.h"
#include <iostream>
using namespace std;

Matrix::Matrix(int row, int column) {
    rows = row;
    columns = column;
    data.resize(rows, vector<int>(columns, 0));
}

Matrix Matrix::operator+(const Matrix& b) {
    if (b.rows != rows || b.columns != columns) {
        cerr << "Matrix sizes not compatible for addition!\n";
        return Matrix();
    }

    Matrix result(rows, columns);
    for (int i = 0; i < rows; i++) {
        for (int k = 0; k < columns; k++) {
            result.data[i][k] = data[i][k] + b.data[i][k];
        }
    }
    return result;
}

Matrix Matrix::operator*(const Matrix& b) {
    if (columns != b.rows) {
        cerr << "Matrix sizes not compatible for multiplication!\n";
        return Matrix();
    }

    Matrix result(rows, b.columns);
    for (int i = 0; i < rows; i++) {
        for (int k = 0; k < b.columns; k++) {
            for (int j = 0; j < columns; j++) {
                result.data[i][k] += data[i][j] * b.data[j][k];
            }
        }
    }
    return result;
}
