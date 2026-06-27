from datetime import datetime


async def greet(session):
    """
    Generate a contextual greeting based on the current local time.
    """

    hour = datetime.now().hour

    if 22 <= hour or hour < 4:
        greeting = (
            "Greet Captain by saying: "
            "'Good evening, Captain. Burning the midnight oil again? "
            "How may I assist you tonight?'"
        )

    elif 4 <= hour < 12:
        greeting = (
            "Greet Captain by saying: "
            "'Good morning, Captain. Systems are online. "
            "How can I help you today?'"
        )

    elif 12 <= hour < 17:
        greeting = (
            "Greet Captain by saying: "
            "'Good afternoon, Captain. "
            "What would you like to work on?'"
        )

    else:
        greeting = (
            "Greet Captain by saying: "
            "'Good evening, Captain. "
            "What can I do for you?'"
        )

    await session.generate_reply(instructions=greeting)