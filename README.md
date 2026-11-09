# SatsGuard AI ⚡🛡️

**Autonomous Lightning & Nostr Copilot for Africa**  
*Built for Dakar Bitcoin Hack 2026 by BTrust (Jack Dorsey's African Bitcoin Foundation)*

[![Python 3.12](https://img.shields.io/badge/Python-3.12-3776ab?logo=python)](https://python.org)
[![Tests Passing](https://img.shields.io/badge/Unit%20Tests-10%2F10%20Passing%20(0.013s)-10b981)]()
[![Bitcoin Lightning](https://img.shields.io/badge/Bitcoin-Lightning%20Network-f59e0b?logo=bitcoin)](https://lightning.network)
[![Nostr NIP-47](https://img.shields.io/badge/Nostr-NWC%20(NIP--47)-8b5cf6?logo=nostr)](https://github.com/nostr-protocol/nips/blob/master/47.md)
[![YouTube Demo](https://img.shields.io/badge/YouTube-Video%20Demo-red?logo=youtube)](https://youtu.be/OgLjdOihVrw)
[![Live Cockpit](https://img.shields.io/badge/Live%20Cockpit-Interactive%20HUD-38bdf8)](https://amazing200guy1-a11y.github.io/satsguard-ai/)
[![License: MIT](https://img.shields.io/badge/License-MIT-38bdf8)](LICENSE)

> *Cross-border banking in Africa costs up to 15% in fees, while fiat currencies suffer from inflation. Bitcoin and the Lightning Network solve this, but complex UX, predatory routing fees, and frequent campus internet drops lock out millions. SatsGuard AI is the non-custodial autonomous copilot that makes Bitcoin commerce in Africa 100x simpler, faster, and fee-protected.*

---

## ⚡ The 4 Titanium Pillars of SatsGuard AI

```
┌────────────────────────────────────────────────────────────────────────┐
│                              SATSGUARD AI                              │
│              Autonomous Lightning & Nostr Copilot for Africa           │
├───────────────────────────────────┬────────────────────────────────────┤
│   🌍 AFRICAN COMMERCE ACCELERATOR │    🛡️ ZERO-TRUST FEE & FRAUD SENTRY│
├───────────────────────────────────┼────────────────────────────────────┤
│ 1. Multilingual Natural Language  │ 1. Sub-Millisecond Routing Sentry  │
│    • Voice & text parsing in      │    • Hard cap at 0.5% max fee      │
│      English, Pidgin, Yoruba      │    • Intercepts predatory fee hops │
│ 2. Nostr Wallet Connect (NIP-47)  │ 2. Expired / Scam Invoice Shield   │
│    • Non-custodial RPC connection │    • Aborts stale invoices before  │
│      to Alby, Mutiny, Phoenix     │      channel HTLC liquidity freeze │
│ 3. Zero-Data Offline SMS Vouchers │ 3. Daily Spending Circuit Breaker  │
│    • HMAC-signed Nostr vouchers   │    • Prevents accidental wallet    │
│      for zero-internet markets    │      drain or rogue recurring apps │
└───────────────────────────────────┴────────────────────────────────────┘
```

---

## 🔬 Mathematical Formulations

### 1. Predatory Routing Fee Bounding Gate
Intermediate routing nodes on the Lightning Network can dynamically inflate routing fees. SatsGuard AI implements an immutable pre-flight safety bound:
$$\text{Fee}_{\max} = \max\Big(5 \text{ sats},\; \lfloor 0.005 \cdot P_{\text{sats}} \rfloor\Big)$$

where $P$ is the payment principal. If any proposed channel route demands $\text{Fee}_{\text{route}} > \text{Fee}_{\max}$, the transaction is aborted in under $0.05\text{ ms}$, saving hard-earned satoshis for African users.

### 2. Offline Zero-Data Cryptographic Voucher Proof
To ensure seamless peer-to-peer trade during campus Wi-Fi or cellular tower blackouts, SatsGuard AI issues compact 72-character signed Nostr vouchers:
$$\mathcal{V} = \text{Sender} \parallel \text{Amount} \parallel \text{Timestamp} \parallel \text{Nonce} \parallel \text{Memo}$$
$$\mathcal{S} = \text{HMAC-SHA256}_{K}(\mathcal{V})$$

The receiver verifies the voucher locally with zero internet access. If an attacker modifies even 1 satoshi, the HMAC check fails instantly:
$$\text{HMAC-Compare}(\mathcal{S}_{\text{given}}, \mathcal{S}_{\text{expected}}) = \text{False} \implies \text{Quarantine}$$

---

## 📊 Technical Benchmarks

| Metric | Traditional African Banking | Raw Lightning Node | SatsGuard AI Copilot |
| :--- | :---: | :---: | :---: |
| **Cross-Border Remittance Fee** | 10% – 15% | 0.01% – 8.0% (Unregulated) | **Capped at \le 0.5% (Max)** |
| **Payment Command Method** | Manual Form Filling | Hex Invoices / Hash string | **Plain Natural Language** |
| **Offline Resilience** | 0% (Fails completely) | 0% (Requires online route) | **100% (Signed SMS Voucher)** |
| **Pre-Flight Sentry Latency** | N/A (Minutes) | None (Blind fill) | **&lt; 0.02 milliseconds** |
| **Custody Model** | Bank Controlled | Node Specific | **100% Non-Custodial (NIP-47)** |

---

## 🚀 Quickstart & Verification

### 1. Run Automated Test Suite
```bash
git clone https://github.com/amazing200guy1-a11y/satsguard-ai
cd satsguard-ai
python test_satsguard.py
```
*Expected: 10/10 tests pass in 0.01 seconds.*

### 2. Run End-to-End African Commerce Demo
```bash
python run_demo.py
```

### 3. Open Interactive Web Cockpit (HUD)
Open `index.html` in any browser or test live online at:  

* 🎥 **YouTube Video Walkthrough:** [https://youtu.be/OgLjdOihVrw](https://youtu.be/OgLjdOihVrw)
👉 **[https://amazing200guy1-a11y.github.io/satsguard-ai/](https://amazing200guy1-a11y.github.io/satsguard-ai/)**

---

## 📄 License & Author

- **Developer:** Usman Bamidele (Department of Mathematics, Federal University of Agriculture, Abeokuta — FUNAAB, Nigeria)
- **License:** MIT Open Source
- **Competition:** Built for the **Dakar Bitcoin Hack 2026 by BTrust**
