import pandas as pd
import numpy as np

from ohio_concept_drift.ohio_data import load_usa_data_per_experiment, load_ohio_data_per_experiment
from ohio_concept_drift.usa.dictionary import USA_STATES_CODES


def summary_ohio_number_of_detection(results_config, target_directory, column_name='total_drift_detection'):
    results = [(experiment, load_ohio_data_per_experiment(experiment_name=experiment, drift_results_directory=drift_path, column_name=column_name)) for
               experiment, drift_path in results_config]

    summary_data_frame = summary_number_of_detection(results)

    with open(f'{target_directory}/{column_name}_tab_summary_v2.tex', "w") as f:
        f.write(build_latex(summary_data_frame))


def summary_usa_number_of_detection(results_config, target_directory, column_name='total_drift_detection'):
    results = [(experiment, load_usa_data_per_experiment(experiment_name=experiment, drift_results_file=drift_path, column_name=column_name)) for
               experiment, drift_path in results_config]

    summary_data_frame = summary_number_of_detection(results)
    summary_data_frame['ML_region'] = summary_data_frame['ML_region'].map(USA_STATES_CODES).str.upper()

    with open(f'{target_directory}/{column_name}_tab_summary_v2.tex', "w") as f:
        f.write(build_latex(summary_data_frame))


def summary_number_of_detection(results_config):
    results = pd.DataFrame(data={})

    for (experiment, drift_results) in results_config:
        print(experiment)

        drift_results.loc['Total'] = drift_results.sum()

        experiment_column = experiment
        total_column = f'{experiment}_total'
        _10k_column = f'{experiment}_10k'
        drift_results[_10k_column] = np.where(drift_results[total_column] > 0, 10_000 * drift_results[experiment_column] / drift_results[total_column], 0)

        drift_results = drift_results[['ML_region', experiment_column, _10k_column]]

        if results.empty:
            results = drift_results
        else:
            results = pd.merge(results, drift_results, on='ML_region')

    return results


def build_latex(results):
    latex_code = results.to_latex(
        index=False,
        # caption="The aggregate number of concept drift instances identified using the designated algorithm.",
        # label=f'tab:{column_name}',
        float_format="%.2f"  # Format floats to 2 decimal places
    )

    latex_code = latex_code.replace('\\toprule', '\hline')
    latex_code = latex_code.replace('\\midrule', '\hline')
    latex_code = latex_code.replace('\\bottomrule', '\hline')

    latex_code = latex_code.replace('& 0 &', '& \\textbf{0} &')
    latex_code = latex_code.replace('& 0.00 &', '& \\textbf{0.00} &')
    latex_code = latex_code.replace('& 0.00 \\', '& \\textbf{0.00} \\')
    latex_code = latex_code.replace('ML_region', 'Region')
    latex_code = latex_code.replace('HAT_ADWIN & HAT_ADWIN_10k', '\multicolumn{2}{c|}{\makecell{HAT \\\\ ADWIN}}')
    latex_code = latex_code.replace('HT_ADWIN & HT_ADWIN_10k', '\multicolumn{2}{c|}{\makecell{HT \\\\ ADWIN}}')
    latex_code = latex_code.replace('ARF_ADWIN & ARF_ADWIN_10k', '\multicolumn{2}{c|}{\makecell{ARF \\\\ ADWIN}}')
    latex_code = latex_code.replace('NB_ADWIN & NB_ADWIN_10k', '\multicolumn{2}{c|}{\makecell{NB \\\\ ADWIN}}')
    latex_code = latex_code.replace('NB_HDDM_ONESIDED & NB_HDDM_ONESIDED_10k', '\multicolumn{2}{c|}{\makecell{NB HDDM \\\\ ONESIDED}}')
    latex_code = latex_code.replace('SRP_HDDM_ONESIDED & SRP_HDDM_ONESIDED_10k', '\multicolumn{2}{c|}{\makecell{SRP HDDM \\\\ ONESIDED}}')
    latex_code = latex_code.replace('HT_HDDM_ONESIDED & HT_HDDM_ONESIDED_10k', '\multicolumn{2}{c|}{\makecell{HT HDDM \\\\ ONESIDED}}')
    latex_code = latex_code.replace('ARF_HDDM_ONESIDED & ARF_HDDM_ONESIDED_10k', '\multicolumn{2}{c|}{\makecell{ARF HDDM \\\\ ONESIDED}}')

    latex_code = latex_code.replace('01_TOLEDO', '01 TOLEDO')
    latex_code = latex_code.replace('02_LIMA', '02 LIMA')
    latex_code = latex_code.replace('03_DAYTON', '03 DAYTON')
    latex_code = latex_code.replace('04_SPRINGFIELD', '04 SPRINGFIELD')
    latex_code = latex_code.replace('05_AKRON', '05 AKRON')
    latex_code = latex_code.replace('06_CANTON', '06 CANTON')
    latex_code = latex_code.replace('07_MANSFIELD', '07 MANSFIELD')
    latex_code = latex_code.replace('08_STEUBENVILLE', '08 STEUBENVILLE')
    latex_code = latex_code.replace('09_YOUNGSTOWN', '09 YOUNGSTOWN')
    latex_code = latex_code.replace('10_RURAL', '10 RURAL')

    return latex_code
