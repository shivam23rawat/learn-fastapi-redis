"""
This file creates the FastAPI app instance following the `Factory Function` design pattern.

Usage
-----
Run the app.py file from the root of the repository using `fastapi run .\src\app.py`
"""

from fastapi import FastAPI
from src.api.v1.router import router as v1_router


def create_app() -> FastAPI:
    """
    Creates and configures an instance of the FastAPI application.

    Returns
    -------
    application
        An instance of the FastAPI application with the specified title, description, and version.
    """
    application = FastAPI(
        title="FastAPI Redis Integration Demo",
        description="This app demonstrates the integration of FastAPI with Redis",
        version="0.1.0",
    )

    application.include_router(v1_router)

    return application


app = create_app()
