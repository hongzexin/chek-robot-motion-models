# CHEK Robot Motion Models

中文主版 | Chinese-first with English support

> A community-driven index of robot motion, control, imitation, locomotion, and manipulation models across brands.

[社区入口 / Community Entry](https://app-dev.chekkk.com)

## 为什么这次结构会更好用 / Why this structure is better

这个仓库现在改成了“根目录做导航，内容目录按条目展开”的组织方式，参考了 `awesome-design-md` 的优点：

- 根目录 `README.md` 负责总导航
- [`motion-models/`](./motion-models/README.md) 里每个资源一个文件夹，点进去就能看下载入口和风险说明
- [`brands/`](./brands/README.md) 按品牌聚合，方便横向比较
- [`downloads/`](./downloads/README.md) 按下载方式聚合，方便先找直链或 gated 资源
- [`categories/`](./categories/README.md) 按能力路线聚合，方便看 showcase、locomotion、manipulation、foundation motion
- [`data/`](./data/models.json) 继续保留为机器可读数据源

## 快速入口 / Quick entry points

- [全部条目 / All entries](./motion-models/README.md)
- [按品牌浏览 / Browse by brand](./brands/README.md)
- [按下载方式浏览 / Browse by access type](./downloads/README.md)
- [按分类浏览 / Browse by category](./categories/README.md)
- [机器可读数据 / Machine-readable data](./data/models.json)

## 品牌导航 / Brand navigation

- [ANYbotics](./brands/anybotics/README.md) (1 entries)
- [AgiBot](./brands/agibot/README.md) (1 entries)
- [AgileX](./brands/agilex/README.md) (1 entries)
- [Booster Robotics](./brands/booster-robotics/README.md) (2 entries)
- [Franka](./brands/franka/README.md) (1 entries)
- [Multi-brand](./brands/multi-brand/README.md) (2 entries)
- [OpenLoong](./brands/openloong/README.md) (2 entries)
- [Unitree](./brands/unitree/README.md) (19 entries)

## 推荐先看 / Recommended starting points

| 推荐入口 / Recommended | 品牌 / Brand | 分类 / Category | 下载方式 / Access |
| --- | --- | --- | --- |
| [nvidia/GEAR-SONIC - planner](./motion-models/nvidia-gear-sonic-planner/README.md) | Multi-brand | foundation_motion / multiskill | direct_file |
| [HoloMotion v1.2 - motion tracking](./motion-models/holomotion-v1-2-motion-tracking/README.md) | Unitree | motion_imitation / full_body_tracking | direct_file |
| [HoloMotion v1.2 - velocity tracking](./motion-models/holomotion-v1-2-velocity-tracking/README.md) | Unitree | locomotion / walk | direct_file |
| [mujocolab/g1_spinkick_example](./motion-models/mujocolab-g1-spinkick-example/README.md) | Unitree | showcase / fight | direct_file |
| [leggedrobotics/legged_gym](./motion-models/legged-gym-anymal/README.md) | ANYbotics | locomotion / walk | repo_entry |
| [agibot-world/GO-1](./motion-models/agibot-go-1/README.md) | AgiBot | foundation_motion / multiskill | model_page |
| [lerobot/xvla-agibot-world](./motion-models/lerobot-xvla-agibot-world/README.md) | AgileX | manipulation / multiskill | model_page |
| [BoosterRobotics/booster_gym](./motion-models/booster-gym/README.md) | Booster Robotics | locomotion / walk | repo_entry |

## 仓库结构 / Repository layout

```text
.
├── README.md                # 总导航
├── motion-models/           # 每个资源一个文件夹
├── brands/                  # 按品牌聚合
├── downloads/               # 按下载方式聚合
├── categories/              # 按能力路线聚合
├── data/                    # JSON / CSV 数据源
├── docs/                    # schema、标注规则、许可说明
└── scripts/                 # 校验和目录生成脚本
```

## 贡献方式 / Contributing

1. 修改 [`data/models.json`](./data/models.json) 和 [`data/models.csv`](./data/models.csv)
2. 运行：

```bash
python3 scripts/validate_links.py
python3 scripts/generate_catalog.py
```

3. 检查生成的 `motion-models/`、`brands/`、`downloads/`、`categories/`
4. 提交 PR

详细规则见：

- [CONTRIBUTING.md](./CONTRIBUTING.md)
- [Schema](./docs/schema.md)
- [Tagging Rules](./docs/tagging-rules.md)
- [License and Risk Notes](./docs/license-and-risk-notes.md)
