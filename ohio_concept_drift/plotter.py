import matplotlib.pyplot as plt
import numpy as np

from shapely.affinity import scale
from ohio_concept_drift import geometry


def plot_ohio_state(geodata, column_name, file_name, vmax=None, **kwargs):
    # Load the GeoJSON file into a GeoDataFrame

    real_max = np.max(geodata[column_name])
    vmax = vmax if vmax is not None else real_max

    label = kwargs.get('label') if kwargs.get('label') is not None else ''
    step = kwargs.get('step') if kwargs.get('step') is not None else vmax / 10
    is_gt_showed = kwargs.get('is_gt_showed') if kwargs.get('is_gt_showed') is not None else False

    try:
        ohio_state_geometry = geometry.load_ohio_state()

        # Plotting different geometry types with different styles
        fig, ax = plt.subplots(1, 1, figsize=(10, 10))

        # ohio_state_scaled_geometry = geodata.copy()  # Work on a copy to preserve original data
        ohio_state_geometry.plot(ax=ax, color='white', edgecolor='black', legend=True)

        # Replace numeric ticks with custom labels
        ticks = np.arange(0, vmax + step, step)
        max_tick = ticks[-1].astype(float)

        gdf_plot = ohio_state_geometry.plot(column=column_name, ax=ax, vmax=max_tick, legend=False,
                                                   # legend_kwds={
                                                   #     'label': label,  # Custom label for the colorbar
                                                   #     'orientation': "vertical",  # Position the colorbar horizontally
                                                   #     'shrink': 0.88,  # Reduce its size
                                                   #     'pad': 0.01,  # Padding between map and colorbar
                                                   #     # 'anchor': (0.0, 0.0),  # Anchor point for positioning (x, y) relative to axes
                                                   #     # 'bbox_to_anchor': (1.02, 0.5),  # Position slightly outside the right edge
                                                   #
                                                   #     'aspect': 20,  # Aspect ratio of the colorbar
                                                   #     'format': '%.0f'  # Format the tick labels (no decimal places)
                                                   # },
                                                   linewidth=.1, edgecolor='black')

        # Get the colorbar and replace tick labels
        sm = plt.cm.ScalarMappable(cmap='viridis', norm=plt.Normalize(vmin=0, vmax=max_tick))
        sm._A = []  # Hack to prevent warning
        cbar = fig.colorbar(sm, ax=ax, fraction=0.05, pad=0.01, shrink=0.97)

        cbar.set_ticks(ticks)

        if vmax > 100_000:
            tick_labels = ticks
            tick_labels = np.divide(tick_labels, 1000)
            tick_labels = tick_labels.astype(int)
            tick_labels = tick_labels.astype(str)
            tick_labels = [f"{tick}k" for tick in tick_labels]
        else:
            tick_labels = ticks.astype(str)

        if is_gt_showed:
            tick_labels[-1] = f">{tick_labels[-1]}"

        cbar.set_ticklabels(tick_labels)

        # Optional: set colorbar label
        cbar.set_label(label, fontsize=12)

        ax.set_xlim(-85.5, -80.0)

        # Set font size for x and y labels
        ax.set_xlabel('Longitude', fontsize=14)
        ax.set_ylabel('Latitude', fontsize=14)

        # Set font size for tick labels (x-axis and y-axis ticks)
        ax.tick_params(axis='x', labelsize=14)
        ax.tick_params(axis='y', labelsize=14)

        plt.grid(True)

        for idx, row in geodata.iterrows():
            point = row['geometry'].centroid
            text = row['ML_region'][:2]
            print(f"{row[column_name]}; {2 * row[column_name]} < {vmax}")
            if 2 * row[column_name] < vmax:
                ax.annotate(text, xy=(point.x, point.y), horizontalalignment='center', fontsize=11, color='white')
            else:
                ax.annotate(row['ML_region'][:2], xy=(point.x, point.y), horizontalalignment='center', fontsize=11, color='black')

        cincinnati = geometry.load_cincinnati()
        cincinnati_centroid = cincinnati.dissolve().to_crs(epsg=4326).centroid
        ax.annotate('Cincinnati', xy=(cincinnati_centroid.x - .05, cincinnati_centroid.y), horizontalalignment='center', fontsize=9, color='black')

        columbus = geometry.load_columbus()
        columbus_centroid = columbus.dissolve().to_crs(epsg=4326).centroid
        ax.annotate('Columbus/Newark', xy=(columbus_centroid.x + .05, columbus_centroid.y), horizontalalignment='center', fontsize=9, color='black')

        cleveland = geometry.load_cleveland()
        cleveland_centroid = cleveland.dissolve().to_crs(epsg=4326).centroid
        ax.annotate('Cleveland', xy=(cleveland_centroid.x + .1, cleveland_centroid.y - .1), horizontalalignment='center', fontsize=9, color='black')

        fig.savefig(file_name, bbox_inches='tight')

    except FileNotFoundError:
        print("Error: 'my_plot_data.geojson' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def plot_warsaw(geodata, column_name, file_name, vmax=None):
    # Load the GeoJSON file into a GeoDataFrame

    if vmax is None:
        vmax = np.max(geodata[column_name])

    try:
        ohio_state_geometry = geometry.load_ohio_state()

        # Plotting different geometry types with different styles
        fig, ax = plt.subplots(1, 1, figsize=(10, 10))

        # Define the scaling factor
        scale_factor = 1.0
        ohio_scale_factor = 1.0

        ohio_state_scaled_geometry = geodata.copy()  # Work on a copy to preserve original data
        ohio_state_scaled_geometry['geometry'] = ohio_state_scaled_geometry['geometry'].apply(
            lambda geom: scale(geom, xfact=scale_factor, yfact=scale_factor, origin='centroid')
        )

        # Plit Ohio state
        # ohio_state_geometry['geometry'] = ohio_state_geometry['geometry'].apply(
        #     lambda geom: scale(geom, xfact=ohio_scale_factor, yfact=ohio_scale_factor, origin='centroid')
        # )
        # ohio_state_geometry.plot(ax=ax, color='white', edgecolor='black', legend=True)

        # Plot polygons
        # ohio_cities_geometry[ohio_cities_geometry.geometry.type == 'Polygon'].plot(ax=ax, color='red', edgecolor='black', legend=True)
        ohio_state_scaled_geometry.plot(column=column_name, ax=ax, legend=True, cmap='viridis', vmin=0, vmax=vmax, legend_kwds={
            'label': "Total Drift Detection",  # Custom label for the colorbar
            'orientation': "vertical",  # Position the colorbar horizontally
            'shrink': 0.88,  # Reduce its size
            'pad': 0.01,  # Padding between map and colorbar
            # 'anchor': (0.0, 0.0),  # Anchor point for positioning (x, y) relative to axes
            # 'bbox_to_anchor': (1.02, 0.5),  # Position slightly outside the right edge

            'aspect': 20,  # Aspect ratio of the colorbar
            'format': '%.0f'  # Format the tick labels (no decimal places)
        })

        # Plot lines
        # ohio_cities_geometry[ohio_cities_geometry.geometry.type == 'LineString'].plot(ax=ax, color='red', linewidth=1, legend=True)

        # Plot points
        # ohio_cities_geometry[ohio_cities_geometry.geometry.type == 'Point'].plot(ax=ax, marker='o', color='green', markersize=50, legend=True)

        # ax.set_xlim(-85.2, -80.2)

        # Set font size for x and y labels
        ax.set_xlabel('Longitude', fontsize=14)
        ax.set_ylabel('Latitude', fontsize=14)

        # Set font size for tick labels (x-axis and y-axis ticks)
        ax.tick_params(axis='x', labelsize=14)
        ax.tick_params(axis='y', labelsize=14)

        # Set font size for legend text
        # ax.legend(fontsize=14)

        plt.grid(True)
        plt.show()

        fig.savefig(file_name, bbox_inches='tight')

    except FileNotFoundError:
        print("Error: 'my_plot_data.geojson' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
