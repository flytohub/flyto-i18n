"""Regression tests for the canonical supported-project contract."""

import ast
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class SharedProjectContractTests(unittest.TestCase):
    """Prevent supported project scope lists from diverging across tools."""

    def test_only_i18n_contract_assigns_project_dirs(self):
        """Require operational scripts to import the canonical project list."""
        assignments = []
        for path in sorted((ROOT / "scripts").glob("*.py")):
            tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
            for node in tree.body:
                if isinstance(node, ast.Assign) and any(
                    isinstance(target, ast.Name) and target.id == "PROJECT_DIRS"
                    for target in node.targets
                ):
                    assignments.append(path.name)

        self.assertEqual(assignments, ["i18n_contract.py"])


if __name__ == "__main__":
    unittest.main()
