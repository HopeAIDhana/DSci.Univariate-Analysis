class univariate():
 
    def QualQuan (dataset):
        quan=[]
        qual=[]
        for columnsName in dataset.columns:
            #print(column name)
            if(dataset[columnsName].dtype=='O'):
                #print("qual")
                qual.append(columnsName)
            else:
                #print("quan")
                quan.append(columnsName)
        return qual,quan  


