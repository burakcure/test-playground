from matrix import Matrix

print("Selam")
first_sum_matrix=Matrix(3,4)
first_sum_matrix.data[0]=[1,2,3,4]
first_sum_matrix.data[1]=[1,2,3,4]
first_sum_matrix.data[2]=[1,2,3,4]

second_sum_matrix=Matrix(3,4)
second_sum_matrix.data[0]=[4,3,2,1]
second_sum_matrix.data[1]=[4,3,2,1] 
second_sum_matrix.data[2]=[4,3,2,1]

result_sum_matrix=first_sum_matrix+second_sum_matrix
print(result_sum_matrix.data)

first_mult_matrix=Matrix(3,4)
first_mult_matrix.data[0]=[1,2,3,4]
first_mult_matrix.data[1]=[1,2,3,4]
first_mult_matrix.data[2]=[1,2,3,4]

second_mult_matrix=Matrix(4,3)
second_mult_matrix.data[0]=[2,2,2]
second_mult_matrix.data[1]=[4,3,2] 
second_mult_matrix.data[2]=[4,3,2]
second_mult_matrix.data[3]=[4,3,2]


print(first_mult_matrix.data[0][0])


result_mult_matrix=first_mult_matrix*second_mult_matrix

a=Matrix(2,1)
a.set_rows(1)
print(result_mult_matrix.data)