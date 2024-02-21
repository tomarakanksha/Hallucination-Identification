from fastapi import FastAPI, Query
from hallucination_detector import get_hallucination
from fastapi import HTTPException

app = FastAPI()

# Endpoint for user queries
@app.get("/isTruth ")
def is_truth (query: str = Query(..., title="User Query", max_length=50), response: str = Query(..., title="response", max_length=300)):
    if not query:
        return {"answer": "Please provide a query"}
    if not response:
        return {"answer": "Please provide th AI response"}
    else:
        try:
            hallucination, confidence = get_hallucination(query, response)
            return {"hallucination": hallucination, "confidence": confidence}
        except Exception as e:
            print(e)
            raise HTTPException(status_code=500, detail="Error occurred while getting response from LLM model")
        
        