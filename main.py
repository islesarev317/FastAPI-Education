from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from dynamic.get_html_grid import get_html_grid

app = FastAPI()

app.mount("/styles", StaticFiles(directory="styles"))

word_set = []
with open("words.txt", "r") as file:
    for line in file:
        word_and_definition = line.split(" - ")
        word_set.append(word_and_definition)


@app.get("/")
def read_root():
    html_content = get_html_grid(word_set)
    return HTMLResponse(content=html_content)


@app.get("/cards")
async def get_cards():
    return FileResponse("cards.html")

@app.get("/cards_js/")
async def get_cards():
    return JSONResponse(content=word_set)


@app.get("/cards_js/{filter}")
async def get_cards(filter):
    filtered_set = [pair for pair in word_set if pair[0].startswith(filter)]
    return JSONResponse(content=filtered_set)

