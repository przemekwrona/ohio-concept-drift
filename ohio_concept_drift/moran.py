import os

from splot._viz_utils import mask_local_auto

from ohio_concept_drift import ohio_data as data_frame
import pandas as pd
import libpysal
from esda import Moran, Moran_Local
import matplotlib.pyplot as plt
from ohio_concept_drift import geometry
import matplotlib.patches as mpatches

RED = '#d7191c'

color_map = {
    "HH": RED,
    "HL": "orange",
    # "LH": "green",
    "LH": "lightblue",
    "LL": "blue",
    "ns": "lightgrey"
}


def ohio_moran_correlation(results_config, column='total_drift_detection'):
    for (experiment, result_path) in results_config:
        ohio(experiment_name=experiment, drift_results_directory=result_path, column_name=column)


def usa_moran_latex(results_config, target_directory, column='total_drift_detection'):
    results = pd.DataFrame(data={})

    for (experiment, result_path) in results_config:
        print(experiment)

        moran_data_frame = moran_results(experiment_name=experiment, geodata_frame=data_frame.usa_data_frame(drift_results_directory=result_path),
                                         column_name=column)
        simple_moran_data_frame = moran_data_frame[['ML_region', 'label']]
        # simple_moran_data_frame = simple_moran_data_frame.dissolve(by="ML_region")
        simple_moran_data_frame.loc[simple_moran_data_frame['label'] == 'ns', 'label'] = ''
        grouped_moran_data_frame = simple_moran_data_frame.groupby('ML_region')['label'].agg('first').reset_index()

        grouped_moran_data_frame = grouped_moran_data_frame.rename(columns={'label': f'{experiment}'})

        if results.empty:
            results = grouped_moran_data_frame
        else:
            results = pd.merge(results, grouped_moran_data_frame, on='ML_region')

    latex = build_latex(results)

    with open(f'{target_directory}/moran_summary.tex', 'w', encoding='utf-8') as f:
        f.write(latex)

    print("DONE")


def ohio_moran_latex(results_config, target_directory, column='total_drift_detection'):
    results = pd.DataFrame(data={})

    for (experiment, result_path) in results_config:
        print(experiment)

        moran_data_frame = moran_results(experiment_name=experiment, geodata_frame=data_frame.ohio_data_frame(drift_results_directory=result_path),
                                         column_name=column)
        simple_moran_data_frame = moran_data_frame[['ML_region', 'label']]
        # simple_moran_data_frame = simple_moran_data_frame.dissolve(by="ML_region")
        simple_moran_data_frame.loc[simple_moran_data_frame['label'] == 'ns', 'label'] = ''
        grouped_moran_data_frame = simple_moran_data_frame.groupby('ML_region')['label'].agg('first').reset_index()

        grouped_moran_data_frame = grouped_moran_data_frame.rename(columns={'label': f'{experiment}'})

        if results.empty:
            results = grouped_moran_data_frame
        else:
            results = pd.merge(results, grouped_moran_data_frame, on='ML_region')

    latex = build_latex(results)

    with open(f'{target_directory}/moran_summary.tex', 'w', encoding='utf-8') as f:
        f.write(latex)

    print("DONE")


