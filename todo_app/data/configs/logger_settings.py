import logging

log = logging.getLogger('appLog')
log.setLevel(logging.INFO)

formatter = logging.Formatter(
    '### $asctime ### $name ### ${levelname} ### $message ###', style='$')

# Log to file
filehandler = logging.FileHandler("todo_app/data/logs/app.log", "a")
filehandler.setLevel(logging.INFO)
filehandler.setFormatter(formatter)
log.addHandler(filehandler)

# Log to stdout too
streamhandler = logging.StreamHandler()
streamhandler.setLevel(logging.INFO)
streamhandler.setFormatter(formatter)
log.addHandler(streamhandler)