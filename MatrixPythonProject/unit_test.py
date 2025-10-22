from matrix import Matrix
import pytest
@pytest.fixture
def sample_matrices():
    a = Matrix(2, 2)
    b = Matrix(2, 2)
    a.data = [[1, 2], [3, 4]]
    b.data = [[5, 6], [7, 8]]
    return a, b

@pytest.fixture
def sample_matrix():
    a=Matrix(3,2)
    return a

def test_matrix_set_rows_correctness(sample_matrix):
    a=sample_matrix
    a.set_rows(1)
    expected=[[0,0]]
    assert a.data==expected,"Matrix set row function result is incorrect"

def test_matrix_set_columns_correctness(sample_matrix):
    a=sample_matrix
    a.set_columns(1)
    expected=[[0],[0],[0]]
    assert a.data==expected,"Matrix set row function result is incorrect"

def test_matrix_construction_correctness():
    a=Matrix(1,1)
    expected=[[0]]
    assert a.data==expected,"Matrix construction result is incorrect."

def test_matrix_addition_correctness(sample_matrices):
    a, b = sample_matrices
    result = a + b
    expected = [[6, 8], [10, 12]]
    assert result.data == expected, "Matrix addition result is incorrect."

def test_matrix_addition_incompatible_sizes():
    a = Matrix(2, 2)
    b = Matrix(3, 2)
    with pytest.raises(ValueError):
        _ = a + b

def test_matrix_multiplication_correctness(sample_matrices):
    a,b=sample_matrices
    result=a*b
    expected=[[19,22],[43,50]]
    assert result.data==expected, "Matrix multiplication result is incorrect."

