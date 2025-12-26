# Layers of generated mapfiles will be separated into groups:
#
# - `BEACH` - Beach and land related objects.
# - `DEPTHS` - Depths, currents, etc.
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
    "BRIDGE": "BEACH", # Bridge
    "BUAARE": "BEACH", # Built-up area
    "BUISGL": "BEACH", # Building, single
    "CGUSTA": "BEACH", # Coast guard station
    "COALNE": "BEACH", # Coastline
    "CONVYR": "BEACH", # Conveyor
    "FORSTC": "BEACH", # Fortified structure
    "FSHFAC": "BEACH", # Fishing facility
    "LNDARE": "BEACH", # Land area
    "LNDELV": "BEACH", # Land elevation
    "LNDMRK": "BEACH", # Landmark
    "LNDRGN": "BEACH", # Land region
    "MORFAC": "BEACH", # Mooring/Warping facility
    "PONTON": "BEACH", # Pontoon
    "RIVERS": "BEACH", # River
    "ROADWY": "BEACH", # Road
    "SLCONS": "BEACH", # Shoreline construction
    # DEPTHS
    "DEPARE": "DEPTHS", # Depth area
    "DEPCNT": "DEPTHS", # Depth contour
    "SOUNDG": "DEPTHS", # Sounding
    # SEABED
    "CANALS": "SPECIAL", # Canal
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
}


def get_layer_group(feature):
    if feature:
        return _layer_groups.get(feature.upper(), "MISC")

    return "MSC"
