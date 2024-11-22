from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.chrome.options import Options
import pandas as pd
import os
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import json

# 创建Options对象以自定义Chrome设置
options = Options()
options.page_load_strategy = 'none'  # 解决速度慢问题
options.add_argument('blink-settings=imagesEnabled=false')  # 禁止图片加载
options.add_argument('--disable-javascript')  # 禁用javascript
options.add_argument('--disable-plugins')  # 禁用插件
options.add_argument('--disable-gpu')  # 禁用显卡

# 指定 ChromeDriver 的路径
driver = webdriver.Chrome(service=Service(r"C:\Users\29124\Desktop\chrome-win64\chromedriver.exe"), options=options)

# 设置要抓取的URL模板
base_url = 'https://you.ctrip.com/restaurantlist/Xian7/list-x175-c4915-p{}.html?ordertype=0'

# 定义只保留中英文字符和数字的函数
def keep_chinese_and_english(text):
    return re.sub(r'[^A-Za-z0-9\u4e00-\u9fa5]+', '', text)  # 只保留中英文字符和数字

# 读取上次保存的页码
def read_last_page():
    try:
        with open(r'C:\Users\29124\Desktop\爬虫数据\last_page.json', 'r') as f:
            data = json.load(f)
            return data.get('last_page', 1)  # 默认从第1页开始
    except (FileNotFoundError, json.JSONDecodeError):
        # 如果文件不存在或格式错误，初始化为第一页并创建文件
        with open(r'C:\Users\29124\Desktop\爬虫数据\last_page.json', 'w') as f:
            json.dump({'last_page': 1}, f)
        return 1  # 从第一页开始

# 保存当前页码
def save_last_page(page_number):
    with open(r'C:\Users\29124\Desktop\爬虫数据\last_page.json', 'w') as f:
        json.dump({'last_page': page_number}, f)

# 读取上次保存的页码
page_number = read_last_page()

# 存储所有餐厅信息的列表
all_restaurants = []

