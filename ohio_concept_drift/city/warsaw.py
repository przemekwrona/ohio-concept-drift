import geopandas as gpd
import logging


class Warsaw:
    def __init__(self):
        # Path to your GeoJSON files
        self.geojson_districts_file = 'resources/warsaw/warszawa-dzielnice.geojson'

        # Load and concatenate all GeoJSONs
        self.districts = gpd.read_file(self.geojson_districts_file)

    def get_district(self, point):
        point_in_district = self.districts.contains(point)
        districts = self.districts[point_in_district & (self.districts['cartodb_id'] != 1)]

        if len(districts) == 0:
            logging.warning(f"Expected found districts of length 1, but got {len(districts)}. Point {point} does not fit to any district")
            return None, None

        if len(districts) > 1:
            raise ValueError(f"Expected DataFrame of length 1, but got {len(districts)}. None of districts")

        district_name = districts.iloc[0]['name'].upper()

        if district_name in ["PRAGA PÓŁNOC", "PRAGA POŁUDNIE", "BIAŁOŁĘKA", "TARGÓWEK", "WESOŁA", "WAWER", "REMBERTÓW"]:
            vistula_bank = "RIGHT_VISTULA_BANK"
        elif district_name in ["WOLA", "MOKOTÓW", "BEMOWO", "ŚRÓDMIEŚCIE", "OCHOTA", "BIELANY", "URSUS", "ŻOLIBORZ", "URSYNÓW", "WŁOCHY", "WILANÓW"]:
            vistula_bank = "LEFT_VISTULA_BANK"
        else:
            raise ValueError(f"Not recognized district: {district_name}")

        return district_name, vistula_bank
