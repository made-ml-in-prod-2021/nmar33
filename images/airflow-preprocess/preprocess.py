import os
import pandas as pd
import click


@click.command()
@click.option("--input_dir", required=True)
@click.option("--output_dir", required=True)
def preprocess(input_dir: str, output_dir: str):
    train_data = pd.read_csv(os.path.join(input_dir, "data.csv"))
    label = pd.read_csv(os.path.join(input_dir, "target.csv"))
    train_data["label"] = label

    os.makedirs(output_dir, exist_ok=True)
    train_data.to_csv(os.path.join(output_dir, "train_data.csv"), index=False)


if __name__ == "__main__":
    preprocess()
