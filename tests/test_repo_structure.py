"""Phase 1 smoke test: required deliverables exist and are non-trivial.
This tests project structure only. It does NOT test any hardware or compiler."""
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
FILES = [
    "README.md", "LICENSE.md", ".gitignore", "requirements.txt", "Makefile",
    "docs/architecture.md", "docs/microarchitecture.md",
    "docs/hardware_software_interface.md", "docs/verification_plan.md",
    "docs/roadmap.md", "docs/environment.md",
    "scripts/check_env.sh", "scripts/run_tests.sh",
    ".github/workflows/ci.yml",
]
DIRS = ["rtl", "compiler", "verification", "tests", "fpga", "scripts"]


class RepoStructure(unittest.TestCase):
    def test_files_exist_and_nonempty(self):
        for f in FILES:
            p = ROOT / f
            self.assertTrue(p.is_file(), f"missing {f}")
            self.assertGreater(p.stat().st_size, 100, f"{f} is nearly empty")

    def test_dirs_exist(self):
        for d in DIRS:
            self.assertTrue((ROOT / d).is_dir(), f"missing dir {d}")

    def test_no_unverified_claims_marker(self):
        # Every spec doc must carry a status line so drafts are not mistaken for verified specs.
        for f in ["docs/architecture.md", "docs/microarchitecture.md",
                  "docs/hardware_software_interface.md", "docs/verification_plan.md"]:
            self.assertIn("Status:", (ROOT / f).read_text(), f"{f} lacks a Status: line")


if __name__ == "__main__":
    unittest.main()
