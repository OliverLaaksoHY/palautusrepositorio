# AGENTS.md

## Repository shape
- Homework submission repo, not one application. Each exercise under `viikko1/`–`viikko4/` is an independent `uv` project with its own `pyproject.toml`, `.python-version` (Python 3.14), and usually `uv.lock`. There is no root manifest or shared test runner — run commands from the relevant project directory.
- `viikko2/varasto/` only has a `.pylintrc` (no source); `viikko2/git-branch-harjoitus/` is a git-branching exercise. `osamaara.py` at the root is a standalone script.

## TDD rules for `viikko4/tdd-ostoskori`
- Run tests with `uv run pytest` from the project root: `cd viikko4/tdd-ostoskori && uv run pytest -q`. Tests import `src/` modules directly, so this works without setting `PYTHONPATH`.
- Do not change `src/ostos.py` or `src/tuote.py`; they are provided support classes.
- Do not edit tests (`src/tests/`) unless explicitly asked.
- Implement only the smallest amount of code needed to make the current tests pass — no extra features, generalization, or refactoring. Work in `src/ostoskori.py`.

## Commands for other projects
- Every other pytest project uses the same pattern from its own directory: `uv run pytest -q` (`viikko1/nhl-statistics`, `viikko1/riippuvuuksien-injektointi`, `viikko4/maksukortti-mock`, `viikko4/mock-demo`, `viikko4/verkkokauppa`). `viikko2/nhl-reader` has no tests.
- Lint `viikko2/nhl-reader` with its nonstandard config filename: `cd viikko2/nhl-reader && uv run pylint src --rcfile=.pylintrc-tiedoston`.
- Robot: `cd viikko3/hello-robot && uv run robot src`; `cd viikko3/login && uv run robot src`, or a specific file under `src/tests/` (add `--test "Name"` to focus).

## Login app (`viikko3/login`) gotchas
- Start the Flask server before Robot tests: `cd viikko3/login && uv run python src/index.py`. It listens on port 5001; verify with `curl localhost:5001/ping` (`Pong`). `src/index.py` is the app entrypoint, not a test suite — never run `robot src/index.py`.
- `src/AppLibrary.py` calls the running app at `http://localhost:5001` to reset state and create users, so tests are not hermetic. `src/tests/resource.robot` defaults to visible chromium (`HEADLESS=false`).
- Validation really lives in `UserService.validate`: non-empty username/password, matching confirmation, and a password that is not only letters. There are no length rules. Duplicate usernames are rejected by `UserRepository.create`.
- Browser `Fill Secret` needs `$password` (no braces); `${password}` will not work. Robot keyword matching is case- and space-insensitive, but arguments still need two or more spaces after the keyword.
- Generated Robot artifacts (`output.xml`, `log.html`, `report.html`, `browser/`, `playwright-log.txt`) are gitignored; do not commit them.

## Repo-local config
- `viikko2/nhl-reader/opencode.json` is gitignored and contains a live API key. Never print, copy, or commit it.
