import json

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