def build_latex(results):
    latex = results.to_latex(index=False)

    latex = latex.replace('\\\\', '\\\\ \hline')
    latex = latex.replace('ML_region', 'Region')
    latex = latex.replace('NB_ADWIN', '\\rotatebox[origin=c]{90}{\makecell{NB ADWIN}}')
    latex = latex.replace('ARF_ADWIN', '\\rotatebox[origin=c]{90}{\makecell{ARF ADWIN}}')
    latex = latex.replace('HAT_ADWIN', '\\rotatebox[origin=c]{90}{\makecell{HAT ADWIN}}')
    latex = latex.replace('HT_ADWIN', '\\rotatebox[origin=c]{90}{\makecell{HT ADWIN}}')
    latex = latex.replace('NB_HDDM_ONESIDED', '\\rotatebox[origin=c]{90}{\makecell{NB HDDM \\\\ ONESIDED}}')
    latex = latex.replace('SRP_HDDM_ONESIDED', '\\rotatebox[origin=c]{90}{\makecell{SRP HDDM \\\\ ONESIDED}}')
    latex = latex.replace('HT_HDDM_ONESIDED', '\\rotatebox[origin=c]{90}{\makecell{HT HDDM \\\\ ONESIDED}}')
    latex = latex.replace('ARF_HDDM_ONESIDED', '\\rotatebox[origin=c]{90}{\makecell{ARF HDDM \\\\ ONESIDED}}')
    latex = latex.replace('01_TOLEDO', '01 TOLEDO')
    latex = latex.replace('02_LIMA', '02 LIMA')
    latex = latex.replace('03_DAYTON', '03 DAYTON')
    latex = latex.replace('04_SPRINGFIELD', '04 SPRINGFIELD')
    latex = latex.replace('05_AKRON', '05 AKRON')
    latex = latex.replace('06_CANTON', '06 CANTON')
    latex = latex.replace('07_MANSFIELD', '07 MANSFIELD')
    latex = latex.replace('08_STEUBENVILLE', '08 STEUBENVILLE')
    latex = latex.replace('09_YOUNGSTOWN', '09 YOUNGSTOWN')
    latex = latex.replace('10_RURAL', '10 RURAL')
    latex = latex.replace('\\toprule', '\hline')
    latex = latex.replace('\\midrule', '')
    latex = latex.replace('\\bottomrule', '')
    latex = latex.replace('HH', '\cellcolor{red}{\color{white}HH}')
    latex = latex.replace('HL', '\cellcolor{orange}{\color{white}HL}')
    latex = latex.replace('LH', '\cellcolor{cyan}{\color{white}LH}')
    latex = latex.replace('LL', '\cellcolor{blue}{\color{white}LH}')

    latex = latex.replace('\\bottomrule', '')

    return latex


def usa_moran_correlation(results_config, column='total_drift_detection'):
    for (experiment, result_path) in results_config:
        usa(experiment_name=experiment, drift_results_directory=result_path, column_name=column)
        # usa('ARF_HDDM_ONESIDED', 'experiments/usa/ARF_HDDM_ONESIDED/ARF_HDDM_ONESIDED_drift_log.csv', column)


def ohio(experiment_name, drift_results_directory, column_name):
    gdf = data_frame.ohio_data_frame(drift_results_directory=drift_results_directory)
    plot_ohio_moran_correlation(experiment_name, gdf, column_name)


def usa(experiment_name, drift_results_directory, column_name):
    gdf = data_frame.usa_data_frame(drift_results_directory=drift_results_directory)
    plot_usa_moran_correlation(experiment_name, gdf, column_name)


def moran_results(experiment_name, geodata_frame, column_name):
    merged = geodata_frame.dissolve(by="ML_region")
    merged = merged.reset_index().rename(columns={"index": "ML_region"})

    # 1. Zmienna, dla której liczymy autokorelację
    y = merged[column_name].values  # poziom przestępczości

    # 2. Utworzenie macierzy wag przestrzennych (sąsiedztwo Queen)
    w = libpysal.weights.Queen.from_dataframe(merged, use_index=True)
    w.transform = 'r'  # normalizacja

    # 3. Obliczenie Moran’s I
    moran = Moran(y, w)

    print(f"Experiment name: {experiment_name}\n\n")

    print("Moran's I:", moran.I)
    print("p-value:", moran.p_sim)

    # 4. Wykres rozrzutu Moran'a
    moran_loc = Moran_Local(y, w)
    _, _, _, labels = mask_local_auto(moran_loc, p=0.05)
    merged['label'] = labels
    label_in_ml_region = merged[['ML_region', 'label']]
    return pd.merge(geodata_frame, label_in_ml_region, on='ML_region')


