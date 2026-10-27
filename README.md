# Agent Guidelines

简体中文 | [English](README.en.md)

可选择、可自定义、可合并的 **AGENTS.md 协作规则**，用于 Codex 等支持项目指令的 Agent。按任务选取模块，将正文整合到自己的项目指令中；不预设使用者的身份、学科或工作习惯。

本项目提供中英文独立版本。现有无语言后缀的文件为中文，`.en.md` 为对应英文；两种语言表达相同要求，使用时选择一种即可。模块与示例都是普通 Markdown，不会自动启用或加载其他文件。

## 模块怎么选

| 模块 | 中文 / English | 解决的问题 | 适用场景 |
| --- | --- | --- | --- |
| core | [中文](modules/core.md) / [English](modules/core.en.md) | 前提检查、证据与判断、资料与指令的区分、禁止编造 | 建议所有组合保留，或使用已有等效规则 |
| execution | [中文](modules/execution.md) / [English](modules/execution.en.md) | 自主执行、澄清、授权与隐私、完成与验收 | 调查、检索、修改、运行或交付任务 |
| research | [中文](modules/research.md) / [English](modules/research.en.md) | 相关工作、创新判断、实验设计、复现与结果解释 | 文献分析、科研设计、实验执行 |
| continuity | [中文](modules/continuity.md) / [English](modules/continuity.en.md) | 任务状态、断点恢复、多 Agent 交接 | 多阶段、长时间或需要接续的任务 |
| paper-writing | [中文](modules/paper-writing.md) / [English](modules/paper-writing.en.md) | 贡献叙事、实验论证职责、逐句审校 | 论文撰写、修改与审校 |

模块没有自动导入关系。`core` 提供公共原则，其他模块按需选用；已有等效项目规则时可合并去重。`research` 不强制启用 `continuity`，`paper-writing` 也不要求创建实验或状态文件。不选用某个模块，不会取消已有的用户约束、项目规则或工具权限。

## 推荐组合

| 任务 | 建议选择 |
| --- | --- |
| 一般执行任务 | core + execution |
| 仅在对话中分析用户已提供的文献 | core + research |
| 需要外部检索的文献分析 | core + execution + research |
| 多阶段工程任务 | core + execution + continuity |
| 科研实验 | core + execution + research；需要恢复时加 continuity |
| 仅在对话中起草或审阅论文内容 | core + paper-writing；需要文献或实验分析时加 research |
| 需要修改文件、检索或运行工具的论文任务 | core + execution + paper-writing；按需加 research / continuity |

涉及工具执行、文件修改、外部传输或资源使用时，应加入 `execution`，或确认项目已有等效边界。只读检索仍可能向外部服务发送查询内容。纯对话组合适用于不需要上述操作的任务。

## 使用方法

1. 选择语言及模块，阅读各模块的适用范围。
2. 将所选模块的完整正文合入目标项目的 `AGENTS.md`，或从下表中的完整示例开始。已有 `AGENTS.md` 时，先审阅合并，保留项目自身的构建、测试与目录约定。
3. 使用[中文自定义模板](templates/CUSTOMIZATION.example.md)或[英文模板](templates/CUSTOMIZATION.example.en.md)，填写必要偏好、项目配置和已真实确认的授权。删除不需要的字段。
4. 合并重复项并明确处理冲突。不要依赖拼接顺序来扩大授权或改变研究主张，也不要同时粘贴同一规则的两种语言。
5. 在目标 Agent 中确认实际加载的指令和作用范围，再以真实任务检查行为；未确认加载或未测试的行为应保留为未验证。

| 完整示例 | 中文 | English | 包含的模块 |
| --- | --- | --- | --- |
| 最小执行组合 | [AGENTS.minimal.md](examples/AGENTS.minimal.md) | [AGENTS.minimal.en.md](examples/AGENTS.minimal.en.md) | core + execution |
| 完整科研组合 | [AGENTS.research.md](examples/AGENTS.research.md) | [AGENTS.research.en.md](examples/AGENTS.research.en.md) | 五个模块；仍按各自适用范围触发 |

示例中的模块正文已内联。将所选示例复制并命名为目标项目实际使用的 `AGENTS.md`；这里的示例文件名本身不是自动加载入口。最小组合指模块数量较少，仍保留完整的执行边界。

