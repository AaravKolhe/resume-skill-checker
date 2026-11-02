"""Synthetic fixtures only; no candidate data is used in these tests."""
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "skills/hiring-panel/scripts/check_pdf_text.py"
spec = importlib.util.spec_from_file_location("pdf_check", SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class TextChecks(unittest.TestCase):
    def test_normalization_and_exact_metrics(self):
        result = module.inspect_texts(["EXPERIENCE\nSQL   analysis  $2,000  5%"],
                                      ["experience", "sql analysis", "$2,000", "5%"])
        self.assertEqual(result["findings"], [])
        self.assertEqual(module.inspect_texts(["$2,000"], ["$20,000"])
                         ["missing_expected_fields"], ["$20,000"])

    def test_missing_blank_corrupt_and_draft(self):
        result = module.inspect_texts(["[ADD: Result] \ufffd", ""], ["Python"])
        self.assertEqual(result["blank_pages"], [2])
        self.assertEqual(result["placeholder_count"], 1)
        self.assertEqual(result["replacement_character_count"], 1)
        self.assertEqual(result["missing_expected_fields"], ["Python"])

    def test_real_pdf_cli_and_no_overwrite(self):
        from reportlab.pdfgen.canvas import Canvas
        from pypdf import PdfWriter
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            pdf = root / "example.pdf"
            canvas = Canvas(str(pdf))
            canvas.drawString(72, 720, "Example Candidate | SQL | 25 projects")
            canvas.save()
            expected = root / "expected.json"
            expected.write_text(json.dumps(["Example Candidate", "SQL", "25 projects"]))
            output = root / "audit.json"
            command = [sys.executable, str(SCRIPT), str(pdf), "--expect-json", str(expected)]
            completed = subprocess.run(command + ["--output", str(output)], capture_output=True, text=True)
            self.assertEqual(completed.returncode, 0, completed.stderr)
            self.assertEqual(json.loads(output.read_text())["page_count"], 1)
            before = output.read_bytes()
            self.assertEqual(subprocess.run(command + ["--output", str(output)], capture_output=True).returncode, 2)
            self.assertEqual(output.read_bytes(), before)
            expected.write_text(json.dumps(["Missing credential"]))
            self.assertEqual(subprocess.run(command, capture_output=True).returncode, 1)
            expected.write_text("[]")
            self.assertEqual(subprocess.run(command, capture_output=True).returncode, 2)
            expected.write_text(json.dumps(["Example Candidate"]))
            encrypted = root / "encrypted.pdf"
            writer = PdfWriter()
            writer.add_blank_page(width=612, height=792)
            writer.encrypt("test-only")
            with encrypted.open("wb") as handle:
                writer.write(handle)
            self.assertEqual(subprocess.run([sys.executable, str(SCRIPT), str(encrypted),
                                            "--expect-json", str(expected)], capture_output=True).returncode, 2)


if __name__ == "__main__":
    unittest.main()
