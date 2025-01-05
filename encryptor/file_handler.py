import os

def validate_file(path: str) -> bool:
    return os.path.exists(path)

def get_output_path(input_path: str, suffix: str) -> str:
    base, ext = os.path.splitext(input_path)
    return f"{base}_{suffix}{ext}"