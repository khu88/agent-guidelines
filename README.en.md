# Agent Guidelines

[简体中文](README.md) | English

Selectable, customizable, and composable **AGENTS.md collaboration guidelines** for Codex and other agents that support project instructions. Choose modules for the task and merge their content into your own project instructions. No user identity, discipline, or working habits are assumed.

This project provides separate Chinese and English versions. Existing files without a language suffix are in Chinese; `.en.md` files are their English counterparts. Both languages express the same requirements, so choose one for use. Modules and examples are ordinary Markdown; they do not automatically enable or load other files.

## Choosing modules

| Module | 中文 / English | What it addresses | When to use it |
| --- | --- | --- | --- |
| core | [中文](modules/core.md) / [English](modules/core.en.md) | Checking premises, evidence and judgment, distinguishing content from instructions, prohibiting fabrication | Recommended for every combination, or use equivalent existing rules |
| execution | [中文](modules/execution.md) / [English](modules/execution.en.md) | Autonomous execution, clarification, authorization and privacy, completion and acceptance | Investigation, search, editing, execution, or delivery tasks |
| research | [中文](modules/research.md) / [English](modules/research.en.md) | Related work, novelty assessment, experimental design, reproducibility, and interpretation of results | Literature analysis, research design, and experiments |
| continuity | [中文](modules/continuity.md) / [English](modules/continuity.en.md) | Task status, resuming interrupted work, and handoff between agents | Tasks with multiple stages, long durations, or a need for continuation |
| paper-writing | [中文](modules/paper-writing.md) / [English](modules/paper-writing.en.md) | Contribution-focused narratives, the argumentative role of experiments, and sentence-by-sentence review | Drafting, revising, and reviewing papers |

Modules do not automatically import one another. `core` provides shared principles; select other modules as needed and consolidate duplicates when equivalent project rules already exist. `research` does not require `continuity`, and `paper-writing` does not require experiment or status files. Omitting a module does not remove existing user constraints, project rules, or tool permissions.

## Recommended combinations

| Task | Suggested selection |
| --- | --- |
| General execution tasks | core + execution |
| Analyzing user-provided literature entirely within the conversation | core + research |
| Literature analysis requiring external searches | core + execution + research |
| Engineering tasks with multiple stages | core + execution + continuity |
| Research experiments | core + execution + research; add continuity when resumption is needed |
| Drafting or reviewing paper content entirely within the conversation | core + paper-writing; add research for literature or experimental analysis |
| Paper tasks requiring file edits, searches, or tool execution | core + execution + paper-writing; add research / continuity as needed |

When a task involves tool execution, file changes, external transmission, or resource use, include `execution` or confirm that the project already has equivalent boundaries. Even a read-only search may send query content to an external service. Conversation-only combinations apply to tasks that do not require these operations.

### Alternating between official services and third-party relays

**`HANDOFF.md` is especially useful for users who alternate between official services and third-party API relay services while continuing the same project.** With `continuity` selected, current conclusions, unresolved issues, recommended next steps, and a starting prompt can be kept in project files, giving a new session a clear starting point and reducing reliance on a single chat history.

When the module's trigger conditions apply, update changed handoff information before switching. In the new session, have the agent read `HANDOFF.md`, the referenced `STATUS.md`, and necessary project files, then check the current code, artifacts, and verification status. Continuation requires the target agent to have access to these files. Handoff files do not automatically synchronize chat history, service configuration, or permissions, and do not authorize disclosure of sensitive content to another service.

## How to use

1. Choose a language and modules, and read each module's scope.
2. Merge the full text of the selected modules into the target project's `AGENTS.md`, or start with a complete example from the table below. If an `AGENTS.md` already exists, review and merge the content first, preserving the project's own build, test, and directory conventions.
3. Use the [English customization template](templates/CUSTOMIZATION.example.en.md) or its [Chinese counterpart](templates/CUSTOMIZATION.example.md) to record necessary preferences, project configuration, and authorization that has actually been confirmed. Remove fields you do not need.
4. Consolidate duplicate rules and resolve conflicts explicitly. Do not rely on concatenation order to expand authorization or change research claims, and do not paste both language versions of the same rule.
5. Confirm which instructions the target agent actually loads and where they apply, then check behavior on real tasks. Treat unconfirmed loading and untested behavior as unverified.

