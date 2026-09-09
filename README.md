# AIREACH 高价值客户猎手

AIREACH 高价值客户猎手（每日哨兵 · 通用版）——外贸企业 AIREACH 潜客巡检与高价值挖掘技能。

- **画像来源**：直接读取 AiReach 后台已填写的公司画像（client_profile_get / aw_icp_get），不做本地 ICP 收集。
- **每日合规检查**：只推送不精准客户（含不精准理由 / 所属图谱分支 / 排除建议）。
- **高价值跟进卡**：按后台画像标准筛选高价值客户，输出跟进建议 + 沟通渠道 + 地区语言话术。
- **强制交付**：每次执行必出 HTML 报告 + 确保每日 09:00 定时任务存在。

## 一键安装（把下面命令发给 Accio Work 执行）

### Windows
```powershell
git clone https://github.com/zecun5146-create/AIREACH高价值客户猎手.git && powershell -NoProfile -ExecutionPolicy Bypass -File "AIREACH高价值客户猎手\install.ps1"
```

### macOS / Linux
```bash
git clone https://github.com/zecun5146-create/AIREACH高价值客户猎手.git && bash "AIREACH高价值客户猎手/install.sh"
```

安装后请**完全退出 Accio Work 再重新打开**（不是最小化）。

## 手动安装

下载本仓库 ZIP → 解压 → 将 `AIREACH高价值客户猎手/` 目录复制到 `agent-core/skills/` 下 → 重启 Accio Work。

## 依赖

需已安装并授权 **OKKI AiReach** 插件（潜客查询、画像接口均走 aireach-cli）。
