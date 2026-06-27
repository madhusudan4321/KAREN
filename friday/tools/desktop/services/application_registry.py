from pathlib import Path
import configparser
from rapidfuzz import process, fuzz


APPLICATION_DIRS = [

    Path("/usr/share/applications"),

    Path.home() / ".local/share/applications",

]


class ApplicationRegistry:

    def __init__(self):

        self.apps = {}

        self.scan()

    def scan(self):

        self.apps.clear()

        for directory in APPLICATION_DIRS:

            if not directory.exists():

                continue

            for desktop_file in directory.glob("*.desktop"):

                parser = configparser.ConfigParser(interpolation=None)

                try:

                    parser.read(desktop_file)

                    if "Desktop Entry" not in parser:

                        continue

                    entry = parser["Desktop Entry"]

                    name = entry.get("Name")

                    exec_cmd = entry.get("Exec")

                    if not name or not exec_cmd:

                        continue

                    exec_cmd = exec_cmd.split()[0]

                    self.apps[name.lower()] = {

                        "name": name,

                        "exec": exec_cmd,

                        "desktop": str(desktop_file),

                    }

                except Exception:

                    continue

    def get(self, name: str):

        query = name.lower().strip()

        # Exact match
        if query in self.apps:
            return self.apps[query]

        # Fuzzy search
        match = process.extractOne(
            query,
        self.apps.keys(),
        scorer=fuzz.WRatio,
        score_cutoff=70,
        )

        if match is None:
            return None

        matched_name = match[0]

        return self.apps[matched_name]

    def list(self):

        return sorted(self.apps.keys())