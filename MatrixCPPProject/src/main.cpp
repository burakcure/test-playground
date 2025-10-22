#include <iostream>
#include "Matrix.h"
#include "matrix.cpp"
using namespace std;

int main() {
    Matrix A(2, 2);
    Matrix B(2, 2);

    A.data = {{1, 2}, {3, 4}};
    B.data = {{5, 6}, {7, 8}};

    Matrix C = A + B;
    Matrix D = A * B;

    cout << "C (A+B):" << endl;
    for (auto& row : C.data) {
        for (auto& val : row) cout << val << " ";
        cout << endl;
    }

    cout << "D (A*B):" << endl;
    for (auto& row : D.data) {
        for (auto& val : row) cout << val << " ";
        cout << endl;
    }
}
