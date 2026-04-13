# 标签规则 / Tagging rules

## 总原则 / Core rules

标签的目的不是炫技，而是让用户快速判断：

- 这是干什么的
- 适配谁
- 能不能下
- 离真机有多远

## 机型归一化 / Robot model normalization

推荐这些常见写法：

- `Unitree G1` -> `unitree_g1`
- `Unitree H1` -> `unitree_h1`
- `Unitree Go2` -> `unitree_go2`
- 未明确到单型号时，可写：
  - `unitree_humanoid_family`
  - `multi_brand_humanoid`

## 一级分类规则 / category_level_1 rules

### `showcase`

适合迎宾、跳舞、武术、高吸睛动作演示。

### `motion_imitation`

主要价值在于跟踪 mocap、reference motion 或通用动作模仿。

### `locomotion`

以走路、速度控制、基础移动控制为主。

### `manipulation`

抓取、搬运、桌面任务、双臂操作等。

### `task_policy`

面向一个明确任务的策略，如 pick-place。

### `generative_motion`

更偏生成、采样、文本或约束驱动的动作生成。

### `foundation_motion`

更像通用底座、planner、decoder、motion controller 组件。

## `action_style` 选择规则

- `dance`：主要用于舞蹈、节奏展示
- `fight`：搏击、对打、攻击姿态
- `karate`：偏武术、套路、空手道
- `full_body_tracking`：跟踪整身动作
- `walk`：走路、基础 locomotion
- `pick_place`：抓取和放置
- `multiskill`：一个资源覆盖多个动作风格

如果一个资源兼顾多个风格，优先选择最能代表用户使用场景的主风格，并在 `notes` 中补充其他风格。

## 下载方式判定规则 / Download type rules

### `direct_file`

只有当页面明确提供可直接请求的模型文件链接时使用。

### `model_page`

用于 Hugging Face 模型页、项目页等入口页；如果文件是否公开不稳定，也优先用这个。

### `repo_entry`

代码仓库入口。适用于仓库里可能有脚本、说明、导出方式，但并不保证直接附带权重。

### `gated`

需要登录、申请、同意使用条款后才能下载。

## 风险说明写法建议 / Risk note style

尽量写成真正帮用户避坑的话，例如：

- 需要 DOF 对齐和控制频率对齐
- 更像模型页入口，权重存在性需二次确认
- 更适合仿真复现，真机仍需部署链路适配
- 对商演效果友好，但不代表真机即插即用

