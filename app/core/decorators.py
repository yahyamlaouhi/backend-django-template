import functools
import os
import uuid


def image_file_path(func):
    """Generate file path for a new image"""

    @functools.wraps(func)
    def wrapper_file_path(instance, filename):
        model = func(instance, filename)
        ext = filename.split(".")[-1]
        filename = f"{uuid.uuid4()}.{ext}"
        return os.path.join(f"upload/{model}/", filename)

    return wrapper_file_path
