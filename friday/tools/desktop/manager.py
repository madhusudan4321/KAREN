from . import applications
from . import screenshot
from . import power


def desktop(action: str, target: str = ""):

    action = action.lower()

    if action == "open":
        return applications.open_application(target)

    elif action == "close":
        return applications.close_application(target)

    elif action == "restart":
        return applications.restart_application(target)

    elif action == "list":
        return applications.list_running_applications()

    elif action == "lock":
        return power.lock()

    elif action == "shutdown":
        return power.shutdown()

    elif action == "reboot":
        return power.reboot()

    elif action == "logout":
        return power.logout()

    elif action == "screenshot":
        return screenshot.capture()

    return {
        "success": False,
        "message": "Unknown desktop action."
    }