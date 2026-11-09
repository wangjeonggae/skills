# Trae 全局 Skills 同步仓库

本仓库用于在多台电脑之间同步 Trae 的**全局技能目录**（即各机器上的 `~/.trae/skills`）。
换电脑时克隆本仓库即可直接使用同一套技能，改完推送即可保持一致。

## 目录说明

- 每个子目录 = 一个技能，目录名与技能 `SKILL.md` frontmatter 里的 `name` 保持一致
- 收录内容：第三方技能包（如 pm-skills 系列：`pm-master`、`pm-prd-writer`、`pm-advisor-*`、`pm-method-*` 等）与自建技能
- 排除内容：`tabbit` 软链、`.DS_Store` 等系统文件（见 `.gitignore`）

## 新电脑首次搭建（只做一次）

```bash
cd ~/.trae
mv skills skills.bak        # 备份原有目录（可选）
git clone https://github.com/wangjeonggae/skills.git skills
```

克隆后如需保存凭据，执行一次：

```bash
git config --global credential.helper osxkeychain
```

## 日常同步

**本机改了技能后 → 上传：**

```bash
cd ~/.trae/skills
git status                  # 先看一眼改了哪些
git add -A
git commit -m "update skills"
git push
```

**换到另一台电脑 → 拉取：**

```bash
cd ~/.trae/skills
git pull
```

## 注意事项

- **只同步 `skills` 目录**，不要把整个 `~/.trae` 纳入 git（其中包含插件缓存与敏感配置）
- 多台电脑都改过时，先 `git pull` 再 `git push`，避免冲突
- GitHub 已不支持密码认证，push 时 `Password` 处需填 **Personal Access Token**，不是登录密码
