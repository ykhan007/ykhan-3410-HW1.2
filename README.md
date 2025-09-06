# YourInitials-3410-HW1.2

## Homework 1.2 – Selection Sort + Distance Challenge

### Programming Challenge
1. Combined **distance calculation code** with a **Selection Sort implementation** in one project.  
2. Used the **Natural History Museum (Albuquerque, NM)** as the origin, and programmatically found distances to **five chosen locations** in Albuquerque.  
3. Stored locations in a list and sorted them using **Selection Sort**, so the closest location comes first.  
4. Printed the places in **ascending order by distance**.  
5. **No user input** is required — all locations are hardcoded in the Python file.  

### How It Works
- Uses the **Nominatim API (OpenStreetMap)** to look up latitude/longitude of locations.  
- Calculates straight-line distances in miles using the **Haversine formula**.  
- Sorts the list of `(distance, location)` pairs using **Selection Sort**.  
- Prints the sorted list, starting with the closest location to the museum. 
