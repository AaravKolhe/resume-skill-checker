"""Local PDF extraction checks; never an ATS score or acceptance prediction."""
import argparse
import json
from pathlib import Path
import re
import sys
import unicodedata


def normalize(text):
    return " ".join(unicodedata.normalize("NFKC", text).casefold().split())


def inspect_texts(pages, expected):
    text = "\n".join(pages)
    normalized = normalize(text)
    missing = [field for field in expected if normalize(field) not in normalized]
    blank = [index + 1 for index, page in enumerate(pages) if not page.strip()]
    placeholders = len(re.findall(r"\[\s*ADD\s*:", text, re.IGNORECASE))
    replacements = text.count("\ufffd")
    findings = []
    if not pages:
        findings.append("no_pages")
    if blank:
        findings.append("pages_without_extractable_text")
    if missing:
        findings.append("expected_fields_not_found")
    if placeholders:
        findings.append("unresolved_factual_prompts")
    if replacements:
        findings.append("replacement_characters")
    return {
        "status": "issues_found" if findings else "no_issues_observed",
        "page_count": len(pages),
        "characters_per_page": [len(page) for page in pages],
        "blank_pages": blank,
        "expected_field_count": len(expected),
        "missing_expected_fields": missing,
        "placeholder_count": placeholders,
        "replacement_character_count": replacements,
        "findings": findings,
        "limitations": "Text extraction and substring checks only. Layout, reading order, "
                      "job qualifications, and real ATS acceptance are not verified.",
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", type=Path)
    parser.add_argument("--expect-json", type=Path, required=True,
                        help="Nonempty JSON array of expected source-supported strings")
    parser.add_argument("--output", type=Path, help="New local JSON audit path; never overwrites")
    args = parser.parse_args(argv)
    try:
        if args.output and args.output.exists():
            raise ValueError("Output already exists; choose a new audit filename")
        expected = json.loads(args.expect_json.read_text(encoding="utf-8-sig"))
        if not isinstance(expected, list) or not expected or not all(
            isinstance(value, str) and value.strip() for value in expected
        ):
            raise ValueError("Expected fields must be a nonempty JSON array of nonblank strings")
        from pypdf import PdfReader
        reader = PdfReader(args.pdf)
        if reader.is_encrypted:
            raise ValueError("Encrypted PDF: use an authorized unencrypted export for this check")
        result = inspect_texts([page.extract_text() or "" for page in reader.pages], expected)
        result.update({"file": str(args.pdf.resolve()), "extractor": "pypdf"})
        status = 1 if result["findings"] else 0
        payload = json.dumps(result, ensure_ascii=False, indent=2)
        if args.output:
            with args.output.open("x", encoding="utf-8") as handle:
                handle.write(payload + "\n")
        print(payload)
        return status
    except Exception as exc:
        print(json.dumps({"status": "unverified", "error": str(exc)}, ensure_ascii=False),
              file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
