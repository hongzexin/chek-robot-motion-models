# CHEK Robot Motion Models

中文主版 | Chinese-first with English support

> A community-driven index of robot motion, control, imitation, locomotion, and manipulation models across brands.

[社区入口 / Community Entry](https://app-dev.chekkk.com)

## 项目简介 / What this repo is

这是一个面向机器人玩家、机器人演示团队、展会互动团队、商演从业者的开源索引仓库。

它的目标不是上传一堆第三方模型权重，而是把分散在 GitHub、Hugging Face 和其他公开页面里的机器人动作模型、控制模型、动作模仿底座、locomotion 策略、manipulation 任务模型整理成一个持续可维护的资料库。

This repository is an index, not a mirror of third-party checkpoints. We focus on discoverability, tagging, comparability, and community contribution.

当前已开始覆盖的品牌和平台包括：

- Unitree
- OpenLoong
- Booster Robotics
- ANYbotics / ANYmal ecosystem
- AgiBot
- AgileX
- Franka
- Multi-brand foundation model routes

## 为什么做这个仓库 / Why this repo exists

最近公开网上关于机器人动作模型的内容越来越多，但真正对人有帮助的索引并不多。

常见的问题很真实：

- 视频很多，但能下的入口很少
- 标题写得像“已经开源”，点进去却只有论文或演示视频
- 有些资源是单动作策略，有些其实只是 locomotion 底模
- 有些页面能看不能下，有些需要登录或同意条款
- 很多模型看起来很热闹，但离真机部署还差 DOF 对齐、控制频率、观测定义、sim2real 和部署框架

这个仓库就是想把这些信息讲人话，帮大家少走弯路。

## 这个仓库适合谁 / Who this repo is for

### 1. 机器人玩家 / Robot builders and hobbyists

你更关心：

- 哪个模型是真权重
- 哪个资源更适合先跑起来
- 哪个适配 G1、H1、Go2
- 哪个只是模型页入口
- 哪个适合做动作模仿底座

### 2. 机器人表演和商演团队 / Performance, exhibition, and demo operators

你更关心：

- 哪个动作适合迎宾、引流、展会互动
- 哪个适合跳舞、短视频传播、武术展示
- 哪个更容易做出演示效果
- 哪个资源更像“能快速试”的 demo 方案

## 快速开始 / Quick start

1. 先看 [Top 推荐模型](#top-推荐模型--top-picks)
2. 再看 [按业务场景筛选](#按业务场景筛选--filter-by-business-scenario)
3. 如果你想批量处理，直接用：
   - [`data/models.json`](./data/models.json)
   - [`data/models.csv`](./data/models.csv)
4. 如果你准备贡献新条目，先读：
   - [`docs/schema.md`](./docs/schema.md)
   - [`docs/tagging-rules.md`](./docs/tagging-rules.md)
   - [`CONTRIBUTING.md`](./CONTRIBUTING.md)

## 资源分类说明 / Resource taxonomy

本仓库会明确区分这些类型，避免“都叫模型，其实不是一类东西”的混乱：

- `showcase`：适合迎宾、跳舞、武术、展示类动作
- `motion_imitation`：动作模仿、全身跟踪、reference tracking
- `locomotion`：走路、速度控制、基础运动控制
- `manipulation`：抓取、操作、任务执行
- `task_policy`：面向特定任务的策略模型
- `generative_motion`：生成式动作模型
- `foundation_motion`：更像底座、planner、通用控制器

下载方式也会区分：

- `direct_file`：公开直链可下
- `model_page`：模型页入口，通常需要自己去 Files 页面确认
- `repo_entry`：仓库入口，需要顺着 README 找权重或导出方式
- `gated`：需要登录或同意条款

## Top 推荐模型 / Top picks

| 场景 / Use case | 机器人 / Robot | 资源 / Resource | 下载方式 / Access | 为什么值得先看 / Why it matters |
| --- | --- | --- | --- | --- |
| 展示动作包 | Unitree G1 | `exptech/g1-moves` | gated | 已知最接近“动作包合集”的公开入口之一 |
| 单动作演示 | Unitree G1 | `mujocolab/g1_spinkick_example` | direct_file | 旋踢示例清晰，适合先跑通下载到部署链路 |
| 动作模仿底座 | Unitree G1 / H1 | `HoloMotion v1.2 - motion tracking` | direct_file | 适合做参考动作追踪 |
| 多动作 tracker | Unitree G1 | `OpenTrack general_tracker_lafan_v1` | repo_entry | cartwheel / kungfu / getup 等都可覆盖 |
| 官方部署起点 | Unitree Go2 / G1 / H1 | `unitree_rl_gym` | repo_entry | 适合先打通官方 RL 和部署环境 |
| 操作类任务 | Unitree G1 | `GR00T-N1.6-G1-PnPAppleToPlate` | model_page | 更适合展示“机器人真的在做事” |
| 整身控制底座 | OpenLoong Qinglong | `OpenLoong-Dyn-Control` | repo_entry | 适合看真实控制软件栈，而不只是动作片段 |
| 官方 locomotion 框架 | Booster T1 / K1 | `booster_gym` | repo_entry | 适合做非 Unitree 人形 locomotion 路线探索 |
| 开放操作模型 | Franka | `MolmoAct-7B-D-0812` | model_page | 适合作为机械臂 manipulation / VLA 入口 |
| 跨本体基础模型 | AgileX / R1-Lite / Franka | `RoboBrain-X0-Preview` | model_page | 适合看多品牌、多本体基础模型路线 |

## 按品牌或机器人型号筛选 / Filter by brand or robot model

| 型号 / Model | 先看这些 / Start here |
| --- | --- |
| G1 | `exptech/g1-moves` · `mujocolab/g1_spinkick_example` · `OpenTrack` · `PathOn-AI/g1-imitate-isaaclab-amp` · `unitree-g1-phase1-locomotion` |
| H1 | `HoloMotion v1.2` |
| Go2 | `unitree_rl_gym` · `diasAiMaster/unitree-go2-velocity-flat` |
| OpenLoong Qinglong | `OpenLoong-Dyn-Control` · `OpenLoong-Gymloong` |
| Booster T1 / K1 | `booster_gym` · `robocup_demo` |
| ANYmal | `legged_gym` |
| AgiBot GO-1 | `agibot-world/GO-1` |
| AgileX manipulation platforms | `lerobot/xvla-agibot-world` · `RoboBrain-X0-Preview` |
| Franka | `MolmoAct-7B-D-0812` · `RoboBrain-X0-Preview` |

## 品牌覆盖速览 / Brand coverage snapshot

| 品牌 / Brand | 代表条目 / Representative entries | 主要方向 / Main direction |
| --- | --- | --- |
| Unitree | `exptech/g1-moves` · `unitree_rl_gym` · `GR00T-N1.6-G1-PnPAppleToPlate` | showcase / locomotion / manipulation |
| OpenLoong | `OpenLoong-Dyn-Control` · `OpenLoong-Gymloong` | whole-body control / locomotion |
| Booster Robotics | `booster_gym` · `robocup_demo` | locomotion / task demo |
| ANYbotics | `legged_gym` | legged locomotion |
| AgiBot | `agibot-world/GO-1` | foundation model |
| AgileX | `lerobot/xvla-agibot-world` | manipulation / VLA |
| Franka | `MolmoAct-7B-D-0812` | manipulation / VLA |
| Multi-brand | `RoboBrain-X0-Preview` | cross-embodiment foundation model |

## 按业务场景筛选 / Filter by business scenario

| 业务场景 / Scenario | 建议先看 / Recommended starting points |
| --- | --- |
| 迎宾 / 展会引流 | `exptech/g1-moves` · `rsamf/g1-dance` · `rsamf/g1-walk` |
| 跳舞 / 短视频传播 | `exptech/g1-moves` · `fan-ziqi/rl_sar` 的 `dance_102` / `gangnam_style` / `charleston` |
| 武术 / 高动态展示 | `rsamf/g1-fight` · `mujocolab/g1_spinkick_example` · `OpenTrack` |
| 先跑通链路 | `unitree_rl_gym` · `hardware-pathon-ai/unitree-g1-phase1-locomotion` |
| 操作类展示 | `nvidia/GR00T-N1.6-G1-PnPAppleToPlate` · `cloudwalk-research/GR00T-N1.6-G1-PnPAppleToPlate` · `cagataydev/groot-n1.6-unitree-g1-pick-basket` |

## 下载方式说明 / Download access notes

| 类型 / Type | 含义 / Meaning | 常见情况 / Typical situation |
| --- | --- | --- |
| `direct_file` | 公开可直接下载文件 | 常见于 `.onnx` 直链 |
| `model_page` | 有模型页，但文件需要进一步确认 | Hugging Face model card 常见 |
| `repo_entry` | 只有代码仓库入口 | 需要顺着 README 找权重或导出指令 |
| `gated` | 需要登录或同意条款 | Hugging Face gated dataset 常见 |

## 风险与免责声明 / Risk and disclaimer

- 能下载，不等于能一键上真机
- 本仓库不默认镜像第三方模型权重
- 真机可用性通常还取决于：
  - 关节定义和 DOF 对齐
  - 控制频率
  - 观测和 action space 定义
  - 仿真环境与 sim2real 参数
  - 实际部署框架（Isaac Lab、MuJoCo、自研 real deploy 等）
- 请始终遵循上游资源的 license、usage terms、gated terms 和 robot safety requirements

## 数据结构说明 / Data structure

本仓库当前提供两个核心数据文件：

- [`data/models.json`](./data/models.json)：更适合作为主数据源
- [`data/models.csv`](./data/models.csv)：适合表格查看、导入 BI 或筛选

字段说明见：

- [`docs/schema.md`](./docs/schema.md)
- [`docs/tagging-rules.md`](./docs/tagging-rules.md)
- [`docs/license-and-risk-notes.md`](./docs/license-and-risk-notes.md)

## 如何贡献 / How to contribute

欢迎提交这些类型的贡献：

- 新的模型入口或下载页
- 已失效链接的修复
- 适配机型、DOF、部署条件补充
- 动作风格和业务场景标签修正
- 对“看起来像开源但其实没有权重”的纠错说明

提交前建议：

1. 先看 [`CONTRIBUTING.md`](./CONTRIBUTING.md)
2. 尽量补齐 `download_type`、`deployment_readiness` 和 `risk_note`
3. 不要把未授权的第三方权重直接传到这个仓库

## Roadmap

- [x] 建立首版模型索引
- [x] 建立统一 schema、标签规则和贡献流程
- [x] 增加更多非 Unitree 品牌条目
- [ ] 增加“数据集 vs 模型 vs 演示页”的单独字段
- [ ] 增加自动化链接巡检
- [ ] 增加 demo-friendliness 和商演适配度的社区评分
- [ ] 增加按品牌和按场景的网页化筛选页

## 致谢与来源说明 / Credits and sources

本仓库的第一版条目来源于公开模型页、公开仓库页和手工整理的机器人动作模型清单。我们感谢所有开源发布者、研究团队和社区维护者。

如果你有更多条目、修正或部署经验，欢迎通过 PR 和 Issue 一起补全。

最后，如果你希望把这些模型线索进一步转成社区讨论、搭子帖子、需求撮合或合作入口，欢迎进入：

[app-dev.chekkk.com](https://app-dev.chekkk.com)
