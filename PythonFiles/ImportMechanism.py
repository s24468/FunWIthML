def setup_imports():
    import importlib
    import subprocess
    import sys

    # Read requirements.txt
    with open('PythonFiles/requirements.txt', 'r') as f:
        requirements = f.read().splitlines()

    # Install and import each package, storing them in a dictionary
    imported_modules = {}
    for package in requirements:
        try:
            imported_modules[package] = importlib.import_module(package)
        except ImportError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            imported_modules[package] = importlib.import_module(package)

    # Return specific modules for convenience
    return (
        imported_modules.get("streamlit"),
        imported_modules.get("pandas"),
        imported_modules.get("numpy"),
        imported_modules.get("plotly.express"),
        imported_modules.get("transformers").pipeline,
    )
