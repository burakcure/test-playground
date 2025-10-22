#include "Matrix.h"
#include <gtest/gtest.h>


static std::pair<Matrix, Matrix> sample_matrices() {
    Matrix a(2, 2);
    Matrix b(2, 2);
    a.data = {{1, 2}, {3, 4}};
    b.data = {{5, 6}, {7, 8}};
    return {a, b};
}

TEST(MatrixTest, ConstructionCorrectness) {
    Matrix a(1, 1);
    std::vector<std::vector<int>> expected = {{0}};
    EXPECT_EQ(a.data, expected) << "Matrix construction result is incorrect.";
}

TEST(MatrixTest, AdditionCorrectness) {
    auto [a, b] = sample_matrices();
    Matrix result = a + b;
    std::vector<std::vector<int>> expected = {{6, 8}, {10, 12}};
    EXPECT_EQ(result.data, expected) << "Matrix addition result is incorrect.";
}

TEST(MatrixTest, AdditionIncompatibleSizes) {
    Matrix a(2, 2);
    Matrix b(3, 2);
    Matrix result = a + b;
    EXPECT_TRUE(result.data.empty() || result.data[0].empty())
        << "Addition with incompatible sizes should return an empty matrix.";
}

TEST(MatrixTest, MultiplicationCorrectness) {
    auto [a, b] = sample_matrices();
    Matrix result = a * b;
    std::vector<std::vector<int>> expected = {{19, 22}, {43, 50}};
    EXPECT_EQ(result.data, expected) << "Matrix multiplication result is incorrect.";
}
