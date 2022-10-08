# All the commands for tohdo 

import typer

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
    """[bold green]Add[/bold green] a Task :sparkles: [light_slate_grey italic](Add task name inside quotes)[/]"""
    ...

@app.command('show', rich_help_panel='Command')
def show():
    """Show all Tasks :open_book:"""
    ...

@app.command('done', rich_help_panel='Command')
def done():
    """Mark a task as [#bbf2b3]done ✓[/]"""
    ...

@app.command('undone', rich_help_panel='Command')
def undone():
    '''Mark a task as [purple4]undone ○[/]'''
    ...

@app.command('move', rich_help_panel='Command')
def move():
    """Change task order 🔀"""
    ...

@app.command('delete', rich_help_panel='Command')
def delete():
    """[bright_red]Delete[/] a Task"""
    ...

@app.command('clear', rich_help_panel='Command')
def clean():
    """Clear all tasks marked as done :wastebasket:"""
    ...

@app.command('filter', rich_help_panel='Command')
def filter():
    '''Filter tasks having the same tags :star:'''
    ...

@app.command('username', rich_help_panel='Utils and Config')
def username():
    """Change name :name_badge: [light_slate_grey italic](without resetting data)[/]"""
    ...

@app.command('config', rich_help_panel='Utils and Config')
def config():
    """Open the configuration file :wrench:"""
    ...

@app.command('docs', rich_help_panel='Utils and Config')
def docs():
    """Launch docs Website :globe_with_meridians:"""
    ...

@app.command('version', rich_help_panel='Utils and Config')
def version():
    """Show version :bookmark:"""
    ...

if __name__ == '__main__':
    app()



