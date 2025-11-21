# AGENT 指南 – InfoHarbor 个人认知负熵系统

本文件用于指导 AI Coding Agent（如 Codex）在本项目中的行为、优先级和约束。

---

## 1. 项目本质与优先级

**InfoHarbor 的本质：不是“资讯聚合器”，而是“个人认知负熵机器 / Cognitive OS”。**

- 核心目标：
  - 降低认知负荷，减少注意力发散；
  - 成倍提高信息→认知→行动的效率；
  - 持续帮助用户迭代认知模型，抽取更本质的规律与方法论；
  - 提供道-法-术-器多层视角与工具；
  - 自动化交易/行动只是众多“术/器层”输出之一。

**在实现任何功能时，请始终优先考虑：**

> 这个改动是否有助于减少信息熵、提升认知质量、强化 IPO 循环和道法术器层级，而不仅仅是“多一个功能”。

---

## 2. 文档与规范优先级

在本仓库中工作时：

1. 首先阅读并遵循：`docs/PRD.md`  
2. 然后参考（如存在）：  
   - `docs/ARCHITECTURE.md`  
   - `docs/API.md`  
3. 再查看具体代码实现。

如果文档与现有代码冲突：

- 以最新文档为准；
- 更新文档后再调整代码，保持二者一致。

---

## 3. 技术栈约定

除非文档另有说明，默认技术栈为：

- **后端**
  - Python 3.11+
  - FastAPI（REST API）
  - PostgreSQL
  - 可选 Redis / 队列（用于采集与处理任务）

- **前端**
  - Next.js (React + TypeScript)
  - Tailwind CSS（深色 / 极客风主题）

- **基础设施**
  - Docker / docker-compose
  - 简单脚本/Makefile 支持一键启动与测试

如需要改动技术栈或引入新基础设施，请先在 `docs/PRD.md` 或新增设计文档中说明理由。

---

## 4. 目录结构建议

在初始化或扩展项目时，优先采用以下结构：

```text
.
├── AGENTS.md
├── docs/
│   ├── PRD.md
│   ├── ARCHITECTURE.md        # 可由你创建/更新
│   └── API.md                  # 按需创建
├── backend/
│   ├── app/
│   │   ├── main.py             # FastAPI 入口
│   │   ├── api/                # 路由
│   │   ├── models/             # ORM 模型
│   │   ├── schemas/            # Pydantic 模型
│   │   ├── services/           # 领域逻辑 (sources, processing, cards...)
│   │   └── core/               # 配置、依赖注入
│   ├── tests/
│   └── alembic/                # DB 迁移（如使用）
├── frontend/
│   ├── app/
│   ├── components/
│   ├── lib/
│   └── tests/
└── infra/
    ├── docker-compose.yml
    ├── Dockerfile.backend
    ├── Dockerfile.frontend
    └── scripts/
        ├── dev_env.sh
        ├── run_backend.sh
        ├── run_frontend.sh
        └── run_tests.sh
