---
description: "Instructions to use whenever creating or editing assignment markdown files to ensure consistency and clarity for students."
applyTo: "assignments/**/README.md"
---

# Assignment Markdown Structure Guidelines

All assignment markdown files must follow the repository template and the exact header/icon conventions.

## 1. Template Usage

- Assignment files must follow the structure in [templates/assignment-template.md](../../../templates/assignment-template.md).
- Each assignment must be authored as `README.md` inside its assignment folder (e.g. `assignments/python-basics/README.md`).
- Do not remove required sections or change the header icons (icons are part of the UX and should remain).

## 2. Required Sections & Exact Headers

Use the exact headers and icons from the template. Example required headers:

- `# 📘 Assignment: [Assignment Title]`
- `## 🎯 Objective`
- `## 📝 Tasks`
- `### 🛠️	[Task Title]`
- `#### Description`
- `#### Requirements`

For each section:

- **Title**: short, descriptive, and unique within the course.
- **Objective**: 1–2 concise sentences describing learning goals.
- **Tasks**: break work into one or more tasks. Each task should have a clear Description and a short, specific Requirements list (bullet points).
- **Examples**: include example input/output or sample usage in fenced code blocks when helpful.

Only add extra sections (e.g., "Hints", "Resources") when they help learning; keep them clearly labeled and placed after the required sections.