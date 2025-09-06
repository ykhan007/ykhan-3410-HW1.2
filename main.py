# Python 3 only
# Homework 1.2
# Combines: Nominatim API (requests) to get lat/lon + Haversine distance + Selection Sort
# No user input; prints places in ascending order of distance from origin.

import time
import math
import requests
from typing import Tuple, List

# -----------------------------
# Config
# -----------------------------
USER_AGENT = "HW1.2-StudentScript/1.0 (yk@live.nmhu.edu)"  # put your email if your instructor asks
NOMINATIM_URL = "https://nominatim.openstreetmap.org/search"
ORIGIN_NAME = "New Mexico Museum of Natural History & Science, Albuquerque, NM"

# Choose any 5 destinations in/near Albuquerque (you can change these if you like)
DESTINATION_NAMES = [
    "Old Town Plaza, Albuquerque, NM",
    "University of New Mexico, Albuquerque, NM",
    "ABQ BioPark Zoo, Albuquerque, NM",
    "Sandia Peak Tramway, Albuquerque, NM",
    "Albuquerque International Sunport, Albuquerque, NM",
]

# -----------------------------
# Helpers
# -----------------------------
def get_lat_lon(place: str) -> Tuple[float, float]:
    """
    Look up a place name with Nominatim and return (lat, lon) as floats.
    Uses a short sleep to be polite to the API.
    """
    params = {
        "q": place,
        "format": "json",
        "limit": 1,
    }
    headers = {"User-Agent": USER_AGENT}
    r = requests.get(NOMINATIM_URL, params=params, headers=headers, timeout=15)
    r.raise_for_status()
    data = r.json()
    if not data:
        raise ValueError(f"No results for: {place}")
    lat = float(data[0]["lat"])
    lon = float(data[0]["lon"])
    time.sleep(1.0)  # be nice to the public API
    return lat, lon


def haversine_miles(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """
    Great-circle distance between two points on Earth (miles).
    """
    # convert degrees to radians
    rlat1, rlon1 = math.radians(lat1), math.radians(lon1)
    rlat2, rlon2 = math.radians(lat2), math.radians(lon2)

    dlat = rlat2 - rlat1
    dlon = rlon2 - rlon1

    a = (math.sin(dlat / 2) ** 2) + math.cos(rlat1) * math.cos(rlat2) * (math.sin(dlon / 2) ** 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1.0 - a))
    # Earth radius ~ 3958.8 miles (you may see 3961 in some sources)
    return 3958.8 * c


def selection_sort_pairs(pairs: List[Tuple[float, str]]) -> None:
    """
    In-place selection sort of a list of (distance, name) tuples by distance (index 0).
    """
    n = len(pairs)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if pairs[j][0] < pairs[min_idx][0]:
                min_idx = j
        if min_idx != i:
            pairs[i], pairs[min_idx] = pairs[min_idx], pairs[i]


def build_distance_list(origin_name: str, destination_names: List[str]) -> List[Tuple[float, str]]:
    """
    For each destination, compute (distance_miles, name) from origin.
    """
    o_lat, o_lon = get_lat_lon(origin_name)
    out: List[Tuple[float, str]] = []
    for name in destination_names:
        d_lat, d_lon = get_lat_lon(name)
        dist_mi = haversine_miles(o_lat, o_lon, d_lat, d_lon)
        out.append((dist_mi, name))
    return out


def main():
    # 1) Build list of (distance, place-name) from ORIGIN to five destinations
    distances = build_distance_list(ORIGIN_NAME, DESTINATION_NAMES)

    # 2) Sort the list using SELECTION SORT (shortest first)
    selection_sort_pairs(distances)

    # 3) Print the names in ascending order (closest first)
    print(f"Origin: {ORIGIN_NAME}")
    print("Closest locations (ascending by distance):")
    for dist, name in distances:
        print(f"  {name}  —  {dist:.2f} miles")


if __name__ == "__main__":
    main()
