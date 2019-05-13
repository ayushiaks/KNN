# K-Nearest Neighbours

1. K-Nearest Neighboyrs: In pattern recognition, the k-nearest neighbors algorithm (k-NN) is a non-parametric method used for classification. The output is a class membership. An object is classified by a plurality vote of its neighbors, with the object being assigned to the class most common among its k nearest neighbors
2. Naive Bayes: 



## Data

We used the Nursery Dataset, which can be found [here](https://archive.ics.uci.edu/ml/datasets/nursery). The Nursery Database contains examples with the structural information removed, i.e., directly relates NURSERY to the eight input attributes: parents, has_nurs, form, children, housing, finance, social, health. <br />
1. Number of instances: 12960 <br />
2. Number of attributes: 8


## Run
* Pre-processing of data and generation of "data" pickle file  is done using
```python
    python3 preProcess.py
```
* Pre-processing of data and generation of "features" pickle file  is done using
```python
    python3 features.py
```
* K-Nearest Neighbours: <br />
    Change path to knn/ <br />
    1. Predict class using K-Nearest Neighbours by: <br />
    ```python

    python3 k-nearest.py
    ```
    <br />
    


