import csv, os, sys

def die(msg):
    print("\n❌ HEALTHCHECK FAILED:\n" + msg)
    sys.exit(1)

def read_csv(path):
    with open(path, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))

# Paths (edit dates only if you changed filenames)
EV_INDEX = "04_Evidence/EV-INDEX_Evidence_Index_v0.1_2026-02-07.csv"
SOA      = "02_Registers/ISMS-005_SoA_v0.1_2026-02-07.csv"
CAPA     = "03_Audit_Pack/AUD-006_CAPA_Tracker_v0.1_2026-02-07.csv"

for p in [EV_INDEX, SOA, CAPA]:
    if not os.path.exists(p):
        die(f"Missing required file: {p}")

# 1) EV-INDEX: unique IDs + linked file exists
ev_rows = read_csv(EV_INDEX)
ev_ids = []
missing_ev_files = []
for r in ev_rows:
    evid = (r.get("Evidence ID") or "").strip()
    fname = (r.get("Linked File Name") or "").strip()
    if evid:
        ev_ids.append(evid)
    if fname:
        fpath = os.path.join("04_Evidence", fname)
        if not os.path.exists(fpath):
            missing_ev_files.append(f"{evid} -> {fname}")

dupes = sorted(set([x for x in ev_ids if ev_ids.count(x) > 1]))
if dupes:
    die("Duplicate Evidence IDs in EV-INDEX:\n- " + "\n- ".join(dupes))

if missing_ev_files:
    die("EV-INDEX references evidence files that do NOT exist:\n- " + "\n- ".join(missing_ev_files))

ev_set = set(ev_ids)

# 2) SoA: Implemented rows must have evidence and those EV IDs must exist
soa_rows = read_csv(SOA)
soa_issues = []
for r in soa_rows:
    ctrl = (r.get("Control ID") or "").strip()
    status = (r.get("Status") or "").strip().lower()
    ev = (r.get("Evidence IDs (EV-###)") or "").strip()

    if status == "implemented":
        if not ev:
            soa_issues.append(f"{ctrl}: Implemented but Evidence IDs empty")
        else:
            parts = [x.strip() for x in ev.split(";")]
            for p in parts:
                if p and p not in ev_set:
                    soa_issues.append(f"{ctrl}: Evidence {p} not found in EV-INDEX")

if soa_issues:
    die("SoA issues (Implemented controls must map to valid evidence):\n- " + "\n- ".join(soa_issues))

# 3) CAPA: all must be Closed
capa_rows = read_csv(CAPA)
open_caps = []
for r in capa_rows:
    cid = (r.get("CAPA ID") or "").strip()
    status = (r.get("Status") or "").strip().lower()
    if status and status != "closed":
        open_caps.append(f"{cid}: {r.get('Status')}")

if open_caps:
    die("CAPA items not Closed:\n- " + "\n- ".join(open_caps))

# 4) Git tracked junk check (DS_Store should not be tracked)
tracked_ds = []
try:
    import subprocess
    out = subprocess.check_output(["git", "ls-files"], text=True)
    for line in out.splitlines():
        if ".DS_Store" in line:
            tracked_ds.append(line)
except Exception:
    pass

if tracked_ds:
    die("Tracked .DS_Store found (should not be tracked):\n- " + "\n- ".join(tracked_ds))

print("\n✅ HEALTHCHECK PASSED")
print("- EV-INDEX OK (no missing evidence files, no duplicate EV IDs)")
print("- SoA OK (Implemented controls have valid evidence)")
print("- CAPA OK (all Closed)")
print("- Repo OK (no tracked .DS_Store)")
