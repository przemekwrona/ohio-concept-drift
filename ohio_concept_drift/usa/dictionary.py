USA_STATES_CODES = {
    "AL": "AL Alabama",
    "AK": "AK Alaska",
    "AZ": "AZ Arizona",
    "AR": "AR Arkansas",
    "CA": "CA California",
    "CO": "CO Colorado",
    "CT": "CT Connecticut",
    "DE": "DE Delaware",
    "FL": "FL Florida",
    "GA": "GA Georgia",
    "HI": "HI Hawaii",
    "ID": "ID Idaho",
    "IL": "IL Illinois",
    "IN": "IN Indiana",
    "IA": "IA Iowa",
    "KS": "KS Kansas",
    "KY": "KY Kentucky",
    "LA": "LA Louisiana",
    "ME": "ME Maine",
    "MD": "MD Maryland",
    "MA": "MA Massachusetts",
    "MI": "MI Michigan",
    "MN": "MN Minnesota",
    "MS": "MS Mississippi",
    "MO": "MO Missouri",
    "MT": "MT Montana",
    "NE": "NE Nebraska",
    "NV": "NV Nevada",
    "NH": "NH New Hampshire",
    "NJ": "NJ New Jersey",
    "NM": "NM New Mexico",
    "NY": "NY New York",
    "NC": "NC North Carolina",
    "ND": "ND North Dakota",
    "OH": "OH Ohio",
    "OK": "OK Oklahoma",
    "OR": "OR Oregon",
    "PA": "PA Pennsylvania",
    "RI": "RI Rhode Island",
    "SC": "SC South Carolina",
    "SD": "SD South Dakota",
    "TN": "TN Tennessee",
    "TX": "TX Texas",
    "UT": "UT Utah",
    "VT": "VT Vermont",
    "VA": "VA Virginia",
    "WA": "WA Washington",
    "WV": "WV West Virginia",
    "WI": "WI Wisconsin",
    "WY": "WY Wyoming"
}

UNKNOWN = "UNKNOWN"
CAR = "CAR"
PT = "PT"
BIKE = "BIKE"
WALK = "WALK"
OTHER = "OTHER"

USA_TMC_CODES_2009 = {
    "-7": OTHER,  # I prefer not to answer / Refused
    "-8": OTHER,  # I don't know
    "-9": OTHER,  # Not ascertained
    "1": CAR,  # Car
    "2": CAR,  # Van
    "3": CAR,  # SUV
    "4": CAR,  # Pick-up Truck
    "5": CAR,  # Other Truck
    "6": CAR,  # RV
    "7": CAR,  # Motorcycle
    "8": CAR,  # Light Electric Vehicle
    "9": PT,  # Local Public Bus
    "10": PT,  # Commuter Bus
    "11": PT,  # School bus
    "12": OTHER,  # Charter/Tour
    "13": PT,  # City-to-City Bus
    "14": PT,  # Shuttle Bus
    "15": PT,  # Amtrak/Inter-city Train
    "16": PT,  # Commuter Train
    "17": PT,  # Subway/elevated Train
    "18": PT,  # Streetcar/Trolley
    "19": PT,  # Taxicab
    "20": OTHER,  # Ferry
    "21": OTHER,  # Airplane
    "22": BIKE,  # Bicycle
    "23": WALK,  # Walk
    "97": OTHER,  # Other
}

USA_TMC_CODES_2017 = {
    "-7": OTHER,  # I prefer not to answer / Refused
    "-8": OTHER,  # I don't know
    "-9": OTHER,  # Not ascertained
    "1": WALK,  # Walk
    "2": BIKE,  # Bicycle
    "3": CAR,  # Car
    "4": CAR,  # SUV
    "5": CAR,  # Van (Minivan)
    "6": CAR,  # Pickup Truck
    "7": CAR,  # Golf cart/Segway
    "8": CAR,  # Motorcycle/Moped
    "9": CAR,  # RV (motorhome, ATV, Snowmobile)
    "10": PT,  # School bus
    "11": PT,  # Public or Commuter Bus
    "12": OTHER,  # Paratransit/Dial-a-Ride
    "13": PT,  # Private/Charter/Tour/Shuttle Bus
    "14": PT,  # City-to-City Bus (Greyhound, Megabus)
    "15": PT,  # Amtrak/Commuter Rail
    "16": PT,  # Subway/Elevated/Light Rail/Streetcar
    "17": PT,  # Taxi/Limo (including Uber/Lyft)
    "18": PT,  # Rental Car (Inc. Zipcar and Car2Go)
    "19": OTHER,  # Airplane
    "20": OTHER,  # Boat/Ferry/Water Taxi
    "97": OTHER,  # Other
}
