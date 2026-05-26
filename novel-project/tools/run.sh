#!/bin/bash

echo ""
echo "╔═══════════════════════════════════════════════════════════╗"
echo "║         番茄作家助手自动提交工具                         ║"
echo "╚═══════════════════════════════════════════════════════════╝"
echo ""

cd "$(dirname "$0")"

show_menu() {
    echo "请选择操作:"
    echo ""
    echo "  1. 安装依赖"
    echo "  2. 启动调试浏览器"
    echo "  3. 提交单个章节"
    echo "  4. 批量提交章节"
    echo "  5. 运行示例"
    echo "  0. 退出"
    echo ""
    read -p "请输入选项: " choice
    
    case $choice in
        1) install_deps ;;
        2) start_browser ;;
        3) submit_single ;;
        4) submit_batch ;;
        5) run_example ;;
        0) echo ""; echo "再见!"; exit 0 ;;
        *) show_menu ;;
    esac
}

install_deps() {
    echo ""
    echo "[安装依赖]"
    echo ""
    pip install -r fanqie_publisher/requirements.txt
    echo ""
    echo "安装Playwright浏览器..."
    playwright install chromium
    echo ""
    echo "✅ 安装完成"
    read -p "按回车继续..."
    show_menu
}

start_browser() {
    echo ""
    echo "[启动调试浏览器]"
    echo ""
    python -m fanqie_publisher.cli browser --start
    read -p "按回车继续..."
    show_menu
}

submit_single() {
    echo ""
    echo "[提交单个章节]"
    echo ""
    read -p "请输入章节文件路径: " file
    python -m fanqie_publisher.cli submit -f "$file"
    read -p "按回车继续..."
    show_menu
}

submit_batch() {
    echo ""
    echo "[批量提交章节]"
    echo ""
    read -p "请输入章节目录 (默认为../正文): " dir
    if [ -z "$dir" ]; then
        dir="../正文"
    fi
    python -m fanqie_publisher.cli batch -d "$dir" --sort -o "$dir/submit_report.json"
    read -p "按回车继续..."
    show_menu
}

run_example() {
    echo ""
    echo "[运行示例]"
    echo ""
    python fanqie_publisher/examples.py
    read -p "按回车继续..."
    show_menu
}

case "$1" in
    install) install_deps ;;
    browser) start_browser ;;
    submit) submit_single ;;
    batch) submit_batch ;;
    *) show_menu ;;
esac
