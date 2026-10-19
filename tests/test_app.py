from app import respond
def test_faq_response():
 assert respond("How do I reset my password?")["intent"]=="faq"
def test_account_security_escalation():
 r=respond("I think my account was hacked")
 assert r["escalate"] and r["intent"]=="escalation"
def test_unknown_input_falls_back():
 assert respond("purple clouds banana")["intent"]=="unknown"
