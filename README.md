# 华东理工大学自动健康打卡

## 特点
 * 每日凌晨两点自动填报，全部自动
 * 支持多人同时打卡，打卡结果分别显示
 * 账号和密码以Secret形式存储于自己仓库内，正常使用不会导致泄露

## 部署
### 1. 点击右上角的star和fork加入自己的仓库
![image](https://user-images.githubusercontent.com/30517062/193272730-a7d0154d-d23e-440c-a0b6-06733fc30b8f.png)
### 2. 分别点击settings，actions，new repository secret 
![image](https://user-images.githubusercontent.com/30517062/193273198-e08ef3ec-0912-441e-a334-eb8731aca9c6.png)
### 3. `Name` 处输入 `ACCOUNT` ，`Secret`处输入你的学号与信息办密码
具体格式为学号,密码(;学号,密码;...)。例如19001234,123455678(单人使用)和20001111,23123556;21001235,213562321;22001234,09082847(多人使用)。**注意：你的密码不能是S+身份证后8位，若是，请登录华理信息办点右上角登入后自行修改密码。格式中标点 `,` 和 `;` 均为半角标点，使用全角标点 `，` 和 `；` 时即使学号密码正确也会导致打卡失败，请注意输入法的中英文状态。**
![image](https://user-images.githubusercontent.com/30517062/193273739-632909dd-aaf6-4fc0-84cd-6b3cecbd62a5.png)
最后点击 `Add secret`
