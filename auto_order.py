#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
小氢云商城自动化下单脚本
无需 AI 交互，直接通过命令行参数完成下单流程
"""

import sys
import json
import argparse
import requests
from typing import Dict, List, Optional

API_BASE = "http://dilmurat.icu/api"


class XiaoQingYunAPI:
    """小氢云商城 API 封装"""
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        })
    
    def search_goods(self, keyword: str) -> List[Dict]:
        """搜索商品"""
        url = f"{API_BASE}/goods/search"
        params = {"keyword": keyword}
        resp = self.session.get(url, params=params, timeout=30)
        data = resp.json()
        
        if data.get("code") == 200:
            return data.get("data", [])
        return []
    
    def get_goods_detail(self, goods_id: int) -> Dict:
        """获取商品详情"""
        url = f"{API_BASE}/goods/detail"
        params = {"id": goods_id}
        resp = self.session.get(url, params=params, timeout=30)
        data = resp.json()
        
        if data.get("code") == 200:
            return data.get("data", {})
        return {}
    
    def search_courses(self, goods_id: int, inputs: Dict) -> List[Dict]:
        """搜索课程"""
        url = f"{API_BASE}/goods/courses"
        params = {
            "goods_id": goods_id,
            "inputs": json.dumps(inputs)
        }
        resp = self.session.get(url, params=params, timeout=30)
        data = resp.json()
        
        if data.get("code") == 200:
            return data.get("data", [])
        return []
    
    def create_order(self, goods_id: int, pay_type: str, num: int, 
                     inputs: Dict, course_id: str, course_name: str) -> Dict:
        """创建订单"""
        url = f"{API_BASE}/order/create"
        data = {
            "goods_id": goods_id,
            "pay": pay_type,
            "num": num,
            "inputs": json.dumps(inputs),
            "course_id": course_id,
            "course_name": course_name
        }
        resp = self.session.post(url, data=data, timeout=30)
        return resp.json()


class AutoOrder:
    """自动化下单流程"""
    
    def __init__(self):
        self.api = XiaoQingYunAPI()
    
    def interactive_order(self):
        """交互式下单流程"""
        print("=" * 50)
        print("小氢云商城自动化下单系统")
        print("=" * 50)
        
        # 1. 搜索商品
        print("\n【步骤1】搜索商品")
        keyword = input("请输入商品关键词 (如: 学习通/U校园/雨课堂): ").strip()
        
        goods_list = self.api.search_goods(keyword)
        if not goods_list:
            print("❌ 未找到相关商品")
            return
        
        print(f"\n找到 {len(goods_list)} 个商品:")
        for i, goods in enumerate(goods_list, 1):
            print(f"{i}. {goods['name']} (ID: {goods['id']}) - ¥{goods.get('price', 'N/A')}")
        
        # 选择商品
        choice = int(input("\n请选择商品编号: ")) - 1
        if choice < 0 or choice >= len(goods_list):
            print("❌ 无效选择")
            return
        
        selected_goods = goods_list[choice]
        goods_id = selected_goods['id']
        print(f"\n✅ 已选择: {selected_goods['name']}")
        
        # 2. 获取商品详情和输入字段
        print("\n【步骤2】填写订单信息")
        detail = self.api.get_goods_detail(goods_id)
        inputs_config = detail.get("input", [])
        
        user_inputs = {}
        for idx, field in enumerate(inputs_config):
            field_type = field.get("types")
            
            if field_type == 9:  # SKU 选择
                print(f"\n{idx}. {field.get('title', '规格')}:")
                for attr in field.get("attributes", []):
                    print(f"   - {attr.get('value')} (¥{attr.get('price', 'N/A')})")
                value = input("   请输入规格名称: ").strip()
                user_inputs[str(idx)] = value
                
            elif field_type == 1:  # 文本输入
                title = field.get("title", f"字段{idx}")
                value = input(f"{idx}. {title}: ").strip()
                user_inputs[str(idx)] = value
                
            elif field_type in [3, 4]:  # 隐藏字段，稍后自动填充
                pass
        
        # 3. 搜索课程
        print("\n【步骤3】搜索课程")
        print("正在查询课程列表...")
        
        courses = self.api.search_courses(goods_id, user_inputs)
        if not courses:
            print("❌ 未找到课程，请检查账号密码是否正确")
            return
        
        print(f"\n找到 {len(courses)} 门课程:")
        for i, course in enumerate(courses, 1):
            print(f"{i}. {course.get('name', '未知课程')}")
        
        course_choice = int(input("\n请选择课程编号: ")) - 1
        if course_choice < 0 or course_choice >= len(courses):
            print("❌ 无效选择")
            return
        
        selected_course = courses[course_choice]
        course_id = selected_course.get("id", "")
        course_name = selected_course.get("name", "")
        print(f"\n✅ 已选择课程: {course_name}")
        
        # 4. 选择支付方式并下单
        print("\n【步骤4】支付下单")
        print("支付方式: 1.微信支付(wxpay)  2.支付宝(alipay)  3.余额(type_money)")
        pay_choice = input("请选择支付方式(1/2/3，默认1): ").strip() or "1"
        
        pay_map = {"1": "wxpay", "2": "alipay", "3": "type_money"}
        pay_type = pay_map.get(pay_choice, "wxpay")
        
        num = int(input("购买数量(默认1): ").strip() or "1")
        
        print("\n正在创建订单...")
        result = self.api.create_order(
            goods_id=goods_id,
            pay_type=pay_type,
            num=num,
            inputs=user_inputs,
            course_id=course_id,
            course_name=course_name
        )
        
        if result.get("code") == 201:
            print("\n" + "=" * 50)
            print("✅ 订单创建成功!")
            print(f"订单号: {result.get('out_trade_no')}")
            print(f"支付链接: {result.get('url')}")
            print("=" * 50)
        else:
            print(f"\n❌ 下单失败: {result.get('msg', '未知错误')}")
    
    def quick_order(self, goods_id: int, inputs: Dict, course_index: int = 0,
                    pay_type: str = "wxpay", num: int = 1):
        """
        快速下单 - 无需交互，直接传入参数
        
        Args:
            goods_id: 商品ID
            inputs: 输入字段字典，如 {"0": "选修课", "1": "手机号", "2": "密码"}
            course_index: 选择第几个课程(从0开始)
            pay_type: 支付方式 wxpay/alipay/type_money
            num: 购买数量
        """
        # 1. 搜索课程
        courses = self.api.search_courses(goods_id, inputs)
        if not courses:
            return {"success": False, "msg": "未找到课程"}
        
        if course_index >= len(courses):
            return {"success": False, "msg": "课程索引超出范围"}
        
        selected_course = courses[course_index]
        course_id = selected_course.get("id", "")
        course_name = selected_course.get("name", "")
        
        # 2. 创建订单
        result = self.api.create_order(
            goods_id=goods_id,
            pay_type=pay_type,
            num=num,
            inputs=inputs,
            course_id=course_id,
            course_name=course_name
        )
        
        if result.get("code") == 201:
            return {
                "success": True,
                "order_no": result.get("out_trade_no"),
                "pay_url": result.get("url"),
                "course_name": course_name
            }
        else:
            return {"success": False, "msg": result.get("msg", "下单失败")}


def main():
    parser = argparse.ArgumentParser(description="小氢云商城自动化下单")
    parser.add_argument("--interactive", "-i", action="store_true", 
                        help="交互式下单模式")
    parser.add_argument("--goods", "-g", type=int, 
                        help="商品ID (如: 1=学习通全包)")
    parser.add_argument("--inputs", "-in", 
                        help="输入参数JSON，如: '{\"0\":\"选修课\",\"1\":\"手机号\",\"2\":\"密码\"}'")
    parser.add_argument("--course", "-c", type=int, default=0,
                        help="选择第几个课程(从0开始，默认0)")
    parser.add_argument("--pay", "-p", default="wxpay",
                        choices=["wxpay", "alipay", "type_money"],
                        help="支付方式")
    parser.add_argument("--num", "-n", type=int, default=1,
                        help="购买数量")
    
    args = parser.parse_args()
    
    order = AutoOrder()
    
    if args.interactive or len(sys.argv) == 1:
        # 交互式模式
        order.interactive_order()
    else:
        # 命令行模式
        if not args.goods or not args.inputs:
            print("❌ 请提供 --goods 和 --inputs 参数，或使用 --interactive 进入交互模式")
            parser.print_help()
            return
        
        try:
            inputs = json.loads(args.inputs)
        except json.JSONDecodeError:
            print("❌ --inputs 参数必须是有效的JSON格式")
            return
        
        print(f"正在下单: 商品ID={args.goods}, 课程索引={args.course}")
        result = order.quick_order(
            goods_id=args.goods,
            inputs=inputs,
            course_index=args.course,
            pay_type=args.pay,
            num=args.num
        )
        
        if result["success"]:
            print(f"\n✅ 下单成功!")
            print(f"订单号: {result['order_no']}")
            print(f"课程: {result['course_name']}")
            print(f"支付链接: {result['pay_url']}")
        else:
            print(f"\n❌ 下单失败: {result['msg']}")


if __name__ == "__main__":
    main()
