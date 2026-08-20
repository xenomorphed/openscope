import asyncio
from playwright.async_api import async_playwright


print("""
  ██████╗  ██████╗  ███████╗ ███╗   ██╗ ███████╗  ██████╗  ██████╗  ██████╗  ███████╗
 ██╔═══██╗ ██╔══██╗ ██╔════╝ ████╗  ██║ ██╔════╝ ██╔════╝ ██╔═══██╗ ██╔══██╗ ██╔════╝
 ██║   ██║ ██████╔╝ █████╗   ██╔██╗ ██║ ███████╗ ██║      ██║   ██║ ██████╔╝ █████╗
 ██║   ██║ ██╔═══╝  ██╔══╝   ██║╚██╗██║ ╚════██║ ██║      ██║   ██║ ██╔═══╝  ██╔══╝
 ╚██████╔╝ ██║      ███████╗ ██║ ╚████║ ███████║ ╚██████╗ ╚██████╔╝ ██║      ███████╗
  ╚═════╝  ╚═╝      ╚══════╝ ╚═╝  ╚═══╝ ╚══════╝  ╚═════╝  ╚═════╝  ╚═╝      ╚══════╝

by xenomorphed
GitHub: https://github.com/xenomorphed
""")


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        await page.goto("https://python.org")

        print(page.content)

        await browser.close()

asyncio.run(main())
