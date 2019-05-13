import pickle 
import pandas as pd

df = pd.read_csv("nursery.csv",header=None)

infile = open("features.pkl",'rb')
features_mapping = pickle.load(infile)
infile.close()

def remap(data,dict_labels):
    """
    This function take in a dictionnary of labels : dict_labels 
    and replace the values (previously labelencode) into the string.
    ex: dict_labels = {{'col1':{1:'A',2:'B'}}
    """
    for field,values in dict_labels.items():
        print("I am remapping %s"%field)
        field=field-1
        data.replace({field:values},inplace=True)
    print("DONE")

    return data

df=remap(df,features_mapping)

print(df)

df=df.transpose()

data=df.to_dict('list')

# print(data)

filename = 'pkl_files/data.pkl'
outfile = open(filename,'wb')
pickle.dump(data,outfile)
outfile.close()