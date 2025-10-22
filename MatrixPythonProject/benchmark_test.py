# benchmark_test.py
from matrix import Matrix
import numpy as np
import pytest

@pytest.mark.benchmark(group="multiply_100")
def test_multiply_matrix_100(benchmark):
    size = 100
    m1 = Matrix(size, size)
    m2 = Matrix(size, size)

    # matrisleri dolduralım (örnek veri)
    for i in range(size):
        for j in range(size):
            m1.data[i][j] = i + j
            m2.data[i][j] = i * j

    benchmark(lambda: m1 * m2)

@pytest.mark.benchmark(group="multiply_200")
def test_multiply_matrix_200(benchmark):
    size = 200
    m1 = Matrix(size, size)
    m2 = Matrix(size, size)

    # matrisleri dolduralım (örnek veri)
    for i in range(size):
        for j in range(size):
            m1.data[i][j] = i + j
            m2.data[i][j] = i * j

    benchmark(lambda: m1 * m2)

@pytest.mark.benchmark(group="add_100")
def test_add_matrix_100(benchmark):
    size = 100
    m1 = Matrix(size, size)
    m2 = Matrix(size, size)

    # matrisleri dolduralım (örnek veri)
    for i in range(size):
        for j in range(size):
            m1.data[i][j] = i + j
            m2.data[i][j] = i * j

    benchmark(lambda: m1 + m2)


@pytest.mark.benchmark(group="add_200")
def test_add_matrix_200(benchmark):
    size = 200
    m1 = Matrix(size, size)
    m2 = Matrix(size, size)

    # matrisleri dolduralım (örnek veri)
    for i in range(size):
        for j in range(size):
            m1.data[i][j] = i + j
            m2.data[i][j] = i * j

    benchmark(lambda: m1 + m2)


@pytest.mark.benchmark(group="multiply_100")
def test_multiply_matrix_100_numpy(benchmark):

    size = 100
    a = np.array([[i + j for j in range(size)] for i in range(size)])
    b = np.array([[i * j for j in range(size)] for i in range(size)])

    # Benchmark — NumPy çarpımı
    benchmark(lambda: np.dot(a, b))

@pytest.mark.benchmark(group="multiply_200")
def test_multiply_matrix_200_numpy(benchmark):

    size = 200
    a = np.array([[i + j for j in range(size)] for i in range(size)])
    b = np.array([[i * j for j in range(size)] for i in range(size)])

    # Benchmark — NumPy çarpımı
    benchmark(lambda: np.dot(a, b))

@pytest.mark.benchmark(group="add_100")
def test_add_matrix_100_numpy(benchmark):

    size = 100
    a = np.array([[i + j for j in range(size)] for i in range(size)])
    b = np.array([[i * j for j in range(size)] for i in range(size)])

    # Benchmark — NumPy çarpımı
    benchmark(lambda: np.add(a, b))

@pytest.mark.benchmark(group="add_200")
def test_add_matrix_200_numpy(benchmark):

    size = 200
    a = np.array([[i + j for j in range(size)] for i in range(size)])
    b = np.array([[i * j for j in range(size)] for i in range(size)])

    # Benchmark — NumPy çarpımı
    benchmark(lambda: np.add(a, b))