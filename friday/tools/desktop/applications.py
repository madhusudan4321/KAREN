import shutil

from friday.tools.desktop.services.application_registry import ApplicationRegistry
from friday.tools.desktop.services.launcher import (
    launch_application,
    close_application_process,
    list_running_processes,
)

registry = ApplicationRegistry()


def open_application(app: str):

    info = registry.get(app)

    if info is None:
        return {
            "success": False,
            "message": f"'{app}' is not installed."
        }

    executable = info["exec"]

    if shutil.which(executable) is None:
        return {
            "success": False,
            "message": f"{executable} is not available."
        }

    return launch_application(executable)


def close_application(app: str):

    info = registry.get(app)

    if info is None:
        return {
            "success": False,
            "message": f"'{app}' is not installed."
        }

    return close_application_process(info["exec"])


def restart_application(app: str):

    close_application(app)

    return open_application(app)


def list_running_applications():

    return list_running_processes()