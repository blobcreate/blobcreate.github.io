#!/usr/bin/env python3
"""
简单的HTTP服务器，用于在本地测试HTML批量处理工具
使用方法：
1. 在终端中，导航到此文件所在目录
2. 运行命令：python3 server.py
3. 在浏览器中访问：http://localhost:6500
"""

import http.server
import socketserver
import os

PORT = 6500

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        http.server.SimpleHTTPRequestHandler.end_headers(self)
    
    def do_GET(self):
        # 处理根路径请求，重定向到index.html
        if self.path == '/':
            self.path = './'
        # pp/docs 自动定向到 pp/docs.html 但是不改变地址栏显示
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

handler = MyHTTPRequestHandler

with socketserver.TCPServer(("", PORT), handler) as httpd:
    print(f"服务器运行在 http://localhost:{PORT}")
    print("按 Ctrl+C 停止服务器")
    httpd.serve_forever()