def plot_ohio_moran_correlation(experiment_name, geodata_frame, column_name):
    gdf = moran_results(experiment_name, geodata_frame, column_name)

    fig, ax = plt.subplots()

    # ✅ Custom legend
    patches = [mpatches.Patch(color=v, label=k) for k, v in color_map.items()]
    ax.legend(handles=patches, title="Spatial Cluster", loc="upper right", bbox_to_anchor=(1.35, 1.02))

    gdf["color"] = gdf["label"].map(color_map)

    gdf.plot(column='label', ax=ax, color=gdf['color'], linewidth=0.1, edgecolor='black')

    # lisa_cluster(moran_loc, ax=ax, gdf=merged, p=0.05)

    ax.set_axis_on()

    ax.set_xlim(-85.5, -80.0)

    FONT_SIZE = 12
    # Set font size for x and y labels
    ax.set_xlabel('Longitude', fontsize=FONT_SIZE)
    ax.set_ylabel('Latitude', fontsize=FONT_SIZE)

    # Set font size for tick labels (x-axis and y-axis ticks)
    ax.tick_params(axis='x', labelsize=FONT_SIZE)
    ax.tick_params(axis='y', labelsize=FONT_SIZE)

    plt.grid(True)

    for idx, row in gdf.iterrows():
        point = row['geometry'].centroid
        text = row['ML_region'][:2]
        if row['color'] == RED:
            ax.annotate(text, xy=(point.x, point.y), horizontalalignment='center', fontsize=8, color='white')
        else:
            ax.annotate(text, xy=(point.x, point.y), horizontalalignment='center', fontsize=8, color='black')

    ohio_state_geometry = geometry.load_ohio_state()
    ohio_state_geometry.plot(ax=ax, color=(0, 0, 0, 0), edgecolor='black', legend=True)

    cincinnati = geometry.load_cincinnati()
    cincinnati_centroid = cincinnati.dissolve().to_crs(epsg=4326).centroid
    ax.annotate('Cincinnati', xy=(cincinnati_centroid.x - .05, cincinnati_centroid.y), horizontalalignment='center', fontsize=7, color='black')

    columbus = geometry.load_columbus()
    columbus_centroid = columbus.dissolve().to_crs(epsg=4326).centroid
    ax.annotate('Columbus/Newark', xy=(columbus_centroid.x + .05, columbus_centroid.y), horizontalalignment='center', fontsize=7, color='black')

    cleveland = geometry.load_cleveland()
    cleveland_centroid = cleveland.dissolve().to_crs(epsg=4326).centroid
    ax.annotate('Cleveland', xy=(cleveland_centroid.x + .1, cleveland_centroid.y - .1), horizontalalignment='center', fontsize=7, color='black')

    fig.savefig(f'ohio/{experiment_name}/moran_correlation.pdf', bbox_inches='tight')
    plt.show()
    # plot_local_autocorrelation(moran_loc, gdf, column_name)


def plot_usa_moran_correlation(experiment_name, geodata_frame, column_name):
    gdf = moran_results(experiment_name, geodata_frame, column_name)

    fig, ax = plt.subplots()

    # ✅ Custom legend
    patches = [mpatches.Patch(color=v, label=k) for k, v in color_map.items()]
    ax.legend(handles=patches, title="Spatial Cluster", loc="upper right", bbox_to_anchor=(1.35, 1.02))

    gdf["color"] = gdf["label"].map(color_map)

    gdf.plot(column='label', ax=ax, color=gdf['color'], linewidth=0.1, edgecolor='black')

    # lisa_cluster(moran_loc, ax=ax, gdf=merged, p=0.05)

    ax.set_axis_on()

    ax.set_xlim(-130.0, -65.0)
    ax.set_ylim(15.0, 60.0)

    FONT_SIZE = 12
    # Set font size for x and y labels
    ax.set_xlabel('Longitude', fontsize=FONT_SIZE)
    ax.set_ylabel('Latitude', fontsize=FONT_SIZE)

    # Set font size for tick labels (x-axis and y-axis ticks)
    ax.tick_params(axis='x', labelsize=FONT_SIZE)
    ax.tick_params(axis='y', labelsize=FONT_SIZE)

    plt.grid(True)

    for idx, row in gdf.iterrows():
        point = row['geometry'].centroid
        text = row['ML_region'][:2]
        if row['color'] == RED:
            ax.annotate(text, xy=(point.x, point.y), horizontalalignment='center', fontsize=8, color='white')
        else:
            ax.annotate(text, xy=(point.x, point.y), horizontalalignment='center', fontsize=8, color='black')

    os.makedirs(f'usa/{experiment_name}/', exist_ok=True)

    fig.savefig(f'usa/{experiment_name}/moran_correlation.pdf', bbox_inches='tight')
    plt.show()
    # plot_local_autocorrelation(moran_loc, gdf, column_name)
