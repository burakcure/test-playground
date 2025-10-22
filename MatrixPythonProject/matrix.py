
class Matrix:
    
    def __init__(self,rows=0,columns=0):
        self.rows=rows
        self.columns=columns
        self.data=[[0 for _ in range(columns)] for _ in range(rows)]

    def set_rows(self,rows):
        self.rows=rows
        self.render_data()

    def set_columns(self,columns):
        self.columns=columns
        self.render_data()
        


    def render_data(self):

        if self.rows<len(self.data):
            min_rows=self.rows
        else:
            min_rows=len(self.data)

        if self.columns<len(self.data[0]):
            min_columns=self.columns
        else:
            min_columns=len(self.data[0])

        new_data=[[0 for _ in range(min_columns)] for _ in range(min_rows)]

        for row in range(len(new_data)):
            for column in range(len(new_data[0])):
                new_data[row][column]=self.data[row][column]

        self.data=new_data


    def __add__(self, second_matrix):


        if self.rows!=second_matrix.rows or self.columns!=second_matrix.columns:
            raise ValueError("Matrix sizes are not equal.")
        
        result_matrix =Matrix(self.rows,self.columns)

        for row in range(self.rows):
            
            for column in range(self.columns):

                result_matrix.data[row][column]=self.data[row][column]+second_matrix.data[row][column]

        return result_matrix

        


    def __mul__(self, second_matrix):

        if self.columns!=second_matrix.rows:
            return ValueError("Matrix sizes are not eligible to multiplicate.")
        
        new_matrix=Matrix(self.rows,second_matrix.columns)

        for i in range(self.rows):
            for j in range(second_matrix.columns):
                for k in range(self.columns):
                        new_matrix.data[i][k]+=self.data[i][j]*second_matrix.data[j][k]


        return new_matrix