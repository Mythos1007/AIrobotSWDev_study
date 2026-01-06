# ﻿1. 프로젝트.

#    CRUD --> 미니 주소록(설비 및 운용장비), 명암관리(센서, 값 --> 통계, 분석)

#                  - Linux Log 파일?

#   추가프로젝트

#   1. 로그 분석기 ( /var/log --> syslog(kernel), dpkg.log(설치),   | apache2.log(Web log)

#                      -- 통계, 분석 --> sqlite 활용

#   2. 미니 시뮬레이터'

#                          - 가상 데이터 만들기 ( led, 온도, 조도, 습도 특정 시간마다 )

#                          - 분석기, 어플이 센서값 들을 읽어와 통계, 분석...

#                          - log 파일---> ((JSON)) --> DB 

# [ 화면 예제 ]

# ==================================================

#  시스템 이상 징후 요약 (syslog)

# ==================================================

# 분석 대상  : /var/log/syslog

# 기간       : 최근 6시간

# [중요 이벤트]

# - 서비스 재시작          : 7건

# - 장치 연결/해제         : 5건

# - 네트워크 단절          : 3건

# - 커널 경고              : 2건

# 서비스 재시작 상세

# - systemd: docker.service 재시작 (3회)

# - systemd: NetworkManager 재시작 (2회)

# - systemd: bluetooth.service 재시작 (2회)

# 장치 이벤트

# - USB disconnect : 3건

# - USB reconnect  : 2건

# 네트워크 이벤트

# - eth0 link down : 2회

# - eth0 link up   : 2회


# ==================================================

# ==================================================
#  시스템 이벤트 타임라인 (syslog)

# ==================================================
# 분석 파일 : /var/log/syslog

# 기간      : 2025-12-17 05:00 ~ 06:00

# 05:12  [WARN ] kernel        - CPU throttling activated

# 05:13  [INFO ] systemd      - docker.service restarted

# 05:14  [WARN ] NetworkManager - eth0 link down

# 05:14  [INFO ] NetworkManager - eth0 link up

# 05:15  [ERROR] systemd      - Failed to start camera.service

# 05:15  [INFO ] systemd      - camera.service restarted

# 05:16  [INFO ] kernel       - usb 1-1: device reset

# 요약 분석

# - 첫 이상 징후 : CPU throttling

# - 연쇄 이벤트  : 네트워크 끊김 → 서비스 실패 → 재시작

# - 추정 원인    : 시스템 부하 또는 전원 불안정

# ==================================================

# ========================================

#  Linux 인증 로그 요약 (auth.log)

# ========================================

# 총 로그 수       : 1,240

# 인식 성공      : 1,198

# 파싱 실패      : 42




# 인증 성공        : 1,012

# 인증 실패        : 72

# 기타             : 156



# 인증 실패 상위 IP

# 1) 203.0.113.44 : 31회

# 2) 198.51.100.12: 18회

# 3) 192.0.2.77   : 9회

