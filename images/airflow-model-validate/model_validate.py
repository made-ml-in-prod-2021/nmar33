import os
import pandas as pd
import click
import pickle

from sklearn.metrics import accuracy_score


@click.command()
@click.option("--model_dir", required=True)
@click.option("--data_dir", required=True)
@click.option("--metric_dir", required=True)
def model_validations(model_dir: str, data_dir: str, metric_dir: str):
    with open(os.path.join(model_dir, "model.pkl"), "rb") as file:
        model = pickle.load(file)
    train_data = pd.read_csv(os.path.join(data_dir, "train.csv"))
    valid_data = pd.read_csv(os.path.join(data_dir, "val.csv"))
    train_accuracy = accuracy_score(
        train_data["label"], model.predict(train_data.drop(["label"], axis=1))
    )
    val_accuracy = accuracy_score(
        valid_data["label"], model.predict(valid_data.drop(["label"], axis=1))
    )

    os.makedirs(metric_dir, exist_ok=True)
    with open(os.path.join(metric_dir, "model_metrics.txt"), "w") as file:
        file.write(f"Train accuracy {train_accuracy}, Val accuracy {val_accuracy}")


if __name__ == "__main__":
    model_validations()
