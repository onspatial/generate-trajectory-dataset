import json
def get_bounding_box(map_name):
    if map_name=='atl-metro':
        return [-84.5505285, 33.64708314, -84.28945431, 33.88663263]

    elif map_name=='atl' or map_name=='atlanta':
        return [-84.41213984, 33.72878582, -84.36418537, 33.76304255]

    elif map_name=='bjng':
        return [116.1632651, 39.7831364, 116.6294095, 40.039197 ]

    elif map_name=='brln':
        return [13.3656432, 52.5066516, 13.4174008, 52.5323714]

    elif map_name=='gmu':
        return [-77.31851683, 38.82516657, -77.29851636, 38.83568792]

    elif map_name=='nola':
        return [-90.0747321, 29.94990921, -90.04599532, 29.96606048]

    elif map_name=='sfco':
        return [-122.51419799, 37.70829506, -122.35784432, 37.8108725 ]

    else :
        return [-84.41213984, 33.72878582, -84.36418537, 33.76304255]