# 循环遍历所有页面
while True:
    url = base_url.format(page_number)  # 格式化URL以访问当前页

    # 添加异常处理
    try:
        driver.get(url)
    except Exception as e:
        print(f"访问页面 {url} 时出错: {e}")
        time.sleep(random.uniform(2, 5))  # 随机等待
        continue  # 跳过当前循环，尝试下一个页面

    time.sleep(random.uniform(2, 5))  # 随机等待页面加载

    # 获取当前页的餐厅信息
    list_mods = driver.find_elements(By.CLASS_NAME, 'list_mod2')

    # 如果没有找到餐厅信息，退出循环
    if not list_mods:
        break

    current_page_restaurants = []  # 存储当前页餐厅信息的列表

    # 遍历每个餐厅模块
    for index in range(len(list_mods)):
        list_mod = list_mods[index]
        try:
            # 获取餐厅信息
            name = keep_chinese_and_english(list_mod.find_element(By.CSS_SELECTOR, 'dt a').text.strip())
            address = keep_chinese_and_english(list_mod.find_elements(By.TAG_NAME, 'dd')[0].text.strip())
            avg_price = ""
            try:
                avg_price_text = list_mod.find_elements(By.TAG_NAME, 'dd')[1].find_element(By.CLASS_NAME, 'price').text.strip()
                avg_price_match = re.search(r'(\d+\.\d+|\d+)', avg_price_text)
                avg_price = avg_price_match.group(1) if avg_price_match else ""
            except:
                avg_price = ""

            # 获取评分
            rating = ""
            try:
                rating_element = WebDriverWait(list_mod, 3).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, '.score strong'))
                )
                rating = re.search(r'(\d+\.\d+)', rating_element.text.strip()).group(1)
            except:
                rating = ""

            # 获取点评数量
            review_count = keep_chinese_and_english(list_mod.find_element(By.CLASS_NAME, 'recomment').text.strip())

            # 获取餐厅类型列表
            type_links = list_mod.find_element(By.CLASS_NAME, 'bottomcomment').find_elements(By.TAG_NAME, 'a')
            types = [keep_chinese_and_english(link.text) for link in type_links]

            # 获取评论链接并点击进入二级页面
            comment_link = list_mod.find_element(By.CLASS_NAME, 'recomment').get_attribute('href')
            driver.get(comment_link)

            # 等待二级页面加载
            time.sleep(random.uniform(2, 5))  # 随机等待

            # 在二级页面获取详细评分分类
            detailed_rating_str = ""
            try:
                comment_count_section = driver.find_element(By.CLASS_NAME, 'comment_count')
                comment_items = comment_count_section.find_elements(By.CSS_SELECTOR, 'dd')
                detailed_rating = [f"{item.find_element(By.CLASS_NAME, 'l_title').text.strip()}{item.find_element(By.CLASS_NAME, 'score').text.strip()}" for item in comment_items]
                detailed_rating_str = "、".join(detailed_rating)
            except Exception:
                detailed_rating_str = ""

            # 获取特色美食
            special_dishes = ""
            try:
                special_dishes_element = driver.find_element(By.CSS_SELECTOR, 'div.text_style p')
                special_dishes = special_dishes_element.text.strip()
                special_dishes = re.sub(r'\s+', '', special_dishes)
            except Exception:
                special_dishes = ""

            # 获取评论
            comments = driver.find_elements(By.CSS_SELECTOR, 'li[itemprop="description"]')
            comment_texts = []
            if comments:
                for comment in comments:
                    text = comment.text.strip()
                    sentences = re.split(r'[，\n\s]+', text)
                    cleaned_sentences = [keep_chinese_and_english(s) for s in sentences if s]
                    comment_texts.append("，".join(cleaned_sentences))
            else:
                comment_texts = [""]

            # 将评分和其他信息添加到餐厅信息中
            restaurant_info = {
                'name': name,
                'address': address,
                'avg_price': avg_price,
                'rating': rating,
                'detailed_rating': detailed_rating_str,
                'review_count': review_count,
                'cuisine': types,
                'special_dishes': special_dishes,
                'comments': comment_texts
            }
            current_page_restaurants.append(restaurant_info)

            # 返回到列表页面
            driver.back()
            time.sleep(random.uniform(3, 4))  # 随机等待

            # 重新获取餐厅列表元素
            list_mods = driver.find_elements(By.CLASS_NAME, 'list_mod2')

        except Exception as e:
            print(f"解析餐厅时出错: {e}")

    # 打印当前页的餐厅信息
    print(f"页面{page_number}数据:")
    for restaurant in current_page_restaurants:
        print(restaurant)

    # 将当前页数据追加到总列表
    all_restaurants.extend(current_page_restaurants)

    # 将当前页数据保存到CSV文件
    try:
        df = pd.DataFrame(current_page_restaurants)
        df.to_csv(r'C:\Users\29124\Desktop\未央区\湘菜.csv', mode='a', index=False,
                  header=not os.path.isfile(r'C:\Users\29124\Desktop\未央区\湘菜.csv'),
                  encoding='utf-8-sig')
        print(f"第{page_number}页的数据保存成功.")

        # 更新最后保存的页码
        save_last_page(page_number)
    except Exception as e:
        print(f"保存错误:{e}")

    # 查找翻页按钮并等待其加载
    while True:
        try:
            next_page = WebDriverWait(driver, 4).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'nextpage'))
            )
            if next_page:
                page_number += 1
                next_page.click()
                break  # 成功翻页后退出循环
        except Exception as e:
            print(f"翻页时出错: {e}，尝试重新加载当前页面.")
            driver.get(url)  # 重新加载当前页面
            time.sleep(random.uniform(2, 5))  # 随机等待

# 关闭浏览器
driver.quit()
