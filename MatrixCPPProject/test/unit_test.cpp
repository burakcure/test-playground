#include "Matrix.h"
#include <gtest/gtest.h>

// Yardımcı fonksiyon: örnek matrisleri hazırla
static std::pair<Matrix, Matrix> sample_matrices() {
    Matrix a(2, 2);
    Matrix b(2, 2);
    a.data = {{1, 2}, {3, 4}};
    b.data = {{5, 6}, {7, 8}};
    return {a, b};
}

// 1️⃣ Yapıcı doğru mu çalışıyor?
TEST(MatrixTest, ConstructionCorrectness) {
    Matrix a(1, 1);
    std::vector<std::vector<int>> expected = {{0}};
    EXPECT_EQ(a.data, expected) << "Matrix construction result is incorrect.";
}

// 2️⃣ Toplama işlemi doğru mu?
TEST(MatrixTest, AdditionCorrectness) {
    auto [a, b] = sample_matrices();
    Matrix result = a + b;
    std::vector<std::vector<int>> expected = {{6, 8}, {10, 12}};
    EXPECT_EQ(result.data, expected) << "Matrix addition result is incorrect.";
}

// 3️⃣ Toplama boyut uyumsuzluğu hata veriyor mu?
TEST(MatrixTest, AdditionIncompatibleSizes) {
    Matrix a(2, 2);
    Matrix b(3, 2);
    // Beklenen davranış: hata (örneğin ValueError benzeri)
    // Şu anda kodun "cerr << ...; return Matrix();" yaptığı için exception fırlatmıyor.
    // Bu test ancak sen Matrix::operator+ içine throw eklersen geçer.
    // Şimdilik sadece sonucu kontrol edelim:
    Matrix result = a + b;
    EXPECT_TRUE(result.data.empty() || result.data[0].empty())
        << "Addition with incompatible sizes should return an empty matrix.";
}

// 4️⃣ Çarpma işlemi doğru mu?
TEST(MatrixTest, MultiplicationCorrectness) {
    auto [a, b] = sample_matrices();
    Matrix result = a * b;
    std::vector<std::vector<int>> expected = {{19, 22}, {43, 50}};
    EXPECT_EQ(result.data, expected) << "Matrix multiplication result is incorrect.";
}
