# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from Calculator import Calculator

# app = FastAPI()
# calculator = Calculator()


# class OperationData(BaseModel):
#     a: float
#     b: float


# @app.post("/add")
# async def add(data: OperationData):
#     result = calculator.add(data.a, data.b)
#     return {"result": result}

# @app.post("/subtract")
# async def subtract(data: OperationData):
#     result = calculator.subtract(data.a, data.b)
#     return {"result": result}

# @app.post("/multiply")
# async def multiply(data: OperationData):
#     result = calculator.multiply(data.a, data.b)
#     return {"result": result}


# @app.post("/divide")
# async def divide(data: OperationData):
#     try:
#         result = calculator.divide(data.a, data.b)
#         return {"result": result}
#     except ValueError as e:
#         raise HTTPException(status_code=400, detail=str(e))