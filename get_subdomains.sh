#!/usr/bin/env bash

set -euo pipefail

export PATH="$HOME/.local/bin:$PATH"
HARVESTER_DIR="${HARVESTER_DIR:-$HOME/theHarvester}"

if command -v theHarvester >/dev/null 2>&1; then
    harvester=(theHarvester)
elif command -v uv >/dev/null 2>&1 && [[ -d "$HARVESTER_DIR" ]]; then
    harvester=(uv run --project "$HARVESTER_DIR" theHarvester)
else
    echo "Error: theHarvester not found (looked on PATH and in $HARVESTER_DIR via uv)." >&2
    exit 127
fi

OUT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/sensitive_data"
mkdir -p "$OUT_DIR"

# "${harvester[@]}" -d bunq.com -b crtsh,bing,duckduckgo -f "$OUT_DIR/subdomains.json"
"${harvester[@]}" -d bunq.com -b crtsh,duckduckgo -f "$OUT_DIR/subdomains.json"

