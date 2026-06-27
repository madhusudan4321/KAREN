from .manager import desktop


def register(mcp):

    @mcp.tool()
    def desktop_manager(action: str, target: str = ""):
        """
        Perform desktop operations.

        Examples:
        open firefox
        close firefox
        restart code
        screenshot
        reboot
        shutdown
        """

        return desktop(action, target)