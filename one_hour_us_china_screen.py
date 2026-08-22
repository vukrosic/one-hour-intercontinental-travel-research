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
    # Provisional SFO/PEK coordinates; replace/verify with a cited public dataset.
    base_km = great_circle_km(37.6213, -122.3790, 40.0799, 116.6031)
    rng = random.Random(SEED)
    rows = []
    for _ in range(N):
        margin = rng.uniform(0.00, 0.25)
        access_min = rng.uniform(5.0, 15.0)
        checkin_security_min = rng.uniform(10.0, 20.0)
        boarding_min = rng.uniform(5.0, 10.0)
        ground_ops_min = rng.uniform(3.0, 8.0)
        climb_descent_min = rng.uniform(8.0, 15.0)
        arrival_egress_min = rng.uniform(5.0, 15.0)
        ld = rng.uniform(4.0, 12.0)          # literature envelope, not a design target
        allocated_mass = rng.uniform(90.0, 180.0)  # kg/passenger incl. allocation
        payload_efficiency = rng.uniform(0.35, 0.75)
        route_km = base_km * (1 + margin)
        non_airborne_min = (access_min + checkin_security_min + boarding_min + ground_ops_min + climb_descent_min + arrival_egress_min)
        airborne_h = (60.0 - non_airborne_min) / 60.0
        speed_kmh = route_km / airborne_h if airborne_h > 0 else None
        # Lower-order transport-work proxy; report as a screen only.
        energy_mj = 9.80665 * route_km * 1000 / (ld * payload_efficiency) * allocated_mass / 1e6
        rows.append((speed_kmh, energy_mj, non_airborne_min, airborne_h * 60.0, margin, ld, allocated_mass))
    speeds = [r[0] for r in rows]
    energies = [r[1] for r in rows]
    print(f"seed={SEED} draws={N} base_distance_km={base_km:.1f}")
    finite_speeds = [x for x in speeds if x is not None]
    print(f"non_airborne_minutes p05/p50/p95={statistics.quantiles([r[2] for r in rows],n=20)[0]:.1f}/{statistics.median([r[2] for r in rows]):.1f}/{statistics.quantiles([r[2] for r in rows],n=20)[-1]:.1f}")
    print(f"positive_airborne_time_fraction={len(finite_speeds)/N:.3f}")
    print(f"airborne_at_least_10_min_fraction={sum(r[3] >= 10.0 for r in rows)/N:.3f}")
    print(f"required_mean_speed_kmh p05/p50/p95={statistics.quantiles(finite_speeds,n=20)[0]:.0f}/{statistics.median(finite_speeds):.0f}/{statistics.quantiles(finite_speeds,n=20)[-1]:.0f}")
    print(f"proxy_energy_mj_per_passenger p05/p50/p95={statistics.quantiles(energies,n=20)[0]:.1f}/{statistics.median(energies):.1f}/{statistics.quantiles(energies,n=20)[-1]:.1f}")
    with open("one_hour_us_china_screen.csv", "w", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["required_mean_speed_kmh", "proxy_energy_MJ_per_passenger", "non_airborne_minutes", "airborne_minutes", "routing_margin", "L_over_D_screen", "allocated_mass_kg"])
        w.writerows(rows)

if __name__ == "__main__":
    run()
