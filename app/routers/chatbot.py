from fastapi import APIRouter, HTTPException
from openai import OpenAI
from schemas.schemas import ChatRequest

router = APIRouter(
    prefix='/chat',
    tags=['chat']
)

client = OpenAI()



@router.post("/chat")
async def chat_bot(request: ChatRequest):
    try:
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Eres un profesor de programación que ayuda a dar consejos de programación y pistas pero no das la solución"},
                {"role": "user", "content": request.question}
            ]
        )
        response_content = completion.choices[0].message
        return {"response": response_content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
'''''
@router.post("/chat")
async def chat_bot():
    return {"response": "hola"}
'''''