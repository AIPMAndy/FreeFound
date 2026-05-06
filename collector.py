#!/usr/bin/env python3
"""
FreeFound 数据收集器
自动从多个平台收集黑客松和孵化器信息
"""

import requests
import json
import time
from datetime import datetime
from typing import List, Dict
import re

class HackathonCollector:
    """黑客松信息收集器"""
    
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        }
        self.hackathons = []
    
    def collect_huodongxing(self, pages=10):
        """收集活动行的黑客松数据"""
        print("📍 收集活动行数据...")
        
        for page in range(1, pages + 1):
            url = f"https://www.huodongxing.com/search?qs=%E9%BB%91%E5%AE%A2%E6%9D%BE&page={page}"
            
            try:
                resp = requests.get(url, headers=self.headers, timeout=10)
                html = resp.text
                
                # 提取活动ID
                event_ids = re.findall(r'/event/(\d+)', html)
                
                for event_id in set(event_ids):
                    event_url = f"https://www.huodongxing.com/event/{event_id}"
                    
                    # 获取活动详情
                    try:
                        detail_resp = requests.get(event_url, headers=self.headers, timeout=10)
                        detail_html = detail_resp.text
                        
                        # 提取标题
                        title_match = re.search(r'<h1[^>]*>([^<]+)</h1>', detail_html)
                        title = title_match.group(1).strip() if title_match else f"活动{event_id}"
                        
                        # 提取时间
                        time_match = re.search(r'(\d{4}\.\d{2}\.\d{2}[-~]\d{4}\.\d{2}\.\d{2})', detail_html)
                        event_time = time_match.group(1) if time_match else ""
                        
                        # 提取地点
                        location_match = re.search(r'<span[^>]*class="[^"]*location[^"]*"[^>]*>([^<]+)</span>', detail_html)
                        location = location_match.group(1).strip() if location_match else ""
                        
                        self.hackathons.append({
                            "title": title,
                            "time": event_time,
                            "location": location,
                            "link": event_url,
                            "source": "活动行",
                            "collected_at": datetime.now().isoformat()
                        })
                        
                        print(f"  ✓ {title}")
                        time.sleep(0.5)  # 避免请求过快
                        
                    except Exception as e:
                        print(f"  ✗ 活动 {event_id} 详情获取失败: {e}")
                        continue
                
                time.sleep(1)
                
            except Exception as e:
                print(f"  ✗ 第 {page} 页失败: {e}")
                continue
        
        print(f"✅ 活动行收集完成: {len(self.hackathons)} 条\n")
    
    def collect_segmentfault(self):
        """收集思否（SegmentFault）的黑客松数据"""
        print("📍 收集思否数据...")
        
        url = "https://segmentfault.com/events?type=hackathon"
        
        try:
            resp = requests.get(url, headers=self.headers, timeout=10)
            html = resp.text
            
            # 简单提取（实际需要根据页面结构调整）
            event_links = re.findall(r'href="(/e/[^"]+)"', html)
            
            for link in set(event_links):
                full_url = f"https://segmentfault.com{link}"
                self.hackathons.append({
                    "title": "思否黑客松活动",
                    "link": full_url,
                    "source": "SegmentFault",
                    "collected_at": datetime.now().isoformat()
                })
            
            print(f"✅ 思否收集完成: {len(event_links)} 条\n")
            
        except Exception as e:
            print(f"✗ 思否收集失败: {e}\n")
    
    def collect_juejin(self):
        """收集掘金的黑客松数据"""
        print("📍 收集掘金数据...")
        
        # 掘金活动API（需要根据实际情况调整）
        url = "https://api.juejin.cn/interact_api/v1/event/list"
        
        try:
            resp = requests.post(url, headers=self.headers, json={
                "keyword": "黑客松",
                "page_no": 1,
                "page_size": 20
            }, timeout=10)
            
            data = resp.json()
            
            if data.get('data'):
                for event in data['data']:
                    self.hackathons.append({
                        "title": event.get('title', ''),
                        "time": event.get('start_time', ''),
                        "link": event.get('url', ''),
                        "source": "掘金",
                        "collected_at": datetime.now().isoformat()
                    })
            
            print(f"✅ 掘金收集完成\n")
            
        except Exception as e:
            print(f"✗ 掘金收集失败: {e}\n")
    
    def save(self, filepath="data/hackathons.json"):
        """保存数据"""
        # 去重
        unique_hackathons = []
        seen_links = set()
        
        for h in self.hackathons:
            if h['link'] not in seen_links:
                seen_links.add(h['link'])
                unique_hackathons.append(h)
        
        # 按时间排序（最新的在前）
        unique_hackathons.sort(key=lambda x: x.get('time', ''), reverse=True)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(unique_hackathons, f, ensure_ascii=False, indent=2)
        
        print(f"💾 已保存 {len(unique_hackathons)} 条黑客松数据到 {filepath}")


