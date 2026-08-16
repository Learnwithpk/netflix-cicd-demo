# Netflix Airflow CI/CD Demo

This small project is designed for a live session to demonstrate Git commands and the basic CI/CD flow around an Airflow project.

## Project structure

```text
netflix_cicd_demo/
├── dags/
│   └── netflix_pipeline.py
├── scripts/
│   ├── extract_watch.py
│   ├── extract_users.py
│   └── validate.py
├── tests/
│   └── test_dag.py
└── .github/
    └── workflows/
        └── airflow-ci.yml
```

## Git commands for the live demo

### 1. Open the project
```bash
cd netflix_cicd_demo
```

### 2. Initialize Git
```bash
git init
```

### 3. Check files
```bash
git status
```

### 4. Stage files
```bash
git add .
```

### 5. Create the first commit
```bash
git commit -m "Initial Netflix Airflow pipeline"
```

### 6. Create a GitHub repository
Create an empty repository named `netflix-cicd-demo`, then connect it:

```bash
git branch -M main
git remote add origin <YOUR_GITHUB_REPOSITORY_URL>
git push -u origin main
```

### 7. Make a change
Edit `scripts/validate.py`, then:

```bash
git status
git diff
git add .
git commit -m "Update validation logic"
git push
```

### 8. Demonstrate a failure
Intentionally remove the comma after:
```python
task_id="extract_watch",
```

Then:
```bash
git add .
git commit -m "Introduce DAG syntax error"
git push
```

Open GitHub -> Actions and show the CI failure.

### 9. Fix it
Restore the comma:

```bash
git add .
git commit -m "Fix DAG syntax error"
git push
```

GitHub Actions should pass again.

## Important teaching point

Git/GitHub = version control and collaboration.

CI = automatically validate/test the code after a change.

CD = automatically deliver/deploy approved code to the target environment.

Airflow = orchestrates the data workflow after the code is deployed.
