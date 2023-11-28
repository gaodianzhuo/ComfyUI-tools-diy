import os
import torch
import numpy as np
import folder_paths
from PIL import Image, ImageOps

class LoadImageHeightWidth:

    @classmethod
    def INPUT_TYPES(s):
        input_dir = folder_paths.get_input_directory()
        files = [
            f for f in os.listdir(input_dir)
            if os.path.isfile(os.path.join(input_dir, f))
        ]
        return {
            "required": {
                "image": (sorted(files), {
                    "image_upload": True
                })
            },
        }

    CATEGORY = "image"

    # RETURN_TYPES = ("IMAGE", "MASK")
    RETURN_TYPES = ("IMAGE", "INT", "INT")
    RETURN_NAMES = ("IMAGE", "Width","Height")

    FUNCTION = "load_image_heitht_width"

    def load_image_heitht_width(self, image):
        image_path = folder_paths.get_annotated_filepath(image)
        i = Image.open(image_path)
        width, height = i.size
        i = ImageOps.exif_transpose(i)
        image = i.convert("RGB")
        image = np.array(image).astype(np.float32) / 255.0
        image = torch.from_numpy(image)[None, ]
        return (image, width ,height)

    @classmethod
    def IS_CHANGED(s, image):
        image_path = folder_paths.get_annotated_filepath(image)
        m = hashlib.sha256()
        with open(image_path, 'rb') as f:
            m.update(f.read())
        return m.digest().hex()

    @classmethod
    def VALIDATE_INPUTS(s, image):
        if not folder_paths.exists_annotated_filepath(image):
            return "Invalid image file: {}".format(image)

        return True
