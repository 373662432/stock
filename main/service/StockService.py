# coding=utf-8

import requests
from flask_apscheduler import APScheduler
from config import Common
from log import Log



class StockService(object):

    def get(self, stock_number='sz300059'):
        """
        传入股票代码，查询相关信息
        :param stock_number: 股票代码, 默认是东方财富编号sz300059
        :return: 返回一个json
        """
        response = self.request(Common.STOCK_URL + stock_number)
        stock_information = response.replace('var hq_str_' + stock_number + '="', '').replace('";', '')
        if len(stock_information) == 1:
            Log.record_log('WARNING', "stock number is invalid... ")
            return ""
        stock_info_list = stock_information.split(",")
        stock_info_list_title = ["股票名字", "今日开盘价", "昨日收盘价", "当前价格", "今日最高价", "今日最低价",
                                 "竞买价，即买一报价", "竞卖价，即卖一报价", "成交的股票数","成交金额",
                                 "买一手数", "买一报价", "买二手数", "买二报价", "买三手数", "买三报价", "买四手数", "买四报价", "买五手数", "买五报价",
                                 "卖一手数", "卖一报价", "卖二手数", "卖二报价", "卖三手数", "卖三报价", "卖四手数", "卖四报价", "卖五手数", "卖五报价",
                                 "时间"]
        stock_info_dict = {}
        for index, i in enumerate(stock_info_list_title):
            stock_info_dict[i] = stock_info_list[index]
        return stock_info_dict

    def request(self, url):
        """
        访问统一控制
        :param url: 传入一个URL统一资源符
        :return: 返回访问的body
        """
        try:
            Log.record_log('INFO', 'Start requesting... ' + url)
            response = requests.get(url)
            response.enconding = 'utf-8'
        except Exception as arr:
            Log.record_log('WARNING', 'request failed... ' + str(arr))
            return ""
        return response.text
