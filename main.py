import asyncio
import sys
import aioconsole
from playwright.async_api import async_playwright, Page, BrowserContext
from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax


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


console = Console()

console = Console()

class CLIBrowser:
    def __init__(self):
        self.playwright = None
        self.browser: Browser = None
        self.context: BrowserContext = None
        self.page: Page = None

    async def start(self):
        """Инициализация браузера и создание базовой сессии."""
        self.playwright = await async_playwright().start()
        self.browser = await self.playwright.chromium.launch(
            headless=True, 
            args=["--start-maximized"]
        )
        self.context = await self.browser.new_context(no_viewport=True)
        self.page = await self.context.new_page()

    async def process_address_bar(self, user_input: str):
        """ПЛЕЙСХОЛДЕР: Обработка введенного адреса."""
        console.print(f"[bold #f8f9fa]User input:[/] {user_input}")

    async def close(self):
        """Безопасное и последовательное закрытие ресурсов без зависания."""
        try:
            if self.page:
                await self.page.close()
            if self.context:
                await self.context.close()
            if self.browser:
                await self.browser.close()
            if self.playwright:
                await self.playwright.stop()
        except Exception as e:
            console.print(f"[dim red]Could not open: {e}[/]")


async def main():
    cli = CLIBrowser()
    await cli.start()

    try:
        while True:
            # Используем асинхронный ввод вместо run_in_executor
            user_input = await aioconsole.ainput("URL > ")
            
            address = user_input.strip()
            if not address:
                continue

            if address.lower() in ["exit", "quit"]:
                break

            await cli.process_address_bar(address)

    except (KeyboardInterrupt, asyncio.CancelledError):
        pass
    finally:
        console.print("\n[bold yellow]Stopping...[/]")
        await cli.close()
        console.print("[bold green]Done.[/]")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        sys.exit(0)
