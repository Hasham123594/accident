# Accident Data Pipeline

## Run (one command)

```bash


git clone https://github.com/Hasham123594/accident.git
cd accident
nix-shell --run "uv pip install -e '.[test]' && uv run --with pytest pytest"

nix-shell --run "uv pip install -e . && uv run python -m accidents_pipeline.pipeline"

