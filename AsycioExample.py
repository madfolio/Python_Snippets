import asyncio

locations = [1,2,3,4,5,6]

class trains:
    def __init__(self, Route, CV, Speed, delay):
        self.CV = CV
        self.Route = Route
        self.delay = delay

    async def start(self):
        print(f"{self.CV} started {self.Route}!")
        await asyncio.sleep(self.delay)
        print(f"{self.CV} finished {self.Route}!")

# Create events
event1 = trains("Route 1", 9, 0.35, 8)
event2 = trains("Route 2", 8, 0.25, 5)

# Run events concurrently in Jupyter
async def main():
    await asyncio.gather(event1.start(), event2.start())

# If using Jupyter, use await or nest_asyncio
await main()
