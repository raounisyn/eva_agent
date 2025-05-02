from src.tools.general import BasicQueryTool
import json

def test_eligibility_query():
    """Test that eligibility queries return basic requirements."""
    tool = BasicQueryTool()
    query = "What are the eligibility requirements for a commercial loan?"
    result = tool.run(query)
    
    # Print the result in a readable format
    print("\nTest Response:")
    print(json.dumps(result, indent=2))
    
    assert isinstance(result, dict)
    assert "direct_answer" in result
    assert isinstance(result["direct_answer"], dict)
    assert "basic_requirements" in result["direct_answer"]["direct_answer"]
    assert isinstance(result["direct_answer"]["direct_answer"]["basic_requirements"], list)
    assert len(result["direct_answer"]["direct_answer"]["basic_requirements"]) > 0
    assert "confidence" in result["direct_answer"]
    assert "suggested_next_steps" in result["direct_answer"]
    assert isinstance(result["direct_answer"]["suggested_next_steps"], list) 