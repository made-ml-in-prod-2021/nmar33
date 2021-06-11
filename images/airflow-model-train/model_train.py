import os
import pandas as pd
import click
import pickle

from sklearn.linear_model import LogisticRegression





@click.command()
@click.option("--input_dir", required=True)
@click.option("--output_dir", required=True)
def model_train(input_dir: str, output_dir: str):
    train = pd.read_csv(os.path.join(input_dir, "train.csv"))
    model = LogisticRegression()
    model.fit(train.drop(['label'], axis=1), train[['label']])


    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "model.pkl"), 'wb') as file:
        pickle.dump(model, file)

if __name__ == "__main__":
    model_train()