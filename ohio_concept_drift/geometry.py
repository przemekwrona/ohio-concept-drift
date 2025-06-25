import json
import geopandas as gpd
import pandas as pd
import sys

OHIO_GEOMETRY = 'resources/ohio.geojson'


def load_geoframe(path):
    """
       Loads GeoJSON data from a specified file into a GeoDataFrame.

       Args:
           geojson_filepath (str): The path to the GeoJSON file.

       Returns:
           geopandas.GeoDataFrame: A GeoDataFrame containing the loaded geometry,
                                   or None if an error occurs.
       """
    try:
        ohio_geometry = gpd.read_file(path)
        print(f"Successfully loaded GeoDataFrame from: {path}")
        return ohio_geometry

    except FileNotFoundError:
        print(f"Error: The file '{path}' was not found. Please ensure the path is correct.", file=sys.stderr)
        return None
    except Exception as e:
        # This catches a broader range of issues that gpd.read_file might raise,
        # including issues with malformed GeoJSON that fiona might report.
        print(f"An error occurred while reading or decoding GeoJSON from '{path}': {e}", file=sys.stderr)
        return None


def load_ohio_state():
    return load_geoframe('resources/ohio.geojson')


def load_toledo():
    """
    relation["type"="boundary"]["border_type"="city"]["place"="city"]["admin_level"="8"]["name"="Toledo"];
    out geom;
    """
    return load_geoframe("resources/toledo.geojson")


def load_dayton():
    """
    relation["type"="boundary"]["border_type"="city"]["place"="city"]["admin_level"="8"]["name"="Dayton"]["gnis:feature_id"="1086666"];
    out geom;
    """
    return load_geoframe("resources/dayton.geojson")


def load_lima():
    """
    relation["type"="boundary"]["border_type"="city"]["place"="city"]["admin_level"="7"]["name"="Lima"]["gnis:feature_id"="1085694"];
    out geom;
    """
    return load_geoframe("resources/lima.geojson")


def load_springfield():
    """
    relation["type"="boundary"]["border_type"="city"]["place"="city"]["admin_level"="8"]["name"="Springfield"]["gnis:feature_id"="1085859"];
    out geom;
    """
    return load_geoframe("resources/springfield.geojson")


def load_canton():
    """
    relation["type"="boundary"]["border_type"="city"]["place"="city"]["admin_level"="8"]["name"="Canton"]["gnis:feature_id"="1086974"];
    out geom;
    """
    return load_geoframe("resources/canton.geojson")


def load_youngstown():
    """
    relation["type"="boundary"]["border_type"="city"]["place"="city"]["admin_level"="8"]["name"="Youngstown"]["gnis:feature_id"="1086573"];
    out geom;
    """
    return load_geoframe("resources/youngstown.geojson")


def load_steubenville():
    """
    relation["type"="boundary"]["border_type"="city"]["place"="city"]["admin_level"="8"]["name"="Steubenville"]["gnis:feature_id"="1086386"];
    out geom;
    """
    return load_geoframe("resources/steubenville.geojson")


def load_akron():
    """
    relation["type"="boundary"]["border_type"="city"]["place"="city"]["admin_level"="8"]["name"="Akron"]["gnis:feature_id"="1086993"];
    out geom;
    """
    return load_geoframe("resources/akron.geojson")


def load_mansfield():
    """
    relation["type"="boundary"]["border_type"="city"]["place"="town"]["admin_level"="8"]["name"="Mansfield"];
    out geom;
    """
    return load_geoframe("resources/mansfield.geojson")


def ohio_cites_geopandas():
    toledo = load_toledo()
    lima = load_lima()
    dayton = load_dayton()
    springfield = load_springfield()
    canton = load_canton()
    youngstown = load_youngstown()
    steubenville = load_steubenville()
    akron = load_akron()
    mansfield = load_mansfield()

    ohio_cities = pd.concat([toledo, lima, dayton, springfield, canton, youngstown, steubenville, akron, mansfield], ignore_index=True)

    return ohio_cities
