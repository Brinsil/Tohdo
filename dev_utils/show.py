# Initial settings for the program

import sys
import shutil
from rich.align import Align
from rich.console import Console, RenderableType
from rich.progress import BarColumn, MofNCompleteColumn, Progress

from settings_config import Settings
from banner import banner

'''
    1 -> Checking if settings.json is created
    2 -> If Flase 
        2.1 -> prompt for minimal default settings
        2.2 -> Print the banner
        2.3 -> Exit
    3 -> if True 
        3.1 -> Fetch username
        3.2 -> Print banner
    4 -> Exit 
'''

console = Console()
settings = Settings()
task_done = 1

class justifyProgress(Progress):
    def get_renderable(self) -> RenderableType:
        return Align.right(super().get_renderable())

def task_progress_bar():
    global task_done
    with justifyProgress(BarColumn(bar_width=shutil.get_terminal_size().columns // 4), MofNCompleteColumn()) as progress:
            task1 = progress.add_task('Progress', total=4)
            progress.update(task1, advance=task_done)
            task_done += 1

def make_prompt_layout() -> None:
    console.rule('Hello !!! :wave: , We need to ask few things to get started')
    config_queries = [
        '[green]What should we call you? : ',
        '[blue]Which type of view would you prefer (list/kanban)?[/] : ',
        '[cyan]Do you want to enable quotes ([green]Y[/]/[red]N[/])?[/] ',
        '[red]Do you want to show task progress ([green]Y[/]/[red]N[/])?[/] '
    ]
    config_keys = [
        'username',
        'view',
        'quotes',
        'task progress'
    ]
    config_values = list()
    for query in config_queries:
        print('')
        config_values.append(console.input(query))
        task_progress_bar()

    settings_config = dict(zip(config_keys, config_values))
    settings.write_settings(settings_config)


if __name__ == '__main__':
    if settings.settings_exists():
        banner() # <- username -- Change banner function to show username
        sys.exit()
    make_prompt_layout()
    banner() # <- username -- Change banner function to show username





