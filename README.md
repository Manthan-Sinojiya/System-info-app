# DevOps Demo: Flask + Git Workflow

This repo is a demo project for a DevOps-style submission:
- Small Flask app
- Dockerfile
- Tests with pytest
- CI configured with GitHub Actions
- Example branching + PR workflow instructions

## Run locally (without Docker)
1. Create virtualenv:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. Run:
   ```bash
   python app.py
   # open http://localhost:8000
   ```

## Run with Docker
```bash
docker build -t demo-flask:1.0.0 .
docker run -p 8000:8000 demo-flask:1.0.0
# open http://localhost:8000
```

## Tests
```bash
pytest
```

## Git workflow (recommended)
We recommend a simple feature-branch workflow:
- `master` — production-ready
- `dev` — integration branch
- `feature/*` — each new feature or fix

Example local flow:
```bash
# init repo (one-time)
git init
git add .
git commit -m "chore: initial project scaffold"

# create remote and push master
git branch -M master
git remote add origin <your-github-repo-url>
git push -u origin master

# create dev branch
git checkout -b dev
git push -u origin dev

# Start a feature
git checkout -b feature
# make changes...
git add .
git commit -m "feat(echo): add /echo POST endpoin"
git push -u origin feature/add-echo-endpoint

# Create a Pull Request from feature/* -> dev (use GitHub UI)
# After code review and CI green, merge to dev
# Later, open PR dev -> master and merge when ready
```

## Example commit messages
- `feat: add /echo endpoint`
- `fix: correct status code for echo`
- `chore: update README`
- `ci: add GitHub Actions workflow`

## Tags
Tag releases with semver:
```bash
git tag -a v0.1.0 -m "Initial demo release"
git push origin v0.1.0
```

## References
- Feature branch workflow (good overview): [Atlassian Git tutorial](https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow)
- Branching guidance: [Microsoft Azure Repos docs](https://learn.microsoft.com/en-us/azure/devops/repos/git/git-branching-guidance)
- Dockerize Flask: [Docker Docs](https://docs.docker.com/language/python/build-images/)
- GitHub Actions for Python projects: [RealPython Guide](https://realpython.com/python-github-actions-ci-cd/)
