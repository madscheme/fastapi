from fastapi import Form

@app.post("/who2")
def greet3(name: str = Form()):
    return f"Hello, {name}?"
