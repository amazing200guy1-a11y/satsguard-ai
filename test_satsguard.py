"""
SatsGuard AI — Comprehensive Automated Test Suite
=================================================
Tests all 5 layers:
  1. African Commerce Multilingual Intent Parser (English, Pidgin, Yoruba)
  2. Predatory Fee Sentry (routing fee caps & expiry checks)
  3. Nostr Wallet Connect (NIP-47 JSON-RPC 2.0 Client)
  4. Offline Zero-Data Cryptographic Voucher Engine (HMAC Verification & Anti-Forgery)
  5. Unified Orchestrator End-to-End Pipeline
"""

import sys
import os
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from satsguard_engine import (
    SatsGuardOrchestrator, AfricanCommerceIntentParser, PredatoryFeeSentry,
    NostrWalletConnectClient, OfflineVoucherEngine, InvoiceDetails
)

class TestSatsGuardAI(unittest.TestCase):

    def setUp(self):
        self.orchestrator = SatsGuardOrchestrator()
        self.parser = AfricanCommerceIntentParser()
        self.sentry = PredatoryFeeSentry()
        self.nwc = NostrWalletConnectClient()
        self.voucher_engine = OfflineVoucherEngine()

    # ── 1. Intent Parser Tests ──────────────────────────────────────────
    def test_intent_parser_english(self):
        prompt = "Pay 25,000 sats for hostel wifi to @kwame"
        res = self.parser.parse_intent(prompt)
        self.assertEqual(res["amount_sats"], 25000)
        self.assertEqual(res["recipient"], "@kwame")
        self.assertEqual(res["category"], "TELECOM_DATA")

    def test_intent_parser_nigerian_pidgin(self):
        prompt = "Send 5000 sats give my brother for food"
        res = self.parser.parse_intent(prompt)
        self.assertEqual(res["amount_sats"], 5000)
        self.assertEqual(res["category"], "FOOD_MARKET")

    def test_intent_parser_utility_bill(self):
        prompt = "Pay 15000 sats for nepa light bill"
        res = self.parser.parse_intent(prompt)
        self.assertEqual(res["amount_sats"], 15000)
        self.assertEqual(res["category"], "UTILITY_POWER")

    # ── 2. Predatory Fee Sentry Tests ───────────────────────────────────
    def test_fee_sentry_clears_normal_route(self):
        inv = InvoiceDetails(
            payment_hash="hash123",
            amount_sats=10000,
            expiry_seconds=3600,
            payee_pubkey="pubkey123",
            description="Clean order"
        )
        # 10 sats fee on 10,000 sats (0.1% fee) -> pristine
        verdict = self.sentry.evaluate_lightning_route(inv, proposed_route_fee_sats=10, wallet_balance_sats=50000)
        self.assertTrue(verdict.approved)
        self.assertEqual(verdict.action, "SETTLE_CLEARED")

    def test_fee_sentry_blocks_predatory_fee_spike(self):
        inv = InvoiceDetails(
            payment_hash="hash456",
            amount_sats=5000,
            expiry_seconds=3600,
            payee_pubkey="pubkey456",
            description="Fee gouge trap"
        )
        # 450 sats fee on 5,000 sats (9.0% fee!) -> Predatory Fee Spike!
        verdict = self.sentry.evaluate_lightning_route(inv, proposed_route_fee_sats=450, wallet_balance_sats=50000)
        self.assertFalse(verdict.approved)
        self.assertEqual(verdict.action, "FEE_SPIKE_ABORT")
        self.assertIn("PREDATORY ROUTING FEE DETECTED", verdict.reason)
        self.assertGreater(verdict.estimated_sats_saved, 0)

    def test_fee_sentry_blocks_expired_invoice(self):
        inv = InvoiceDetails(
            payment_hash="hash789",
            amount_sats=2000,
            expiry_seconds=10,  # 10 second expiry
            payee_pubkey="pubkey789",
            description="Expired",
            created_at=1000.0   # old timestamp in past
        )
        verdict = self.sentry.evaluate_lightning_route(inv, proposed_route_fee_sats=2, wallet_balance_sats=50000)
        self.assertFalse(verdict.approved)
        self.assertEqual(verdict.action, "SCAM_INVOICE_BLOCKED")
        self.assertIn("INVOICE EXPIRED", verdict.reason)

    # ── 3. Nostr Wallet Connect (NIP-47) Tests ──────────────────────────
    def test_nwc_pay_invoice_rpc(self):
        req = self.nwc.create_pay_invoice_request("lnbc50u1p...")
        self.assertEqual(req["kind"], 23194)
        resp = self.nwc.execute_rpc(req)
        self.assertEqual(resp["result_type"], "pay_invoice")
        self.assertEqual(resp["result"]["status"], "SETTLED")

    # ── 4. Offline Cryptographic Voucher Tests ──────────────────────────
    def test_offline_voucher_issuance_and_verification(self):
        voucher = self.voucher_engine.issue_offline_voucher("npub1usman...", 12000, "market_yam")
        self.assertTrue(voucher.startswith("nostr:voucher:v1:"))
        
        valid, data = self.voucher_engine.verify_offline_voucher(voucher)
        self.assertTrue(valid)
        self.assertEqual(data["amount_sats"], 12000)
        self.assertEqual(data["memo"], "market_yam")

    def test_offline_voucher_anti_forgery(self):
        voucher = self.voucher_engine.issue_offline_voucher("npub1usman...", 12000, "market_yam")
        # Attacker tampers with amount (changes 12000 to 99999)
        tampered = voucher.replace(":12000:", ":99999:")
        valid, data = self.voucher_engine.verify_offline_voucher(tampered)
        self.assertFalse(valid)
        self.assertEqual(data["error"], "SIGNATURE_FORGERY_DETECTED")

    # ── 5. Unified Orchestrator End-to-End Tests ────────────────────────
    def test_orchestrator_successful_execution(self):
        res = self.orchestrator.execute_prompt(
            user_prompt="Pay 8000 sats for campus data bundle",
            wallet_balance_sats=50000,
            simulated_route_fee_sats=4
        )
        self.assertEqual(res["status"], "SETTLED")
        self.assertEqual(res["parsed"]["amount_sats"], 8000)
        self.assertEqual(self.orchestrator.telemetry["total_sats_settled"], 8000)


if __name__ == "__main__":
    unittest.main()
