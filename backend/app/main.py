from fastapi import FastAPI

app = FastAPI(
    title="Ziwei Insight API",
    version="0.1.0",
    description="紫微斗数 AI 命盘推理系统",
)


@app.get("/")
def root() -> dict[str, str]:
    return {
        "name": "ziwei-insight",
        "docs": "/docs",
        "health": "/health",
    }


@app.get("/health")
def health() -> dict[str, str]:
    return {
        "status": "ok",
        "service": "ziwei-insight",
    }


@app.get("/hello/{name}")
def hello(name: str, lang: str = "zh") -> dict[str, str]:
    if lang == "en":
        return {"message": f"Hello, {name}"}
    return {"message": f"你好，{name}"}
