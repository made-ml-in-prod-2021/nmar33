import os
import pandas as pd
import click

from sklearn.model_selection import train_test_split




@click.command()
@click.option("--input_dir", required=True)
@click.option("--val_size", required=True)
@click.option("--rnd_state", required=True)
def preprocess(input_dir: str, val_size: str, rnd_state: str):
    train_data = pd.read_csv(os.path.join(input_dir, "train_data.csv"))
    train, val = train_test_split(train_data, test_size=float(val_size), random_state=int(rnd_state))


    os.makedirs(input_dir, exist_ok=True)
    train.to_csv(os.path.join(input_dir, "train.csv"), index=False)
    val.to_csv(os.path.join(input_dir, "val.csv"), index=False)


if __name__ == "__main__":
    preprocess()