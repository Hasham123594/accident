# Accident Data Pipeline

## Run (one command)

```bash


git clone https://github.com/Hasham123594/accident.git
cd accident
nix-shell --run "uv run --with pytest pytest"
nix-shell --run "uv run python -m accidents_pipeline.pipeline"
