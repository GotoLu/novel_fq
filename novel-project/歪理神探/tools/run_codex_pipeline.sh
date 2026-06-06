#!/usr/bin/env bash
set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

export NOVEL_PIPELINE_LLM_COMMAND="env TERM=xterm-256color codex exec --cd ${PROJECT_ROOT} -s read-only --output-last-message {output_file} -"

python3 "${PROJECT_ROOT}/novel-project/tools/novel_pipeline.py" --run --restart-after-audit "$@"
