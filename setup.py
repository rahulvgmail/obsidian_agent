from setuptools import setup, find_packages

setup(
    name="rag_application",
    version="0.1",
    packages=find_packages(),
    setup_requires=["numpy==1.21.0"],
    install_requires=[
        "numpy==1.21.0",
        "pandas==1.3.0",
        "flask==2.1.0",
        "fastapi==0.68.0",
        "uvicorn==0.15.0",
        "scikit-learn==0.24.2",
        "transformers==4.11.3",
        "torch==1.9.0",
        "pathlib==1.0.1",
    ],
    entry_points={
        "console_scripts": [
            "rag_app=app.main:main",
        ],
    },
)
