from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import random

app = FastAPI()

phrases = ["Investments", "Smallcase", "Stocks", "buy-the-dip", "TickerTape"]

@app.get("/api/v1", response_class=HTMLResponse)
def get_random_phrase():
    phrase = random.choice(phrases)
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Phrase Generator</title>
        <style>
            body {{
                background-color: #f7f9fc;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }}
            .container {{
                text-align: center;
            }}
            .phrase {{
                font-size: 2.5rem;
                color: #2c3e50;
                background: #e3eaf2;
                padding: 20px 40px;
                border-radius: 12px;
                box-shadow: 0 5px 15px rgba(0,0,0,0.1);
                transition: all 0.3s ease;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="phrase">{phrase}</div>
        </div>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)
