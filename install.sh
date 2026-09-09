#!/bin/bash
set -e
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SKILL_NAME="AIREACH高价值客户猎手"
SRC_DIR="$SCRIPT_DIR/$SKILL_NAME"

if [ ! -d "$SRC_DIR" ]; then
    echo "[错误] 未找到技能目录: $SRC_DIR"
    exit 1
fi

SKILLS_DIRS=()
for d in "$HOME/.accio/accounts/"*/agents/*/agent-core/skills; do
    [ -d "$d" ] && SKILLS_DIRS+=("$d")
done

if [ ${#SKILLS_DIRS[@]} -eq 0 ]; then
    echo "[错误] 未找到 Accio Work 的 skills 目录。"
    exit 1
fi

for t in "${SKILLS_DIRS[@]}"; do
    rm -rf "$t/$SKILL_NAME"
    cp -R "$SRC_DIR" "$t/$SKILL_NAME"
    echo "[OK] 已安装到: $t/$SKILL_NAME"
done

echo ""
echo "安装完成！请完全退出 Accio Work 再重新打开（不是最小化）。"
