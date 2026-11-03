#!/usr/bin/env python3
"""
Optimized V2X Dataset Synthesizer (IEEE Data Port Format Compliant)
Generates high-fidelity synthetic V2X message payload sequences for multi-label classification.
"""

import os
import random
import json
import argparse
import pandas as pd
import numpy as np

MESSAGE_TYPES = ['BSM', 'CAM', 'DENM', 'SPAT', 'MAP', 'RSA']
ANOMALY_LABELS = ['NORMAL', 'SYBIL_ATTACK', 'TAMPERED_LOCATION', 'REPLAY_ATTACK', 'FALSE_INFO']

VEHICLE_IDS = [f"VEH_{i:04d}" for i in range(1, 300)]
RSU_IDS = [f"RSU_{i:03d}" for i in range(1, 80)]

V2X_VOCAB_TEMPLATES = {
    'BSM': [
        "MSG_TYPE:BSM VEH_ID:{veh} LAT:{lat:.6f} LON:{lon:.6f} ELEV:{elev:.2f} SPEED:{speed:.2f} HEADING:{heading:.1f} STEER_ANGLE:{steer:.1f} LAT_ACCEL:{accel:.2f} BRAKE_STATUS:{brake} SEC_MARK:{sec} SIG:{sig} VERIFIED:{ver}",
        "V2X_HEADER_BSM ID:{veh} POS:[{lat:.6f},{lon:.6f}] ALT:{elev:.1f} VEL:{speed:.2f} CRSE:{heading:.1f} BRAKE_SYS:{brake} TSTAMP:{sec} VERIFY_KEY:{sig} STATUS:{ver}",
        "BSM_PDU SENDER:{veh} GPS_LAT:{lat:.6f} GPS_LON:{lon:.6f} SPEED_KPH:{speed:.1f} ANGLE:{heading:.1f} TRANSMISSION:{brake} SECONDS:{sec} MAC:{sig} AUTH_CHECK:{ver}"
    ],
    'CAM': [
        "MSG_TYPE:CAM STATION_ID:{veh} LAT:{lat:.6f} LON:{lon:.6f} SPEED:{speed:.2f} HEADING:{heading:.1f} LIGHT_STATUS:{brake} CURVATURE:{accel:.2f} TIME:{sec} CERT:{sig} INTEGRITY:{ver}",
        "ITS_G5_CAM NODE:{veh} POS_LAT:{lat:.6f} POS_LON:{lon:.6f} KPH:{speed:.1f} HEADING_DEG:{heading:.1f} DRIVE_DIR:FORWARD STAMP:{sec} AUTH:{sig} STATE:{ver}"
    ],
    'DENM': [
        "MSG_TYPE:DENM STATION_ID:{rsu} EVENT:ROAD_HAZARD CAUSE:{cause} SEVERITY:HIGH LAT:{lat:.6f} LON:{lon:.6f} TIME:{sec} VALIDITY:300s MAC:{sig} DISCREPANCY:{discrepancy}",
        "ITS_DENM ORIGIN:{rsu} EVENT_TYPE:{cause} ALERT_ZONE:[{lat:.6f},{lon:.6f}] DURATION:180s TIMESTAMP:{sec} DIG_SIG:{sig} HAZARD_VERIFIED:{ver}"
    ],
    'SPAT': [
        "MSG_TYPE:SPAT RSU_ID:{rsu} INTERSECTION_ID:INT_9410 PHASE:{phase} MIN_END:{min_end} MAX_END:{max_end} PEDESTRIAN_CALL:FALSE SEC:{sec} AUTH:{sig} SYNC:{ver}",
        "V2I_SPAT INFRA:{rsu} SIGNAL_GROUP:{phase} STATE:PROTECTED_MOVEMENT REMAINING:{min_end}s TIMESTAMP:{sec} CHECKSUM:{sig} INTERSECTION_SYNC:{ver}"
    ],
    'MAP': [
        "MSG_TYPE:MAP RSU_ID:{rsu} INTERSECTION_ID:INT_9410 LANES_COUNT:4 NODE_LIST:[{lat:.6f},{lon:.6f}] SPEED_LIMIT:50KPH MAC:{sig} TOPO_HASH:{ver}",
        "V2I_MAP NODE:{rsu} GEOMETRY_VERSION:3 LANES:L1_L2_L3_L4 LAT_REF:{lat:.6f} LON_REF:{lon:.6f} HASH:{sig} MAP_VALID:{ver}"
    ],
    'RSA': [
        "MSG_TYPE:RSA SENDER:{rsu} ALERT_CODE:{rsa_code} ADVISORY_SPEED:{speed:.1f} LAT:{lat:.6f} LON:{lon:.6f} TIMESTAMP:{sec} SIG:{sig} ADVISORY_STATUS:{ver}",
        "ITS_RSA RS_ID:{rsu} WARNING:{rsa_code} RECOMMENDED_KPH:{speed:.1f} LOCATION:[{lat:.6f},{lon:.6f}] MAC:{sig} SIGN_VALID:{ver}"
    ]
}

