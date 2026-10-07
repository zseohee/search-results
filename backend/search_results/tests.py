from django.test import SimpleTestCase

from search_results.views.tagging import classify_category, extract_tags

class TaggingTests(SimpleTestCase):
    def test_extract_tags_matches_case_insensitively(self):
        tags = extract_tags("ASL interpreter and SSI benefits")
        self.assertIn("ASL", tags)
        self.assertIn("SSI", tags)
        self.assertIn("benefits", tags)

    def test_category_priority_is_job_then_event_then_welfare(self):
        self.assertEqual(classify_category("Hiring event for a workshop"), "job")
        self.assertEqual(classify_category("Community workshop this Friday"), "event")
        self.assertEqual(classify_category("SSI grant for home support"), "welfare")
        self.assertEqual(classify_category("Braille display review"), "other")
