# 紫微斗数 AI 命盘推理系统 · `ziwei-insight`

> 输入生辰 → 确定性排盘 → 规则引擎判格局 → RAG 检索命理知识 → DeepSeek 流式推理 → React 动画呈现。
> 支持手相照片上传与命盘互证，历史记录本地持久化。

当前状态：**规划阶段**（仅文档与脚手架，尚未开始功能编码）。

仓库：<https://github.com/jizhanpeng/ziwei-insight>

## 文档索引

| 文档 | 内容 |
|---|---|
| [01-项目计划书](docs/01-项目计划书.md) | 目标、参考仓库分析、技术选型、架构、模块设计、里程碑、风险、验收 |
| [02-工作记录](docs/02-工作记录.md) | 按时间记录进展、决策、产出、下一步；含 ADR |
| [03-错误记录](docs/03-错误记录.md) | 真实错误与预判问题的现象、根因、修复、防复发 |
| [04-测试文档](docs/04-测试文档.md) | 测试分层、黄金命盘、API/SSE、RAG/LLM/手相评测、E2E、性能、安全、CI |

## 技术栈（规划）

- **后端**：Python 3.11 · FastAPI · Pydantic v2 · Uvicorn
- **排盘**：`iztro-py` + 自研时间校正/规则引擎
- **LLM**：LangChain 1.x · LangGraph 1.x · DeepSeek `deepseek-reasoner` + `deepseek-chat`
- **RAG**：Chroma 本地持久化 · 硅基流动 BGE-M3 · BM25 · RRF · rerank
- **手相**：Qwen-VL（DashScope）抽取掌纹特征 + 用户手动修正
- **数据**：SQLite · SQLAlchemy 2.0 · Alembic
- **前端**：React 19 · Vite · TypeScript · Tailwind CSS · Framer Motion
- **测试**：pytest · httpx · Playwright · RAGAS · pytest-benchmark
- **运行**：本机启动，无需 Docker、无需部署

## 参考仓库

- [Renhuai123/ziwei-doushu](https://github.com/Renhuai123/ziwei-doushu) —— 排盘严谨性、真太阳时、四化、格局规则
- [learnwithu/mingli-master](https://github.com/learnwithu/mingli-master) —— `iztro-py` 排盘、格局量化、解读流程、参考语料

> `_refs/` 为本地参考代码，不纳入版本控制。

## 环境要求

| 项 | 要求 | 本机现状 |
|---|---|---|
| Python | ≥ 3.11 | 3.9.13（需新建 conda 环境） |
| Node | ≥ 20 | 18.19.0（需升级） |
| Docker | 不需要 | 未安装 |
| 网络 | VPN（GitHub / PyPI / DeepSeek / 硅基流动 / DashScope） | 已开启 |

## API Key

| 用途 | 变量 |
|---|---|
| DeepSeek 推理/成文 | `DEEPSEEK_API_KEY` |
| Embedding / Rerank（可选） | `SILICONFLOW_API_KEY` |
| 手相视觉模型 | `DASHSCOPE_API_KEY` |

```bash
cp .env.example .env
# 填入 key 后
conda create -n ziwei python=3.11 -y
conda activate ziwei
pip install -r backend/requirements.txt   # 待 M1 创建
python scripts/dev.py                     # 待 M2 创建
```

## 许可与声明

代码计划采用 MIT 许可（待确认）。本项目用于传统文化研究与技术演示，不构成医疗、法律、投资、婚恋决策依据。参考仓库代码遵循各自许可；古籍为公版；非商用授权内容默认不入库。手相照片仅在本机存储，调用视觉模型前会明确告知并征得同意。
