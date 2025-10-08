import pandas

from ohio_concept_drift.ohio_data import plot_ohio, load_data_per_eperiment
from ohio_concept_drift.warsaw_data import plot_warsaw
from ohio_concept_drift.latex import latex_ohio, latex_warsaw
from ohio_concept_drift.warsaw_arff import arff_warsaw_surveys


def task_plot_ohio():
    plot_ohio('NB_ADWIN', 'experiments/Ohio/Eksperyment 2 NB ADWIN HDDM pełne przebiegi/Eksperyment_2/NB_ADWIN')
    plot_ohio('NB_HDDM_ONESIDED', 'experiments/Ohio/Eksperyment 2 NB ADWIN HDDM pełne przebiegi/Eksperyment_2/NB_HDDM_ONESIDED')

    plot_ohio('SRP_HDDM_ONESIDED', 'experiments/Ohio/Eksperyment 3 SRP HDDM pełne przeliczenie/SRP_HDDM_ONESIDED')

    plot_ohio('ARF_ADWIN', 'experiments/Ohio/Eksperyment 4/ARF_ADWIN')
    plot_ohio('HAT_ADWIN', 'experiments/Ohio/Eksperyment 4/HAT_ADWIN')
    plot_ohio('HT_ADWIN', 'experiments/Ohio/Eksperyment 4/HT_ADWIN')
    plot_ohio('HT_HDDM_ONESIDED', 'experiments/Ohio/Eksperyment 4/HT_HDDM_ONESIDED')

    plot_ohio('ARF_HDDM_ONESIDED', 'experiments/Ohio/ARF_HDDM_ONESIDED')


