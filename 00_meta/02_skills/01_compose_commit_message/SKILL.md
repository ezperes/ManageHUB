---
name: compose-commit-message
description: Generate and archive an English commit message from the Git staged changes in the ManageHUB repository. Use when asked to compose, suggest, save, or prepare a commit message, including when the user asks to inspect staged changes before committing.
---

# Compose Commit Message

Generate one proposed commit message from the staged changes and archive it; never run `git commit`.

## Workflow

1. Run `scripts/inspect_staged_changes.py` from this skill directory.
2. If `staged` is false, show the working-tree summary and ask the user which files to stage. Stage only the confirmed paths, then run the inspection again. Never run `git add .` on your own initiative; use it only when the user explicitly requests it.
3. Read `references/commit-convention.md`, inspect `git diff --cached`, and classify the change. Ask for clarification rather than guessing when the module, scope, type, or breaking-change status is not clear.
4. Draft the message in English and validate it against the reference.
5. Save it using `scripts/save_commit_message.py --message-file <path> --description <snake_case_description> --areas <comma_separated_areas>`.
6. Report the saved file and the proposed subject. Do not create a Git commit unless separately asked.

## Output requirements

- Use the staged diff as the source of truth.
- Mention only material changes in the body.
- Treat files used solely by tooling, metadata, or documentation as incidental unless they are the commit's purpose.
- Use the module hierarchy visible in the repository. Do not infer business modules from filenames alone.
- Use `git diff --cached --name-status -M` semantics for file counts; a rename is a moved file, not a create plus delete.

## Breaking changes and uncertainty

Use `!` after the scope only when a staged change breaks a documented or reasonably implied public contract. State the incompatibility in a bullet. If confidence is insufficient, ask the user before saving.
