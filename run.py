import multiprocessing
multiprocessing.set_start_method("spawn", force=True)

import uvicorn

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
