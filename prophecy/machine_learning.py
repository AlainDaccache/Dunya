import logging
import pandas as pd
from pathlib import Path

from joblib import dump
from sklearn import preprocessing
from sklearn.experimental import enable_hist_gradient_boosting  # noqa
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

path = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
test_size = 0.2
random_state = 1
logger.info("Preparing dataset...")
dataset = pd.read_csv(path, delimiter=";").rename(columns=lambda x: x.lower().replace(" ", "_"))
train_df, test_df = train_test_split(dataset, test_size=test_size, random_state=random_state)

# separate features from target
y_train = train_df["quality"]
X_train = train_df.drop("quality", axis=1)
y_test = test_df["quality"]
X_test = test_df.drop("quality", axis=1)

logger.info("Training model...")
scaler = preprocessing.StandardScaler().fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

model = HistGradientBoostingRegressor(max_iter=50).fit(X_train, y_train)

y_pred = model.predict(X_test)
error = mean_squared_error(y_test, y_pred)
logger.info(f"Test MSE: {error}")

logger.info("Saving artifacts...")
Path("artifacts").mkdir(exist_ok=True)
dump(model, "artifacts/model.joblib")
dump(scaler, "artifacts/scaler.joblib")
