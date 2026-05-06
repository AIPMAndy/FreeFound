#!/usr/bin/env python3
"""
FreeFound API Server
提供简单的 REST API 访问数据
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import os
from urllib.parse import urlparse, parse_qs

class FreeFoundAPIHandler(BaseHTTPRequestHandler):
    
    def _set_headers(self, status=200):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
    
    def do_OPTIONS(self):
        self._set_headers()
    
    def do_GET(self):
        parsed_path = urlparse(self.path)
        path = parsed_path.path
        query = parse_qs(parsed_path.query)
        
        # 路由处理
        if path == '/api/hackathons':
            self.get_hackathons(query)
        elif path == '/api/incubators':
            self.get_incubators(query)
        elif path == '/api/stats':
            self.get_stats()
        elif path == '/':
            self.get_info()
        else:
            self._set_headers(404)
            self.wfile.write(json.dumps({
                "error": "Not Found",
                "message": "API endpoint not found"
            }).encode())
    
    def get_hackathons(self, query):
        """获取黑客松数据"""
        try:
            with open('data/hackathons.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # 筛选参数
            location = query.get('location', [None])[0]
            source = query.get('source', [None])[0]
            limit = int(query.get('limit', [100])[0])
            
            # 过滤数据
            if location:
                data = [h for h in data if location in h.get('location', '')]
            
            if source:
                data = [h for h in data if source in h.get('source', '')]
            
            # 限制返回数量
            data = data[:limit]
            
            self._set_headers()
            self.wfile.write(json.dumps({
                "success": True,
                "count": len(data),
                "data": data
            }, ensure_ascii=False).encode('utf-8'))
            
        except Exception as e:
            self._set_headers(500)
            self.wfile.write(json.dumps({
                "error": "Internal Server Error",
                "message": str(e)
            }).encode())
    
    def get_incubators(self, query):
        """获取孵化器数据"""
        try:
            with open('data/incubators.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # 筛选参数
            location = query.get('location', [None])[0]
            type_ = query.get('type', [None])[0]
            limit = int(query.get('limit', [100])[0])
            
            # 过滤数据
            if location:
                data = [i for i in data if location in i.get('location', '')]
            
            if type_:
                data = [i for i in data if type_ in i.get('type', '')]
            
            # 限制返回数量
            data = data[:limit]
            
            self._set_headers()
            self.wfile.write(json.dumps({
                "success": True,
                "count": len(data),
                "data": data
            }, ensure_ascii=False).encode('utf-8'))
            
        except Exception as e:
            self._set_headers(500)
            self.wfile.write(json.dumps({
                "error": "Internal Server Error",
                "message": str(e)
            }).encode())
    
    def get_stats(self):
        """获取统计信息"""
        try:
            with open('data/hackathons.json', 'r', encoding='utf-8') as f:
                hackathons = json.load(f)
            
            with open('data/incubators.json', 'r', encoding='utf-8') as f:
                incubators = json.load(f)
            
            # 统计信息
            stats = {
                "hackathons": {
                    "total": len(hackathons),
                    "by_source": {},
                    "by_location": {}
                },
                "incubators": {
                    "total": len(incubators),
                    "by_type": {},
                    "by_location": {}
                }
            }
            
            # 黑客松统计
            for h in hackathons:
                source = h.get('source', 'Unknown')
                location = h.get('location', 'Unknown')
                stats['hackathons']['by_source'][source] = stats['hackathons']['by_source'].get(source, 0) + 1
                stats['hackathons']['by_location'][location] = stats['hackathons']['by_location'].get(location, 0) + 1
            
            # 孵化器统计
            for i in incubators:
                type_ = i.get('type', 'Unknown')
                location = i.get('location', 'Unknown')
                stats['incubators']['by_type'][type_] = stats['incubators']['by_type'].get(type_, 0) + 1
                stats['incubators']['by_location'][location] = stats['incubators']['by_location'].get(location, 0) + 1
            
            self._set_headers()
            self.wfile.write(json.dumps({
                "success": True,
                "data": stats
            }, ensure_ascii=False).encode('utf-8'))
            
        except Exception as e:
            self._set_headers(500)
            self.wfile.write(json.dumps({
                "error": "Internal Server Error",
                "message": str(e)
            }).encode())
    
    def get_info(self):
        """API 信息"""
        info = {
            "name": "FreeFound API",
            "version": "1.0.0",
            "description": "黑客松与孵化器信息聚合 API",
            "endpoints": {
                "/api/hackathons": {
                    "method": "GET",
                    "description": "获取黑客松列表",
                    "params": {
                        "location": "按地点筛选（可选）",
                        "source": "按来源筛选（可选）",
                        "limit": "返回数量限制（默认100）"
                    },
                    "example": "/api/hackathons?location=北京&limit=10"
                },
                "/api/incubators": {
                    "method": "GET",
                    "description": "获取孵化器列表",
                    "params": {
                        "location": "按地点筛选（可选）",
                        "type": "按类型筛选（可选）",
                        "limit": "返回数量限制（默认100）"
                    },
                    "example": "/api/incubators?location=北京&limit=10"
                },
                "/api/stats": {
                    "method": "GET",
                    "description": "获取统计信息",
                    "example": "/api/stats"
                }
            },
            "github": "https://github.com/AIPMAndy/FreeFound"
        }
        
        self._set_headers()
        self.wfile.write(json.dumps(info, ensure_ascii=False, indent=2).encode('utf-8'))
    
    def log_message(self, format, *args):
        """自定义日志格式"""
        print(f"[{self.log_date_time_string()}] {format % args}")


def run_server(port=8080):
    """启动 API 服务器"""
    server_address = ('', port)
    httpd = HTTPServer(server_address, FreeFoundAPIHandler)
    
    print("=" * 60)
    print(f"🚀 FreeFound API Server")
    print("=" * 60)
    print(f"📡 服务地址: http://localhost:{port}")
    print(f"📚 API 文档: http://localhost:{port}/")
    print(f"🎯 黑客松: http://localhost:{port}/api/hackathons")
    print(f"🏢 孵化器: http://localhost:{port}/api/incubators")
    print(f"📊 统计: http://localhost:{port}/api/stats")
    print("=" * 60)
    print("按 Ctrl+C 停止服务\n")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\n👋 服务已停止")
        httpd.server_close()


if __name__ == "__main__":
    import sys
    
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
    run_server(port)
