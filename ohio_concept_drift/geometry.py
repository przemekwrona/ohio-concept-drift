import json
import geopandas as gpd
import pandas as pd
import sys
import overpass
import os

OHIO_GEOMETRY = 'resources/ohio/ohio.geojson'


def request_overpass(request_body, ml_region, geojson_file_name):
    geojson_file_path = f"resources/ohio/{geojson_file_name}"
    if os.path.exists(geojson_file_path):
        return

    api = overpass.API()
    response = api.get(request_body)

    multipolygons = []
    for feature in response["features"]:
        if feature['geometry']['type'] == 'MultiPolygon':
            feature['properties']['ML_region'] = ml_region
            multipolygons.append(feature)

    response["features"] = multipolygons

    with open(geojson_file_path, "w") as f:
        json.dump(response, f, indent=4)


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


def load_rural():
    rural_request_body = """
    (
        relation["ref"="ATB"]["border_type"="county"]["boundary"="administrative"];
        relation["ref"="AUG"]["border_type"="county"]["boundary"="administrative"];
        relation["ref"="BEL"]["border_type"="county"]["boundary"="administrative"];
        relation["ref"="BRO"]["border_type"="county"]["boundary"="administrative"];
        relation["ref"="CAR"]["border_type"="county"]["boundary"="administrative"];
        relation["ref"="COL"]["border_type"="county"]["boundary"="administrative"];
        relation["ref"="CRA"]["border_type"="county"]["boundary"="administrative"];
        relation["ref"="FUL"]["border_type"="county"]["boundary"="administrative"];
        relation["ref"="LAW"]["border_type"="county"]["boundary"="administrative"];
        relation["ref"="WAS"]["border_type"="county"]["boundary"="administrative"];
        relation["ref"="ADA"]["border_type"="county"]["boundary"="administrative"];
        relation["ref"="ASD"]["border_type"="county"]["boundary"="administrative"];
        relation["ref"="ATH"]["border_type"="county"]["boundary"="administrative"];
        relation["ref"="CHP"]["border_type"="county"]["boundary"="administrative"];
        relation["ref"="CLI"]["border_type"="county"]["boundary"="administrative"];
        relation["ref"="COS"]["border_type"="county"]["boundary"="administrative"];
        relation["ref"="DAR"]["border_type"="county"]["boundary"="administrative"];
        relation["ref"="DEF"]["border_type"="county"]["boundary"="administrative"];
        relation["ref"="ERI"]["border_type"="county"]["boundary"="administrative"];
        relation["ref"="GAL"]["border_type"="county"]["boundary"="administrative"];
        relation["ref"="GUE"]["border_type"="county"]["boundary"="administrative"];
        relation["ref"="HAN"]["border_type"="county"]["boundary"="administrative"];
        relation["ref"="HAR"]["border_type"="county"]["boundary"="administrative"];
        relation["ref"="HAS"]["border_type"="county"]["boundary"="administrative"];
        relation["ref"="HEN"]["border_type"="county"]["boundary"="administrative"];
        relation["ref"="HIG"]["border_type"="county"]["boundary"="administrative"];
        relation["ref"="HOC"]["border_type"="county"]["boundary"="administrative"];
        relation["ref"="JAC"]["border_type"="county"]["boundary"="administrative"];
        relation["ref"="KNO"]["border_type"="county"]["boundary"="administrative"];
        relation["ref"="LOG"]["border_type"="county"]["boundary"="administrative"];
        relation["ref"="MAR"]["border_type"="county"]["boundary"="administrative"];
        relation["ref"="MEG"]["border_type"="county"]["boundary"="administrative"];
        relation["ref"="MER"]["border_type"="county"]["boundary"="administrative"];
        relation["ref"="MOE"]["border_type"="county"]["boundary"="administrative"];
        relation["ref"="MRG"]["border_type"="county"]["boundary"="administrative"];
        relation["ref"="MRW"]["border_type"="county"]["boundary"="administrative"];
        relation["ref"="MUS"]["border_type"="county"]["boundary"="administrative"];
        relation["ref"="NOB"]["border_type"="county"]["boundary"="administrative"];
        relation["ref"="OTT"]["border_type"="county"]["boundary"="administrative"];
        relation["ref"="PAU"]["border_type"="county"]["boundary"="administrative"];
        relation["ref"="PER"]["border_type"="county"]["boundary"="administrative"];
        relation["ref"="PIK"]["border_type"="county"]["boundary"="administrative"];
        relation["ref"="PRE"]["border_type"="county"]["boundary"="administrative"];
        relation["ref"="PUT"]["border_type"="county"]["boundary"="administrative"];
        relation["ref"="ROS"]["border_type"="county"]["boundary"="administrative"];
        relation["ref"="SAN"]["border_type"="county"]["boundary"="administrative"];
        relation["ref"="SCI"]["border_type"="county"]["boundary"="administrative"];
        relation["ref"="SEN"]["border_type"="county"]["boundary"="administrative"];
        relation["ref"="SHE"]["border_type"="county"]["boundary"="administrative"];
        relation["ref"="TUS"]["border_type"="county"]["boundary"="administrative"];
        relation["ref"="VAN"]["border_type"="county"]["boundary"="administrative"];
        relation["ref"="VIN"]["border_type"="county"]["boundary"="administrative"];
        relation["ref"="WAY"]["border_type"="county"]["boundary"="administrative"];
        relation["ref"="WIL"]["border_type"="county"]["boundary"="administrative"];
        relation["ref"="WYA"]["border_type"="county"]["boundary"="administrative"];
    );
    out geom;
    """

    request_overpass(rural_request_body, '10_RURAL', 'rural.geojson')
    return load_geoframe("resources/ohio/rural.geojson")


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
    rural = load_rural()

    ohio_cities = pd.concat([toledo, lima, dayton, springfield, akron, canton, mansfield, steubenville, youngstown, rural], ignore_index=True)

    return ohio_cities


def warsaw_districts_geopandas():
    warsaw_districts = load_geoframe("resources/warsaw/warszawa-dzielnice.geojson")

    return warsaw_districts
