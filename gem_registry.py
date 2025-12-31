"""
gem_registry.py — Unified Gem Registry Loader (Polyrifringence Engine v8.10+)

Now includes:
 • X-axis function (symbolic role)
 • Y-axis recursive stability (score + tier)
 • Z-axis domain (physical / symbolic / observer)
 • Dual naming (biblical + modern) and aliases
 • Source provenance, tags, notes
 • Optional stability computation (env-gated)

Auto-stability is only applied when:
    POLYRIFRINGENCE_AUTO_STABILITY=1
and you explicitly call maybe_auto_compute_stability(...)
with PVS/REGF/damping data from your benchmark pipeline.

Canonical Codex foundation materials and physical calibration references
are defined in docs/gem_registry.json and loaded by this module.
"""

import json
import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, Optional, List, Any, Tuple


# -------------------------------------------------------------------------
# Dataclass with extended fields
# -------------------------------------------------------------------------
@dataclass
class Gem:
    # Core physical / structural fields
    name: str
    A: float
    B: float
    delta_n: float
    anisotropic: bool
    cls: str
    foundation: Optional[int]
    symbol: str
    color: str
    label: str

    # Naming & semantics
    biblical_name: Optional[str] = None
    modern_name: Optional[str] = None
    aliases: List[str] = field(default_factory=list)
    notes: Optional[str] = None
    tags: List[str] = field(default_factory=list)
    source: Dict[str, Any] = field(default_factory=dict)

    # Optical detail
    birefringence_type: Optional[str] = None
    n_486: Optional[float] = None
    n_589: Optional[float] = None
    n_656: Optional[float] = None

    # Periodic table axes
    x_function: str = "Mediator"   # Origin / Transformer / Mediator / Observer
    z_layer: str = "Symbolic"      # Physical / Symbolic / Observer
    y_stability_score: Optional[float] = None
    y_stability_tier: Optional[str] = None
    stability_history: List[Dict[str, Any]] = field(default_factory=list)


# -------------------------------------------------------------------------
# Load / write registry JSON
# -------------------------------------------------------------------------
REG_PATH = (Path(__file__).resolve().parent / "gem_registry.json").resolve()

if not REG_PATH.exists():
    raise RuntimeError(
        f"Canonical gem registry not found at {REG_PATH}. "
        "This repository requires gem_registry.json at the project root."
    )

# Meta is stored as top-level keys starting with "_"
REGISTRY_META: Dict[str, Any] = {}


