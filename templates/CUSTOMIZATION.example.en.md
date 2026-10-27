# Customization template

Fill in the fields you need. Remove unnecessary fields and merge confirmed content suitable for public release into the project's AGENTS.md. Keep personal or sensitive settings in the current conversation or a local file that has been explicitly loaded.

This is an ordinary Markdown template. It does not automatically load content, interpolate values, or grant permissions. Do not infer missing background information or treat unfilled budget and permission fields as approved. Example values and placeholders do not constitute authorization.

## Personal and communication preferences

| Field | Value or default handling |
| --- | --- |
| Identity or professional background | Not filled in; optional, provide only when it affects explanation depth |
| Research or project area | Not filled in; use the current project context rather than assuming a fixed discipline |
| Response language | Follow the user's current request by default |
| Explanation depth | Adapt to task complexity by default and include the information needed to assess conclusions |
| Output format | Use clear paragraphs and necessary lists or tables unless otherwise specified |
| Paper style and submission requirements | Not filled in; provide the target requirements or a verifiable source if they should apply |

## Project configuration

| Field | Value or default handling |
| --- | --- |
| Project objective and scope | To be filled in; do not infer task objectives from the template |
| Modules actually selected | Select modules and copy their content, not just their names |
| Build, test, and verification commands | Use actual project files or confirmed procedures; do not guess runnable commands |
| Resource constraints and run counts | Not filled in; confirm first when they affect costs or experimental conditions |
| Status-record policy | Omitting continuity adds none of its record requirements; if selected, follow its trigger conditions |
| Status-record path | STATUS.md in the project root by default, or specify an existing equivalent record |
| Handoff-record path | HANDOFF.md in the project root by default, or specify an existing equivalent record |
| Experiment-record and artifact locations | Follow existing project conventions; otherwise determine them within the task's authorization |
| Actions requiring individual approval | To be filled in; leaving this blank does not remove the approval boundaries in execution |
| Explicitly prohibited actions | To be filled in; existing prohibitions remain in force |

## Valid preauthorization records

Complete a separate record for each preauthorization and have the user explicitly confirm that it is active. An agent may record authorization actually received, but cannot authorize actions on the user's behalf, expand its scope, or invent approval that was never given.

| Field | Value |
| --- | --- |
| Objective and specific targets | Not filled in |
| Permitted operation types | Not filled in |
| Scope and exclusions | Not filled in |
| Budget, currency, and resource quotas | Not filled in; this does not mean unlimited |
| Maximum run count or other quantity limits | Not filled in |
| Validity period or expiration conditions | Not filled in |
| Whether each action needs approval | Not filled in; follow existing user-defined checkpoints |
| Source of explicit approval | Not filled in; record only the actual approving message or document |

Until confirmation is complete, the table is only a record awaiting completion. Do not substitute AUTO_PROCEED, a broad "allow everything," or silence for specific authorization. Do not store passwords, tokens, or other credentials here.

## Checks before merging

- Include personal background only when the task needs it; keep the public version suitable for public release.
- Resolve conflicts with existing project rules explicitly rather than concealing them through override order.
- Preserve core evidence requirements, accurate status reporting, and authorization boundaries; adjust only applicability and actual parameters.
- If a module is not used, remove configuration expectations that depend on it. Do not assume other files will be read automatically.
