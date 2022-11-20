"""
Este módulo contiene el pipeline de sklearn que clasifica
el dataset del titanic .
Lo hemos compuesto por dos preprocesos . Uno para numéricas y
otro para categóricas
Para numéricas : imputación y scaling
Para categóricas : One Hot Encoding
"""

from sklearn.tree import DecisionTreeClassifier
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer


num_pipeline = Pipeline([
    ("imputer", SimpleImputer()),
    ("ss", StandardScaler())

])



ct = ColumnTransformer([

    ("cat", OneHotEncoder(), ["pclass", "sex", "embarked"]),

    ("num", num_pipeline, ["age","fare"])

])

pipeline = Pipeline([

    ("ct", ct),

    ("model", DecisionTreeClassifier())

])