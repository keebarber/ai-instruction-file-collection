#!/usr/bin/env python3
"""
Build rendered, styled HTML pages for every Markdown file in this collection.

Output: a `view/` folder mirroring the repo tree, with one self-contained
`.html` page per `.md` file. The root `index.html` links to these pages.

Re-run after editing any markdown:  python3 build-views.py
Requires: pip install markdown
"""
import os, re, html, datetime
import markdown

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "view")

# folder -> (accent color, friendly label)
CATS = {
    "coding-agents":    ("#2563eb", "Coding agents"),
    "writing-and-voice":("#db2777", "Writing & voice"),
    "asking-questions": ("#0d9488", "Asking questions"),
    "system-prompts":   ("#7c3aed", "System prompts"),
    "skills":           ("#ea580c", "Skills"),
    "career-context":   ("#0369a1", "Career context"),
}
DEFAULT_CAT = ("#4f46e5", "Reference")

# filename -> (badge label, css class) for the fidelity chip
FIDELITY = {
    "humanlayer-writing-a-good-CLAUDE-md.md": ("Verbatim (condensed)", "b-condensed"),
    "anthropic-claude-code-best-practices.md": ("Verbatim (condensed)", "b-condensed"),
    "agents-md-spec-and-examples.md": ("Verbatim (condensed)", "b-condensed"),
    "openai-codex-agents-md-guide.md": ("Verbatim (condensed)", "b-condensed"),
    "shanraisshan-CLAUDE.md": ("Verbatim", "b-verbatim"),
    "how-to-write-code-rules.cheatsheet.md": ("Distilled", "b-distilled"),
    "avoid-ai-writing.SKILL.md": ("Verbatim · MIT", "b-verbatim"),
    "words-and-phrases-to-avoid.cheatsheet.md": ("Distilled", "b-distilled"),
    "how-to-write-and-sound.md": ("Distilled", "b-distilled"),
    "when-and-how-to-ask-questions.md": ("Distilled", "b-distilled"),
    "candidate-profile.md": ("Authored", "b-authored"),
    "job-description-analyzer.SKILL.md": ("Verbatim · MIT", "b-verbatim"),
    "resume-cover-letter.SKILL.md": ("Verbatim", "b-verbatim"),
    "interview-prep-generator.SKILL.md": ("Verbatim · MIT", "b-verbatim"),
    "salary-negotiation-prep.SKILL.md": ("Verbatim · MIT", "b-verbatim"),
    "systematic-debugging.SKILL.md": ("Verbatim", "b-verbatim"),
    "test-driven-development.SKILL.md": ("Verbatim", "b-verbatim"),
    "verification-before-completion.SKILL.md": ("Verbatim", "b-verbatim"),
    "skill-creator.SKILL.md": ("Verbatim · Apache 2.0", "b-verbatim"),
}

