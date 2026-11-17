# Contributing to Workhorse

Thank you for your interest in contributing to **Workhorse**! Workhorse is designed as a high-performance terminal workstation and autonomous agent runtime that turns even the smallest models into reliable workhorses.

## Code of Conduct

We are committed to providing a welcoming, inclusive, and harassment-free environment for everyone. Please be respectful and constructive in all discussions, issues, and pull requests.

## Development Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/kingjethro999/workhorse.git
   cd workhorse
   ```

2. **Set Up Python Virtual Environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   pip install -e .
   ```

3. **Install Git Hooks:**
   The repository includes an automated version bumper hook:
   ```bash
   cp scripts/git-hooks/pre-commit .git/hooks/pre-commit
   chmod +x .git/hooks/pre-commit
   ```

4. **Run Tests:**
   ```bash
   pytest
   ```

5. **Web Showcase Development (`/web`):**
   ```bash
   cd web
   zyrk install
   npm run dev
   ```

## Pull Request Guidelines

1. Ensure all tests pass before submitting.
2. Follow existing code style and formatting conventions.
3. Keep pull requests focused on a single feature or bug fix.
4. Verify non-blocking UI behavior and 5-Cycle resilience guarantees.
5. Update relevant documentation and language translations when modifying public APIs or CLI flags.

## Versioning Scheme

Workhorse uses an automated commit-driven versioning scheme:
- Every regular commit increments the patch version (+0.0.1).
- Reaching `x.x.9` rolls over to `x.(x+1).0`.
- Reaching `x.599.9` rolls over to `(x+1).0.0`.
