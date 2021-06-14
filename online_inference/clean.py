import os

files_to_delete = [
    './data/train_test_dataset/test.csv', 
    './data/train_test_dataset/train.csv',
    './logs/log.txt',
    './model/model.pkl',
    './outputs/metrics.yaml',
    './outputs/predict.csv',
    './data/fake_dataset/fake_dataset.csv'
    ]

for file in files_to_delete:
    try:
        os.remove(file)
    except:
        continue