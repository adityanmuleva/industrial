{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Country</th>\n",
       "      <th>Age</th>\n",
       "      <th>Salary</th>\n",
       "      <th>Purchased</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>France</td>\n",
       "      <td>44.0</td>\n",
       "      <td>72000.0</td>\n",
       "      <td>No</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Spain</td>\n",
       "      <td>27.0</td>\n",
       "      <td>48000.0</td>\n",
       "      <td>Yes</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Germany</td>\n",
       "      <td>30.0</td>\n",
       "      <td>54000.0</td>\n",
       "      <td>No</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Spain</td>\n",
       "      <td>38.0</td>\n",
       "      <td>61000.0</td>\n",
       "      <td>No</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Germany</td>\n",
       "      <td>40.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Yes</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Country   Age   Salary Purchased\n",
       "0   France  44.0  72000.0        No\n",
       "1    Spain  27.0  48000.0       Yes\n",
       "2  Germany  30.0  54000.0        No\n",
       "3    Spain  38.0  61000.0        No\n",
       "4  Germany  40.0      NaN       Yes"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "datasets = pd.read_csv(\"/home/aaditya/Ml/Machine Learning A-Z/Part 1 - Data Preprocessing/Data.csv\")\n",
    "datasets.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Country</th>\n",
       "      <th>Age</th>\n",
       "      <th>Salary</th>\n",
       "      <th>Purchased</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>France</td>\n",
       "      <td>44.0</td>\n",
       "      <td>72000.0</td>\n",
       "      <td>No</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Spain</td>\n",
       "      <td>27.0</td>\n",
       "      <td>48000.0</td>\n",
       "      <td>Yes</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Germany</td>\n",
       "      <td>30.0</td>\n",
       "      <td>54000.0</td>\n",
       "      <td>No</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Spain</td>\n",
       "      <td>38.0</td>\n",
       "      <td>61000.0</td>\n",
       "      <td>No</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Germany</td>\n",
       "      <td>40.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Yes</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>France</td>\n",
       "      <td>35.0</td>\n",
       "      <td>58000.0</td>\n",
       "      <td>Yes</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Spain</td>\n",
       "      <td>NaN</td>\n",
       "      <td>52000.0</td>\n",
       "      <td>No</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>France</td>\n",
       "      <td>48.0</td>\n",
       "      <td>79000.0</td>\n",
       "      <td>Yes</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Germany</td>\n",
       "      <td>50.0</td>\n",
       "      <td>83000.0</td>\n",
       "      <td>No</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>France</td>\n",
       "      <td>37.0</td>\n",
       "      <td>67000.0</td>\n",
       "      <td>Yes</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Country   Age   Salary Purchased\n",
       "0   France  44.0  72000.0        No\n",
       "1    Spain  27.0  48000.0       Yes\n",
       "2  Germany  30.0  54000.0        No\n",
       "3    Spain  38.0  61000.0        No\n",
       "4  Germany  40.0      NaN       Yes\n",
       "5   France  35.0  58000.0       Yes\n",
       "6    Spain   NaN  52000.0        No\n",
       "7   France  48.0  79000.0       Yes\n",
       "8  Germany  50.0  83000.0        No\n",
       "9   France  37.0  67000.0       Yes"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X = datasets.iloc[:,:-1].values\n",
    "Y = datasets.iloc[:, -1:].values\n",
    "datasets"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/home/aaditya/anaconda3/lib/python3.7/site-packages/sklearn/utils/deprecation.py:58: DeprecationWarning: Class Imputer is deprecated; Imputer was deprecated in version 0.20 and will be removed in 0.22. Import impute.SimpleImputer from sklearn instead.\n",
      "  warnings.warn(msg, category=DeprecationWarning)\n"
     ]
    }
   ],
   "source": [
    "from sklearn.preprocessing import Imputer\n",
    "imputer = Imputer(missing_values = 'NaN',strategy = 'mean', axis=0)\n",
    "imputer = imputer.fit(X[:,1:3])\n",
    "(X[:,1:3])= imputer.transform(X[:,1:3])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/home/aaditya/anaconda3/lib/python3.7/site-packages/sklearn/preprocessing/_encoders.py:371: FutureWarning: The handling of integer data will change in version 0.22. Currently, the categories are determined based on the range [0, max(values)], while in the future they will be determined based on the unique values.\n",
      "If you want the future behaviour and silence this warning, you can specify \"categories='auto'\".\n",
      "In case you used a LabelEncoder before this OneHotEncoder to convert the categories to integers, then you can now use the OneHotEncoder directly.\n",
      "  warnings.warn(msg, FutureWarning)\n",
      "/home/aaditya/anaconda3/lib/python3.7/site-packages/sklearn/preprocessing/_encoders.py:392: DeprecationWarning: The 'categorical_features' keyword is deprecated in version 0.20 and will be removed in 0.22. You can use the ColumnTransformer instead.\n",
      "  \"use the ColumnTransformer instead.\", DeprecationWarning)\n",
      "/home/aaditya/anaconda3/lib/python3.7/site-packages/sklearn/preprocessing/label.py:235: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  y = column_or_1d(y, warn=True)\n"
     ]
    }
   ],
   "source": [
    "from sklearn.preprocessing import LabelEncoder, OneHotEncoder\n",
    "labelencoder_X = LabelEncoder()\n",
    "X[:,0] = labelencoder_X.fit_transform(X[:,0])\n",
    "onehotencoder = OneHotEncoder(categorical_features = [0])\n",
    "X = onehotencoder.fit_transform(X).toarray()\n",
    "\n",
    " labelencoder_Y = LabelEncoder()\n",
    "Y = labelencoder_Y.fit_transform(Y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[-1.        ,  2.64575131, -0.77459667,  0.26306757,  0.12381479],\n",
       "       [ 1.        , -0.37796447, -0.77459667, -0.25350148,  0.46175632],\n",
       "       [-1.        , -0.37796447,  1.29099445, -1.97539832, -1.53093341],\n",
       "       [-1.        , -0.37796447,  1.29099445,  0.05261351, -1.11141978],\n",
       "       [ 1.        , -0.37796447, -0.77459667,  1.64058505,  1.7202972 ],\n",
       "       [-1.        , -0.37796447,  1.29099445, -0.0813118 , -0.16751412],\n",
       "       [ 1.        , -0.37796447, -0.77459667,  0.95182631,  0.98614835],\n",
       "       [ 1.        , -0.37796447, -0.77459667, -0.59788085, -0.48214934]])"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size = 0.2,random_state=0)\n",
    "\n",
    "from sklearn.preprocessing import StandardScaler\n",
    "Sc_X = StandardScaler()\n",
    "X_train = Sc_X.fit_transform(X_train)\n",
    "X_test = Sc_X.transform(X_test)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
