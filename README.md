# LuoguCrawler
爬取洛谷markdown题面。

众所周知，洛谷题目页面有一个“复制markdown”按钮，由于洛谷代码做了混淆处理，本人也没法爬取。

直到看到 [luogu API](https://docs.lgapi.cn/open/openapi) 之后，才知道之前完全是浪费时间，经过了一番学习（其实是逼迫AI教我）后，写了一个爬取luogu双语题面的python代码，这里直接给出python代码，你只需要将这份代码放到工作目录，然后在另一份代码中调用 ```save_md``` 函数即可，不懂的话看下面的例子。

下载ls.py，拖到工作目录。

在工作目录下创建另外一个python文件，比如 ```app.py```。

输入以下内容：

```
import ls
ls.save_md("P1001")
```

此时，你的工作目录下就出现了 ```P1001.md``` 。
