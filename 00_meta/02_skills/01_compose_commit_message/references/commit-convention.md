# ManageHUB commit convention

## Message format

```text
[impact-sphere] type(scope): imperative summary

- Material change 1
- Material change 2
```

Write every part in English. Keep the summary concise, imperative, lowercase, and without a final period. Add bullets only for material implementation details; omit the body when there is nothing useful to add.

## Types

| Type | Use for |
| --- | --- |
| `feat` | A new user-visible capability. |
| `fix` | A correction to faulty behavior. |
| `improve` | A deliberate enhancement to an existing capability without introducing a fundamentally new one or correcting faulty behavior. |
| `refactor` | An internal change that preserves intended behavior. |
| `docs` | Documentation-only changes. |
| `test` | Adding or changing tests. |
| `prompt` | Creating or editing a prompt when the prompt itself is the commit's primary objective. |
| `chore` | Routine maintenance, local configuration, or operational work. |
| `build` | Dependencies, packaging, or the build process. |
| `ci` | Continuous integration or delivery automation. |

Use a concise lowercase scope for the affected feature or technical area. Omit neither the type nor the scope. Use `!` immediately after the scope only for a breaking change: `feat(api)!: change response schema`.

## Bracketed impact sphere

The bracketed value identifies the project sphere in which the commit causes its greatest material effect. Determine it by asking: **where would the behavior, architectural consequences, or regressions introduced by this commit be materially perceived?** It does not identify the directory containing most changed files, the documentation section describing the change, or the technical topic used as the conventional-commit scope.

Choose the narrowest sphere that fully contains the commit's material impact, using this hierarchy:

1. **Module** — use `[module]` when one functional module is the primary affected unit.
2. **App** — use `[app]` when the effect spans multiple modules of one app or changes the app as a whole.
3. **Product sphere** — use `[ManageHUB]` or `[sroHUB]` when the effect spans multiple apps or establishes a concern for that entire product sphere.
4. **Project** — use `[project]` when the effect materially crosses ManageHUB and sroHUB, establishes repository-wide governance or architecture, or primarily affects infrastructure outside both product spheres.

Apply these rules:

- Judge impact from changed behavior, contracts, architecture, or development governance; use paths only as evidence.
- Select by effect, not edit volume: a small change to a shared contract can have a broader sphere than many local file edits.
- Prefer the smallest sphere containing all primary effects. Do not broaden the value because of incidental tests, documentation, metadata, or supporting edits.
- If one sphere is clearly dominant, use it even when the commit contains secondary support changes elsewhere.
- When two modules or apps are equally primary, use `[area1+area2]`, ordered by their first material appearance in the staged diff.
- When three or more primary areas share one parent sphere, use their shared parent instead of listing them.
- When equally primary effects cross ManageHUB and sroHUB, use `[project]` rather than `[ManageHUB+sroHUB]`.
- Use the logical module or app name visible in the repository architecture. For an app such as `masterdata`, use `[masterdata]`; never use the generic labels `[module]` or `[app]` literally.
- Do not invent a sphere from a folder name alone. For example, engineering documents that establish rules for the whole repository use `[project]`, not `[engineering]`.

Examples:

```text
[identity] feat(permissions): add delegated access rules
[sroHUB] refactor(domain): align membership and governance boundaries
[project] improve(commit-message): refine impact sphere guidance
[project] docs(architecture): establish internal engineering guidance
[project] chore(tooling): standardize repository-wide development checks
```

## Archive format

Save each proposal in `00_meta/01_Commit_Messages/` as:

```text
[YYYY-MM-DD][NNNNN](brief_description).md
```

`NNNNN` is the next global sequence number, zero-padded to five digits. `brief_description` is a short English `snake_case` description. The archive file contains the commit message followed by:

```md
## Metadata

- Generated: YYYY-MM-DD HH:MM BRT
- Touched areas: area1, area2
- Files: X created, Y modified, Z moved, W deleted
- Source: staged changes (`git diff --cached`)
```

The diff and detailed historical context remain available through `git show`.
