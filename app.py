from fastapi import FastAPI
from pydantic import BaseModel,Field
app=FastAPI(title="Voice AI Customer Support Agent",version="0.1.0")
FAQ=[{"question":"How do I reset my password?","answer":"Use the password reset link on the sign-in page."},{"question":"How do I request a refund?","answer":"Share your order ID with support so the refund can be reviewed."},{"question":"How can I contact support?","answer":"Open a support ticket with your account email and a short description."}]
RISK={"fraud","charged twice","security breach","account hacked","hacked","emergency"}
class Turn(BaseModel):
 transcript:str=Field(min_length=1,max_length=5000)
 conversation_id:str="demo"
def respond(transcript):
 text=transcript.lower()
 if any(x in text for x in RISK):return {"intent":"escalation","reply":"This may need specialist attention. I will prepare an escalation for a human support agent.","escalate":True,"matched_faq":None}
 words=set(text.split()); best=None; score=0
 for item in FAQ:
  n=len(words & set((item["question"]+" "+item["answer"]).lower().split()))
  if n>score:best,score=item,n
 if best and score>=2:return {"intent":"faq","reply":best["answer"],"escalate":False,"matched_faq":best["question"]}
 return {"intent":"unknown","reply":"I’m not confident I understood. Could you rephrase that or ask for a human support agent?","escalate":False,"matched_faq":None}
@app.get("/health")
def health():return {"status":"ok"}
@app.get("/faq")
def faq():return {"items":FAQ}
@app.post("/turn")
def turn(r:Turn):return {"conversation_id":r.conversation_id,**respond(r.transcript)}
