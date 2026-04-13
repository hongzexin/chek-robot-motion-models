# Contributing to CHEK Robot Motion Models

中文为主，英文补充。Chinese-first, English-friendly.

感谢你帮助这个仓库变得更有用。这个项目的重点不是“堆很多链接”，而是把机器人动作模型资料整理成真正可筛选、可判断、可维护的索引。

## 你可以贡献什么 / What to contribute

- 新模型条目
- 失效链接修复
- 机型适配信息
- DOF、变体、控制频率等部署提示
- 对下载方式的更正
- 对业务场景标签的补充
- 风险说明和 license 说明

## 提交前的基本原则 / Ground rules

1. 不要上传未明确授权的第三方模型权重
2. 优先提交“索引信息”和“下载入口”
3. 对不确定的内容请明确标注，而不是猜测
4. 区分模型、数据集、代码仓库入口和演示页
5. 如果某个资源只能看不能下，也有价值，但要说明清楚

## 新条目最少应包含 / Minimum fields for a new entry

- `id`
- `name`
- `platform`
- `robot_brand`
- `robot_model`
- `category_level_1`
- `action_style`
- `download_type`
- `download_url`
- `deployment_readiness`
- `short_description_zh`
- `license_note`
- `risk_note`

## 推荐提交流程 / Suggested workflow

1. 先阅读 [`docs/schema.md`](./docs/schema.md)
2. 再阅读 [`docs/tagging-rules.md`](./docs/tagging-rules.md)
3. 同时更新：
   - [`data/models.json`](./data/models.json)
   - [`data/models.csv`](./data/models.csv)
4. 运行：

```bash
python3 scripts/validate_links.py
```

如果你想额外检查远程链接：

```bash
python3 scripts/validate_links.py --check-http
```

## PR 建议写法 / Suggested PR description

- 这个条目是什么
- 为什么值得收录
- 下载入口是什么类型
- 适配什么机型
- 是否有真机部署风险
- 哪些信息是确认的
- 哪些信息仍需二次核验

## 社区入口 / Community entry

如果你不只是想提 PR，也想发讨论、收需求、找搭子或交流部署经验，欢迎进入：

[app-dev.chekkk.com](https://app-dev.chekkk.com)

