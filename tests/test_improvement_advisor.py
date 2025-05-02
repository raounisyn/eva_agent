import unittest
from src.tools.improvement_advisor import ImprovementAdvisorTool

class TestImprovementAdvisor(unittest.TestCase):
    def setUp(self):
        self.advisor = ImprovementAdvisorTool()
        
        # Sample business data for testing
        self.sample_business_data = {
            "financial_metrics": {
                "profit_margin": 0.08,  # Below threshold of 0.1
                "cash_flow_ratio": 0.9,  # Below threshold of 1.0
                "debt_to_equity": 2.5,   # Above threshold of 2.0
                "revenue_growth": 0.12,
                "operating_costs": 0.65
            },
            "operational_metrics": {
                "production_efficiency": 0.75,  # Below threshold of 0.8
                "resource_utilization": 0.65,   # Below threshold of 0.7
                "quality_control_score": 0.85,
                "inventory_turnover": 4.2
            },
            "market_position": {
                "market_share": 0.15,
                "unique_selling_points": [
                    "Advanced technology platform",
                    "Strong customer service",
                    "Competitive pricing"
                ],
                "untapped_markets": [
                    "International expansion",
                    "New product lines",
                    "Digital transformation services"
                ],
                "market_threats": [
                    "New competitors entering market",
                    "Regulatory changes",
                    "Technology disruption"
                ]
            },
            "growth_plans": [
                "Expand to new geographic markets",
                "Develop new product line",
                "Implement digital transformation"
            ]
        }

    def test_improvement_advisor_analysis(self):
        """Test the complete improvement advisor analysis"""
        result = self.advisor.run(self.sample_business_data)
        
        # Test that we got all expected sections in the result
        self.assertIn("analysis", result)
        self.assertIn("suggestions", result)
        self.assertIn("implementation_roadmap", result)
        self.assertIn("priority_levels", result)
        self.assertIn("estimated_impact", result)
        
        # Test financial analysis
        financial_analysis = result["analysis"]["financial"]
        self.assertIn("strengths", financial_analysis)
        self.assertIn("concerns", financial_analysis)
        self.assertIn("recommendations", financial_analysis)
        
        # Test operational analysis
        operational_analysis = result["analysis"]["operational"]
        self.assertIn("efficiency_metrics", operational_analysis)
        self.assertIn("bottlenecks", operational_analysis)
        self.assertIn("improvement_opportunities", operational_analysis)
        
        # Test market analysis
        market_analysis = result["analysis"]["market"]
        self.assertIn("market_share", market_analysis)
        self.assertIn("competitive_advantages", market_analysis)
        self.assertIn("growth_opportunities", market_analysis)
        self.assertIn("threats", market_analysis)
        
        # Test suggestions
        suggestions = result["suggestions"]
        self.assertGreater(len(suggestions), 0)
        for suggestion in suggestions:
            self.assertIn("category", suggestion)
            self.assertIn("area", suggestion)
            self.assertIn("suggestion", suggestion)
            self.assertIn("priority", suggestion)
            self.assertIn("estimated_impact", suggestion)
        
        # Test implementation roadmap
        roadmap = result["implementation_roadmap"]
        self.assertIn("short_term", roadmap)
        self.assertIn("medium_term", roadmap)
        self.assertIn("long_term", roadmap)
        
        # Test priority levels
        priorities = result["priority_levels"]
        self.assertIn("immediate", priorities)
        self.assertIn("short_term", priorities)
        self.assertIn("long_term", priorities)
        
        # Test impact estimation
        impact = result["estimated_impact"]
        self.assertIn("financial_impact", impact)
        self.assertIn("operational_impact", impact)
        self.assertIn("market_impact", impact)

    def test_financial_analysis(self):
        """Test specific financial analysis functionality"""
        result = self.advisor._analyze_financials(self.sample_business_data["financial_metrics"])
        
        # Test that we identified the correct concerns
        expected_concerns = [
            "Low profit margin",
            "Potential cash flow issues",
            "High debt levels"
        ]
        for concern in expected_concerns:
            self.assertIn(concern, result["concerns"])
        
        # Test that we have recommendations for each concern
        self.assertEqual(len(result["concerns"]), len(result["recommendations"]))

    def test_operational_analysis(self):
        """Test specific operational analysis functionality"""
        result = self.advisor._analyze_operations(self.sample_business_data["operational_metrics"])
        
        # Test that we identified the correct bottlenecks
        expected_bottlenecks = [
            "Production process inefficiencies",
            "Underutilized resources"
        ]
        for bottleneck in expected_bottlenecks:
            self.assertIn(bottleneck, result["bottlenecks"])
        
        # Test that we have improvement opportunities
        self.assertGreater(len(result["improvement_opportunities"]), 0)

    def test_market_analysis(self):
        """Test specific market analysis functionality"""
        result = self.advisor._analyze_market_position(self.sample_business_data["market_position"])
        
        # Test market share
        self.assertEqual(result["market_share"], 0.15)
        
        # Test competitive advantages
        self.assertEqual(len(result["competitive_advantages"]), 3)
        
        # Test growth opportunities
        self.assertEqual(len(result["growth_opportunities"]), 3)
        
        # Test threats
        self.assertEqual(len(result["threats"]), 3)

if __name__ == '__main__':
    unittest.main() 