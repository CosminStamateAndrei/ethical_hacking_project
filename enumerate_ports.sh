#!/usr/bin/env bash

set -euo pipefail

# Not going to work yet, DON'T DO IT, maybe subdomains do not allow scanning, maybe filter???
nmap -iL hosts.txt -Pn --open -oA sensitive_data/scans

