# 数据结构说明 / Schema

本仓库当前以 `data/models.json` 为主数据源，同时同步导出 `data/models.csv` 供表格和脚本使用。

## 字段总览 / Field overview

| 字段 / Field | 类型 / Type | 必填 / Required | 说明 / Notes |
| --- | --- | --- | --- |
| `id` | string | yes | 全局唯一标识，推荐 kebab-case |
| `name` | string | yes | 条目显示名 |
| `source_owner` | string | yes | 发布者或组织名 |
| `source_repo_or_model` | string | yes | Hugging Face model id 或 GitHub repo path |
| `platform` | string | yes | `GitHub` / `Hugging Face` / `Other` |
| `robot_brand` | string | yes | 机器人品牌，如 `Unitree` |
| `robot_model` | string | yes | 原始机型描述 |
| `robot_model_normalized` | string | yes | 规范化机型名，例如 `unitree_g1` |
| `dof_or_variant` | string | no | DOF 或机型变体说明 |
| `category_level_1` | string | yes | 一级分类 |
| `category_level_2` | string | no | 二级分类 |
| `action_style` | string | yes | 主要动作风格 |
| `download_type` | string | yes | 下载入口类型 |
| `download_url` | string | yes | 主要下载或入口链接 |
| `homepage_url` | string | no | 首页或补充说明页 |
| `requires_login` | boolean | yes | 是否需要登录 |
| `requires_accept_terms` | boolean | yes | 是否需要同意条款 |
| `has_direct_weights` | boolean | yes | 是否明确有权重文件 |
| `weight_format` | string | no | 权重格式，如 `onnx` |
| `is_official` | boolean | yes | 是否为官方或机构官方发布 |
| `deployment_readiness` | string | yes | 部署就绪度 |
| `short_description_zh` | string | yes | 中文短描述 |
| `short_description_en` | string | yes | 英文短描述 |
| `notes` | string | no | 补充备注 |
| `license_note` | string | yes | 许可说明 |
| `risk_note` | string | yes | 风险说明 |
| `last_checked_note` | string | yes | 最近一次检查备注 |
| `source_confidence` | string | yes | 信息可信度，如 `high` / `medium` / `low` |

## 一级分类建议 / Suggested values for category_level_1

- `showcase`
- `motion_imitation`
- `locomotion`
- `manipulation`
- `generative_motion`
- `task_policy`
- `foundation_motion`

## 动作风格建议 / Suggested values for action_style

- `greeting`
- `dance`
- `fight`
- `karate`
- `full_body_tracking`
- `walk`
- `run`
- `box_move`
- `pick_place`
- `table_tennis`
- `multiskill`

## 下载方式建议 / Suggested values for download_type

- `direct_file`
- `model_page`
- `repo_entry`
- `gated`

## 部署就绪度建议 / Suggested values for deployment_readiness

- `index_only`
- `research_repro`
- `sim_ready`
- `real_robot_possible`
- `demo_friendly`

## 设计原则 / Design principles

1. 先保证“可判断”，再追求“字段多”
2. 对不确定项明确标注，而不是猜测
3. 保持中英文兼容，中文优先服务真实用户
4. 不把数据集伪装成模型
5. 不把 repo 入口伪装成直链权重