HAZARD_CAUSES = ["SLIPPERY_ROAD", "ACCIDENT_AHEAD", "ROADWORK", "EMERGENCY_VEHICLE", "ANIMAL_ON_ROAD"]
SPAT_PHASES = ["RED_HOLD", "GREEN_PROCEED", "YELLOW_WARN", "PROTECTED_LEFT"]
RSA_CODES = ["WORK_ZONE", "ICE_WARNING", "HEAVY_FOG", "CONSTRUCTION_AHEAD"]

def generate_v2x_sample(sample_id):
    msg_type = random.choice(MESSAGE_TYPES)
    
    # 65% normal, 35% anomalous
    is_anomaly = random.random() < 0.35
    
    anomalies = []
    if is_anomaly:
        num_anomalies = random.choice([1, 1, 2])
        chosen = random.sample(['SYBIL_ATTACK', 'TAMPERED_LOCATION', 'REPLAY_ATTACK', 'FALSE_INFO'], num_anomalies)
        anomalies.extend(chosen)
    else:
        anomalies.append('NORMAL')
        
    veh = random.choice(VEHICLE_IDS)
    rsu = random.choice(RSU_IDS)
    lat = 37.7749 + random.uniform(-0.03, 0.03)
    lon = -122.4194 + random.uniform(-0.03, 0.03)
    speed = random.uniform(5.0, 110.0)
    heading = random.uniform(0.0, 359.9)
    elev = random.uniform(10.0, 50.0)
    steer = random.uniform(-15.0, 15.0)
    accel = random.uniform(-3.0, 3.0)
    brake = random.choice(["OFF", "ACTIVE", "ABS_ENGAGED"])
    sec = random.randint(400000, 999999)
    sig = f"0x{random.randint(0x10000000, 0xFFFFFFFF):08X}"
    ver = "TRUE"
    discrepancy = "NONE"

    cause = random.choice(HAZARD_CAUSES)
    phase = random.choice(SPAT_PHASES)
    min_end = random.randint(5, 45)
    max_end = min_end + random.randint(5, 20)
    rsa_code = random.choice(RSA_CODES)

    # Inject distinctive feature markers for deep neural net learning
    if 'TAMPERED_LOCATION' in anomalies:
        lat += random.choice([-8.5, 8.5, 12.0]) # Massive GPS delta anomaly
        lon += random.choice([-8.5, 8.5, 12.0])
        ver = "GPS_OFFSET_TAMPER_DETECTED"

    if 'REPLAY_ATTACK' in anomalies:
        sec = 100001 # Stale / expired timestamp
        sig = "0x00000000_EXPIRED_REPLAY_HASH"
        ver = "EXPIRED_STAMP_REPLAY"

    if 'SYBIL_ATTACK' in anomalies:
        veh = f"SYBIL_GHOST_{random.randint(10, 99):02d}"
        ver = "UNREGISTERED_GHOST_NODE"

    if 'FALSE_INFO' in anomalies:
        discrepancy = "UNVERIFIED_SPOOFED_HAZARD_ALERT_DISCREPANCY"
        ver = "FALSE_PAYLOAD_CLAIM"

    template = random.choice(V2X_VOCAB_TEMPLATES[msg_type])
    payload_text = template.format(
        veh=veh, rsu=rsu, lat=lat, lon=lon, elev=elev, speed=speed,
        heading=heading, steer=steer, accel=accel, brake=brake,
        sec=sec, sig=sig, cause=cause, phase=phase, min_end=min_end,
        max_end=max_end, rsa_code=rsa_code, ver=ver, discrepancy=discrepancy
    )

    labels = [msg_type] + anomalies
    multi_label_str = " ".join(list(set(labels)))

    return {
        "sample_id": f"V2X_{sample_id:06d}",
        "raw_text": payload_text,
        "primary_type": msg_type,
        "anomalies": ",".join(anomalies),
        "multi_labels": multi_label_str
    }

def main():
    parser = argparse.ArgumentParser(description="Generate synthetic V2X dataset.")
    parser.add_argument("--samples", type=int, default=6000, help="Number of V2X samples to generate")
    parser.add_argument("--output", type=str, default="data/v2x_dataset.csv", help="Output CSV path")
    args = parser.parse_args()

    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    print(f"Generating {args.samples} high-fidelity synthetic V2X messages...")

    samples = [generate_v2x_sample(i) for i in range(1, args.samples + 1)]
    df = pd.DataFrame(samples)
    df.to_csv(args.output, index=False)

    print(f"Optimized dataset saved to {args.output}")
    print(f"Sample distribution:\n{df['primary_type'].value_counts()}")
    print("\nAnomaly counts:")
    all_anomalies = [a for sub in df['anomalies'].str.split(',') for a in sub]
    print(pd.Series(all_anomalies).value_counts())

if __name__ == "__main__":
    main()
