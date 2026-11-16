# AGENTS.md

## Repository shape
- This is a homework submission repo, not one application. Each exercise under `viikko1/`, `viikko2/`, and `viikko3/` is an independent `uv` project with its own `pyproject.toml`, `uv.lock`, and `.python-version` (Python 3.14).
- There is no root manifest or shared test runner. Run commands from the relevant project directory.
- `viikko2/varasto/` only has a `.pylintrc` (no source). `viikko2/git-branch-harjoitus/` is a git-branching exercise.

## Commands
- Python tests:
  - `cd viikko1/nhl-statistics && uv run pytest -q`
  - `cd viikko1/riippuvuuksien-injektointi && uv run pytest -q`
- Robot Framework:
  - `cd viikko3/hello-robot && uv run robot src`
  - `cd viikko3/login && uv run robot src`
  - Single login test: `cd viikko3/login && uv run robot --test "Register With Valid Username And Password" src/tests/register.robot`
- Lint `viikko2/nhl-reader` with its custom config filename:
  - `cd viikko2/nhl-reader && uv run pylint src --rcfile=.pylintrc-tiedoston`
- `viikko2/nhl-reader` has no tests; `uv run pytest` reports "no tests ran".

## Login app (`viikko3/login`)
- Project uses the uv-library and commands are executed in the following form `uv run ...`
- Start the Flask server before running Robot tests: `cd viikko3/login && uv run python src/index.py`. It listens on port 5001; verify with `curl localhost:5001/ping` (returns `Pong`).
- Do not run `robot src/index.py`; that file is the app entrypoint, not a test suite. Run `robot src` or a specific test file under `src/tests/`.
- Entrypoint is `src/index.py`; routes are in `src/app.py`; users are stored in memory by `src/repositories/user_repository.py`.
- Robot tests are in `src/tests/`; shared keywords/variables are in `resource.robot`. `src/AppLibrary.py` calls the running app at `http://localhost:5001` to reset state and create users.
- Current redirects: successful registration -> `/welcome`, failed registration -> `/register`, successful login -> `/ohtu`.
- Registration validation lives in `UserService.validate` (username >= 3, password >= 8, matching confirmation, at least one non-letter character). Duplicate usernames are rejected by `UserRepository.create`.
- Browser library `Fill Secret` requires `$password` style (without braces). `${password}` is a normal Robot variable and will not work with that keyword.
- Robot keyword matching is case- and space-insensitive (`Set username` == `Set Username`), but arguments still need two spaces or more after the keyword.
- Generated Robot artifacts (`output.xml`, `log.html`, `report.html`, `browser/`, `playwright-log.txt`) are ignored; do not commit them.
