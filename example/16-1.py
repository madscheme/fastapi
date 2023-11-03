from fastapi import Form

@app.get("/who2")
def greet2(name: str = Form()):
    return f"Hello, {name}?"
