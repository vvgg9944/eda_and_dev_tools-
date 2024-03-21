import pandas as pd

from eda import abalones

X_numeric = abalones.drop(['Rings', 'Sex'], axis=1)
y = abalones['Rings']

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X_numeric, y, test_size=0.25, random_state=42)
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR

model_knn_num = KNeighborsRegressor()
model_svr_num = SVR()

model_knn_num.fit(X_train, y_train)
model_knn_num_pred = model_knn_num.predict(X_test)

model_svr_num.fit(X_train, y_train)
model_svr_num_pred = model_svr_num.predict(X_test)

from sklearn.metrics import r2_score
print(f'For KNN R2-score is {r2_score(model_knn_num_pred,y_test)}, for SVR - {r2_score(model_svr_num_pred, y_test)}')

# For KNN R2-score is 0.22516108889410913, for SVR - -0.1031419886837972, поэтому KNN в задаче регрессии лучше чем support vector regression

# from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
# from sklearn.compose import ColumnTransformer
#
# categorical = ['Sex']
# numerical = ['Length', 'Diameter', 'Height', 'Whole weight', 'Shucked weight',
#              'Viscera weight', 'Shell weight']
# ct = ColumnTransformer([
#     ('ohe', OneHotEncoder(handle_unknown='ignore'), categorical),
#     ('scaling', MinMaxScaler(), numerical)
# ])
#
# X_train_transformed = ct.fit_transform(X_train_full)
# X_test_transformed = ct.transform(X_test_full)
#
# new_features = list(ct.named_transformers_['ohe'].get_feature_names_out())
# new_features.extend(numerical)
#
# X_train_transformed = pd.DataFrame(X_train_transformed, columns=new_features)
# X_test_transformed = pd.DataFrame(X_test_transformed, columns=new_features)
#
# # 1st model - KNN
#
# from sklearn.neighbors import KNeighborsRegressor
#
# model_1 = KNeighborsRegressor()
#
# model_1.fit(X_train_transformed, y_train_full)
# model_1_pred = model_1.predict(X_test_transformed)



