import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # tensorflow should stop it with the useless warnings

from . import (
    datasets,
    mlp,
    mlts
)

import seaborn
import jupyterthemes
import html
from pathlib import Path


p8_colors = ["#15985C", "#DD841E", "#2A4958", "#2C6048", "#8B683F", "#4598C0", "#41C78A", "#ECA34E", "#19668C", "#62A1C0", "#60C798", "#ECB473"] 
p8_palette = seaborn.color_palette(p8_colors)

def setup_plot_style(dark=False):
    if dark:
        theme = "monokai"
    else:
        theme = None # TODO: select favorite light theme
    seaborn.set_style("ticks")
    jupyterthemes.jtplot.style(theme=theme, grid=True, figsize=(20, 5))
    seaborn.set_palette(p8_palette)


def setup_slide_style(theme="night"):
    from traitlets.config.manager import BaseJSONConfigManager
    path = Path.home() / ".jupyter" / "nbconfig"
    cm = BaseJSONConfigManager(config_dir=str(path))
    cm.update(
        "rise",
        {
            "theme": theme,
            "transition": "fade",
            "start_slideshow_at": "selected",
         }
    )




def show_command(cmd):
    """
    Display a terminal command with HTML layour
    """
    from IPython.display import display, HTML
    return HTML(
                f"<div style='margin:0 0 5px; overflow:hidden; padding:10px; background-color:DimGray; border:1px solid DimGray; -webkit-border-radius: 5px;border-radius: 5px;'><tt>{html.escape(cmd)}</tt></p>"
    )