import subprocess


def lock():

    subprocess.Popen(["loginctl", "lock-session"])

    return {"success": True}


def logout():

    subprocess.Popen(["loginctl", "terminate-user", "$USER"])

    return {"success": True}


def shutdown():

    subprocess.Popen(["systemctl", "poweroff"])

    return {"success": True}


def reboot():

    subprocess.Popen(["systemctl", "reboot"])

    return {"success": True}