def _backfill_defaults(name: str, data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Ensure all new fields exist so Gem(...) doesn't break when older JSONs are loaded.
    Safe to use even when file is already v2.0.0.
    """
    data.setdefault("biblical_name", None)
    data.setdefault("modern_name", None)
    data.setdefault("aliases", [])
    data.setdefault("notes", None)
    data.setdefault("tags", [])
    data.setdefault("source", {})

    data.setdefault("birefringence_type", None)
    data.setdefault("n_486", None)
    data.setdefault("n_589", data.get("A", None))
    data.setdefault("n_656", None)

    data.setdefault("x_function", "Mediator")
    data.setdefault("z_layer", "Symbolic")
    data.setdefault("y_stability_score", None)
    data.setdefault("y_stability_tier", None)
    data.setdefault("stability_history", [])

    return data


def load_registry() -> Dict[str, Gem]:
    """
    Load the unified gem registry into Gem objects (with backward compatibility).

    Skips top-level metadata keys beginning with "_".
    """
    global REGISTRY_META

    raw = json.loads(REG_PATH.read_text(encoding="utf-8"))

    gems: Dict[str, Gem] = {}
    meta: Dict[str, Any] = {}

    for name, payload in raw.items():
        if name.startswith("_"):
            meta[name] = payload
            continue

        payload = _backfill_defaults(name, payload)
        gems[name] = Gem(name=name, **payload)

    REGISTRY_META = meta
    return gems


def _canonical_order(items: Dict[str, Gem]) -> List[Tuple[str, Gem]]:
    """
    Deterministic ordering:
      1) foundation stones sorted by foundation index
      2) non-foundation physical/meta stones sorted by name
    """
    def key(pair: Tuple[str, Gem]) -> Tuple[int, int, str]:
        name, g = pair
        if g.foundation is not None:
            group = 0
            f_val = g.foundation
        else:
            group = 1
            f_val = 999
        return (group, f_val, name)

    return sorted(items.items(), key=key)


def write_registry(gems: Dict[str, Gem]):
    """
    Persist updated gem objects back to JSON, preserving meta keys.
    """
    out: Dict[str, Any] = {}

    # Preserve metadata
    for mk, mv in REGISTRY_META.items():
        out[mk] = mv

    for name, g in _canonical_order(gems):
        out[name] = {
            "A": g.A,
            "B": g.B,
            "delta_n": g.delta_n,
            "anisotropic": g.anisotropic,
            "class": g.cls,
            "foundation": g.foundation,
            "symbol": g.symbol,
            "color": g.color,
            "label": g.label,

            "biblical_name": g.biblical_name,
            "modern_name": g.modern_name,
            "aliases": g.aliases,
            "notes": g.notes,
            "tags": g.tags,
            "source": g.source,

            "birefringence_type": g.birefringence_type,
            "n_486": g.n_486,
            "n_589": g.n_589,
            "n_656": g.n_656,

            "x_function": g.x_function,
            "z_layer": g.z_layer,
            "y_stability_score": g.y_stability_score,
            "y_stability_tier": g.y_stability_tier,
            "stability_history": g.stability_history,
        }

    REG_PATH.write_text(json.dumps(out, indent=2), encoding="utf-8")


# -------------------------------------------------------------------------
# Global registry (loaded once)
# -------------------------------------------------------------------------
GEMS: Dict[str, Gem] = load_registry()


# -------------------------------------------------------------------------
# Helpers / subsets / search
# -------------------------------------------------------------------------
def codex_gems() -> Dict[str, Gem]:
    """Return only the 12 + 1 Codex foundation gems."""
    return {k: g for k, g in GEMS.items() if g.foundation is not None}


def physical_gems() -> Dict[str, Gem]:
    """Return only non-foundation physical / RSANCS reference materials."""
    return {k: g for k, g in GEMS.items() if g.foundation is None}


def get_color(name: str) -> str:
    """Convenience access to hex color for a gem."""
    return GEMS[name].color if name in GEMS else "#999999"


def describe(name: str) -> str:
    """Human-readable gem description with dual naming + function."""
    if name not in GEMS:
        return f"[unknown gem: {name}]"
    g = GEMS[name]
    kind = "Codex" if g.foundation is not None else "Physical"
    bib = g.biblical_name or g.label
    mod = g.modern_name or "—"
    fnc = g.x_function
    return (f"{bib} / {mod} — n₀≈{g.A:.3f}, Δn={g.delta_n:.3f}, "
            f"{'Aniso' if g.anisotropic else 'Iso'} ({kind}, {fnc})")


def search_gems(query: str) -> List[Gem]:
    """
    Simple substring search across name, label, biblical/modern names, aliases and tags.
    """
    q = query.lower()
    results: List[Gem] = []

    for g in GEMS.values():
        haystack = " ".join([
            g.name,
            g.label or "",
            g.biblical_name or "",
            g.modern_name or "",
            " ".join(g.aliases),
            " ".join(g.tags),
        ]).lower()
        if q in haystack:
            results.append(g)

    return results


# -------------------------------------------------------------------------
# Validation
# -------------------------------------------------------------------------
_ALLOWED_X = {"Origin", "Transformer", "Mediator", "Observer"}
_ALLOWED_Z = {"Physical", "Symbolic", "Observer"}
_ALLOWED_TIERS = {None, "Tier-S", "Tier-A", "Tier-B", "Tier-C"}


def validate_registry(gems: Optional[Dict[str, Gem]] = None) -> List[str]:
    """
    Validate the registry for basic consistency.
    Returns a list of error strings (empty if OK).
    """
    if gems is None:
        gems = GEMS

    errors: List[str] = []

    for name, g in gems.items():
        if g.x_function not in _ALLOWED_X:
            errors.append(f"{name}: invalid x_function={g.x_function!r}")
        if g.z_layer not in _ALLOWED_Z:
            errors.append(f"{name}: invalid z_layer={g.z_layer!r}")
        if g.y_stability_tier not in _ALLOWED_TIERS:
            errors.append(f"{name}: invalid y_stability_tier={g.y_stability_tier!r}")
        if g.anisotropic and g.birefringence_type is None:
            # Not fatal, but worth flagging
            errors.append(f"{name}: anisotropic=True but birefringence_type missing")

    return errors


# -------------------------------------------------------------------------
# Stability computation (env-gated helper)
# -------------------------------------------------------------------------
def compute_stability(
    pvs_data: Dict[str, float],
    regf_data: Dict[str, float],
    damped_fraction: Dict[str, float],
) -> None:
    """
    Compute and update stability score + tier using the canonical formula.

    pvs_data:        gem -> mean_PVS (in mrad or consistent units; lower is better)
    regf_data:       gem -> REGF contribution 0..1
    damped_fraction: gem -> damping success fraction 0..1

    Writes updated scores back into the JSON registry (in-place).
    """

    # Protect against empty input
    if not pvs_data:
        return

    # Normalizer for 1/PVS inversion
    inv_values = [(1.0 / (v + 1e-12)) for v in pvs_data.values() if v > 0]
    if not inv_values:
        return

    max_inv = max(inv_values)
    min_inv = min(inv_values)

    for name, g in GEMS.items():
        if name not in pvs_data:
            continue

        # Invert PVS and normalize to 0..1
        inv_pvs = 1.0 / (pvs_data[name] + 1e-12)
        norm_inv = (inv_pvs - min_inv) / (max_inv - min_inv + 1e-12)

        regf = float(regf_data.get(name, 0.0))
        damp = float(damped_fraction.get(name, 0.0))

        # Weighted composite score
        score = 0.6 * norm_inv + 0.25 * regf + 0.15 * damp
        score = max(0.0, min(score, 1.0))

        # Map to discrete tier
        if score > 0.85:
            tier = "Tier-S"
        elif score > 0.60:
            tier = "Tier-A"
        elif score > 0.35:
            tier = "Tier-B"
        else:
            tier = "Tier-C"

        # Append to history and set current values
        g.y_stability_score = float(score)
        g.y_stability_tier = tier
        g.stability_history.append({
            "score": float(score),
            "tier": tier,
            "env": "manual",
        })

    write_registry(GEMS)


def maybe_auto_compute_stability(
    pvs_data: Dict[str, float],
    regf_data: Dict[str, float],
    damped_fraction: Dict[str, float],
) -> None:
    """
    Env-gated wrapper around compute_stability.

    If POLYRIFRINGENCE_AUTO_STABILITY=1, stability is computed and written.
    Otherwise this is a no-op.

    Intended usage in benchmark / analysis scripts:

        from gem_registry import maybe_auto_compute_stability

        pvs_by_gem = {...}
        regf_by_gem = {...}
        damp_by_gem = {...}

        maybe_auto_compute_stability(pvs_by_gem, regf_by_gem, damp_by_gem)
    """
    flag = os.getenv("POLYRIFRINGENCE_AUTO_STABILITY", "0")
    if flag.strip() == "1":
        compute_stability(pvs_data, regf_data, damped_fraction)


# -------------------------------------------------------------------------
# Diagnostic entrypoint
# -------------------------------------------------------------------------
if __name__ == "__main__":
    print("🔍 Gem Registry — Summary\n")

    errs = validate_registry()
    if errs:
        print("Validation issues:")
        for e in errs:
            print("  -", e)
        print()
    else:
        print("Registry validation: OK\n")

    codex = codex_gems()
    phys = physical_gems()

    print(f"{len(codex)} Codex foundations, {len(phys)} physical references.\n")

    for i, (name, g) in enumerate(_canonical_order(GEMS), 1):
        f = f"{g.foundation:>2}" if g.foundation is not None else "— "
        print(f"{i:>2}. {f} | {name:<12} | n₀={g.A:.4f} Δn={g.delta_n:.3f} | "
              f"{g.cls:<11} | {g.color} | {g.biblical_name or g.label} / {g.modern_name or '—'} "
              f"| {g.x_function}/{g.z_layer} | {g.y_stability_tier or 'Tier-?'}")
