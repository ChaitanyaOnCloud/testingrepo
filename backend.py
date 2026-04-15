from fastapi import FastAPI, HTTPException

app = FastAPI()

# Dummy in-memory data
data_store = {
    1: {"name": "Item1", "value": 100},
    2: {"name": "Item2", "value": 200}
}

# Root API
@app.get("/")
def home():
    return {"message": "Backend is running"}

# Get all items
@app.get("/items")
def get_items():
    return data_store

# Get item by ID
@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in data_store:
        raise HTTPException(status_code=404, detail="Item not found")
    return data_store[item_id]

# Add new item
@app.post("/items")
def add_item(item_id: int, name: str, value: int):
    if item_id in data_store:
        raise HTTPException(status_code=400, detail="Item already exists")
    
    data_store[item_id] = {"name": name, "value": value}
    return {"message": "Item added", "data": data_store[item_id]}

# Delete item
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in data_store:
        raise HTTPException(status_code=404, detail="Item not found")
    
    deleted = data_store.pop(item_id)
    return {"message": "Item deleted", "data": deleted}
