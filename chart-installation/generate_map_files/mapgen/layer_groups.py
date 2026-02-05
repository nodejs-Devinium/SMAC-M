# Layers of generated mapfiles will be separated into groups:
#
# - `BEACH` - Beach and land related objects.
# - `BRIDGES` - Bridges.
# - `DEPTH_AREA` - Depth area (with filled polygons).
# - `DEPTH_DATA` - Depth contour and sounding.
# - `LAND` - Land area (with filled polygons).
# - `SEABED` - Seabed, obstructions, pipelines.
# - `SIGNALS` - Buoys, beacons, lights, fog signals, radar.
# - `SPECIAL` - Special areas.
# - `TEXT` - Text layers (e.g. area names).
# - `TRAFFIC` - Traffic routes, etc.
#
# - `COMMON` - Common layers (should be used with all other layers if presented).
#
# - `BROKEN` - Layers that cause errors because of missing attributes, etc.
#
# - `CLEANUP` - A group of synthetic layers that should be used to clear
#               the remainings from rendered layers with smaller navigational
#               purpose indexes.
#
# - `MISC` - Everything else.
#
# This module contains a dictionary of the LAYER:GROUP mappings and a function
# that returns GROUP by LAYER feature name.
#
# S-57 objects/layers description is taken from here:
# https://pro.arcgis.com/en/pro-app/3.3/help/production/maritime/s-57-object-finder.htm

_layer_groups = {
    # BEACH
    "ACHARE": "BEACH", # Anchorage area
    "BUAARE": "BEACH", # Built-up area
    "BUISGL": "BEACH", # Building, single
    "CGUSTA": "BEACH", # Coast guard station
    "COALNE": "BEACH", # Coastline
    "CONVYR": "BEACH", # Conveyor
    "FORSTC": "BEACH", # Fortified structure
    "FSHFAC": "BEACH", # Fishing facility
    "LNDELV": "BEACH", # Land elevation
    "LNDMRK": "BEACH", # Landmark
    "LNDRGN": "BEACH", # Land region
    "MORFAC": "BEACH", # Mooring/Warping facility
    "RIVERS": "BEACH", # River
    "ROADWY": "BEACH", # Road
    "SLCONS": "BEACH", # Shoreline construction
    # BRIDGES
    "BRIDGE": "BRIDGES", # Bridge
    "PONTON": "BRIDGES", # Pontoon
    # DEPTH_AREA
    "DEPARE": "DEPTH_AREA", # Depth area
    # DEPTH_DATA
    "DEPCNT": "DEPTH_DATA", # Depth contour
    "SOUNDG": "DEPTH_DATA", # Sounding
    # LAND
    "LNDARE": "LAND", # Land area
    # SEABED
    "CBLARE": "SEABED", # Cable area
    "CBLOHD": "SEABED", # Cable, overhead
    "CBLSUB": "SEABED", # Cable, submarine
    "DMPGRD": "SEABED", # Dumping ground
    "OBSTRN": "SEABED", # Obstruction
    "PIPARE": "SEABED", # Pipeline area
    "PIPOHD": "SEABED", # Pipeline, overhead
    "PIPSOL": "SEABED", # Pipeline, submarine/on land
    "UWTROC": "SEABED", # Underwater/awash rock
    "WEDKLP": "SEABED", # Weed/Kelp
    "WRECKS": "SEABED", # Wreck
    # SIGNALS
    "BCNCAR": "SIGNALS", # Beacon, cardinal
    "BCNISD": "SIGNALS", # Beacon, isolated danger
    "BCNLAT": "SIGNALS", # Beacon, lateral
    "BCNSAW": "SIGNALS", # Beacon, safe water
    "BCNSPP": "SIGNALS", # Beacon, special purpose
    "BOYCAR": "SIGNALS", # Buoy, cardinal
    "BOYINB": "SIGNALS", # Buoy installation
    "BOYISD": "SIGNALS", # Buoy isolated danger
    "BOYLAT": "SIGNALS", # Buoy, lateral
    "BOYSAW": "SIGNALS", # Buoy safe water
    "BOYSPP": "SIGNALS", # Buoy special purpose
    "FOGSIG": "SIGNALS", # Fog signal
    "LIGHTS": "SIGNALS", # Light
    "RADRNG": "SIGNALS", # Radar range
    "RADSTA": "SIGNALS", # Radar station
    "RDOCAL": "SIGNALS", # Radio calling-in point
    "RDOSTA": "SIGNALS", # Radio station
    "RTPBCN": "SIGNALS", # Radar transponder beacon
    # SPECIAL
    "CANALS": "SPECIAL", # Canal
    "CHKPNT": "SPECIAL", # Checkpoint
    "CONZNE": "SPECIAL", # Contiguous zone
    "COSARE": "SPECIAL", # Continental shelf area
    "CTNARE": "SPECIAL", # Caution area
    "EXEZNE": "SPECIAL", # Exclusive economic zone
    "FSHZNE": "SPECIAL", # Fishery zone
    "MIPARE": "SPECIAL", # Military practice area
    "PRCARE": "SPECIAL", # Precautionary area
    "RESARE": "SPECIAL", # Restricted area
    "STSLNE": "SPECIAL", # Straight territorial sea baseline
    "TESARE": "SPECIAL", # Territorial sea area
    # TEXT
    "SEAARE": "TEXT", # Sea area/named water area
    # TRAFFIC
    "AIRARE": "TRAFFIC", # Airport/airfield
    "FAIRWY": "TRAFFIC", # Fairway
    "FERYRT": "TRAFFIC", # Ferry route
    "SUBTLN": "TRAFFIC", # Submarine transit lane
    # COMMON
    "M_COVR": "COMMON", # Coverage
    # BROKEN
    "CTRPNT": "BROKEN", # Control point (HEIGHT)
    "SBDARE": "BROKEN", # Seabed area (NATSUR)
    # CLEANUP (a group of synthetic layers)
    "CLNDEP": "CLEANUP", # Cleanup layer based on DEPARE polygon data
    "CLNLND": "CLEANUP", # Cleanup layer based on LNDARE polygon data
}


def get_layer_group(feature):
    if feature:
        return _layer_groups.get(feature.upper(), "MISC")

    return "MISC"

def get_layer_groups():
    all_values = _layer_groups.values()
    unique_values = set(all_values)
    unique_values.add('MISC')
    return list(unique_values)
