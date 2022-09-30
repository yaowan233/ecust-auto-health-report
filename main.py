from playwright.sync_api import Playwright, sync_playwright
from playwright._impl._api_types import TimeoutError as Terror
import os


def run(playwright: Playwright, stu_id, password) -> None:
    browser = playwright.chromium.launch()
    context = browser.new_context()
    # Open new page
    page = context.new_page()
    page.goto(
        "https://sso.ecust.edu.cn/authserver/login?service=https%3A%2F%2Fworkflow.ecust.edu.cn%2Fdefault%2Fwork%2Fuust%2Fzxxsmryb%2Fmrybcn.jsp")
    # Click [placeholder="用户名"]
    page.click("[placeholder=\"用户名\"]")
    print(1)
    # Fill [placeholder="用户名"]
    page.fill("[placeholder=\"用户名\"]", stu_id)
    print(2)
    # Click [placeholder="密码"]
    page.click("[placeholder=\"密码\"]")
    print(3)
    # Fill [placeholder="密码"]
    page.fill("[placeholder=\"密码\"]", password)
    print(4)
    # Click button:has-text("登录")
    page.click("button:has-text(\"登录\")")
    print(5)
    # assert page.url == "https://workflow.ecust.edu.cn/default/work/uust/zxxsmryb/mrybcn.jsp"
    # Click ins
    page.click("ins")
    # Click text=下一步
    page.click("text=下一步")
    page.click("label:has-text(\"健康\")")
    # Click #radio_sfycxxwc42
    page.click("#radio_sfycxxwc42")
    # Click text=*行程码是否绿码： 是否 >> ins
    page.click("#radio_xcm5")
    page.click("text=在上海")
    # Click text=提交
    page.click("text=提交")
    # Click text=确定
    page.click("text=确定")
    # Click text=确定
    page.click("text=确定")
    # ---------------------
    context.close()
    browser.close()


data = os.environ.get('ACCOUNT').split(';')  # 字符串预处理

for i in data:
    account, password = i.split(',')
    print(account, password)
    try:
        with sync_playwright() as playwright:
            run(playwright, account.strip(), password.strip())
    except Terror:
        print('健康打卡失败，可能已自行打卡，请注意需自行填写')
        raise
    except Exception as e:
        print(f'健康打卡失败 错误原因{e}')
        raise
    else:
        print(f'{account} 今日已完成健康打卡')
