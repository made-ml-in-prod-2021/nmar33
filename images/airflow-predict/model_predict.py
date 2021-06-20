import os
import pandas as pd
import click
import pickle

from sklearn.metrics import accuracy_score


@click.command()
@click.option("--prod_model_dir", required=True)
@click.option("--data_raw", required=True)
@click.option("--predict_dir", required=True)
def model_validations(prod_model_dir: str, data_raw: str, predict_dir: str):

    with open(os.path.join(prod_model_dir, "model.pkl"), "rb") as file:
        model = pickle.load(file)
    data = pd.read_csv(os.path.join(data_raw, "data.csv"))
    predictions = model.predict(data)

    os.makedirs(predict_dir, exist_ok=True)
    pd.DataFrame(predictions).to_csv(
        os.path.join(predict_dir, "predictions.csv"), index=False
    )


if __name__ == "__main__":
    model_validations()
