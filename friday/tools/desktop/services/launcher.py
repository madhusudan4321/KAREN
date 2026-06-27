import subprocess
import psutil


def launch_application(executable: str):

    subprocess.Popen([executable])

    return {
        "success": True,
        "message": f"{executable} launched."
    }


def close_application_process(executable: str):

    killed = 0

    executable = executable.lower()

    for proc in psutil.process_iter(["name", "cmdline"]):

        try:

            name = (proc.info["name"] or "").lower()

            cmd = " ".join(proc.info.get("cmdline") or []).lower()

            if executable in name or executable in cmd:

                proc.kill()

                killed += 1

        except Exception:
            pass

    if killed == 0:

        return {
            "success": False,
            "message": "Application is not running."
        }

    return {
        "success": True,
        "message": f"Closed {killed} process(es)."
    }


def list_running_processes():

    apps = set()

    for proc in psutil.process_iter(["name"]):

        try:

            if proc.info["name"]:

                apps.add(proc.info["name"])

        except Exception:
            pass

    return sorted(apps)