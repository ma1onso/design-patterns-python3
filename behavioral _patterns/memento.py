class Editor:
    _text = ''
    _x = 0
    _y = 0
    _selection_witdh = None

    def set_text(self, new_text):
        self._text = new_text

    def set_cursor(self, x, y):
        self._x = x
        self._y = y

    def set_selection_width(self, width):
        self._selection_witdh = width

    def create_snapshot(self):
        return Snapshot(
            self, self._text, self._x, self._y, self._selection_witdh
        )
    

class Snapshot:
    def __init__(self, editor: Editor, text: str, x_cursor: int, y_cursor: int, selection_width: int) -> None:
        self.editor = editor
        self.text = text
        self.x_cursor = x_cursor
        self.y_cursor = y_cursor
        self.selection_width = selection_width

    def restore(self):
        self.editor.set_text(self.text)
        self.editor.set_cursor(self.x_cursor, self.y_cursor)
        self.editor.set_selection_width(self.selection_width)


class Command:
    def __init__(self, editor: Editor) -> None:
        # In this case we're only creating one backup, but is possible create a list
        self.backup = None
        self.editor = editor

    def make_backup(self):
        self.backup = self.editor.create_snapshot()

    def undo(self):
        if self.backup != None:
            self.backup.restore()
            print('Backup restored successfully ✅')
        else:
            print('There is not an available backup 🥲')


if __name__ == '__main__':
    editor = Editor()
    editor.set_text('My main editor')
    editor.set_cursor(100, 44)
    editor.set_selection_width(400)

    command = Command(editor)

    command.undo()

    command.make_backup()
    command.undo()
