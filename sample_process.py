from Controller import Controller
from datetime import datetime
import json
import pandas as pd

from sklearn.datasets import load_boston
from sklearn.metrics import r2_score
from result_dir import make_dir_if_not_exists
from settings import DIR_RESULT, DIR_REPORT

def main(additional_parameters):
    test_size = additional_parameters['test_size']/100

    features, target = load_boston(return_X_y=True)

    score_func = r2_score
    with open('constructor.json', 'r') as fp:
        constructor_json = json.load(fp)

    c = Controller(features=features,
                   target=target,
                   test_size=test_size,
                   score_func=score_func,
                   pipeline_constructor_json=constructor_json,
                   pipelines_to_test=additional_parameters['no_of_pipeline'])

    results_df = pd.DataFrame(c.results)
    report_path = f'{DIR_RESULT}/{DIR_REPORT}/'
    make_dir_if_not_exists(report_path)
    results_df.to_csv(f"{report_path}result.csv")

    return DIR_RESULT


'''from Controller import Controller
from datetime import datetime
import json
import pandas as pd
from sklearn.datasets import load_boston
from sklearn.metrics import r2_score

test_size = 0.2

features, target = load_boston(return_X_y=True)

score_func = r2_score
with open('constructor.json', 'r') as fp:
    constructor_json = json.load(fp)

c = Controller(features=features,
               target=target,
               test_size=test_size,
               score_func=score_func,
               pipeline_constructor_json=constructor_json,
               pipelines_to_test=10)

results_df = pd.DataFrame(c.results)
results_df.to_csv(f"{str(datetime.today()).replace(' ', '_').replace(':', '_').replace('-', '_').replace('.', '_')}_result.csv")'''




