from ohio_concept_drift.warsaw_data import plot_warsaw
from ohio_concept_drift.latex import summary_usa_data
from ohio_concept_drift.warsaw_arff import arff_warsaw_surveys
from ohio_concept_drift import config, moran
from ohio_concept_drift import detection_summary
from ohio_concept_drift.ohio_data import plot_ohio, plot_usa


def task_plot_ohio():
    for (experiment, results_directory) in config.ohio_config:
        plot_ohio(experiment, results_directory)

    detection_summary.summary_ohio_number_of_detection(results_config=config.ohio_config, target_directory='ohio', column_name='total_drift_detection')

    moran.ohio_moran_correlation(results_config=config.ohio_config)
    moran.ohio_moran_latex(results_config=config.ohio_config, target_directory='ohio')


def task_plot_usa():
    summary_usa_data()

    # for (experiment, results_directory) in config.usa_results_config:
    #     plot_usa(experiment, results_directory)
    #
    # detection_summary.summary_usa_number_of_detection(results_config=config.usa_results_config, target_directory='usa', column_name='total_drift_detection')
    #
    # moran.usa_moran_correlation(results_config=config.usa_results_config)
    # moran.usa_moran_latex(results_config=config.usa_results_config, target_directory='usa')


def task_plot_warsaw():
    plot_warsaw()


def task_warsaw_arff():
    arff_warsaw_surveys()


# moran.ohio_moran_correlation()
# task_basic_statistic_latex()
task_plot_usa()
# task_plot_ohio()
# task_warsaw_arff()

# task_plot_ohio()
# plot_warsaw()

# latex_warsaw()
# task_prepare_latex_table()