PAGE_CSS = """
:root{
  --paper:#fbfaf7;--card:#fff;--ink:#1d2230;--ink-soft:#3f465a;--ink-faint:#7c8499;
  --line:#e7e3da;--line-soft:#efece4;--accent:__ACCENT__;--accent-ink:#4f46e5;
  --code-bg:#f5f3ee;--shadow:0 1px 2px rgba(20,24,40,.04),0 6px 20px rgba(20,24,40,.05);
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--paper);color:var(--ink);
  font:16.5px/1.72 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  -webkit-font-smoothing:antialiased}
a{color:var(--accent-ink)}
a:hover{text-decoration:underline}

/* top bar */
.bar{position:sticky;top:0;z-index:10;background:rgba(251,250,247,.88);backdrop-filter:saturate(1.4) blur(8px);
  border-bottom:1px solid var(--line)}
.bar-in{max-width:860px;margin:0 auto;padding:11px clamp(18px,4vw,32px);display:flex;align-items:center;gap:14px;flex-wrap:wrap}
.back{display:inline-flex;align-items:center;gap:7px;font-weight:600;font-size:14px;color:var(--ink-soft);text-decoration:none;
  border:1px solid var(--line);background:#fff;padding:6px 12px;border-radius:9px;box-shadow:var(--shadow)}
.back:hover{color:var(--ink);text-decoration:none;border-color:#d9d4c8}
.crumb{font-size:13px;color:var(--ink-faint);font-family:ui-monospace,SFMono-Regular,Menlo,monospace}
.crumb b{color:var(--accent);font-weight:600}
.bar .right{margin-left:auto;display:flex;align-items:center;gap:9px}
.chip{font-size:11.5px;font-weight:600;padding:3px 10px;border-radius:999px;white-space:nowrap}
.b-verbatim{background:#e7f6ec;color:#1a7f43}
.b-condensed{background:#e3f3f1;color:#0d7d72}
.b-distilled{background:#fdf0dd;color:#b6741a}
.b-authored{background:#efe9fb;color:#6d3fc4}
.b-links{background:#eceef2;color:#5a6276}
.raw{font-size:13px;font-weight:600;color:var(--ink-soft);text-decoration:none}
.raw:hover{color:var(--ink)}

/* accent rule under bar */
.accent-rule{height:3px;background:var(--accent)}

/* article */
main{max-width:820px;margin:0 auto;padding:38px clamp(18px,4vw,32px) 90px}
.doc h1{font-size:clamp(26px,3.6vw,34px);line-height:1.15;letter-spacing:-.02em;margin:.2em 0 .5em}
.doc h2{font-size:23px;letter-spacing:-.01em;margin:1.9em 0 .55em;padding-bottom:.28em;border-bottom:1px solid var(--line)}
.doc h3{font-size:18.5px;margin:1.7em 0 .5em}
.doc h4{font-size:15.5px;margin:1.5em 0 .4em;color:var(--ink-soft);text-transform:none}
.doc p{margin:.5em 0 1em}
.doc a{color:var(--accent-ink);word-break:break-word}
.doc ul,.doc ol{padding-left:1.35em;margin:.5em 0 1.2em}
.doc li{margin:.32em 0}
.doc li>ul,.doc li>ol{margin:.3em 0 .4em}
.doc strong{color:var(--ink)}
.doc hr{border:none;border-top:1px solid var(--line);margin:2.2em 0}
.doc blockquote{margin:1.2em 0;padding:.55em 1.1em;border-left:4px solid var(--accent);
  background:#fff;border-radius:0 10px 10px 0;color:var(--ink-soft);box-shadow:var(--shadow)}
.doc blockquote p{margin:.35em 0}
.doc code{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:.86em;
  background:var(--code-bg);padding:.12em .42em;border-radius:6px;color:#9d174d}
.doc pre{background:#1d2230;color:#e8eaf0;padding:16px 18px;border-radius:12px;overflow:auto;
  font-size:13.5px;line-height:1.6;margin:1.1em 0;box-shadow:var(--shadow)}
.doc pre code{background:none;color:inherit;padding:0;font-size:13.5px}
.doc table{border-collapse:collapse;width:100%;margin:1.2em 0;font-size:14.5px;
  background:#fff;border:1px solid var(--line);border-radius:10px;overflow:hidden;box-shadow:var(--shadow)}
.doc th,.doc td{text-align:left;padding:9px 13px;border-bottom:1px solid var(--line-soft);vertical-align:top}
.doc th{background:#f6f4ee;font-size:12.5px;text-transform:uppercase;letter-spacing:.04em;color:var(--ink-soft)}
.doc tr:last-child td{border-bottom:none}
.doc img{max-width:100%}

/* frontmatter panel */
.frontmatter{background:#fff;border:1px solid var(--line);border-left:4px solid var(--accent);
  border-radius:10px;padding:12px 16px;margin:0 0 26px;box-shadow:var(--shadow)}
.frontmatter .fm-label{font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--ink-faint);margin-bottom:6px}
.frontmatter pre{margin:0;background:none;color:var(--ink-soft);box-shadow:none;padding:0;font-size:13px;line-height:1.6;white-space:pre-wrap}

footer{max-width:820px;margin:0 auto;padding:0 clamp(18px,4vw,32px) 60px;color:var(--ink-faint);font-size:13px}
footer a{font-weight:600}
"""

