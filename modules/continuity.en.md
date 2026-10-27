## Task continuity and handoff

This section applies only when writing records is allowed and any of the following is true: the task involves multiple implementation stages, experiments requiring sustained work, a long-running process, possible interruption and resumption, continuation by another agent or in another session, or substantial handoff costs. Do not create or update record files for local changes completed in a single turn, read-only reviews, pure Q&A, or tasks where the user explicitly prohibits file writes.

Prefer project-designated locations and existing status files. If the project specifies none, maintain `STATUS.md` and `HANDOFF.md` in the project root by default. Do not duplicate them in subdirectories or create equivalent files merely to standardize the format.

- `STATUS.md`: Record the objective, scope, acceptance criteria, completed and ongoing work, blockers, actual test and verification results, unverified items, key commands, logs or outputs, paths to evidence and artifacts, and important results.
- `HANDOFF.md`: Record current conclusions, unresolved issues, recommended next steps, and a starting prompt that the next agent can use directly. Refer to the status file or original records for detailed evidence and configuration rather than copying them.

`HANDOFF.md` is especially useful when alternating between official services and third-party API relay services while continuing the same task. When this section's trigger conditions apply, update changed handoff information before switching. In the new session, read the handoff record and the status and project files it references, then check the current code, artifacts, and verification status before continuing. The target agent must have access to these files. Handoff records do not automatically synchronize chat history, service configuration, or permissions, and do not authorize disclosure of sensitive content to another service.

Update these files only when objectives, significant progress or results, blockers, or handoff status actually change. Update existing files with these names; do not overwrite or remove unrelated content. When agents work in parallel, the lead agent consolidates status updates to avoid overwriting one another's work.

Record status based on actual evidence; do not present plans as completed work. Explicitly mark unknown fields as unknown, and do not guess conditions or results. Keep records concise, verifiable, and actionable for continuation. Prioritize accurate evidence locations and instructions for reproduction; follow the project's research-record requirements for detailed experimental fields.
