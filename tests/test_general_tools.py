import unittest
from src.tools.general import BasicQueryTool, ProfileAnalysisTool

class TestBasicQueryTool(unittest.TestCase):
    def setUp(self):
        self.query_tool = BasicQueryTool()

    def test_eligibility_query(self):
        query = "Am I eligible for a loan?"
        result = self.query_tool.run(query)
        
        self.assertEqual(result["query_type"], "eligibility")
        self.assertIn("basic_requirements", result["direct_answer"])
        self.assertTrue(isinstance(result["confidence_score"], float))
        self.assertTrue(0 <= result["confidence_score"] <= 1)

    def test_process_query(self):
        query = "What is the loan application process?"
        result = self.query_tool.run(query)
        
        self.assertEqual(result["query_type"], "process")
        self.assertIn("application", result["direct_answer"].lower())
        self.assertIn("process", result["direct_answer"].lower())

    def test_documentation_query(self):
        query = "What documents do I need?"
        result = self.query_tool.run(query)
        
        self.assertEqual(result["query_type"], "documentation")
        self.assertIn("documents", result["direct_answer"].lower())
        self.assertTrue(len(result["next_steps"]) > 0)

    def test_terms_query(self):
        query = "What are the interest rates?"
        result = self.query_tool.run(query)
        
        self.assertEqual(result["query_type"], "terms")
        self.assertIn("rates", result["direct_answer"].lower())

    def test_general_query(self):
        query = "Tell me about your loans"
        result = self.query_tool.run(query)
        
        self.assertEqual(result["query_type"], "general")
        self.assertIn("loan", result["direct_answer"].lower())
        self.assertTrue(result["confidence_score"] < 0.8)  # General queries have lower confidence

    def test_invalid_query(self):
        query = ""  # Empty query
        result = self.query_tool.run(query)
        
        self.assertIn("error", result)
        self.assertIn("suggested_action", result)

class TestProfileAnalysisTool(unittest.TestCase):
    def setUp(self):
        self.profile_tool = ProfileAnalysisTool()

    def test_qualified_profile(self):
        profile = {
            "years_in_business": 3,
            "annual_revenue": 500000,
            "credit_score": 700,
            "equipment_needs": True,
            "real_estate_collateral": True,
            "accounts_receivable": 150000
        }
        
        result = self.profile_tool.run(profile)
        
        self.assertEqual(result["eligibility_status"], "pre-qualified")
        self.assertGreater(result["confidence_score"], 0.7)
        self.assertTrue(len(result["qualifying_loan_types"]) >= 2)
        self.assertLessEqual(result["suggested_loan_amount"], profile["annual_revenue"] * 0.75)

    def test_unqualified_profile(self):
        profile = {
            "years_in_business": 1,
            "annual_revenue": 100000,
            "credit_score": 600,
            "equipment_needs": False
        }
        
        result = self.profile_tool.run(profile)
        
        self.assertEqual(result["eligibility_status"], "needs_review")
        self.assertLess(result["confidence_score"], 0.5)
        self.assertTrue(len(result["risk_factors"]) > 0)
        self.assertTrue(len(result["improvement_areas"]) > 0)

    def test_borderline_profile(self):
        profile = {
            "years_in_business": 2,
            "annual_revenue": 250000,
            "credit_score": 650,
            "equipment_needs": True,
            "debt_service_ratio": 1.3
        }
        
        result = self.profile_tool.run(profile)
        
        self.assertEqual(result["eligibility_status"], "pre-qualified")
        self.assertTrue(len(result["risk_factors"]) > 0)  # Should identify the high debt service ratio
        self.assertTrue("Equipment Financing" in result["qualifying_loan_types"])

    def test_invalid_profile(self):
        profile = {}  # Empty profile
        result = self.profile_tool.run(profile)
        
        self.assertEqual(result["status"], "error")
        self.assertIn("message", result)

    def test_loan_type_matching(self):
        profile = {
            "years_in_business": 3,
            "annual_revenue": 1000000,
            "credit_score": 720,
            "equipment_needs": True,
            "real_estate_collateral": True,
            "accounts_receivable": 200000
        }
        
        result = self.profile_tool.run(profile)
        
        self.assertIn("Working Capital Loan", result["qualifying_loan_types"])
        self.assertIn("Equipment Financing", result["qualifying_loan_types"])
        self.assertIn("Commercial Real Estate Loan", result["qualifying_loan_types"])
        self.assertIn("Invoice Financing", result["qualifying_loan_types"])

if __name__ == '__main__':
    unittest.main() 