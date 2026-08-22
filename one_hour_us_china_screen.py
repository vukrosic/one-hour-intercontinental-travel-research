#!/usr/bin/env python3
"""Low-order, civilian feasibility screen; not a vehicle design tool.

Uses only broad, editable assumptions. It intentionally omits geometry,
propulsion, trajectories, materials, and operational guidance.
"""
import csv, math, random, statistics

N = 1000
SEED = 20260822
R_EARTH_KM = 6371.0

def great_circle_km(lat1, lon1, lat2, lon2):
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dp, dl = math.radians(lat2-lat1), math.radians(lon2-lon1)
    a = math.sin(dp/2)**2 + math.cos(p1)*math.cos(p2)*math.sin(dl/2)**2
    return 2 * R_EARTH_KM * math.asin(math.sqrt(a))

def run():
    # Placeholder city coordinates; replace only with a cited public dataset.
    base_km = great_circle_km(33.9416, -118.4085, 31.1443, 121.8083)
    rng = random.Random(SEED)
    rows = []
    for _ in range(N):
        margin = rng.uniform(0.00, 0.25)
        climb_descent_min = rng.uniform(8.0, 15.0)
        ld = rng.uniform(4.0, 12.0)          # literature envelope, not a design target
        allocated_mass = rng.uniform(90.0, 180.0)  # kg/passenger incl. allocation
        payload_efficiency = rng.uniform(0.35, 0.75)
        route_km = base_km * (1 + margin)
        cruise_h = 1.0 - climb_descent_min / 60.0
        speed_kmh = route_km / cruise_h
        # Lower-order transport-work proxy; report as a screen only.
        energy_mj = 9.80665 * route_km * 1000 / (ld * payload_efficiency) * allocated_mass / 1e6
        rows.append((speed_kmh, energy_mj, margin, climb_descent_min, ld, allocated_mass))
    speeds = [r[0] for r in rows]
    energies = [r[1] for r in rows]
    print(f"seed={SEED} draws={N} base_distance_km={base_km:.1f}")
    print(f"required_mean_speed_kmh p05/p50/p95={statistics.quantiles(speeds,n=20)[0]:.0f}/{statistics.median(speeds):.0f}/{statistics.quantiles(speeds,n=20)[-1]:.0f}")
    print(f"proxy_energy_mj_per_passenger p05/p50/p95={statistics.quantiles(energies,n=20)[0]:.1f}/{statistics.median(energies):.1f}/{statistics.quantiles(energies,n=20)[-1]:.1f}")
    with open("one_hour_us_china_screen.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["required_mean_speed_kmh", "proxy_energy_MJ_per_passenger", "routing_margin", "climb_descent_min", "L_over_D_screen", "allocated_mass_kg"])
        w.writerows(rows)

if __name__ == "__main__":
    run()
