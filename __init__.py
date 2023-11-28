from .node.ToolsDiy import *

__version__ = "1.0.0"

NODE_CLASS_MAPPINGS = {
    "ToolsDiy": LoadImageHeightWidth,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ToolsDiy": "加载带长宽参数的图片",
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