# ========================================
import os
import sys
import time
import sqlite3
import datetime
import re
from collections import defaultdict
from typing import List, Tuple, Dict
import logging
import json
import argparse
import matplotlib.pyplot as plt
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')    
DB_NAME = 'system_logs.db'
LOG_DIR = '/var/log'
SYSLOG_PATH = os.path.join(LOG_DIR, 'syslog')
AUTHLOG_PATH = os.path.join(LOG_DIR, 'auth.log')
APACHELOG_PATH = os.path.join(LOG_DIR, 'apache2', 'access.log')
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS syslog (
                    id INTEGER PRIMARY KEY,
                    timestamp TEXT,
                    log_level TEXT,
                    component TEXT,
                    message TEXT
                )''')
    c.execute('''CREATE TABLE IF NOT EXISTS authlog (
                    id INTEGER PRIMARY KEY,
                    timestamp TEXT,
                    ip_address TEXT,
                    status TEXT,
                    message TEXT
                )''')
    conn.commit()
    conn.close()
def parse_syslog_line(line: str) -> Tuple[str, str, str, str]:
    match = re.match(r'^(?P<timestamp>\w{3} \d{1,2} \d{2}:\d{2}:\d{2}) (?P<host>\S+) (?P<component>\S+): (?P<message>.+)$', line)
    if match:
        timestamp_str = match.group('timestamp')
        timestamp = datetime.datetime.strptime(timestamp_str, '%b %d %H:%M:%S').replace(year=datetime.datetime.now().year)
        log_level = 'INFO'
        message = match.group('message')
        if 'error' in message.lower():
            log_level = 'ERROR'
        elif 'warn' in message.lower():
            log_level = 'WARN'
        return (timestamp.strftime(DATE_FORMAT), log_level, match.group('component'), message)
    return None
def parse_authlog_line(line: str) -> Tuple[str, str, str, str]:
    match = re.match(r'^(?P<timestamp>\w{3} \d{1,2} \d{2}:\d{2}:\d{2}) (?P<host>\S+) (?P<component>\S+): (?P<message>.+)$', line)
    if match:
        timestamp_str = match.group('timestamp')
        timestamp = datetime.datetime.strptime(timestamp_str, '%b %d %H:%M:%S').replace(year=datetime.datetime.now().year)
        message = match.group('message')
        ip_match = re.search(r'from (\d+\.\d+\.\d+\.\d+)', message)
        ip_address = ip_match.group(1) if ip_match else 'unknown'
        status = 'SUCCESS' if 'Accepted' in message else 'FAILURE' if 'Failed' in message else 'OTHER'
        return (timestamp.strftime(DATE_FORMAT), ip_address, status, message)
    return None
def ingest_syslog():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    with open(SYSLOG_PATH, 'r') as f:
        for line in f:
            parsed = parse_syslog_line(line)
            if parsed:
                c.execute('INSERT INTO syslog (timestamp, log_level, component, message) VALUES (?, ?, ?, ?)', parsed)
    conn.commit()
    conn.close()
def ingest_authlog():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    with open(AUTHLOG_PATH, 'r') as f:
        for line in f:
            parsed = parse_authlog_line(line)
            if parsed:
                c.execute('INSERT INTO authlog (timestamp, ip_address, status, message) VALUES (?, ?, ?, ?)', parsed)
    conn.commit()
    conn.close()
def summarize_syslog(hours: int = 6) -> Dict[str, int]:
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    time_threshold = (datetime.datetime.now() - datetime.timedelta(hours=hours)).strftime(DATE_FORMAT)
    c.execute('SELECT log_level, COUNT(*) FROM syslog WHERE timestamp >= ? GROUP BY log_level', (time_threshold,))
    summary = {row[0]: row[1] for row in c.fetchall()}
    conn.close()
    return summary
def summarize_authlog() -> Dict[str, int]:
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('SELECT status, COUNT(*) FROM authlog GROUP BY status')
    summary = {row[0]: row[1] for row in c.fetchall()}
    conn.close()
    return summary
def plot_authlog_summary(summary: Dict[str, int]):
    labels = summary.keys()
    sizes = summary.values()
    plt.figure(figsize=(8, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title('Authentication Log Summary')
    plt.show()
def main():
    parser = argparse.ArgumentParser(description='System Log Analyzer')
    parser.add_argument('--ingest', action='store_true', help='Ingest log files into the database')
    parser.add_argument('--summarize', action='store_true', help='Summarize log data')
    parser.add_argument('--plot', action='store_true', help='Plot authentication log summary')
    args = parser.parse_args()
    init_db()
    if args.ingest:
        logging.info('Ingesting syslog...')
        ingest_syslog()
        logging.info('Ingesting authlog...')
        ingest_authlog()
    if args.summarize:
        logging.info('Summarizing syslog...')
        syslog_summary = summarize_syslog()
        logging.info(f'Syslog Summary: {syslog_summary}')
        logging.info('Summarizing authlog...')
        authlog_summary = summarize_authlog()
        logging.info(f'Authlog Summary: {authlog_summary}')
    if args.plot:
        logging.info('Plotting authlog summary...')
        authlog_summary = summarize_authlog()
        plot_authlog_summary(authlog_summary)
if __name__ == '__main__':
    main()

