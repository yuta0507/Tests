from selenium import webdriver
import time

driver_path = "/Users/yuta/Chromedriver/chromedriver"

driver = webdriver.Chrome(executable_path=driver_path)

# 開く
driver.get("http://localhost:8888/mini_bbs/login.php")

# Email/PASSを入力
email = driver.find_element_by_name("email")
email.send_keys("yuta@yuta.com")
password = driver.find_element_by_name("password")
password.send_keys("1111")

# ログインボタンをクリック
login_button = driver.find_element_by_id("login")
login_button.click()

time.sleep(1)

# メッセージ入力
input_text = driver.find_element_by_name("message")
input_text.send_keys("Test posting is succeeded")

# メッセージ投稿
post = driver.find_element_by_id("post")
post.click()

time.sleep(1)

# ログアウト
logout = driver.find_element_by_id("logout")
logout.click()

time.sleep(1)

# 閉じる
driver.quit()