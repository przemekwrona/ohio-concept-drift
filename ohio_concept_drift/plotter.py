import geopandas as gpd
import matplotlib.pyplot as plt

from ohio_concept_drift import geometry


def plot_ohio_state():
    # Load the GeoJSON file into a GeoDataFrame
    try:
        ohio_geometry = gpd.read_file(geometry.OHIO_GEOMETRY)

        # Basic plot
        ohio_geometry.plot(edgecolor='black', linewidth=1)
        plt.xlabel('Longitude')
        plt.ylabel('Latitude')
        plt.grid(True)
        plt.show()

        # Plotting different geometry types with different styles
        fig, ax = plt.subplots(1, 1, figsize=(10, 10))

        # Plot polygons
        ohio_geometry[ohio_geometry.geometry.type == 'Polygon'].plot(ax=ax, color='skyblue', edgecolor='white', legend=True)

        # Plot lines
        ohio_geometry[ohio_geometry.geometry.type == 'LineString'].plot(ax=ax, color='red', linewidth=2, legend=True)

        # Plot points
        ohio_geometry[ohio_geometry.geometry.type == 'Point'].plot(ax=ax, marker='o', color='green', markersize=50, legend=True)

        plt.title('Styled GeoJSON Plot')
        plt.xlabel('Longitude')
        plt.ylabel('Latitude')
        plt.grid(True)
        plt.show()

    except FileNotFoundError:
        print("Error: 'my_plot_data.geojson' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
