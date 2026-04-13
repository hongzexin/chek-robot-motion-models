#!/usr/bin/env python3
"""Generate navigable markdown catalog pages from data/models.json.

Inspired by collection-first repositories such as awesome-design-md:
- root README acts as the front door
- one top-level content directory contains one folder per item
- additional navigation pages group items by brand and download type
"""

from __future__ import annotations

import json
import re
import shutil
from collections import defaultdict
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = REPO_ROOT / "data" / "models.json"
MOTION_MODELS_DIR = REPO_ROOT / "motion-models"
BRANDS_DIR = REPO_ROOT / "brands"
DOWNLOADS_DIR = REPO_ROOT / "downloads"
CATEGORIES_DIR = REPO_ROOT / "categories"


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = value.replace("&", " and ")
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "unknown"


def md_link(label: str, path: Path) -> str:
    return f"[{label}]({path.as_posix()})"


def yes_no(value: bool) -> str:
    return "Yes" if value else "No"


def load_records() -> list[dict]:
    with DATA_PATH.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def recreate_dir(path: Path) -> None:
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True, exist_ok=True)


def make_item_table(records: list[dict], base_path: Path) -> str:
    lines = [
        "| 条目 / Entry | 品牌 / Brand | 机器人 / Robot | 分类 / Category | 下载方式 / Access | 下载入口 / Download |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for record in records:
        item_link = md_link(record["name"], base_path / record["id"] / "README.md")
        download_link = f"[打开链接]({record['download_url']})"
        lines.append(
            f"| {item_link} | {record['robot_brand']} | {record['robot_model']} | "
            f"{record['category_level_1']} / {record['action_style']} | "
            f"{record['download_type']} | {download_link} |"
        )
    return "\n".join(lines)


def entry_markdown(record: dict) -> str:
    download_link = f"[{record['download_url']}]({record['download_url']})"
    homepage_line = (
        f"- 首页 / Homepage: [{record['homepage_url']}]({record['homepage_url']})\n"
        if record.get("homepage_url")
        else ""
    )
    return f"""# {record['name']}

> {record['short_description_en']}

## 快速信息 / Quick facts

| 字段 / Field | 值 / Value |
| --- | --- |
| 品牌 / Brand | {record['robot_brand']} |
| 机器人 / Robot | {record['robot_model']} |
| 规范化机型 / Normalized model | `{record['robot_model_normalized']}` |
| 变体 / Variant | {record.get('dof_or_variant') or '-'} |
| 一级分类 / Category | `{record['category_level_1']}` |
| 二级分类 / Subcategory | `{record.get('category_level_2') or '-'}` |
| 动作风格 / Action style | `{record['action_style']}` |
| 下载方式 / Access type | `{record['download_type']}` |
| 部署就绪度 / Readiness | `{record['deployment_readiness']}` |
| 是否官方 / Official | `{yes_no(record['is_official'])}` |
| 是否直权重 / Direct weights | `{yes_no(record['has_direct_weights'])}` |
| 权重格式 / Weight format | `{record.get('weight_format') or '-'}` |
| 需要登录 / Requires login | `{yes_no(record['requires_login'])}` |
| 需要条款同意 / Requires terms | `{yes_no(record['requires_accept_terms'])}` |
| 信息可信度 / Confidence | `{record['source_confidence']}` |

## 中文说明 / Chinese summary

{record['short_description_zh']}

## 下载入口 / Download entry

- 主入口 / Primary link: {download_link}
{homepage_line}- 注意：本仓库只做索引，不镜像第三方模型权重。

## 备注 / Notes

{record.get('notes') or '暂无额外备注。'}

## License 与风险 / License and risk

- License note: {record['license_note']}
- Risk note: {record['risk_note']}
- Last checked: {record['last_checked_note']}

## 相关导航 / Related navigation

- [返回全部条目 / Back to all entries](../README.md)
- [按品牌浏览 / Browse by brand](../../brands/README.md)
- [按下载方式浏览 / Browse by access type](../../downloads/README.md)
- [按分类浏览 / Browse by category](../../categories/README.md)
- [社区入口 / Community](https://app-dev.chekkk.com)
"""


def brand_markdown(brand: str, records: list[dict], title: str | None = None) -> str:
    sorted_records = sorted(records, key=lambda item: (item["robot_model"], item["name"]))
    table = make_item_table(sorted_records, Path("../motion-models"))
    heading = title or brand
    return f"""# {heading}

> Brand landing page for `{brand}` resources in CHEK Robot Motion Models.

共收录 / Total entries: **{len(sorted_records)}**

{table}

## 说明 / Notes

- 这里聚合的是同品牌相关资源，不代表这些资源都来自官方发布。
- 下载入口和真机可用性以上游页面为准。
- 社区入口：[app-dev.chekkk.com](https://app-dev.chekkk.com)
"""


def brands_index_markdown(groups: dict[str, list[dict]]) -> str:
    lines = [
        "# Brands",
        "",
        "按品牌聚合浏览。先选品牌，再进入品牌页看下载入口、分类和对应条目。",
        "",
        "| 品牌 / Brand | 条目数 / Count | 入口 / Entry | 代表资源 / Representative entries |",
        "| --- | --- | --- | --- |",
    ]
    for brand in sorted(groups):
        records = sorted(groups[brand], key=lambda item: item["name"])
        brand_slug = slugify(brand)
        examples = " · ".join(f"`{record['name']}`" for record in records[:3])
        lines.append(
            f"| {brand} | {len(records)} | [打开品牌页](./{brand_slug}/README.md) | {examples} |"
        )
    return "\n".join(lines)


def download_markdown(groups: dict[str, list[dict]]) -> str:
    sections: list[str] = [
        "# Downloads",
        "",
        "按下载方式聚合，方便先找“直链可下”“模型页入口”或“需要登录/gated”的资源。",
        "",
    ]
    order = ["direct_file", "model_page", "repo_entry", "gated"]
    titles = {
        "direct_file": "直链文件 / Direct files",
        "model_page": "模型页入口 / Model pages",
        "repo_entry": "仓库入口 / Repository entries",
        "gated": "受限入口 / Gated access",
    }
    for key in order:
        records = sorted(groups.get(key, []), key=lambda item: (item["robot_brand"], item["name"]))
        sections.append(f"## {titles[key]}")
        sections.append("")
        if not records:
            sections.append("暂无条目。")
            sections.append("")
            continue
        sections.append(make_item_table(records, Path("../motion-models")))
        sections.append("")
    return "\n".join(sections)


def categories_markdown(groups: dict[str, list[dict]]) -> str:
    sections: list[str] = [
        "# Categories",
        "",
        "按一级分类聚合，方便先看 showcase、locomotion、manipulation、foundation motion 等路线。",
        "",
    ]
    for category in sorted(groups):
        records = sorted(groups[category], key=lambda item: (item["robot_brand"], item["name"]))
        sections.append(f"## `{category}`")
        sections.append("")
        sections.append(make_item_table(records, Path("../motion-models")))
        sections.append("")
    return "\n".join(sections)


def motion_models_index_markdown(records: list[dict]) -> str:
    sorted_records = sorted(records, key=lambda item: (item["robot_brand"], item["robot_model"], item["name"]))
    table = make_item_table(sorted_records, Path("."))
    return f"""# Motion Models

这个目录参考 `awesome-design-md` 的内容组织方式：每个资源一个文件夹，每个文件夹一个 `README.md`。

This directory contains one folder per indexed resource so that contributors and visitors can browse entries directly from GitHub.

共收录 / Total entries: **{len(sorted_records)}**

{table}
"""


def root_readme_markdown(records: list[dict]) -> str:
    brand_groups: dict[str, list[dict]] = defaultdict(list)
    for record in records:
        brand_groups[record["robot_brand"]].append(record)

    brand_lines = []
    for brand in sorted(brand_groups):
        brand_slug = slugify(brand)
        brand_lines.append(
            f"- [{brand}](./brands/{brand_slug}/README.md) ({len(brand_groups[brand])} entries)"
        )

    top_picks = sorted(
        records, key=lambda item: (item["download_type"] != "direct_file", item["robot_brand"], item["name"])
    )[:8]
    top_lines = [
        "| 推荐入口 / Recommended | 品牌 / Brand | 分类 / Category | 下载方式 / Access |",
        "| --- | --- | --- | --- |",
    ]
    for record in top_picks:
        top_lines.append(
            f"| [{record['name']}](./motion-models/{record['id']}/README.md) | {record['robot_brand']} | "
            f"{record['category_level_1']} / {record['action_style']} | {record['download_type']} |"
        )

    return f"""# CHEK Robot Motion Models

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

{chr(10).join(brand_lines)}

## 推荐先看 / Recommended starting points

{chr(10).join(top_lines)}

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
"""


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def main() -> int:
    records = load_records()
    recreate_dir(MOTION_MODELS_DIR)
    recreate_dir(BRANDS_DIR)
    recreate_dir(DOWNLOADS_DIR)
    recreate_dir(CATEGORIES_DIR)

    brand_groups: dict[str, list[dict]] = defaultdict(list)
    download_groups: dict[str, list[dict]] = defaultdict(list)
    category_groups: dict[str, list[dict]] = defaultdict(list)

    for record in records:
        brand_groups[record["robot_brand"]].append(record)
        download_groups[record["download_type"]].append(record)
        category_groups[record["category_level_1"]].append(record)

        entry_dir = MOTION_MODELS_DIR / record["id"]
        entry_dir.mkdir(parents=True, exist_ok=True)
        write(entry_dir / "README.md", entry_markdown(record))

    for brand, brand_records in brand_groups.items():
        write(BRANDS_DIR / slugify(brand) / "README.md", brand_markdown(brand, brand_records))

    write(MOTION_MODELS_DIR / "README.md", motion_models_index_markdown(records))
    write(BRANDS_DIR / "README.md", brands_index_markdown(brand_groups))
    write(DOWNLOADS_DIR / "README.md", download_markdown(download_groups))
    write(CATEGORIES_DIR / "README.md", categories_markdown(category_groups))
    write(REPO_ROOT / "README.md", root_readme_markdown(records))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
