from typing import Any, Dict, List
import datetime
from .base import BaseTool

class BasicQueryTool(BaseTool):
    """Tool for handling basic borrower queries about loans and eligibility."""
    name: str = "basic_query"
    description: str = "Handles common questions about commercial lending, eligibility, and application process"

    def run(self, query: str, borrower_context: Dict[str, Any] = None, **kwargs: Any) -> Dict[str, Any]:
        """
        Process basic queries about commercial lending.
        
        Args:
            query: The borrower's question
            borrower_context: Optional context about the borrower (if available)
        """
        # Common lending-related information
        lending_info = {
            "loan_types": [
                "Working Capital Loans",
                "Equipment Financing",
                "Commercial Real Estate Loans",
                "Business Expansion Loans",
                "Invoice Financing"
            ],
            "basic_requirements": [
                "Minimum 2 years in business",
                "Annual revenue > $250,000",
                "Credit score > 650",
                "Profitable business operations",
                "Clean banking history"
            ],
            "document_requirements": [
                "Business financial statements",
                "Tax returns (2 years)",
                "Bank statements (6 months)",
                "Business plan",
                "Financial projections"
            ]
        }

        try:
            # Process query and provide relevant information
            response = {
                "query_type": self._categorize_query(query),
                "direct_answer": self._generate_answer(query, lending_info, borrower_context),
                "additional_info": self._get_additional_info(query, lending_info),
                "next_steps": self._suggest_next_steps(query),
                "confidence_score": self._calculate_confidence(query)
            }
            return response
        except Exception as e:
            return {"error": str(e)}

    def _categorize_query(self, query: str) -> str:
        """Categorize the type of query."""
        query = query.lower()
        if any(term in query for term in ["eligibility", "qualify", "requirements"]):
            return "eligibility"
        elif any(term in query for term in ["document", "paperwork", "required"]):
            return "documentation"
        elif any(term in query for term in ["type", "kind", "category"]):
            return "loan_types"
        elif any(term in query for term in ["process", "step", "how to"]):
            return "application_process"
        else:
            return "general"

    def _generate_answer(self, query: str, info: Dict[str, List[str]], context: Dict[str, Any] = None) -> Dict[str, Any]:
        """Generate a direct answer to the query."""
        query_type = self._categorize_query(query)
        answer = {
            "text": "",
            "relevant_info": []
        }

        if query_type == "eligibility":
            answer["text"] = "Here are the basic eligibility requirements for commercial loans:"
            answer["relevant_info"] = info["basic_requirements"]
        elif query_type == "documentation":
            answer["text"] = "You'll need to provide the following documents:"
            answer["relevant_info"] = info["document_requirements"]
        elif query_type == "loan_types":
            answer["text"] = "We offer the following types of commercial loans:"
            answer["relevant_info"] = info["loan_types"]
        else:
            answer["text"] = "I can help you with information about commercial lending."
            answer["relevant_info"] = []

        return answer

    def _get_additional_info(self, query: str, info: Dict[str, List[str]]) -> Dict[str, Any]:
        """Get additional relevant information based on the query."""
        return {
            "related_topics": self._get_related_topics(self._categorize_query(query)),
            "useful_resources": self._get_useful_resources(self._categorize_query(query))
        }

    def _suggest_next_steps(self, query: str) -> List[str]:
        """Suggest next steps based on the query."""
        query_type = self._categorize_query(query)
        steps = []
        
        if query_type == "eligibility":
            steps = [
                "Review your business financials",
                "Check your credit score",
                "Gather necessary documentation",
                "Contact a loan officer for a detailed assessment"
            ]
        elif query_type == "documentation":
            steps = [
                "Gather all required documents",
                "Ensure documents are up to date",
                "Make copies of all documents",
                "Prepare a document checklist"
            ]
        else:
            steps = [
                "Review our loan products",
                "Check your eligibility",
                "Prepare your documentation",
                "Contact a loan officer"
            ]
        
        return steps

    def _calculate_confidence(self, query: str) -> float:
        """Calculate confidence score for the response."""
        # Simple confidence calculation based on query clarity
        query = query.lower()
        if len(query.split()) > 5:
            return 0.9
        elif len(query.split()) > 3:
            return 0.7
        else:
            return 0.5

    def _get_related_topics(self, query_type: str) -> List[str]:
        """Get related topics based on query type."""
        topics = {
            "eligibility": [
                "Credit Score Requirements",
                "Revenue Requirements",
                "Business Age Requirements",
                "Industry-Specific Requirements"
            ],
            "documentation": [
                "Document Preparation",
                "Document Verification",
                "Common Documentation Issues",
                "Document Submission Process"
            ],
            "loan_types": [
                "Loan Terms",
                "Interest Rates",
                "Repayment Options",
                "Loan Amounts"
            ],
            "application_process": [
                "Application Timeline",
                "Required Information",
                "Application Review",
                "Approval Process"
            ]
        }
        return topics.get(query_type, [])

    def _get_useful_resources(self, query_type: str) -> List[str]:
        """Get useful resources based on query type."""
        resources = {
            "eligibility": [
                "Eligibility Calculator",
                "Requirements Checklist",
                "FAQ Section",
                "Loan Officer Contact"
            ],
            "documentation": [
                "Document Checklist",
                "Document Templates",
                "Document Guidelines",
                "Support Contact"
            ],
            "loan_types": [
                "Loan Comparison Tool",
                "Loan Calculator",
                "Product Brochures",
                "Case Studies"
            ],
            "application_process": [
                "Application Guide",
                "Timeline Calculator",
                "Status Tracker",
                "Support Center"
            ]
        }
        return resources.get(query_type, [])

