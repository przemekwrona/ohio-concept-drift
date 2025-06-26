import matplotlib.pyplot as plt

from shapely.affinity import scale
from ohio_concept_drift import geometry


def plot_ohio_state(geodata):
    # Load the GeoJSON file into a GeoDataFrame
    try:
        ohio_state_geometry = geometry.load_ohio_state()

        # Plotting different geometry types with different styles
        fig, ax = plt.subplots(1, 1, figsize=(10, 10))

        # Define the scaling factor
        scale_factor = 2.5
        ohio_scale_factor = 1.1

        ohio_state_scaled_geometry = geodata.copy()  # Work on a copy to preserve original data
        ohio_state_scaled_geometry['geometry'] = ohio_state_scaled_geometry['geometry'].apply(
            lambda geom: scale(geom, xfact=scale_factor, yfact=scale_factor, origin='centroid')
        )

        # Plit Ohio state
        ohio_state_geometry['geometry'] = ohio_state_geometry['geometry'].apply(
            lambda geom: scale(geom, xfact=ohio_scale_factor, yfact=ohio_scale_factor, origin='centroid')
        )
        ohio_state_geometry.plot(ax=ax, color='white', edgecolor='black', legend=True)

        # Plot polygons
        # ohio_cities_geometry[ohio_cities_geometry.geometry.type == 'Polygon'].plot(ax=ax, color='red', edgecolor='black', legend=True)
        ohio_state_scaled_geometry.plot(column='age', ax=ax, legend=True, cmap='viridis', legend_kwds={
            'label': "Age",  # Custom label for the colorbar
            'orientation': "vertical",  # Position the colorbar horizontally
            'shrink': 0.93,  # Reduce its size
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

        ax.set_xlim(-85.2, -80.2)

        # Set font size for x and y labels
        ax.set_xlabel('Longitude', fontsize=14)
        ax.set_ylabel('Latitude', fontsize=14)

        # Set font size for tick labels (x-axis and y-axis ticks)
        ax.tick_params(axis='x', labelsize=14)
        ax.tick_params(axis='y', labelsize=14)

        # Set font size for legend text
        ax.legend(fontsize=14)

        plt.grid(True)
        plt.show()

        fig.savefig("ohio.pdf", bbox_inches='tight')

    except FileNotFoundError:
        print("Error: 'my_plot_data.geojson' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
