import os

import click
from sklearn.datasets import make_classification
import pandas as pd


@click.command()
@click.option("--output_dir", required=True)
def download(output_dir: str):
    print(1)
    X, y = make_classification(n_samples=100, n_features=20, n_informative=2)
    print(2)

    os.makedirs(output_dir, exist_ok=True)
    print(3)
    pd.DataFrame(X).to_csv(os.path.join(output_dir, "data.csv"), index=False)
    print(4)
    pd.DataFrame(y).to_csv(os.path.join(output_dir, "target.csv"), index=False)
    print(5)


if __name__ == "__main__":
    download()
