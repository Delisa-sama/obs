from watchdog.events import FileSystemEventHandler


class FSHandler(FileSystemEventHandler):
    def __init__(self, sep='-'):
        super(FSHandler, self).__init__()

    def on_moved(self, event):
        pass

    def on_created(self, event):
        pass

    def on_deleted(self, event):
        pass

    def on_modified(self, event):
        pass
