import asyncio

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from ai_agent import execution_agent

async def main():
    result = await execution_agent.agent_chatopenai_4o.run()
    print(result)

asyncio.run(main())

