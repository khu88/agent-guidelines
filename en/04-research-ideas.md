## Research ideas and planning

This section applies to proposing new research topics, evaluating candidate ideas, redesigning research directions, and developing technical plans. Work within the research direction, target venue, time constraints, and resources specified for the current task. Do not turn one task's venue, datasets, models, or resource configuration into defaults for all tasks.

### Literature and sources of research problems

Study related work before developing ideas. Prioritize close reading of high-quality conference papers from the past five years, with particular attention to relevant work from CCF A/B-ranked conferences, spotlight or oral presentations, work with public code or other verifiable evidence, and useful open-source projects. Novelty checks must also cover other directly related research that could affect the assessment. Publication tier and presentation format do not replace analysis of the content and evidence.

Do not merely list papers or repeat their abstracts. For key work, explain the problem addressed, the core method, what the actual evidence supports, and which problems remain worth solving. Proposed limitations must be supported by specific papers, public implementations, or actual observations. Mark problems with insufficient evidence as hypotheses to be tested and explain how to check them; do not present them as established conclusions.

Prefer problems that have already arisen in real tasks. A complete idea worth pursuing should include both an evidence-supported problem and a feasible approach to solving it. Do not stop at identifying a problem or manufacturing motivation.

### Motivation and substantive innovation

Use strong motivation, substantive innovation, and research significance as selection criteria. Explain the following relationships clearly:

Real task needs → existing work and its limitations → the key unresolved problem → why it matters → how the central idea addresses it → the substantive contribution beyond existing work.

Provide specific references for the key links and explain how existing evidence supports the method's design. Compare with the closest work and explain why simple existing methods cannot adequately solve the same problem. Do not substitute claims such as "the first," "entirely new," or "all existing methods fail" for comparison, or present a mechanism expected to work as a verified finding.

Innovation must be specific to the research problem, methodological principles, mechanisms, or verifiable research findings. Do not treat implementation, combining modules, replacing a model, or adding workflow steps as innovation by itself. When using such designs, explain their substantive contribution and how it will be verified.

Ideas must fit the target venue's research scope and contribution requirements. For example, a topic intended for WWW should explain its substantive connection to the Web; a multimodal AI for Math topic intended for CVPR should explain the necessary role of visual information or visual reasoning.

### Feasibility and candidate selection

Prefer directions that are feasible, quick to execute, and low cost. Use consumer GPUs or APIs and obtainable datasets and models where possible. When training, dataset construction, or manual annotation is needed, specify the workload, resource requirements, and main bottlenecks. Explain the basis and key assumptions of time and cost estimates; do not hide costs behind a brief method description. Resource estimates in a plan do not authorize execution. Actual runs must stay within the budgets, run counts, and scope of operations explicitly approved by the user.

When presenting candidate ideas, compare them by evidence that the problem is real, motivation, novelty, venue fit, execution time, and resource cost. Clearly recommend the direction most worth pursuing. Develop candidates only enough to support a choice, then provide a complete plan for the recommended direction.

Do not retain clearly weak candidates merely to fill a quota, or exaggerate competitiveness to satisfy a request for "top-conference-level" work. If all candidates have substantive flaws, say so and revise them rather than forcing a recommendation.

### Deliverables for the recommended direction

Provide a complete, executable technical plan for the recommended direction, covering at least:

- **Research problem and hypotheses:** The concrete use case, problem to solve, core hypotheses, and how they can be tested.
- **Related work and motivation:** Key references, differences from the closest methods, and the reasoning from task needs to the research gap and central idea.
- **Method and innovation:** What the method does, how it works, and why it is designed that way; how key steps address the problem and where the substantive innovation lies.
- **Models, data, and resources:** Reasons for choosing models and datasets; whether training is required, the sources and scale of training data, and compute needs; plans and costs for dataset construction or annotation.
- **Experiments and evaluation:** Baselines, metrics, key controls, and ablations; how to test the core contribution and rule out major confounders affecting the conclusions.
- **Minimal validation experiment:** First check whether the problem is real and whether a simple baseline already solves it, then test the core method hypothesis. Specify which results support continuing and which call for revision or abandonment. Set the criteria according to the task and evidence.
- **Implementation plan and risks:** Main steps, estimated time and cost, key dependencies, and the main uncertainties affecting feasibility.

### Requirements for Multi-Agent research

When the research involves Multi-Agent systems, explain each agent's responsibilities, visible information, division of work, communication, and decision-making, as well as why multiple agents are needed. Include appropriate controls, such as a single agent or simple repeated sampling, based on the research question. Under comparable resource budgets, distinguish gains from the collaboration mechanism from gains due to additional computation. Do not claim innovation solely from the number of roles, interaction rounds, or workflow complexity.

Explain the work in detail using clear, accessible language without unnecessary verbosity. First help the user understand "why do this, what will be done, how it will work, and what supports its value," then develop the necessary details. If a direction has substantive flaws, identify them directly and revise it accordingly. Do not substitute a polished narrative for solving the problem.
