import json
import geopandas as gpd
import sys

OHIO_GEOMETRY = 'resources/ohio.geojson'


def load_ohio_geojson():
    # Assuming you have a GeoJSON file named 'my_data.geojson'
    try:
        with open(OHIO_GEOMETRY, 'r', encoding='utf-8') as f:
            geojson_data = json.load(f)
        print("GeoJSON data loaded successfully:")
        print(geojson_data)

        # You can access specific parts of the GeoJSON data like this:
        if geojson_data.get('type') == 'FeatureCollection':
            for feature in geojson_data['features']:
                print(f"Feature properties: {feature.get('properties')}")
                print(f"Feature geometry: {feature.get('geometry')}")

        return geojson_data

    except FileNotFoundError:
        print("Error: 'my_data.geojson' not found. Please create the file or provide the correct path.")
    except json.JSONDecodeError:
        print("Error: Could not decode GeoJSON. The file might be malformed.")


def load_ohio_geoframe():
    """
       Loads GeoJSON data from a specified file into a GeoDataFrame.

       Args:
           geojson_filepath (str): The path to the GeoJSON file.

       Returns:
           geopandas.GeoDataFrame: A GeoDataFrame containing the loaded geometry,
                                   or None if an error occurs.
       """
    try:
        ohio_geometry = gpd.read_file(OHIO_GEOMETRY)
        print(f"Successfully loaded GeoDataFrame from: {OHIO_GEOMETRY}")
        return ohio_geometry

    except FileNotFoundError:
        print(f"Error: The file '{OHIO_GEOMETRY}' was not found. Please ensure the path is correct.", file=sys.stderr)
        return None
    except Exception as e:
        # This catches a broader range of issues that gpd.read_file might raise,
        # including issues with malformed GeoJSON that fiona might report.
        print(f"An error occurred while reading or decoding GeoJSON from '{OHIO_GEOMETRY}': {e}", file=sys.stderr)
        return None
