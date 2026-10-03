import unittest
from kalmora.ledger import Ledger


class LedgerTests(unittest.TestCase):
    def test_reference_balance_open_items_and_projection(self):
        original={"id":"1100-2026-1","company":"1100","lines":[{"line":3,"account":"43000000","partner":"C1","assignment":"INV1","debit":100,"credit":0,"amount_doc":125},{"line":4,"account":"57200001","debit":0,"credit":100}]}
        ledger=Ledger.from_entries([original]); projected=ledger.project()
        self.assertEqual(ledger.entries[0]["lines"][0]["book_line"],"1100-2026-1#3")
        self.assertEqual(ledger.balances()["1100","43000000"],100)
        self.assertEqual(ledger.open_items()["1100","43000000","C1","INV1"],100)
        projected._entries[0]["lines"][0]["debit"]=200
        self.assertEqual(ledger.balances()["1100","43000000"],100)
        self.assertNotIn("book_line",original["lines"][0])
        self.assertEqual(ledger.entries[0]["lines"][0]["amount_doc"],125)

    def test_company_separation_and_duplicate_ids(self):
        def entry(company):return {"id":company,"company":company,"lines":[{"account":"57200001","debit":3,"credit":0}]}
        ledger=Ledger.from_entries([entry("1100"),entry("3100")])
        self.assertEqual(len(ledger.balances()),2)
        with self.assertRaises(ValueError): Ledger.from_entries([entry("1100"),entry("1100")])
