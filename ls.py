import requests
import os
import json

def save_md(pid):
    try:
        url = f"https://www.luogu.com.cn/problem/{pid}"
        headers = {
            "x-lentille-request": "content-only",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
        }
        r = requests.get(url, headers=headers)
        if r.status_code != 200:
            print(f"请求失败，状态码：{r.status_code}")
            return
        js = r.json()
        p = js["data"]["problem"]
        md = build_md(p)
        fn = f"{pid}_题目信息.md"
        with open(fn, "w", encoding="utf-8") as f:
            f.write(md)
        print(f"题目信息已成功保存到 {fn}")
    except Exception as e:
        print(f"处理请求时出错：{str(e)}")

def build_md(p):
    md = ""
    if p.get('content'):
        md = f"### [{p['content']['locale']}] : {p['pid']} {p['title']}\n\n"
        md += "#### 基本信息\n"
        md += f"- **题目编号**：{p['pid']}\n"
        md += f"- **类型**：{p['type']}\n"
        md += f"- **难度**：{p['difficulty']}\n"
        md += f"- **总提交数**：{p['totalSubmit']}\n"
        md += f"- **总通过数**：{p['totalAccepted']}\n\n"
        md += "#### 题目描述\n"
        md += f"{p['content']['description']}\n\n"
        md += "#### 输入格式\n"
        md += f"{p['content']['formatI']}\n\n"
        md += "#### 输出格式\n"
        md += f"{p['content']['formatO']}\n\n"
        for i, (iin, oout) in enumerate(p['samples']):
            md += f"#### 样例输入 {i+1}\n"
            md += f"```\n{iin}\n```\n\n"
            md += f"#### 样例输出 {i+1}\n"
            md += f"```\n{oout}\n```\n\n"
        if p['content']['hint']:
            md += "#### 说明/提示\n"
            md += f"{p['content']['hint']}\n\n"
    if p.get('contenu') and (not p.get('content') or p['contenu']['locale'] != p['content']['locale']):
        if p.get('content'):
            md += "-----\n"
        md += f"### [{p['contenu']['locale']}] : {p['pid']} {p['title']}\n\n"
        md += "#### 基本信息\n"
        md += f"- **题目编号**：{p['pid']}\n"
        md += f"- **类型**：{p['type']}\n"
        md += f"- **难度**：{p['difficulty']}\n"
        md += f"- **总提交数**：{p['totalSubmit']}\n"
        md += f"- **总通过数**：{p['totalAccepted']}\n\n"
        md += "#### 题目描述\n"
        md += f"{p['contenu']['description']}\n\n"
        md += "#### 输入格式\n"
        md += f"{p['contenu']['formatI']}\n\n"
        md += "#### 输出格式\n"
        md += f"{p['contenu']['formatO']}\n\n"
        for i, (iin, oout) in enumerate(p['samples']):
            md += f"#### 样例输入 {i+1}\n"
            md += f"```\n{iin}\n```\n\n"
            md += f"#### 样例输出 {i+1}\n"
            md += f"```\n{oout}\n```\n\n"
        if p['contenu']['hint']:
            md += "#### 说明/提示\n"
            md += f"{p['contenu']['hint']}\n\n"
    return md

# save_md("P12012")
