#!/usr/bin/env python3
"""Record the Xiaomi 15 on-device validation result for the fork."""
import json
import pathlib
import datetime

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "docs" / "device-evidence"

RECORD = {
    "recorded_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "purpose": "小米 15 真机加载结果与离线识别复现，供 fork 使用者参考",
    "device": {
        "model": "24129PN74C",
        "device": "dada",
        "android": "16",
        "hyperos": "OS3.0.307.0.WOCCNXM",
        "security_patch": "2026-08-01",
        "slot": "_b",
    },
    "root": {
        "impl": "KernelSU (SukiSU Ultra)",
        "manager": "v4.3.0-r2",
        "su_version": "4.3.0-r2:KernelSU",
        "kernel": "原厂 6.6.118-android15",
        "selinux": "Enforcing",
    },
    "framework": {
        "name": "Zygisk Vector",
        "version": "2.2",
        "version_code": 3080,
        "api": 102,
    },
    "module": {
        "package": "io.github.yunyizea.xsofprivacy",
        "versionName": "0.3.1-preview",
        "versionCode": 6,
        "build": "本地构建（含 SystemHelper 4.0.0 适配）",
        "signer_dn": "CN=XSOF Privacy (local build), O=Owner Device, C=CN",
        "signer_sha256": "1b44ceb71266b6dfb18f70228a7b33e34cc09bfa3666d1e140119bef969801d0",
    },
    "scopes": [
        "com.miui.securitycenter",
        "com.miui.guardprovider",
        "com.mobiletools.systemhelper",
    ],
    "target_versions": {
        "com.miui.securitycenter": "12.8.1-260816.0.1 (40001281)",
        "com.miui.guardprovider": "3.0.7-20260708.0",
        "com.mobiletools.systemhelper": "4.0.0-20260610 (34)",
    },
    "load_result": {
        "com.miui.securitycenter": {
            "profile": "ADAPTIVE_UNVERIFIED", "groups": 14, "hooks": 28, "skipped": 0},
        "com.miui.securitycenter.remote": {
            "profile": "ADAPTIVE_UNVERIFIED", "groups": 14, "hooks": 28, "skipped": 0},
        "com.miui.securitycenter:ui": {
            "profile": "ADAPTIVE_UNVERIFIED", "groups": 14, "hooks": 28, "skipped": 0},
        "com.mobiletools.systemhelper": {
            "profile": "ADAPTIVE_UNVERIFIED", "groups": 10, "hooks": 11, "skipped": 0},
        "com.miui.guardprovider": {
            "profile": "ADAPTIVE_UNVERIFIED", "groups": 1, "hooks": 1, "skipped": 0},
    },
    "observed_hits": [
        "listeners",
        "storage.screenshot",
        "storage.fraud_phone",
        "provider.ingress",
        "helper.receiver.SIMStateReceiver",
        "helper.receiver.OnBootReceiver",
    ],
    "not_yet_hit": [
        "guard.ai_detection",
        "helper.encrypted_post",
        "helper.policy_gate",
        "helper.app_usage",
    ],
    "database_observation": {
        "path": "/data/misc/user/0/securitycenter/fraud_detection_data.db",
        "tables_zero_rows": [
            "screenshot", "screen_share", "fraud_phone",
            "voip_record", "fraud_url", "airplane_mode",
        ],
        "note": "模块生效后未观察到新增行。该库为系统在数据清除后重建，历史行数为 0 "
                "不能单独作为拦截证据，主要证据是 HIT 日志。",
    },
    "limitations": [
        "未做停用模块的对照实验",
        "未抓包验证实际上报",
        "未覆盖 clone 用户 999",
        "未验证 GuardProvider 真实通话场景",
        "helper.encrypted_post 仅确认 Hook 注册，未确认实际拦截",
    ],
}


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    target = OUT / "device-validation.json"
    target.write_text(json.dumps(RECORD, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"written {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
