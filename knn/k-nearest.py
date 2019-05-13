import pickle
import pandas as pd
import math
from collections import OrderedDict
import operator
from collections import defaultdict
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_recall_fscore_support

#open pickle file of given data in csv stored as hash values
pkl_file=open("../pkl_files/data.pkl","rb")
data=pickle.load(pkl_file)
pkl_file.close()

k_val = 10


#calculate distance between two instances
def eucledian(a, b):
    return (a-b)*(a-b)

'''Predict class of the test data from the train data by 
   using k-nearest neighbours algorithm
'''
def predict(test, data):
    #dictionary storing predicted class
    predicted = {}
    for_count = 0
    for i in test:
        print(i)
        #list storing distance of all train values from a single test data
        distance = {}
        for j in data:
            dist = 0
            if i!=j:
                #calculate distance between two instances i and j
                for k in range(0, 8):
                    dist += eucledian(data[i][k], data[j][k])
                dist = math.sqrt(dist)
                distance[j] = dist
        #sort distances in increasing order
        sorted_x = sorted(distance.items(), key=operator.itemgetter(1))
        '''creates a dictionary with values initialized to zero
           Stores number of time each class occurs in the k-nearest neighbours
        '''
        last_val_dict = defaultdict(int)
        count = 0
        for j in sorted_x:
            last_val_dict[data[j[0]][8]]=last_val_dict[data[j[0]][8]]+1
            count = count+1
            #calculate only for k-nearest neighbours
            if count>=k_val:
                break
        #Sort the above values to get the one which occurs the most
        last_val_dict_sorted = sorted(last_val_dict.items(), key=operator.itemgetter(1), reverse=True)
        #the predicted value for the ith data is the highest occuring values from the k-nearest neighbours
        predicted[i] = last_val_dict_sorted[0][0]
        
        # for_count = for_count+1
        # if for_count>=1000:
        #     break
   
    return predicted
   

for i in range(1, 2):
    '''convert test to pandas dataframe 
       Generate a random test sample of 30% of the data
       Convert test samples to dictionary for further calculations
    '''
    test = pd.DataFrame(data)
    test = test.transpose()
    test = test.sample(frac=0.3)
    test = test.transpose()
    test = test.to_dict()

    predicted = {}
    predicted = predict(test, data)
    
    correct = 0
    y_true = []
    y_pred = []

    #calculate accuracy
    for i in predicted:
        print(i, data[i][8], predicted[i])
        y_true.append(data[i][8])
        y_pred.append(predicted[i])
        if data[i][8]==predicted[i]:
            # print(data[i][8])
            correct=correct+1
    
    #calculate confusion matrix, precision and recall values
    print(correct/len(predicted))
    print(confusion_matrix(y_true, y_pred))
    print(precision_recall_fscore_support(y_true, y_pred, average='macro'))


