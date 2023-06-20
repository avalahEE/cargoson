#!/usr/bin/env bash
set -e

REPO_ROOT=$(cd "$(dirname "$0")/.."; pwd)
ENV_PATH="${REPO_ROOT}/venv"
PYTHON_BIN="${ENV_PATH}/bin/python3"
PIP_BIN="${ENV_PATH}/bin/pip3"

if [ ! -d "${ENV_PATH}" ]; then
    echo "[+] First time setup, installing dependencies"
    python3 -m venv "$ENV_PATH"
    $PIP_BIN install 'git+https://git.sr.ht/~n0n/jsonschemagen'
    echo
fi

CARGOSON_API_JSON="$REPO_ROOT/schema/cargoson_api.json"
CARGOSON_API_JSON_PRETTY="$REPO_ROOT/schema/cargoson_api.tmp"

echo "# [+] Fetching Cargoson OpenAPI definitions"
curl --progress-bar -o "$CARGOSON_API_JSON" https://app.swaggerhub.com/apiproxy/registry/cargoson/cargoson-api/v1

if command -v jq &> /dev/null
then
    echo "# [+] Prettifying using jq"
    jq -M < "$CARGOSON_API_JSON" > "$CARGOSON_API_JSON_PRETTY"
    mv "$CARGOSON_API_JSON_PRETTY" "$CARGOSON_API_JSON"
else
    echo "# [+] Prettifying using python"
    "$PYTHON_BIN" -m json.tool --indent 2 --no-ensure-ascii "$CARGOSON_API_JSON" > "$CARGOSON_API_JSON_PRETTY"
    mv "$CARGOSON_API_JSON_PRETTY" "$CARGOSON_API_JSON"
fi

"$PYTHON_BIN" "$REPO_ROOT/tools/generate-schema.py" "$CARGOSON_API_JSON"
