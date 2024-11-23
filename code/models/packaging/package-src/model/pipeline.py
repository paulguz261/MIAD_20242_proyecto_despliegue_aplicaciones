from feature_engine.selection import DropFeatures
from sklearn.pipeline import Pipeline
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler
from imblearn.combine import SMOTEENN
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from xgboost import XGBClassifier

from model.config.core import config
from model.processing import features as pp

clf_pipeline = Pipeline(
    [
        # Drop features 
        ("drop_features", 
        DropFeatures(
            features_to_drop=[config.model_config.temp_features]
            )
        ),
        Mappers
        (
           "mapper_qual",
           pp.Mapper(
               variables=config.model_config.qual_vars,
               mappings=config.model_config.qual_mappings,
           ),
        ),
        # Balanceo de clases
        ("balanceo", SMOTE(sampling_strategy=0.5)
         ),
        # Scaler
        ("scaler", StandardScaler()
         ),
        # PCA
        ("PCA", PCA(n_components=0.95)
         ),
        # XGBoost
        ("XGBoost",
            XGBClassifier(
                objective=config.model_config.objective,
                n_estimators=config.model_config.n_estimators,
                max_depth=config.model_config.max_depth,
                learning_rate=config.model_config.learning_rate,
                subsample=config.model_config.subsample,
                colsample_bytree=config.model_config.colsample_bytree,
                min_child_weight=config.model_config.min_child_weight,
                reg_lambda=config.model_config.reg_lambda,
                reg_alpha=config.model_config.reg_alpha,
            ),
        ),
    ]
)
