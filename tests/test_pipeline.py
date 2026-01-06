from pathlib import Path
import pandas as pd

from accidents_pipeline.pipeline import run_pipeline

def test_pipeline_creates_expected_outputs(tmp_path, monkeypatch):
    # copy dataset into temp dir
    src = Path("data/accidents_2017_to_2023_english.csv")
    assert src.exists()

    (tmp_path / "data").mkdir(parents=True, exist_ok=True)
    (tmp_path / "data" / src.name).write_bytes(src.read_bytes())

    # run pipeline in temp dir
    monkeypatch.chdir(tmp_path)
    outputs = run_pipeline()

    # files exist and non-empty
    for p in outputs.values():
        p = Path(p)
        assert p.exists()
        assert p.stat().st_size > 0

    # CSV has expected columns and at most 10 rows
    df = pd.read_csv(outputs["data"])
    assert set(df.columns) == {"cause_of_accident", "total_injured"}
    assert 1 <= len(df) <= 10
