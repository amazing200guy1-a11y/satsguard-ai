# SatsGuard AI — Devpost Submission Copy

> Formatted for the **Dakar Bitcoin Hack 2026 by BTrust**. Copy each section directly into the Devpost submission form.

---

## 🏷️ Project Name
```text
SatsGuard AI
```

## 🎯 Elevator Pitch (Under 200 characters)
```text
Autonomous Lightning & Nostr copilot for Africa — natural language payment commands, sub-millisecond predatory fee sentry, and zero-data offline SMS vouchers.
```

---

## 💡 Inspiration

In Nigeria and across Africa, young people and market traders face two brutal economic realities:
1. **Severe Currency Depreciation & Banking Fees:** Local fiat currencies (like the Naira) suffer rapid inflation, while traditional cross-border banking fees between African nations reach **10% to 15%**.
2. **The Lightning UX & Infrastructure Chasm:** While Bitcoin and the Lightning Network provide the perfect open monetary alternative, regular people are terrified by hex invoice strings, node channel timeouts, predatory routing fee spikes (where intermediate nodes charge 5% to 10% in fees), and constant campus cellular tower drops.

As an African mathematics student at FUNAAB in Abeokuta, Nigeria, I built **SatsGuard AI** for the **BTrust Dakar Bitcoin Hack** to eliminate these barriers: providing an autonomous, non-custodial AI copilot that speaks our languages, guards our hard-earned satoshis against predatory fees, and keeps payments moving even when cellular data goes offline.

---

## 🚀 What it does

SatsGuard AI is an **Autonomous Lightning & Nostr Copilot** that makes Bitcoin commerce in Africa 100x simpler, faster, and safer:

### 1. African Multilingual Natural Language Commerce
Users don't need to understand hex hashes or channel balances. They simply type or speak naturally:
* **English:** *"Pay 25,000 sats for hostel wifi to @kwame"*
* **Nigerian Pidgin:** *"Send 5,000 sats give my brother for food"*
* **Yoruba / Swahili:** Utility bill commands like *"Pay 15,000 sats for nepa light bill"*
SatsGuard AI extracts the satoshi amount, resolves Nostr addresses, and maps the commerce category in milliseconds.

### 2. Sub-Millisecond Predatory Routing Fee Sentry
Intermediate Lightning nodes often charge exorbitant fees on uninformed users. SatsGuard AI enforces an institutional mathematical fee cap:
$$\text{Fee}_{\max} = \max\Big(5 \text{ sats},\; \lfloor 0.005 \cdot P \rfloor\Big)$$
If any routing path demands more than **0.5%** of the payment principal (e.g. charging 450 sats fee on a 5,000 sat payment), the pre-flight sentry halts execution in **0.01 ms**, preventing predatory fee gouging.

### 3. Non-Custodial Nostr Wallet Connect (NIP-47)
SatsGuard AI never holds user keys. It connects directly to the user's existing node (Alby, Mutiny, Phoenix, Umbrel) using the open **NIP-47 (NWC)** standard via encrypted Nostr events (Kind 23194 / 23195).

### 4. Zero-Data Offline SMS Cryptographic Vouchers
When university campus Wi-Fi or cellular networks drop, SatsGuard AI issues compact 72-character signed Nostr vouchers (`nostr:voucher:v1:...`). Verified with HMAC-SHA256 signatures, merchants can accept them offline via SMS, Bluetooth, or QR, with automatic settlement guaranteed upon tower reconnection.

---

## 🛠️ How we built it

* **Backend & Core Engine:** Python 3.12 with zero fragile third-party dependencies.
* **Lightning & Protocol Standards:** BOLT-11 invoice parsing, LNURL resolution, and NIP-47 Nostr Wallet Connect JSON-RPC 2.0.
* **Cryptographic Security:** HMAC-SHA256 atomic nonce verification for offline vouchers.
* **Interactive Web Cockpit:** Pure aerospace titanium & Bitcoin amber dashboard with live channel liquidity meters, NWC RPC lab, fee cap calibration, and real-time flight simulator.

---

## 🚧 Challenges we ran into

1. **Multilingual Entity Extraction without Cloud Latency:** Parsing Nigerian Pidgin and informal African market slang required building a resilient regex and keyword tokenization engine that runs locally in microseconds without relying on expensive, slow cloud LLMs.
2. **Preventing Stuck HTLCs on Stale Invoices:** Intercepting expired invoices before dispatching NWC events prevents channels from tying up outbound liquidity for hours during routing timeouts.
3. **Offline Voucher Anti-Forgery:** Designing an offline voucher small enough to fit inside a single standard SMS message (under 140 characters) while maintaining cryptographic HMAC collision resistance.

---

## 🏆 Accomplishments we're proud of

* **10/10 Automated Unit Tests Passing in 0.013s.**
* **Guaranteed Sub-0.5% Fee Invariant:** Saving African users from paying up to 9% in hidden Lightning routing fees.
* **100% Non-Custodial:** Seamlessly interoperable with the global Nostr and Lightning ecosystem via open NIP-47 standards.
* **Interactive Web Cockpit:** Live on GitHub Pages for judges to test with zero installation.

---

## 📚 What we learned

* Lightning is already fast, but the **pre-flight UX and fee defense layer** is what will bring the next 100 million African users onto Bitcoin.
* Nostr Wallet Connect (NWC) is the single most important protocol primitive for African fintech freedom, disconnecting wallet custody from application interfaces.

---

## 🚀 What's next for SatsGuard AI

* **USSD Direct Dial Integration:** Dialing `*384*SATS#` on basic feature phones (Nokia/Transsion) for non-smartphone market traders.
* **Multi-Relay Nostr Mesh:** Enabling peer-to-peer voucher reconciliation across local Bluetooth mesh networks.
* **Community Merchant PoS:** Expanding into a physical mobile app for African campus merchants and market vendors.

---

## 🔗 Links & Resources

* **GitHub Repository:** `https://github.com/amazing200guy1-a11y/satsguard-ai`
* **Live Interactive Cockpit:** `https://amazing200guy1-a11y.github.io/satsguard-ai/`
* **Test Suite:** `python test_satsguard.py` (10/10 PASS in 0.01s)
* **Demo Simulation:** `python run_demo.py`

---

## 🏷️ Built with (Tags)
`Bitcoin` `Lightning Network` `Nostr` `NWC` `NIP-47` `Python` `Fintech` `Africa` `Zero-Trust` `Cybersecurity`