class IncubatorCollector:
    """孵化器信息收集器"""
    
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        }
        self.incubators = []
    
    def collect_36kr(self):
        """收集36氪的孵化器数据"""
        print("📍 收集36氪孵化器数据...")
        
        # 36氪创投数据库（需要根据实际API调整）
        url = "https://36kr.com/api/search/entity"
        
        try:
            resp = requests.post(url, headers=self.headers, json={
                "keyword": "孵化器",
                "type": "organization"
            }, timeout=10)
            
            data = resp.json()
            
            # 处理返回数据
            print(f"✅ 36氪收集完成\n")
            
        except Exception as e:
            print(f"✗ 36氪收集失败: {e}\n")
    
    def collect_itjuzi(self):
        """收集IT桔子的孵化器数据"""
        print("📍 收集IT桔子数据...")
        
        url = "https://www.itjuzi.com/investfirm?type=incubator"
        
        try:
            resp = requests.get(url, headers=self.headers, timeout=10)
            html = resp.text
            
            # 提取孵化器信息
            print(f"✅ IT桔子收集完成\n")
            
        except Exception as e:
            print(f"✗ IT桔子收集失败: {e}\n")
    
    def add_manual_data(self):
        """添加手工整理的权威数据"""
        print("📍 添加手工整理的孵化器数据...")
        
        # 北京市科委认定的孵化器名单
        beijing_incubators = [
            {
                "name": "中关村创业大街",
                "location": "北京海淀",
                "type": "综合孵化器",
                "level": "国家级",
                "focus": "科技创业",
                "website": "http://www.zgc-innoway.com/"
            },
            # 更多数据...
        ]
        
        self.incubators.extend(beijing_incubators)
        print(f"✅ 添加 {len(beijing_incubators)} 条手工数据\n")
    
    def save(self, filepath="data/incubators.json"):
        """保存数据"""
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(self.incubators, f, ensure_ascii=False, indent=2)
        
        print(f"💾 已保存 {len(self.incubators)} 条孵化器数据到 {filepath}")


def main():
    print("=" * 60)
    print("FreeFound 数据收集器")
    print("=" * 60)
    print()
    
    # 收集黑客松数据
    print("🎯 开始收集黑客松数据...\n")
    hackathon_collector = HackathonCollector()
    hackathon_collector.collect_huodongxing(pages=5)
    # hackathon_collector.collect_segmentfault()
    # hackathon_collector.collect_juejin()
    hackathon_collector.save()
    
    print()
    
    # 收集孵化器数据
    print("🏢 开始收集孵化器数据...\n")
    incubator_collector = IncubatorCollector()
    # incubator_collector.collect_36kr()
    # incubator_collector.collect_itjuzi()
    incubator_collector.add_manual_data()
    incubator_collector.save()
    
    print()
    print("=" * 60)
    print("✅ 数据收集完成！")
    print("=" * 60)


if __name__ == "__main__":
    main()
