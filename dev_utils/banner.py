# Printing the banner for the cli initially when the program is executed

import datetime
from rich.console import Console
from rich.layout import Layout
from rich.panel  import Panel
from rich.columns import Columns

from settings_config import Settings

console = Console()
setting = Settings()

head = '''
████████╗ ██████╗ ██╗  ██╗██████╗  ██████╗
 ╚══██╔══╝██╔═══██╗██║  ██║██╔══██╗██╔═══██╗ 
    ██║   ██║   ██║███████║██║  ██║██║   ██║ 
    ██║   ██║   ██║██╔══██║██║  ██║██║   ██║
    ██║   ╚██████╔╝██║  ██║██████╔╝╚██████╔╝
   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═════╝  ╚═════╝'''

date_now = datetime.datetime.now()
date_text = f'[bold orange3]{date_now.strftime("%d %b %Y | %I:%M %p")}[/] :hourglass:'


body1 = '''
[bold light_sea_green]TOHDO[/] :ledger: is a terminal based interactive [i]to-do[/i] list.

[bold light_sea_green]Tohdo[/] let's you [bold green4]add[/], [bold red3]delete[/], [bold purple]filter[/], [bold dark_slate_gray2]show[/] tasks and let's you 
edit status of each tasks. It also let's you add [bold bright_magenta]tags[/].'''

body2 = '''
[bold light_sea_green]TOHDO[/] stand on the shoulders of giants :angel:
- [bold italic deep_sky_blue1]Typer[/] for command line tool     https://github.com/tiangolo/typer
- [bold italic deep_sky_blue1]Rich[/] for the beautiful terminal https://github.com/Textualize/rich'''
        
body3_message = '''
Type [bold light_sea_green]tohdo --help[/] to see available commands

Type [bold light_sea_green]tohdo --docs[/] to check out the documentation

[bold light_sea_green]Tohdo[/] is maintained with :sparkling_heart: by 
   - Brinsil Elias
'''

body3_sponsor ='''
[bold orange3]Tohdo[/] [dark_cyan]https://github.com/tohdo[/]

[bold orange3]Buy devs a[/] :tea: [dark_cyan]https://ko-fi.com/tohdo[/]

[bold orange3]Twitter[/] [dark_cyan]https://twitter.com/brinsilelias[/]
'''

def make_layout() -> Layout:
    """Define the layout."""
    layout = Layout(name="root")

    layout.split(
        Layout(name="body1", size=5),
        Layout(name="body2", size=5),
        Layout(name="body3", size=10)
    )
    return layout          

def banner() -> None:
    console.print(head, justify='center', style='turquoise4')
    
    username = setting.get_username()
    console.print(f'[blue]Hello [bold]{username}[/][/] :smile:', date_text, justify='center')

    layout = make_layout()
    layout['body1'].update(body1)
    layout['body2'].update(body2)

    body_column = Columns([body3_message, body3_sponsor], expand=True)
    body_panel = Panel(
                body_column, title='[bold deep_pink3]Thanks for trying out[/] [bold light_sea_green]TOHDO[/]',
                border_style='bright_blue',
                expand=False)
    layout['body3'].update(body_panel)
    console.print(layout)
    

if __name__ == '__main__':
    banner()