## 文件格式与 Codex 使用说明

[`AGENTS.md` 格式说明](https://agents.md/)将它定义为普通 Markdown 项目指令文件。本项目沿用 **`AGENTS.md`** 名称；`agent.md` 不是这里的默认入口名。

根据 [Codex 官方说明](https://developers.openai.com/codex/guides/agents-md/)，Codex 会发现全局和项目指令，按目录层级组合；同目录中的 `AGENTS.override.md` 优先于 `AGENTS.md`。其他文件名需按客户端配置，不能仅靠改名或添加 Markdown 链接推定加载成功。组合指令的默认大小上限为 32 KiB，由 `project_doc_max_bytes` 控制；加入其他项目规则后也要检查总大小。上述说明核对于 2026-10-27，实际行为以使用中的客户端及官方文档为准。

本项目不定义模板变量展开或客户端自动导入机制。规则属于行为约定，不能替代工具的权限控制，也不保证模型始终遵循。文档结构检查不等于客户端加载验证或任务效果评测；当前未完成跨客户端行为验证。

## 哪些内容可以自定义

| 配置 | 公共默认 |
| --- | --- |
| 身份、专业程度、研究或项目领域 | 不设定；仅在有用时填写 |
| 回答语言 | 跟随用户当前请求 |
| 篇幅与格式 | 覆盖必要信息，按复杂度调整 |
| 预授权对象、操作、预算、次数、期限 | 不预填授权；以用户明确确认的记录为准 |
| 状态记录 | continuity 为可选模块；选用后仅对符合条件的任务触发 |
| 状态文件名称与位置 | 默认 STATUS.md、HANDOFF.md；可沿用项目已有的两类记录 |
| 论文风格 | 以证据支持的贡献为主线，按目标期刊或会议调整表达 |

`execution` 采用明确授权的默认策略。需要减少重复确认时，可用模板记录用户已经批准的具体操作范围与限额；不得把模板内容当成尚未发生的批准。使用者可以按实际需求调整规则，但文案修改本身不会授予工具权限或构成用户授权。真实性、准确报告验证状态、公平解释证据和不伪造授权，不作为可关闭的风格选项。

个人配置可保存为根目录的 `CUSTOMIZATION.local.md`，或 `CUSTOMIZATION.local.en.md`。这些名称已由 `.gitignore` 排除，但不会因此自动加载；使用时须手动整合或按目标工具配置。不要把凭证、私人身份信息、未公开研究内容或敏感授权写入公开文件。忽略规则不会保护已经纳入 Git 跟踪的文件，发布前仍需检查实际分发内容。

## 双语维护与检查

以 `modules/` 中成对的中英文文件为模块正文来源。修改规则时同步另一语言，保持适用条件、禁止项、授权强度和验收含义一致；一条规则保留一个主要归属，其他模块仅补充场景特有要求。语言分歧应修正，不能靠后粘贴的版本决定含义。

四份示例由 [scripts/sync_examples.py](scripts/sync_examples.py) 同步，避免示例与模块漂移。工具只使用 Python 3 标准库，在已有 Python 3 环境下，从本目录执行：

```sh
python3 scripts/sync_examples.py --check
```

修改模块后，下面的命令会重写四份示例，再检查是否同步：

```sh
python3 scripts/sync_examples.py --write
python3 scripts/sync_examples.py --check
```

这些检查只确认示例与模块一致，不检验翻译质量或 Agent 行为。自定义组合可直接复制需要的模块，无需运行脚本。提交改动前检查双语含义、Markdown 链接以及示例同步。

## 发布状态

当前版本尚未指定许可证，许可证与权利署名待维护者确定。确定许可后，将在根目录添加 `LICENSE` 并同步更新本节；当前版本不声明已采用开源许可证。[GitHub 许可说明](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository)解释了公开仓库与使用、修改、分发许可的区别。

本地维护时可使用根目录 `STATUS.md` 和 `HANDOFF.md` 记录进度与交接。这些文件已加入 `.gitignore`，不属于模板分发材料。该设置不会影响用户在自己的项目中选用 `continuity`；采用该模块时应自行决定项目记录是否纳入版本控制。
