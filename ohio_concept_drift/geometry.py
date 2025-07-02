import json
import geopandas as gpd
import pandas as pd
import sys

OHIO_GEOMETRY = 'resources/ohio/ohio.geojson'


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
    return load_geoframe('resources/ohio/ohio.geojson')


def load_toledo():
    """
    (
      relation["ref"="LUC"]["border_type"="county"]["boundary"="administrative"];
      relation["ref"="WOO"]["border_type"="county"]["boundary"="administrative"];
      relation["ref"="MOE"]["border_type"="county"]["boundary"="administrative"];
    );
    out geom;
    """
    return load_geoframe("resources/ohio/toledo.geojson")


def load_dayton():
    """
    (
      relation["ref"="GRE"]["border_type"="county"]["boundary"="administrative"];
      relation["ref"="MIA"]["border_type"="county"]["boundary"="administrative"];
      relation["ref"="MOT"]["border_type"="county"]["boundary"="administrative"];
    );
    out geom;
    """
    return load_geoframe("resources/ohio/dayton.geojson")


def load_lima():
    """
    (
      relation["ref"="ALL"]["border_type"="county"]["boundary"="administrative"];
    );
    out geom;
    """
    return load_geoframe("resources/ohio/lima.geojson")


def load_springfield():
    """
    (
      relation["ref"="CLA"]["border_type"="county"]["boundary"="administrative"];
    );
    out geom;
    """
    return load_geoframe("resources/ohio/springfield.geojson")


def load_canton():
    """
    (
      relation["ref"="STA"]["border_type"="county"]["boundary"="administrative"];
    );
    out geom;
    """
    return load_geoframe("resources/ohio/canton.geojson")


def load_youngstown():
    """
    (
      relation["ref"="MAH"]["border_type"="county"]["boundary"="administrative"];
      relation["ref"="TRU"]["border_type"="county"]["boundary"="administrative"];
    );
    out geom;
    """
    return load_geoframe("resources/ohio/youngstown.geojson")


def load_steubenville():
    """
    (
      relation["name"="Brooke County"]["border_type"="county"]["boundary"="administrative"]["admin_level"=6];
      relation["ref"="HAN"]["border_type"="county"]["boundary"="administrative"];
      relation["ref"="JEF"]["border_type"="county"]["boundary"="administrative"];
    );
    out geom;
    """
    return load_geoframe("resources/ohio/steubenville.geojson")


def load_akron():
    """
    (
      relation["ref"="POR"]["border_type"="county"]["boundary"="administrative"];
      relation["ref"="SUM"]["border_type"="county"]["boundary"="administrative"];
    );
    out geom;
    """
    return load_geoframe("resources/ohio/akron.geojson")


def load_mansfield():
    """
    (
      relation["ref"="RIC"]["border_type"="county"]["boundary"="administrative"];
    );
    out geom;
    """
    return load_geoframe("resources/ohio/mansfield.geojson")


def ohio_cites_geopandas():
    toledo = load_toledo()
    lima = load_lima()
    dayton = load_dayton()
    springfield = load_springfield()
    akron = load_akron()
    canton = load_canton()
    mansfield = load_mansfield()
    steubenville = load_steubenville()
    youngstown = load_youngstown()

    # ohio_cities = pd.concat([toledo, lima, dayton, springfield, canton, youngstown, steubenville, akron, mansfield], ignore_index=True)
    ohio_cities = pd.concat([toledo, lima, dayton, springfield, akron, canton, mansfield, steubenville, youngstown], ignore_index=True)
    # ohio_cities = pd.concat([steubenville], ignore_index=True)

    return ohio_cities
