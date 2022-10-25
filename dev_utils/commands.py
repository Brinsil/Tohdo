# All the commands for tohdo 

from datetime import datetime
import typer
from rich.console import Console

from tohdo_model import Tohdo
from database import insert_tohdo, get_all_tohdos

console = Console()

'''
    Commands :
        add -> Add a task to the database
        show -> Show all task in the default view
        done -> Mark done for a task
        undone -> Mark undone for a task
        move -> Move the order of a task
        delete -> Delete a task
        clean -> Clear all task
        filter -> Show tasks with same tags

    Utils and Config :
        username -> Change username
        config -> Launch settings.json file
        docs -> Launch documentation
        version -> Show current version
        repo -> Launch github repository 
'''

app = typer.Typer(help='A terminal based to-do list', rich_markup_mode='rich')

@app.command('add', rich_help_panel='Command')
def add():
    """[bold green]Add[/bold green] a Section containing multiple tasks :sparkles: [light_slate_grey italic](Add section and task name inside quotes)[/]"""

    section = console.input('Add a section : ')
    task_count = int(console.input('Enter number of tasks : '))
    for i in range(task_count):
        task = console.input(f'Enter task {i + 1} : ')
        date_completed = console.input('Enter the due date : ')
        status = 'To-Do'
        id = i + 1
        tohdo = Tohdo(id, task, section, date_completed)
        insert_tohdo(tohdo)


@app.command('show', rich_help_panel='Command')
def show():
    """Show all Tasks :open_book:"""
    tasks = get_all_tohdos()
    console.print(tasks)

@app.command('done', rich_help_panel='Command')
def done():
    """Mark a task as [strike][#bbf2b3]done ✓[/]"""
    ...

@app.command('doing', rich_help_panel='Command')
def doing():
    """Mark a task as [#87ffd7]doing[/]"""
    ...

@app.command('undone', rich_help_panel='Command')
def undone():
    '''Mark a task as [#875fff]undone ○[/]'''
    ...

@app.command('move', rich_help_panel='Command')
def move():
    """Change task order 🔀"""
    ...

@app.command('delete', rich_help_panel='Command')
def delete():
    """[bright_red]Delete[/] a Task"""
    ...

@app.command('clean', rich_help_panel='Command')
def clean():
    """[gold1]Clear[/] all tasks marked as [strike]done[/] :wastebasket:"""
    ...

@app.command('filter', rich_help_panel='Command')
def filter():
    '''[deep_pink3]Filter[/] tasks having the same tags :star:'''
    ...

@app.command('username', rich_help_panel='Configuration and Help')
def username():
    """Change name :name_badge: [light_slate_grey italic](without resetting data)[/]"""
    ...

@app.command('config', rich_help_panel='Configuration and Help')
def config():
    """Open the configuration file :wrench:"""
    ...

@app.command('docs', rich_help_panel='Configuration and Help')
def docs():
    """Launch docs Website :globe_with_meridians:"""
    ...

@app.command('version', rich_help_panel='Configuration and Help')
def version():
    """Show version :bookmark:"""
    ...

if __name__ == '__main__':
    app()
