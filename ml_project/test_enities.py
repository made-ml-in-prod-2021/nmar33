from .src.enities import read_configs


def test_read_configs():
    config_path = './configs/config_for_test.yaml'
    cnfg = read_configs(config_path)

    assert cnfg.paths.output_model_path == './model/model.pkl'
    assert cnfg.paths.predict_path == './outputs/predict.csv'
    assert cnfg.train_config.model_type == 'LR'
