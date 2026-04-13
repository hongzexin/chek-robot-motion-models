# Scripts

## `validate_links.py`

用于校验这个仓库的核心索引文件。

It validates:

- `data/models.json` 是否可读
- 必填字段是否齐全
- 枚举值是否合法
- `data/models.csv` 与 JSON 的 `id` 是否一致
- URL 语法是否正确
- 可选地执行远程 HTTP 检查

## 用法 / Usage

基础校验：

```bash
python3 scripts/validate_links.py
```

带远程链接检查：

```bash
python3 scripts/validate_links.py --check-http
```

## 说明 / Notes

- 默认模式不会请求远程网络，适合本地快速检查
- `--check-http` 会访问远程链接，适合在提交前做一次增强检查
- 当前以 `models.json` 为主数据源，`models.csv` 作为同步导出视图

## `generate_catalog.py`

用于把机器可读数据生成成更适合 GitHub 浏览的目录结构，参考 `awesome-design-md` 的“内容目录按条目展开”思路。

会自动生成：

- `motion-models/`
- `brands/`
- `downloads/`
- `categories/`
- 根目录 `README.md`

用法：

```bash
python3 scripts/generate_catalog.py
```
