# 华东理工大学自动健康打卡

## 特点
 * 每日零点自动填报，全部自动
 * 支持多人同时打卡，打卡结果分别显示
 * 账号和密码以Secret形式存储于自己仓库内，正常使用不会导致泄露

## 部署
### 1. 点击右上角的star和fork加入自己的仓库
![image](https://user-images.githubusercontent.com/30517062/193272730-a7d0154d-d23e-440c-a0b6-06733fc30b8f.png)
### 2. 分别点击settings，actions，new repository secret 
![image](https://user-images.githubusercontent.com/30517062/193273198-e08ef3ec-0912-441e-a334-eb8731aca9c6.png)
### 3. `Name` 处输入 `ACCOUNT` ，`Secret`处输入你的学号与信息办密码
具体格式为`学号 密码 学号 密码 ...`。例如`19001234 jkl123456`(单人使用)和`20001111 abc123456 21001235 efg987645 22001234 asd147258`(多人使用)。**注意：你的密码不能是S+身份证后8位，若是，请登录[华理信息办](https://i.ecust.edu.cn/)，点右上角登入后自行修改密码。**
![image](https://user-images.githubusercontent.com/30517062/193273739-632909dd-aaf6-4fc0-84cd-6b3cecbd62a5.png)
最后点击 `Add secret`
### 4. 启动workflow
按下图点击。确保打开workflow
![image](https://user-images.githubusercontent.com/30517062/193445833-ae8c6ab9-018a-439f-b685-783d7514dbe8.png)
## 手动运行脚本
随便更改readme内的内容进行一次push就行了。
