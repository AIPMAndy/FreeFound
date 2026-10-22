"""Regression tests for local API & source quality helpers (offline)."""
import unittest
from datetime import date
from api_server import derived_event_status, parse_limit, select_items, stats

class APITests(unittest.TestCase):
    def test_limit_validation(self):
        for invalid in ("0", "-1", "201", "abc", "2.0"):
            with self.subTest(invalid=invalid):
                with self.assertRaises(ValueError):
                    parse_limit({"limit":[invalid]})
        self.assertEqual(parse_limit({}),100)

    def test_hackathon_expiry(self):
        rec={"time":"2026.05.01-2026.05.30"}
        self.assertEqual(derived_event_status(rec,date(2026,10,22)),"已结束")
        self.assertEqual(derived_event_status({"time":""}),"时间待核")
        self.assertEqual(derived_event_status({"time":"2026.12.01-2026.12.03"},date(2026,10,22)),"日期未过（报名待核）")

    def test_filtering_is_case_insensitive(self):
        rows=[{"title":"AI Demo","location":"北京","source":"官方","time":"2026.05.01-2026.05.02"},
              {"title":"Other","location":"上海","source":"社区","time":""}]
        filtered=select_items("hackathons",{"location":["北京"],"q":["ai"]},rows)
        self.assertEqual(len(filtered),1)
        self.assertEqual(filtered[0]["derived_status"],"已结束")

    def test_resources(self):
        rows=[{"name":"Devpost","category":"找活动"},{"name":"YC","category":"找队友"}]
        self.assertEqual([x["name"] for x in select_items("resources",{"category":["找队友"]},rows)],["YC"])

    def test_stats_data(self):
        result=stats()
        self.assertIn("hackathons",result)
        self.assertIn("resources",result)
        self.assertIn("incubators",result)

if __name__=="__main__":
    unittest.main()
