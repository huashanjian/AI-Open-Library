import sys
import re
import unicodedata
from pathlib import Path

try:
    from pypdf import PdfReader
except Exception as e:
    print("ERROR: pypdf is required. Install with 'pip install pypdf'.", file=sys.stderr)
    sys.exit(2)


def ascii_slug(text: str) -> str:
    text = unicodedata.normalize('NFKD', text)
    text = text.encode('ascii', 'ignore').decode('ascii')
    text = re.sub(r"[^A-Za-z0-9]+", "_", text)
    text = re.sub(r"_+", "_", text).strip("_")
    return text or "untitled"


def guess_title_from_page(reader: PdfReader) -> str | None:
    try:
        page0 = reader.pages[0]
        text = page0.extract_text() or ""
        # take top lines and pick the first reasonably long line
        lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
        for ln in lines[:20]:
            if 8 <= len(ln) <= 200 and re.search(r"[A-Za-z]{3,}", ln):
                return ln
    except Exception:
        pass
    return None


AMBIGUOUS_NAMES = {
    "book.pdf", "book_(3).pdf", "pdf.pdf", "pdf_(3).pdf",
    "index.pdf", "notes.pdf", "lecture-notes.pdf", "lecture-notes_(3).pdf",
    "dm.pdf", "RW.pdf", "mas.pdf", "Agent_Learning)_-_mas_(3).pdf",
    "mml-book.pdf", "SzeliskiBook_20100903_draft.pdf", "rlbook.pdf",
    "ESLII_print12_toc.pdf", "ISLRv2_website.pdf",
}


def iter_targets(args: list[str]):
    for p in args:
        f = Path(p)
        if f.is_dir():
            for cand in f.glob("*.pdf"):
                if cand.name in AMBIGUOUS_NAMES:
                    yield cand
        elif f.exists():
            yield f
        else:
            # allow simple globbing patterns
            for cand in Path().glob(p):
                if cand.is_file():
                    yield cand


def main(paths: list[str]) -> int:
    for f in iter_targets(paths):
        try:
            reader = PdfReader(str(f))
        except Exception as e:
            print(f"ERR\t{f.name}\topen_failed\t{e}")
            continue

        md = getattr(reader, 'metadata', None)
        title = None
        author = None
        if md:
            # pypdf returns a DocumentInformation-like object with .title/.author
            title = getattr(md, 'title', None) or None
            author = getattr(md, 'author', None) or None

        if not title:
            title = guess_title_from_page(reader)

        base_parts = []
        if title:
            base_parts.append(title)
        if author:
            base_parts.append(author)

        if base_parts:
            new_base = ascii_slug("_".join(base_parts))
        else:
            new_base = ascii_slug(f.stem)

        suggestion = f.with_name(new_base + f.suffix)
        print("SUGGEST\t" + f.name + "\t" + suggestion.name)
    return 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scripts/pdf_probe.py <pdf|dir|glob> [<pdf|dir|glob> ...]")
        sys.exit(1)
    sys.exit(main(sys.argv[1:]))