PAGE_TMPL = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(title)s · AI Instruction File Collection</title>
<style>%(css)s</style>
</head>
<body>
<div class="bar">
  <div class="bar-in">
    <a class="back" href="%(index_rel)s">← Overview</a>
    <span class="crumb"><b>%(cat_label)s</b> / %(fname)s</span>
    <span class="right">%(chip)s<a class="raw" href="%(raw_rel)s">raw ↧</a></span>
  </div>
</div>
<div class="accent-rule"></div>
<main>
  <article class="doc">
%(frontmatter)s%(body)s
  </article>
</main>
<footer>
  <p>Rendered from <code>%(relpath)s</code> · part of the <a href="%(index_rel)s">AI Instruction File Collection</a>. Source &amp; license in <a href="%(sources_rel)s">SOURCES.md</a>.</p>
</footer>
</body>
</html>
"""

md = markdown.Markdown(extensions=["extra", "sane_lists", "toc", "attr_list"])

def split_frontmatter(text):
    """Return (frontmatter_or_None, body). Handles leading --- ... --- YAML."""
    if text.startswith("---"):
        m = re.match(r"^---\s*\n(.*?)\n---\s*\n?", text, re.DOTALL)
        if m:
            return m.group(1).strip(), text[m.end():]
    return None, text

def category_for(rel):
    top = rel.split(os.sep)[0]
    return CATS.get(top, DEFAULT_CAT)

def build():
    md_files = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        if "/.git" in dirpath or dirpath.endswith("/.git") or os.sep+"view" in dirpath:
            continue
        for fn in filenames:
            if fn.lower().endswith(".md"):
                md_files.append(os.path.relpath(os.path.join(dirpath, fn), ROOT))
    md_files.sort()

    for rel in md_files:
        src = os.path.join(ROOT, rel)
        with open(src, encoding="utf-8") as f:
            text = f.read()
        fm, body_md = split_frontmatter(text)
        md.reset()
        body_html = md.convert(body_md)

        out_path = os.path.join(OUT, rel[:-3] + ".html")  # strip .md
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        depth = out_path[len(OUT)+1:].count(os.sep)  # dirs under view/
        index_rel = "../" * (depth + 1) + "index.html"
        sources_rel = "../" * (depth + 1) + "SOURCES.md"
        raw_rel = "../" * (depth + 1) + rel  # back to the real .md

        accent, cat_label = category_for(rel)
        fname = os.path.basename(rel)
        title = fname[:-3]

        badge = FIDELITY.get(fname)
        if badge is None and fname.lower() == "readme.md":
            badge = ("Index", "b-links")
        chip = f'<span class="chip {badge[1]}">{html.escape(badge[0])}</span>' if badge else ""

        fm_html = ""
        if fm:
            fm_html = ('<div class="frontmatter"><div class="fm-label">Skill metadata · YAML frontmatter</div>'
                       f'<pre>{html.escape(fm)}</pre></div>\n')

        page = PAGE_TMPL % {
            "title": html.escape(title),
            "css": PAGE_CSS.replace("__ACCENT__", accent),
            "index_rel": index_rel,
            "sources_rel": sources_rel,
            "raw_rel": raw_rel,
            "cat_label": html.escape(cat_label),
            "fname": html.escape(fname),
            "chip": chip,
            "frontmatter": fm_html,
            "body": body_html,
            "relpath": html.escape(rel),
        }
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(page)
        print("wrote", os.path.relpath(out_path, ROOT))

    print(f"\n{len(md_files)} pages built into view/  ({datetime.date.today()})")

if __name__ == "__main__":
    build()
