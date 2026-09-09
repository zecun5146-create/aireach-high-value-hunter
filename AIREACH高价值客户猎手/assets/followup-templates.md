# 跟进话术模板（assets）

按客户所在地区/国家的语言编写话术，同时向使用者展示中文对照版。
以下为通用结构模板，发送前替换占位符，并结合客户实际（主营/规模/痛点）定制。**价值点占位 {VALUE_PROPS_1..4} 取自 AiReach 后台画像（client_profile_get.profile 的 products / company_type / mode）；落款占位取自 client_profile_get.profile.company_name。**

## 模板结构
1. **Subject/标题**：价值导向，点出客户业务规模或痛点。
2. **开场**：认可客户行业地位/规模（用工具实拉的事实）。
3. **痛点共鸣**：2-3 个该规模企业常见的经营瓶颈。
4. **方案价值**：能力清单 4 条以内（{VALUE_PROPS_1..4}）。
5. **行动邀约**：20 分钟演示/电话，低门槛。
6. **落款**：{SENDER_NAME} · {COMPANY_NAME} · {SENDER_PHONE}。

## 印尼语模板（印尼客户）
Subject: Mengembangkan Pertumbuhan Ekspor {COMPANY} dengan Sistem Digital Terpadu

Halo {CONTACT},

{COMPANY} dikenal sebagai salah satu produsen/eksportir terkemuka di Indonesia — {SCALE_FACT}, operasi ekspor Anda jelas berjalan dalam skala besar.

Pada skala tersebut, sebagian besar produsen menghadapi tiga kendala yang sama: calon pelanggan luar negeri tersebar di berbagai platform, tindak lanjut masih tercatat di spreadsheet, dan tidak ada satu pandangan terpadu mengenai pipeline penjualan.

Kami membantu produsen ekspor seperti {COMPANY} menyelesaikan hal ini dengan satu sistem terpadu:
- {VALUE_PROPS_1}
- {VALUE_PROPS_2}
- {VALUE_PROPS_3}
- {VALUE_PROPS_4}

Apakah Anda bersedia meluangkan waktu 20 menit minggu ini untuk melihat bagaimana sistem ini cocok dengan proses bisnis Anda saat ini? Kami siap menyesuaikan dengan prioritas tim Anda.

Hormat kami,
{SENDER_NAME} · {COMPANY_NAME} · {SENDER_PHONE}

## 英语模板（英语地区客户）
Subject: Scaling {COMPANY}'s export growth with one unified outbound system

Hi {CONTACT},

{COMPANY} stands out as one of the leading {INDUSTRY} players — with {SCALE_FACT}, your export operation clearly runs at scale.

At that scale, most manufacturers hit the same three bottlenecks: overseas leads scattered across platforms, follow-ups living in spreadsheets, and no single view of the sales pipeline.

We help export businesses like {COMPANY} solve exactly this with an all-in-one system:
- {VALUE_PROPS_1}
- {VALUE_PROPS_2}
- {VALUE_PROPS_3}
- {VALUE_PROPS_4}

Would you be open to a 20-minute call this week to see how this maps to your current process? Happy to align with your team's priorities.

Best regards,
{SENDER_NAME} · {COMPANY_NAME} · {SENDER_PHONE}

## 其他地区
- 俄语客户：用俄语商务模板（参考印尼语结构）。
- 西语客户（阿根廷/墨西哥）：用西班牙语商务模板。
- 生成规则：始终先定位客户国家 → 选择该国商务语言 → 输出目标语言版 + 中文对照版。

## 中文对照版模板（给使用者看）
主题：以统一数字化系统助力 {COMPANY} 出口增长

{CONTACT} 你好，

{COMPANY} 是{国家}领先的{行业}企业之一——{规模事实}，贵司的出口业务显然已具规模。

在这个规模上，大多数企业都会遇到同样的三大瓶颈：海外潜客分散在各平台、跟进记录停留在电子表格、销售管道缺乏统一视图。

我们帮助像 {COMPANY} 这样的出口企业，用一套一体化系统解决这些问题：
- {VALUE_PROPS_1}
- {VALUE_PROPS_2}
- {VALUE_PROPS_3}
- {VALUE_PROPS_4}

本周能否安排 20 分钟，看看这套系统如何与贵司现有流程匹配？我们愿意配合贵司团队的优先事项。

此致，
{SENDER_NAME} · {COMPANY_NAME} · {SENDER_PHONE}
