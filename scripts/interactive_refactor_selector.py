#!/usr/bin/env python3
"""
Interactive selector for refactor scope.

Input JSON schema (minimum):
{
  "goal": "optional",
  "modules": [
    {
      "id": "frontend.page-content",
      "label": "Home Page Container",
      "path": "app/page-content.tsx",
      "risk": "medium",
      "effort": "L",
      "parts": ["logic", "state", "ui", "tests", "docs"]
    }
  ]
}

Output JSON schema:
{
  "goal": "...",
  "selected": [
    {
      "id": "...",
      "label": "...",
      "path": "...",
      "parts": ["...", "..."]
    }
  ],
  "meta": {
    "selected_module_count": 1,
    "selected_part_count": 5,
    "selection_completed_at": "2026-..."
  }
}
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import sys
from typing import Dict, List, Sequence, Set


def read_json(path: str) -> Dict:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, dict):
        raise ValueError("Input JSON must be an object")
    modules = data.get("modules")
    if not isinstance(modules, list) or not modules:
        raise ValueError("Input JSON must contain non-empty 'modules' array")
    for i, mod in enumerate(modules, start=1):
        if not isinstance(mod, dict):
            raise ValueError(f"modules[{i}] must be object")
        if not isinstance(mod.get("id"), str) or not mod["id"].strip():
            raise ValueError(f"modules[{i}].id must be non-empty string")
        if not isinstance(mod.get("label"), str) or not mod["label"].strip():
            raise ValueError(f"modules[{i}].label must be non-empty string")
        parts = mod.get("parts")
        if not isinstance(parts, list) or not parts or not all(
            isinstance(p, str) and p.strip() for p in parts
        ):
            raise ValueError(f"modules[{i}].parts must be non-empty string array")
    return data


def parse_selection(expr: str, max_index: int) -> List[int]:
    text = expr.strip().lower()
    if text in {"all", "*", "a"}:
        return list(range(1, max_index + 1))
    if text in {"none", "n"}:
        return []

    selected: Set[int] = set()
    for token in expr.split(","):
        part = token.strip()
        if not part:
            continue
        if "-" in part:
            s, e = part.split("-", 1)
            start = int(s.strip())
            end = int(e.strip())
            if start > end:
                start, end = end, start
            if start < 1 or end > max_index:
                raise ValueError("Range out of bounds")
            for i in range(start, end + 1):
                selected.add(i)
        else:
            idx = int(part)
            if idx < 1 or idx > max_index:
                raise ValueError("Index out of bounds")
            selected.add(idx)
    return sorted(selected)


def prompt_selection(prompt: str, max_index: int, allow_empty: bool = False) -> List[int]:
    while True:
        raw = input(prompt).strip()
        try:
            chosen = parse_selection(raw, max_index)
            if not chosen and not allow_empty:
                print("At least one selection is required.")
                continue
            return chosen
        except Exception as exc:
            print(f"Invalid selection: {exc}")
            print("Use formats: 1,3,5-7 or all")


def print_modules(modules: Sequence[Dict]) -> None:
    print("\n=== Refactor Candidate Modules ===")
    print("No | ID | Label | Risk | Effort | Path")
    print("---|----|-------|------|--------|-----")
    for i, mod in enumerate(modules, start=1):
        risk = str(mod.get("risk", "-")).strip() or "-"
        effort = str(mod.get("effort", "-")).strip() or "-"
        path = str(mod.get("path", "-")).strip() or "-"
        print(f"{i:>2} | {mod['id']} | {mod['label']} | {risk} | {effort} | {path}")


def print_parts(module: Dict) -> None:
    print(f"\n=== Parts for {module['id']} ({module['label']}) ===")
    for i, part in enumerate(module["parts"], start=1):
        print(f"{i:>2}. {part}")


def build_selection(data: Dict) -> Dict:
    modules: List[Dict] = data["modules"]
    print_modules(modules)
    mod_indices = prompt_selection(
        "\nSelect modules (e.g. 1,3-5 or all): ", len(modules), allow_empty=False
    )

    selected_modules: List[Dict] = []
    total_parts = 0

    for mi in mod_indices:
        mod = modules[mi - 1]
        print_parts(mod)
        part_indices = prompt_selection(
            "Select parts for this module (e.g. 1,2 or all): ",
            len(mod["parts"]),
            allow_empty=False,
        )
        parts = [mod["parts"][pi - 1] for pi in part_indices]
        total_parts += len(parts)
        selected_modules.append(
            {
                "id": mod["id"],
                "label": mod["label"],
                "path": mod.get("path"),
                "parts": parts,
            }
        )

    print("\n=== Selection Summary ===")
    for item in selected_modules:
        print(f"- {item['id']} ({item['label']}): {', '.join(item['parts'])}")
    print(f"Modules selected: {len(selected_modules)}")
    print(f"Parts selected: {total_parts}")

    confirm = input("\nType YES to confirm and lock selection: ").strip()
    if confirm != "YES":
        raise RuntimeError("Selection not confirmed. Aborted.")

    now = dt.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"
    return {
        "goal": data.get("goal"),
        "selected": selected_modules,
        "meta": {
            "selected_module_count": len(selected_modules),
            "selected_part_count": total_parts,
            "selection_completed_at": now,
        },
    }


def write_output(path: str, payload: Dict) -> None:
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    print(f"\nSelection saved to: {path}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Interactive refactor scope selector")
    parser.add_argument("--input", required=True, help="Input candidates JSON path")
    parser.add_argument("--output", required=True, help="Output selection JSON path")
    args = parser.parse_args()

    if not sys.stdin.isatty():
        print("Interactive mode requires a TTY.", file=sys.stderr)
        return 2

    try:
        data = read_json(args.input)
        payload = build_selection(data)
        write_output(args.output, payload)
        return 0
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
