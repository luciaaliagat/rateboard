from playwright.async_api import async_playwright
from playwright_stealth import stealth_async


async def launch_browser():
    playwright = await async_playwright().start()
    browser = await playwright.chromium.launch(headless=True)
    return playwright, browser


async def navigate(browser, url):
    page = await browser.new_page()
    await page.goto(url)
    await stealth_async(page)
    return page


async def extract(page, selector):
    await page.wait_for_selector(selector)
    return (await page.locator(selector).inner_text()).strip()


def clean_text(text, strip_list):
    for s in strip_list:
        text = text.replace(s, "")
    return text


def parse_float(text):
    try:
        return float(text.replace(",", ""))
    except ValueError:
        return None


async def fetch_rates(
    url, buy_selector, sell_selector,
    buy_strip=None, sell_strip=None
):
    buy_strip = buy_strip or []
    sell_strip = sell_strip or []

    playwright, browser = await launch_browser()

    try:
        page = await navigate(browser, url)

        buy_text = await extract(page, buy_selector)
        sell_text = await extract(page, sell_selector)

        buy_clean = clean_text(buy_text, buy_strip)
        sell_clean = clean_text(sell_text, sell_strip)

        buy_rate = parse_float(buy_clean)
        sell_rate = parse_float(sell_clean)

        if buy_rate is None or sell_rate is None:
            print("Error parsing rates.")
            return None

        return buy_rate, sell_rate

    finally:
        await browser.close()
        await playwright.stop()
