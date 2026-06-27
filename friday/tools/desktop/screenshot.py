import os
import mss
from datetime import datetime


def capture():

    folder = os.path.expanduser("~/Pictures")

    os.makedirs(folder, exist_ok=True)

    filename = datetime.now().strftime("karen_%Y%m%d_%H%M%S.png")

    path = os.path.join(folder, filename)

    with mss.mss() as sct:

        sct.shot(output=path)

    return {
        "success": True,
        "path": path,
    }