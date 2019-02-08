import logging

from watchdog.events import LoggingEventHandler


class LogHandler(LoggingEventHandler):
    def __init__(self):
        super(LogHandler, self).__init__()
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        self.log_handler = logging.FileHandler('changes.log', 'a+', 'utf-8')
        self.formatter = logging.Formatter('%(asctime)s - %(message)s')
        self.log_handler.setFormatter(self.formatter)
        self.logger.addHandler(self.log_handler)

    def on_moved(self, event):
        what = 'directory' if event.is_directory else 'file'
        self.logger.info("Moved %s: from %s to %s", what, event.src_path,
                         event.dest_path)

    def on_created(self, event):
        what = 'directory' if event.is_directory else 'file'
        self.logger.info("Created %s: %s", what, event.src_path)

    def on_deleted(self, event):
        what = 'directory' if event.is_directory else 'file'
        self.logger.info("Deleted %s: %s", what, event.src_path)

    def on_modified(self, event):
        what = 'directory' if event.is_directory else 'file'
        self.logger.info("Modified %s: %s", what, event.src_path)
