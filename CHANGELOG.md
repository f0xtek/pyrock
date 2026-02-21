# Changelog

All notable changes to this project will be documented in this file.

## [1.0.0] - 2026-02-21

### Security
- Fixed Flask debug mode: `debug=True` replaced with `debug=False` to prevent exposure of sensitive information in production
- Replaced weak PRNG (`random.choice`) with cryptographically secure `secrets.choice` for passphrase generation
- Added HTTP request timeout to `requests.get()` to prevent indefinite hanging

### Dependencies Updated
- `flask` bumped from 2.2.5 → 3.1.3
- `requests` bumped from 2.22.0 → 2.32.4
- `werkzeug` bumped from 2.2.3 → 3.1.6
- `jinja2` bumped from 3.1.2 → 3.1.6
- `urllib3` bumped from 1.25.11 → 2.6.3
- `zipp` bumped from 3.15.0 → 3.19.1
- `certifi` bumped from 2022.12.7 → 2023.7.22

### Changed
- Upgraded project Python version requirement to 3.13

### Added
- README.md with project overview, installation instructions, usage guide, and security notes
