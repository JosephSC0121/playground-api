from fastapi import APIRouter
from openai import OpenAI
router = APIRouter(
    prefix='/chat',
    tags=['chat']
)

client = OpenAI()

@router.get("/chat")
def chat_bot():
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
        {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
    ]
    )

    return(completion.choices[0].message)