def task_prepare_latex_table():
    column_name = 'total_drift_detection'
    NB_ADWIN = load_data_per_eperiment('NB_ADWIN', 'experiments/Ohio/Eksperyment 2 NB ADWIN HDDM pełne przebiegi/Eksperyment_2/NB_ADWIN', column_name)
    NB_HDDM_ONESIDED = load_data_per_eperiment('NB_HDDM_ONESIDED',
                                               'experiments/Ohio/Eksperyment 2 NB ADWIN HDDM pełne przebiegi/Eksperyment_2/NB_HDDM_ONESIDED', column_name)

    SRP_HDDM_ONESIDED = load_data_per_eperiment('SRP_HDDM_ONESIDED', 'experiments/Ohio/Eksperyment 3 SRP HDDM pełne przeliczenie/SRP_HDDM_ONESIDED',
                                                column_name)

    ARF_ADWIN = load_data_per_eperiment('ARF_ADWIN', 'experiments/Ohio/Eksperyment 4/ARF_ADWIN', column_name)
    HAT_ADWIN = load_data_per_eperiment('HAT_ADWIN', 'experiments/Ohio/Eksperyment 4/HAT_ADWIN', column_name)
    HT_ADWIN = load_data_per_eperiment('HT_ADWIN', 'experiments/Ohio/Eksperyment 4/HT_ADWIN', column_name)
    HT_HDDM_ONESIDED = load_data_per_eperiment('HT_HDDM_ONESIDED', 'experiments/Ohio/Eksperyment 4/HT_HDDM_ONESIDED', column_name)

    ARF_HDDM_ONESIDED = load_data_per_eperiment('ARF_HDDM_ONESIDED', 'experiments/Ohio/ARF_HDDM_ONESIDED', column_name)

    results = pandas.merge(NB_ADWIN, NB_HDDM_ONESIDED, on="ML_region")
    results = pandas.merge(results, SRP_HDDM_ONESIDED, on="ML_region")
    results = pandas.merge(results, ARF_ADWIN, on="ML_region")
    results = pandas.merge(results, HAT_ADWIN, on="ML_region")
    results = pandas.merge(results, HT_ADWIN, on="ML_region")
    results = pandas.merge(results, HT_HDDM_ONESIDED, on="ML_region")
    results = pandas.merge(results, ARF_HDDM_ONESIDED, on="ML_region")

    results.loc['Total'] = results.sum()

    results['NB_ADWIN_10k'] = 10_000 * results['NB_ADWIN'] / results['NB_ADWIN_total']
    results['NB_HDDM_ONESIDED_10k'] = 10_000 * results['NB_HDDM_ONESIDED'] / results['NB_HDDM_ONESIDED_total']
    results['SRP_HDDM_ONESIDED_10k'] = 10_000 * results['SRP_HDDM_ONESIDED'] / results['SRP_HDDM_ONESIDED_total']
    results['ARF_ADWIN_10k'] = 10_000 * results['ARF_ADWIN'] / results['ARF_ADWIN_total']
    results['HAT_ADWIN_10k'] = 10_000 * results['HAT_ADWIN'] / results['HAT_ADWIN_total']
    results['HT_ADWIN_10k'] = 10_000 * results['HT_ADWIN'] / results['HT_ADWIN_total']
    results['HT_HDDM_ONESIDED_10k'] = 10_000 * results['HT_HDDM_ONESIDED'] / results['HT_HDDM_ONESIDED_total']
    results['ARF_HDDM_ONESIDED_10k'] = 10_000 * results['ARF_HDDM_ONESIDED'] / results['ARF_HDDM_ONESIDED_total']

    results = results[['ML_region',
                       'HAT_ADWIN', 'HAT_ADWIN_10k',
                       'HT_ADWIN', 'HT_ADWIN_10k',
                       'ARF_ADWIN', 'ARF_ADWIN_10k',
                       'NB_ADWIN', 'NB_ADWIN_10k',
                       'NB_HDDM_ONESIDED', 'NB_HDDM_ONESIDED_10k',
                       'SRP_HDDM_ONESIDED', 'SRP_HDDM_ONESIDED_10k',
                       'HT_HDDM_ONESIDED', 'HT_HDDM_ONESIDED_10k',
                       'ARF_HDDM_ONESIDED', 'ARF_HDDM_ONESIDED_10k'
                       ]]

    latex_code = results.to_latex(
        index=False,
        caption="The aggregate number of concept drift instances identified using the designated algorithm.",
        label=f'tab:{column_name}',
        float_format="%.2f"  # Format floats to 2 decimal places
    )

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
    latex_code = latex_code.replace('& 0 &', '& \\textbf{0} &')
    latex_code = latex_code.replace('& 0.00 &', '& \\textbf{0.00} &')
    latex_code = latex_code.replace('& 0.00 \\', '& \\textbf{0.00} \\')
    latex_code = latex_code.replace('01 TOLEDO02 LIMA03 DAYTON04 SPRINGFIELD05 AKRON06 CANTON07 MANSFIELD08 STEUBENVILLE09 YOUNGSTOWN10 RURAL', '\\textbf{Total}')

    latex_code = latex_code.replace('ML_region', 'Region')
    latex_code = latex_code.replace('HAT_ADWIN & HAT_ADWIN_10k', '\multicolumn{2}{c|}{\makecell{HAT \\\\ ADWIN}}')
    latex_code = latex_code.replace('HT_ADWIN & HT_ADWIN_10k', '\multicolumn{2}{c|}{\makecell{HT \\\\ ADWIN}}')
    latex_code = latex_code.replace('ARF_ADWIN & ARF_ADWIN_10k', '\multicolumn{2}{c|}{\makecell{ARF \\\\ ADWIN}}')
    latex_code = latex_code.replace('NB_ADWIN & NB_ADWIN_10k', '\multicolumn{2}{c|}{\makecell{NB \\\\ ADWIN}}')
    latex_code = latex_code.replace('NB_HDDM_ONESIDED & NB_HDDM_ONESIDED_10k', '\multicolumn{2}{c|}{\makecell{NB HDDM \\\\ ONESIDED}}')
    latex_code = latex_code.replace('SRP_HDDM_ONESIDED & SRP_HDDM_ONESIDED_10k', '\multicolumn{2}{c|}{\makecell{SRP HDDM \\\\ ONESIDED}}')
    latex_code = latex_code.replace('HT_HDDM_ONESIDED & HT_HDDM_ONESIDED_10k', '\multicolumn{2}{c|}{\makecell{HT HDDM \\\\ ONESIDED}}')
    latex_code = latex_code.replace('ARF_HDDM_ONESIDED & ARF_HDDM_ONESIDED_10k', '\multicolumn{2}{c|}{\makecell{ARF HDDM \\\\ ONESIDED}}')

    with open(f'ohio/{column_name}_tab_summary.tex', "w") as f:
        f.write(latex_code)


def task_plot_warsaw():
    plot_warsaw()


def task_ohio_latex():
    latex_warsaw()
    latex_ohio()


def task_warsaw_arff():
    arff_warsaw_surveys()


# task_warsaw_arff()

# task_plot_ohio()
# plot_warsaw()

# latex_warsaw()
# task_prepare_latex_table()
