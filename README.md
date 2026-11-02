# Lab Agent 智能实验室预约管理系统

这是一个集成了“实验室管理 + 预约审批 + AI 智能问答”的全栈项目，适用于学校/机构/企业内部实验室资源的统一管理。

项目包含两部分：

- Backend：基于 FastAPI 的 REST API 服务
- Frontend：基于 Vue 3 + Vite 的管理端界面

## 项目概览

该系统支持以下核心能力：

- 用户注册 / 登录 / 个人资料管理 / 修改密码
- 实验室信息管理（新增、编辑、删除、查询）
- 设备信息管理（按实验室维度查询与维护）
- 实验室预约申请、取消、审核与状态管理
- 管理员审批预约，控制实验室/设备的使用权限
- AI 助手对话：回答实验室规则、开放时间、设备信息等问题
- 基于知识库的智能检索：读取 `backend/data/kb` 中的文档资料
- 文件上传与资源访问（例如图片、文档等）

## 技术栈

### 后端

- Python
- FastAPI
- SQLAlchemy
- Pydantic
- PyMySQL
- JWT（认证）
- ChromaDB（向量知识库）
- LangGraph / OpenAI SDK（AI 对话代理）

### 前端

- Vue 3
- Vite
- Element Plus
- Vue Router
- Axios

## 项目结构

```text
lab_agent/
├── backend/
│   ├── app/
│   │   ├── api/                 # API 路由
│   │   ├── common/              # 通用响应、异常处理
│   │   ├── config.py            # 配置项加载
│   │   ├── database.py          # 数据库连接
│   │   ├── dependencies/        # 认证依赖
│   │   ├── models/              # 数据模型
│   │   ├── schemas/             # 请求/响应结构体
│   │   ├── services/            # 业务逻辑
│   │   └── utils/               # 工具函数
│   ├── data/
│   │   ├── kb/                  # 实验室知识库文档
│   │   └── chroma/              # 向量数据库
│   ├── uploads/                 # 上传文件目录
│   ├── .env.example             # 环境变量模板
│   ├── requirements.txt         # Python 依赖
│   └── app/main.py              # FastAPI 启动入口
├── frontend/
│   ├── src/                     # Vue 代码
│   ├── package.json             # 前端依赖与脚本
│   ├── vite.config.js          # Vite 配置
│   └── README.md               # 前端说明
├── package.json                 # 根目录依赖
├── .gitignore
└── README.md                    # 项目说明
```

## 关键功能说明

### 1. 认证与权限

后端采用 JWT 认证机制，存在不同角色：

- 普通用户：可登录、预约、查看个人预约记录
- 管理员：可审核预约、维护实验室/设备数据

### 2. 实验室与设备管理

管理员可在后台维护以下资源：

- 实验室名称、位置、容量、开放时间、关闭时间
- 实验室设备、型号、数量、状态等信息

### 3. 预约流程

用户可提交预约申请，系统会记录：

- 预约人
- 预约实验室或设备
- 日期与时间段
- 备注信息
- 审核状态

预约状态包括：

- 待审核
- 已通过
- 已拒绝
- 已取消

### 4. AI 智能助手

AI 模块支持：

- 解释实验室预约规则
- 查询开放时间与安全规范
- 提供实验室/设备查询信息
- 根据用户请求辅助预约流程

知识库文件位于：

- `backend/data/kb/安全规范.md`
- `backend/data/kb/开放时间.md`
- `backend/data/kb/设备使用.md`
- `backend/data/kb/预约规则.md`

这些文件会被加载进 ChromaDB 向量库，用于语义检索和 AI 回答增强。

## 环境准备

### 1. Python 环境

建议使用 Python 3.10+。

### 2. Node.js 环境

前端依赖需要 Node.js 22 或更高版本（项目中已声明）。

## 快速开始

### 1. 安装后端依赖

```bash
cd backend
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. 配置环境变量

复制模板文件：

```bash
cp .env.example .env
```

编辑 `backend/.env`，至少填写：

```env
DATABASE_URL=mysql+pymysql://用户名:密码@主机:端口/数据库名
JWT_SECRET_KEY=your-secret-key
JWT_EXPIRE_HOURS=24
JWT_ALGORITHM=HS256
LLM_API_KEY=your-llm-key
LLM_BASE_URL=https://api.provider.example.com/v1
LLM_MODEL=your-model-name
```

说明：

- `DATABASE_URL` 需要指向可用的数据库实例（通常为 MySQL / MariaDB）
- `LLM_API_KEY`、`LLM_BASE_URL`、`LLM_MODEL` 用于 AI 助手功能

### 3. 启动后端

```bash
cd backend
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

后端 API 文档地址：

- Swagger UI: `http://localhost:8000/docs`
- Redoc: `http://localhost:8000/redoc`

### 4. 启动前端

```bash
cd frontend
npm install
npm run dev
```

默认前端地址：

- `http://localhost:5173`

## 默认访问方式

启动完成后，可通过浏览器访问前端页面完成：

- 登录 / 注册
- 实验室列表查看
- 预约申请
- 管理员审批
- AI 智能问答

## 备注

- 上传文件保存在 `backend/uploads/`
- 知识库文档位于 `backend/data/kb/`
- 向量库数据位于 `backend/data/chroma/`
- 启动应用时，后端会自动创建数据库表结构（基于 SQLAlchemy 模型）

## 可能的后续优化方向

- 增加权限分组与更细粒度的角色控制
- 引入 Redis 提升缓存和会话性能
- 增加预约冲突检测与自动提醒
- 提升 AI 助手的工具调用稳定性与多轮上下文能力
- 做更多统计分析报表（预约趋势、设备使用率等）

## 许可证

本项目未声明明确许可证，默认仅供学习、开发和内部使用。

## 贡献说明

如需扩展功能或修复问题，可在本地分支中提交修改，并结合项目中的 FastAPI 与 Vue 前端结构进行迭代开发。
