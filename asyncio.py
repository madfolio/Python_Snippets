import asyncio

class TimedEvent:
    def __init__(self, name, delay):
        self.name = name
        self.delay = delay

    async def start(self):
        print(f"{self.name} started!")
        await asyncio.sleep(self.delay)
        print(f"{self.name} finished!")

# Create events
event1 = TimedEvent("Event 1", 10)
event2 = TimedEvent("Event 2", 5)

# Run events concurrently in Jupyter
async def main():
    await asyncio.gather(event1.start(), event2.start())

# If using Jupyter, use await or nest_asyncio
await main()
