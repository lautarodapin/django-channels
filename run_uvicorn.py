import uvicorn

class App:
    pass
app = App()

if __name__ == "__main__":
    uvicorn.run("example:app", host="0.0.0.0", port=8000, log_level='debug')