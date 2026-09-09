# AIREACH高价值客户猎手 - Windows 一键安装脚本
$ErrorActionPreference = "Continue"
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$skillName = "AIREACH高价值客户猎手"
$srcDir = Join-Path $scriptDir $skillName

if (-not (Test-Path $srcDir)) {
    Write-Host "[错误] 未找到技能目录: $srcDir"
    exit 1
}

$home = $env:USERPROFILE
$skillsCandidates = @()
$pattern = Join-Path $home ".accio\accounts\*\agents\*\agent-core\skills"
foreach ($d in (Get-ChildItem -Path $pattern -Directory -ErrorAction SilentlyContinue)) {
    $skillsCandidates += $d.FullName
}

if ($skillsCandidates.Count -eq 0) {
    Write-Host "[错误] 未找到 Accio Work 的 skills 目录，请确认已安装并登录 Accio Work。"
    exit 1
}

foreach ($t in $skillsCandidates) {
    $dest = Join-Path $t $skillName
    if (Test-Path $dest) { Remove-Item $dest -Recurse -Force }
    Copy-Item -Path $srcDir -Destination $dest -Recurse -Force
    Write-Host "[OK] 已安装到: $dest"
}

Write-Host ""
Write-Host "安装完成！请完全退出 Accio Work 再重新打开（不是最小化）。"
