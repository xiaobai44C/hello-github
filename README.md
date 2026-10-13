# hello-github 👋

我的第一个 GitHub 仓库，用来练手 Git 和 GitHub 的基本操作。

## 这个仓库里有什么

| 文件 | 说明 |
| --- | --- |
| `README.md` | 你正在看的这个文件 |
| `.gitignore` | 告诉 Git 哪些文件不用跟踪（日志、缓存、依赖等） |
| `LICENSE` | MIT 开源协议 |
| `hello.py` | 一个能跑的小示例，随便改着玩 |

## 跑一下示例

```bash
python hello.py
```

## Git 常用命令速查

### 日常三连（最常用）

```bash
git status              # 看看改了哪些文件
git add .               # 把所有改动加入暂存区
git commit -m "说明"     # 提交，说明要写清楚这次改了啥
git push                # 推到 GitHub
```

### 查看记录

```bash
git log --oneline       # 简洁的提交历史
git diff                # 看还没提交的改动
```

### 分支

```bash
git branch              # 看有哪些分支
git switch -c feature-x # 新建并切到 feature-x 分支
git switch main         # 切回主分支
```

### 撤销（新手救命用）

```bash
git restore <文件>       # 丢弃某个文件未提交的改动
git restore --staged .  # 把 add 进去的东西撤回来
git reset --soft HEAD~1 # 撤销上一次提交，改动保留
```

### 提交信息怎么写

推荐用这个格式，`类型: 干了啥`：

```
feat: 新增登录功能
fix: 修复导出崩溃
docs: 更新 README
refactor: 重构订单模块
```

## 下一步可以试试

- [ ] 改一下 `hello.py`，然后走一遍 add → commit → push
- [ ] 开个新分支练手，再合并回来
- [ ] 试着提一个 Issue 给自己
- [ ] 给它加个 GitHub Actions 自动跑测试

---

> 仓库由 WorkBuddy 生成于 2026-10-13
