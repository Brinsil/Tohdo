# All the commands for tohdo 

import os
import typer
from datetime import datetime
from rich.console import Console

from tohdo_model import Tohdo
from database import insert_tohdo, get_all_tohdos, get_tohdo, update_tohdo, get_count, delete_tohdo, clear_tohdo
from settings_config import Settings

console = Console()
settings = Settings()

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
        date_completed = datetime.strptime(date_completed, '%d/%m/%y').isoformat()
        date_added = datetime.now().isoformat()
        status = 'To-do'
        id = i + 1
        tohdo = Tohdo(id, task, section, date_added, date_completed, status)
        insert_tohdo(tohdo)


@app.command('show', rich_help_panel='Command')
def show():
    """Show all Tasks :open_book:"""
    tasks = get_all_tohdos()
    console.print(tasks)

@app.command('done', rich_help_panel='Command')
def done():
    """Mark a task as [strike][#bbf2b3]done ✓[/]"""
    id = console.input('Enter the position of the task: ')
    task = get_tohdo(id)
    task_id = task.id
    task_status = task.status = 'Done'
    update_tohdo(task_id, 'Status', task_status)
    show()

@app.command('doing', rich_help_panel='Command')
def doing():
    """Mark a task as [#87ffd7]doing[/]"""
    id = console.input('Enter the position of the task: ')
    task = get_tohdo(id)
    task_id = task.id
    task_status = task.status = 'Doing'
    update_tohdo(task_id, 'Status', task_status)
    show()

@app.command('undone', rich_help_panel='Command')
def undone():
    '''Mark a task as [#875fff]undone ○[/]'''
    id = console.input('Enter the position of the task: ')
    task = get_tohdo(id)
    task_id = task.id
    task_status = task.status = 'To-do'
    update_tohdo(task_id, 'Status', task_status)
    show()

@app.command('move', rich_help_panel='Command')
def move():
    """Change task order 🔀"""
    count = get_count()
    id = int(console.input('Enter the position of task: '))
    new_id = int(console.input('Enter the new position of task: '))
    task = get_tohdo(id)
    delete_tohdo(id)
    task.id = new_id
    print(task.id)
    for i in range(id + 1, count):
        update_tohdo(i, 'Id', i - 1)
    insert_tohdo(task)


@app.command('delete', rich_help_panel='Command')
def delete():
    """[bright_red]Delete[/] a Task"""
    id = console.input('Enter the id: ')
    delete_tohdo(id)
    show()

@app.command('clean', rich_help_panel='Command')
def clean():
    """[gold1]Clear[/] all tasks marked as [strike]done[/] :wastebasket:"""
    clear_tohdo()
    show()

@app.command('filter', rich_help_panel='Command')
def filter():
    '''[deep_pink3]Filter[/] tasks having the same tags :star:'''
    ...

@app.command('username', rich_help_panel='Configuration and Help')
def username():
    """Change name :name_badge: [light_slate_grey italic](without resetting data)[/]"""
    username = settings.get_username()
    prompt = console.input(f'Do you want to change the username {username} (Y/N): ')
    if prompt == 'Y' or prompt == 'y':
        username = console.input('Enter the username: ')
        settings_config = settings.get_settings()
        settings_config['username'] = username
        settings.write_settings(settings_config)

@app.command('config', rich_help_panel='Configuration and Help')
def config():
    """Open the configuration file :wrench:"""
    '''
    path = settings.get_full_settings_path()
    os.system(f'open -a TextEdit {path}')
    '''
    typer.launch(settings.get_full_settings_path(), locate=True)

@app.command('docs', rich_help_panel='Configuration and Help')
def docs():
    """Launch docs Website :globe_with_meridians:"""
    ...

@app.command('version', rich_help_panel='Configuration and Help')
def version():
    """Show version :bookmark:"""
    typer.echo(f'Tohdo Version: {__version__}')
    typer.Exit()

if __name__ == '__main__':
    app()
