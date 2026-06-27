"""
System tools — time, environment info, shell commands, etc.
"""

import datetime
import platform
import socket
import getpass
import psutil


def register(mcp):

    @mcp.tool()
    def get_current_time() -> str:
        """Return the current date and time in ISO 8601 format."""
        return datetime.datetime.now().isoformat()

    @mcp.tool()
    def get_system_info() -> dict:
        """
        Return detailed information about the host system.
        """

        memory = psutil.virtual_memory()
        disk = psutil.disk_usage("/")

        battery = psutil.sensors_battery()

        return {
            "user": getpass.getuser(),

            "hostname": socket.gethostname(),

            "os": platform.system(),

            "os_version": platform.version(),

            "machine": platform.machine(),

            "python_version": platform.python_version(),

            "cpu_usage_percent": psutil.cpu_percent(interval=1),

            "memory": {
                "used_gb": round(memory.used / (1024 ** 3), 2),
                "total_gb": round(memory.total / (1024 ** 3), 2),
                "percent": memory.percent,
            },

            "disk": {
                "used_gb": round(disk.used / (1024 ** 3), 2),
                "total_gb": round(disk.total / (1024 ** 3), 2),
                "percent": disk.percent,
            },

            "boot_time": datetime.datetime.fromtimestamp(
                psutil.boot_time()
            ).strftime("%Y-%m-%d %H:%M:%S"),

            "battery": (
                None
                if battery is None
                else {
                    "percent": battery.percent,
                    "plugged": battery.power_plugged,
                }
            ),
        }

    @mcp.tool()
    def get_network_info() -> dict:
        """
        Return hostname and IP address.
        """

        hostname = socket.gethostname()

        try:
            ip = socket.gethostbyname(hostname)
        except Exception:
            ip = "Unavailable"

        return {
            "hostname": hostname,
            "ip_address": ip,
        }

    @mcp.tool()
    def get_cpu_usage() -> dict:
        """
        Return current CPU usage.
        """

        return {
            "cpu_usage_percent": psutil.cpu_percent(interval=1)
        }

    @mcp.tool()
    def get_memory_usage() -> dict:
        """
        Return RAM usage.
        """

        memory = psutil.virtual_memory()

        return {
            "used_gb": round(memory.used / (1024 ** 3), 2),
            "total_gb": round(memory.total / (1024 ** 3), 2),
            "percent": memory.percent,
        }

    @mcp.tool()
    def get_disk_usage() -> dict:
        """
        Return storage usage.
        """

        disk = psutil.disk_usage("/")

        return {
            "used_gb": round(disk.used / (1024 ** 3), 2),
            "total_gb": round(disk.total / (1024 ** 3), 2),
            "percent": disk.percent,
        }