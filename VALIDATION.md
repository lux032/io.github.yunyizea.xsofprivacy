# 0.3.0 验证范围

日期：2026-11-05。包名 io.github.yunyizea.xsofprivacy，versionCode 5，versionName 0.3.0-preview。

新增两个可选作用域：GuardProvider 的 AI 通话检测入口（1 个目标）以及 SystemHelper
中的许可判断、加密提交、应用统计线程和 7 类专用 Receiver（10 个目标）。原 XSOF
仍为 14 组、28 个目标。三个作用域合计 25 组、39 个目标，按进程分别安装。

已完成：

- 原 XSOF 全部 28 个目标的识别与缺失/歧义回归。
- 两个新增 APK 的 11 个目标、精确配置与特征配置一致性、返回值策略核对。
- 错误包/错误 APK、开关证据缺失、提交方法歧义、服务行为证据缺失的跳过测试。
- Java 17 编译、D8 8.7.18 DEX 生成、apksig 8.7.3 v3 签名验证。
- resources.arsc 不压缩，签名后偏移 788，满足 4 字节对齐。
- APK 包名/版本/入口一致，无额外权限、旧模块包名、测试类或框架实现。
- 作用域数组包括 com.miui.securitycenter、com.miui.guardprovider、com.mobiletools.systemhelper。

使用者提供 LSPosed 2.2.1 (7912)，HyperOS 3.0.307.0.WNCCNXM.C11。
原 XSOF 有使用者实机生效反馈；本次 0.3.0 新增功能未经过真机注入、停止效果、
采集变化、网络请求、耗电或长期稳定性验证。不能将编译和识别测试当作效果证明。

## 本机补充验证（小米 15）

环境：`24129PN74C` / `dada`，HyperOS `OS3.0.307.0.WOCCNXM`，Android 16，
Zygisk Vector `2.2`（3080 / API 102），KernelSU SukiSU Ultra `4.3.0-r2`。
手机管家 `12.8.1-260816.0.1`（`40001281`），GuardProvider `3.0.7-20260708.0`，
SystemHelper `4.0.0-20260610`（34）。

三个作用域均已实机注入，跳过 0 组：

| 作用域 | 组 | hooks |
|---|---:|---:|
| `com.miui.securitycenter`（含 `.remote`、`:ui`） | 14 | 28 |
| `com.mobiletools.systemhelper` | 10 | 11 |
| `com.miui.guardprovider` | 1 | 1 |

已观察到 `HIT` 的组：`listeners`、`storage.screenshot`、`storage.fraud_phone`、
`provider.ingress`、`helper.receiver.SIMStateReceiver`、`helper.receiver.OnBootReceiver`。
`guard.ai_detection` 与 `helper.encrypted_post` 尚未观察到 `HIT`。

对应数据库侧观察：`/data/misc/user/0/securitycenter/fraud_detection_data.db` 的
`screenshot`、`fraud_phone`、`screen_share`、`voip_record` 四表在模块生效后保持 0 行，
文件修改时间停在启用之前。此行数结论只覆盖该库，不代表其他存储位置或上传通道。

`SystemHelper 4.0.0` 的 `helper.encrypted_post` 识别规则已调整，原因与验证过程见
[README 版本适配说明](README.md#版本适配说明本分支)。

真机验证局限：未做停用模块的对照实验；未抓包确认上报是否实际发生；
未验证 GuardProvider 在真实通话场景下的行为；未覆盖 clone 用户（user 999）。

安装包沿用之前实验签名，使用 AAPT2+D8+apksig 直接构建；Gradle 未完整执行。
输入 APK 的信息、证据和行为边界见 docs/extended-analysis.md。

APK SHA-256：
`651b63fd37a8e38bc014e1bfb42f26693e077d9d3b771b0840fe98b4f8263221`
