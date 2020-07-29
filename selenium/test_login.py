import os
from selenium import webdriver
from selenium.webdriver import ChromeOptions

TEST_HOST = os.getenv("TEST_HOST") or "localhost"
TEST_PORT = os.getenv("TEST_PORT") or 3000

chrome_options = ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-gpu')


def test_signup():
    """
        This tests the signup page using a new username & password
    """

    driver = webdriver.Chrome(chrome_options=chrome_options)

    driver.get(f"http://{TEST_HOST}:{TEST_PORT}/users/sign_up")

    # if any of these aren't present, they will throw an exception and fail the test
    email_field = driver.find_element_by_id("user_email")
    password_field = driver.find_element_by_id("user_password")
    password_2_field = driver.find_element_by_id("user_password_confirmation")

    signup_button = driver.find_element_by_name("commit")

    email_field.send_keys("slackbeard+1@protonmail.com")
    password_field.send_keys("secret")
    password_2_field.send_keys("secret")

    signup_button.click()

    assert driver.current_url == f"http://{TEST_HOST}:{TEST_PORT}"

    message = driver.find_element_by_class_name("alert-success")

    # Check that we are welcomed, i.e. that we signed up:
    assert message.get_attribute("innerHTML").startswith("Welcome!")

def test_login_success():
    """
        This tests a successful login using a known user / pass from the fixture data
    """

    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get(f"http://{TEST_HOST}:{TEST_PORT}")

    # if any of these aren't present, they will throw an exception and fail the test
    email_field = driver.find_element_by_id("user_email")
    password_field = driver.find_element_by_id("user_password")
    login_button = driver.find_element_by_name("commit")

    # Log in using fixture data:
    email_field.send_keys("slackbeard@protonmail.com")
    password_field.send_keys("password")
    login_button.click()

    message = driver.find_element_by_class_name("alert-success")

    assert message.get_attribute("innerHTML").startswith("Signed in successfully")


if __name__ == "__main__":
    test_func()
