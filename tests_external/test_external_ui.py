from playwright.sync_api import Page, expect

base_url = "https://demo.applitools.com/"


def test_login_valid_credentials(page: Page):
    page.goto(base_url)
    page.get_by_placeholder("username").fill("test_user")
    page.get_by_placeholder("password").fill("test_password")
    page.click("#log-in")
    expect(page).to_have_url("https://demo.applitools.com/app.html")


def test_ui_elements_exist(page: Page):
    page.goto(base_url)
    expect(page.get_by_placeholder("username")).to_be_visible()
    expect(page.get_by_placeholder("password")).to_be_visible()
    expect(page.locator("#log-in")).to_be_visible()
