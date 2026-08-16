def test_basic_pipeline_files_exist():
    from pathlib import Path

    assert Path("dags/netflix_pipeline.py").exists()
    assert Path("scripts/extract_watch.py").exists()
    assert Path("scripts/extract_users.py").exists()
    assert Path("scripts/validate.py").exists()