class ProfileAnalysisTool(BaseTool):
    """Tool for analyzing borrower profiles and providing initial assessments."""
    name: str = "profile_analysis"
    description: str = "Analyzes borrower profile data to provide initial loan eligibility assessment"

    def run(self, profile_data: Dict[str, Any], **kwargs: Any) -> Dict[str, Any]:
        """
        Analyze borrower profile and provide assessment.
        
        Args:
            profile_data: Dictionary containing borrower profile information
        """
        try:
            assessment = self._assess_profile(profile_data)
            suitable_loans = self._determine_suitable_loans(profile_data)
            improvements = self._suggest_improvements(profile_data)
            
            return {
                "assessment": assessment,
                "suitable_loans": suitable_loans,
                "suggested_improvements": improvements,
                "next_steps": self._determine_next_steps(assessment.get("pre_qualified", False))
            }
        except Exception as e:
            return {"error": str(e)}

    def _assess_profile(self, profile: Dict[str, Any]) -> Dict[str, Any]:
        """Assess the borrower's profile for loan eligibility."""
        assessment = {
            "pre_qualified": True,
            "strengths": [],
            "areas_for_improvement": []
        }

        # Check business age
        if profile.get("years_in_business", 0) >= 2:
            assessment["strengths"].append("Established business history")
        else:
            assessment["areas_for_improvement"].append("Business needs more operating history")

        # Check revenue
        if profile.get("annual_revenue", 0) >= 250000:
            assessment["strengths"].append("Strong revenue base")
        else:
            assessment["areas_for_improvement"].append("Revenue below minimum threshold")

        # Check credit score
        if profile.get("credit_score", 0) >= 650:
            assessment["strengths"].append("Good credit history")
        else:
            assessment["areas_for_improvement"].append("Credit score needs improvement")

        # Determine pre-qualification
        if len(assessment["areas_for_improvement"]) > 1:
            assessment["pre_qualified"] = False

        return assessment

    def _determine_suitable_loans(self, profile: Dict[str, Any]) -> List[str]:
        """Determine which loan types are suitable for the borrower."""
        suitable_loans = []
        
        # Based on business needs and profile
        if profile.get("needs_working_capital", False):
            suitable_loans.append("Working Capital Loan")
        if profile.get("needs_equipment", False):
            suitable_loans.append("Equipment Financing")
        if profile.get("needs_real_estate", False):
            suitable_loans.append("Commercial Real Estate Loan")
        if profile.get("needs_expansion", False):
            suitable_loans.append("Business Expansion Loan")
            
        return suitable_loans

    def _suggest_improvements(self, profile: Dict[str, Any]) -> List[str]:
        """Suggest improvements to strengthen the loan application."""
        improvements = []
        
        if profile.get("years_in_business", 0) < 2:
            improvements.append("Continue building business history")
        if profile.get("annual_revenue", 0) < 250000:
            improvements.append("Work on increasing annual revenue")
        if profile.get("credit_score", 0) < 650:
            improvements.append("Improve credit score through timely payments")
            
        return improvements

    def _determine_next_steps(self, pre_qualified: bool) -> List[str]:
        """Determine next steps based on pre-qualification status."""
        if pre_qualified:
            return [
                "Gather required documentation",
                "Complete loan application",
                "Schedule meeting with loan officer",
                "Prepare for underwriting process"
            ]
        else:
            return [
                "Work on suggested improvements",
                "Review eligibility requirements",
                "Consult with financial advisor",
                "Reassess in 3-6 months"
            ]

class GeneralTool(BaseTool):
    """Tool for handling general queries and providing basic information."""
    name: str = "general"
    description: str = "Handles general queries and provides basic information"

    def run(self, query: str, **kwargs: Any) -> Dict[str, Any]:
        """
        Process general queries and provide information.
        
        Args:
            query: The user's question
        """
        try:
            # Process query and provide relevant information
            response = {
                "query_type": self._categorize_query(query),
                "response": self._generate_response(query),
                "suggestions": self._get_suggestions(query)
            }
            return response
        except Exception as e:
            return {"error": str(e)}

    def _categorize_query(self, query: str) -> str:
        """Categorize the type of query."""
        query = query.lower()
        if any(term in query for term in ["help", "assist", "support"]):
            return "help"
        elif any(term in query for term in ["what", "how", "why"]):
            return "information"
        elif any(term in query for term in ["hello", "hi", "greeting"]):
            return "greeting"
        else:
            return "general"

    def _generate_response(self, query: str) -> Dict[str, Any]:
        """Generate a response to the query."""
        query_type = self._categorize_query(query)
        
        if query_type == "help":
            return {
                "text": "I'm here to help! I can assist you with business analysis and general information.",
                "suggestions": [
                    "Ask about business improvements",
                    "Request general information",
                    "Get help with specific topics"
                ]
            }
        elif query_type == "information":
            return {
                "text": "I can provide information about various topics. What would you like to know?",
                "suggestions": [
                    "Business analysis",
                    "General information",
                    "Specific topics"
                ]
            }
        elif query_type == "greeting":
            return {
                "text": "Hello! How can I assist you today?",
                "suggestions": [
                    "Ask about business improvements",
                    "Get general information",
                    "Request help"
                ]
            }
        else:
            return {
                "text": "I'm here to help. What would you like to know?",
                "suggestions": [
                    "Business analysis",
                    "General information",
                    "Specific help"
                ]
            }

    def _get_suggestions(self, query: str) -> List[str]:
        """Get relevant suggestions based on the query."""
        query_type = self._categorize_query(query)
        
        if query_type == "help":
            return [
                "Ask about business improvements",
                "Request general information",
                "Get help with specific topics"
            ]
        elif query_type == "information":
            return [
                "Business analysis",
                "General information",
                "Specific topics"
            ]
        else:
            return [
                "Business improvements",
                "General information",
                "Help and support"
            ] 