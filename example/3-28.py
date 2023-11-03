@app.get("/happy")
def happy(status_code=200):
    return ":)"
