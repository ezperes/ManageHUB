# ManageHUB commit convention

## Message format

```text
[module/app/context] type(scope): imperative summary

- Material change 1
- Material change 2
```

Write every part in English. Keep the summary concise, imperative, lowercase, and without a final period. Add bullets only for material implementation details; omit the body when there is nothing useful to add.

## Types

| Type | Use for |
| --- | --- |
| `feat` | A new user-visible capability. |
| `fix` | A correction to faulty behavior. |
| `refactor` | An internal change that preserves intended behavior. |
| `docs` | Documentation-only changes. |
| `test` | Adding or changing tests. |
| `prompt` | Creating or editing a prompt when the prompt itself is the commit's primary objective. |
| `chore` | Routine maintenance, local configuration, or operational work. |
| `build` | Dependencies, packaging, or the build process. |
| `ci` | Continuous integration or delivery automation. |

Use a concise lowercase scope for the affected feature or technical area. Omit neither the type nor the scope. Use `!` immediately after the scope only for a breaking change: `feat(api)!: change response schema`.

## Bracketed area

Choose the bracketed area by relevance to the objective, not by the number of changed files.

- One dominant module/app/context: `[module]`.
- Two equally material modules or spheres: `[module1+module2]`, ordered by their first appearance in the staged diff.
- A dominant module with small supporting changes in other areas: use only the dominant module.
- Three or more equally material areas within one shared higher sphere: use that sphere, such as `[sroHUB]` or `[ManageHUB]`.
- Material changes across distinct higher spheres: `[project]`.

Use the logical app or module name from the repository structure. For a subapp such as `masterdata`, use `[masterdata]`; do not replace it with a generic label such as `[app]`.

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
