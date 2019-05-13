import pickle

features_mapping={}
reverse_features_mapping={}

f = open("temp.txt", "r")
count1=1
for x in f:
    x=x.rstrip()
    p=x.split(',')
    print(p)
    count2=1
    temp={}
    temp1={}
    for i in p:
        i=i.strip()
        temp[i]=count2
        temp1[count2]=i
        count2=count2+1
    features_mapping[count1]=temp
    reverse_features_mapping[count1]=temp1
    count1=count1+1
# print(features_mapping)
print(reverse_features_mapping)

filename = 'pkl_files/features.pkl'
outfile = open(filename,'wb')
pickle.dump(features_mapping,outfile)
outfile.close()

filename = 'pkl_files/reverse_features.pkl'
outfile = open(filename,'wb')
pickle.dump(reverse_features_mapping,outfile)
outfile.close()