improt pandas as pd
df = pd.read_csv('derma.csv')
df = df.dropna()

X = df.values[:, :35]
y = df.values[:, 35]

kf = KFold(10, shuffle=True, random_state=727)

for i, (train_index, test_index) in enumerate(kf.split(X)):
    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(X[train_index], y[train_index])
    predictions = knn.predict(X[test_index])
    print(f'Iteration {i+1}:\nConfusion Matrix')
    display(confusion_matrix(y[test_index], predictions))
  
