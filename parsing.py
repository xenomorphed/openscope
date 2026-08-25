import asyncio
import shlex


async def parse_command(cmd: str) -> list[str]:
    return await asyncio.to_thread(shlex.split, cmd, posix=True)