| Complete example | 中文 | English | Included modules |
| --- | --- | --- | --- |
| Minimal execution combination | [AGENTS.minimal.md](examples/AGENTS.minimal.md) | [AGENTS.minimal.en.md](examples/AGENTS.minimal.en.md) | core + execution |
| Full research combination | [AGENTS.research.md](examples/AGENTS.research.md) | [AGENTS.research.en.md](examples/AGENTS.research.en.md) | All five modules, each still governed by its own scope |

The module text is included inline in each example. Copy the selected example and name it `AGENTS.md` in the target project. The example filenames used here are not automatic loading entry points. "Minimal" means fewer modules; it still preserves the full execution boundaries.

## File format and Codex usage

The [`AGENTS.md` format documentation](https://agents.md/) defines it as an ordinary Markdown file for project instructions. This project uses the name **`AGENTS.md`**; `agent.md` is not the default entry point here.

According to the [official Codex documentation](https://developers.openai.com/codex/guides/agents-md/), Codex discovers global and project instructions and combines them by directory hierarchy. Within the same directory, `AGENTS.override.md` takes precedence over `AGENTS.md`. Other filenames require client configuration; renaming a file or adding a Markdown link alone does not establish that it loads successfully. The default combined instruction size limit is 32 KiB, controlled by `project_doc_max_bytes`; check the total size after adding other project rules. These details were checked on 2026-10-27. Refer to the client in use and the official documentation for actual behavior.

This project does not define template-variable expansion or automatic client imports. These rules are behavioral agreements, cannot replace tool permission controls, and do not guarantee consistent model compliance. Document structure checks are not client-loading verification or task-effectiveness evaluations. Cross-client behavior has not yet been verified.

## What can be customized

| Setting | Public default |
| --- | --- |
| Identity, expertise, research or project area | Unspecified; fill in only when useful |
| Response language | Follow the user's current request |
| Length and format | Cover necessary information and adapt to complexity |
| Preauthorized targets, operations, budgets, counts, and duration | No authorization is prefilled; use records explicitly confirmed by the user |
| Status records | continuity is optional; when selected, it applies only to qualifying tasks |
| Status-file names and locations | STATUS.md and HANDOFF.md by default; existing project records serving these two roles may be reused |
| Paper style | Center the narrative on evidence-supported contributions and adapt to the target journal or conference |

`execution` uses explicit authorization as its default policy. To reduce repeated confirmation, use the template to record the specific operations, scope, and limits the user has already approved. Do not treat template content as approval that has not occurred. Users may adapt the rules to their needs, but changing the text does not itself grant tool permissions or constitute user authorization. Truthfulness, accurate verification-status reporting, fair interpretation of evidence, and not fabricating authorization are not optional style settings.

Personal configuration can be saved as `CUSTOMIZATION.local.en.md` or `CUSTOMIZATION.local.md` in the root directory. These names are excluded by `.gitignore`, but that does not make them load automatically; merge them manually or configure the target tool. Do not put credentials, private identifying information, unpublished research content, or sensitive authorization in public files. Ignore rules do not protect files already tracked by Git, so inspect the actual distribution content before publishing.

## Bilingual maintenance and checks

Use the paired Chinese and English files in `modules/` as the source for module text. When changing a rule, update the other language and preserve its applicability, prohibitions, authorization strength, and acceptance meaning. Give each rule one primary home; other modules should add only requirements specific to their scenarios. Resolve language discrepancies rather than letting whichever version is pasted last determine the meaning.

The four examples are synchronized by [scripts/sync_examples.py](scripts/sync_examples.py) to prevent drift between examples and modules. The tool uses only the Python 3 standard library. With an existing Python 3 environment, run this from the project directory:

```sh
python3 scripts/sync_examples.py --check
```

After changing modules, the following commands rewrite all four examples and then check synchronization:

```sh
python3 scripts/sync_examples.py --write
python3 scripts/sync_examples.py --check
```

These checks only confirm that examples match their modules; they do not evaluate translation quality or agent behavior. For custom combinations, copy the modules you need directly; running the script is unnecessary. Before submitting changes, check bilingual meaning, Markdown links, and example synchronization.

## Publication status

This version does not yet specify a license. The license and rights attribution remain for the maintainer to determine. Once a license is chosen, a root `LICENSE` file will be added and this section updated; this version does not claim to be under an open-source license. [GitHub's licensing documentation](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository) explains the distinction between a public repository and permission to use, modify, and distribute its content.

Local maintainers may use root `STATUS.md` and `HANDOFF.md` files to record progress and handoffs. These files are included in `.gitignore` and are not part of the template distribution. This setting does not affect users' selection of `continuity` in their own projects; when adopting that module, decide whether your project's records should be version-controlled.
