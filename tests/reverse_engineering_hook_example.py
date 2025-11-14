#!/usr/bin/env python3
"""
JS 逆向场景：拦截加密数据后自动停止所有定时器

场景说明：
- 网页 JS 代码不可控（不能修改源码）
- JS 中有多个定时器在运行
- Hook 拦截到目标数据后需要立即停止所有定时器
- 避免定时器继续占用资源
"""

import never_jscore

print("=" * 70)
print("JS 逆向场景：Hook 拦截 + 自动清理定时器")
print("=" * 70)

ctx = never_jscore.Context(enable_extensions=True, enable_logging=True)

# 模拟真实场景：复杂的目标网页 JS（不可修改）
target_website_js = """
// ========== 模拟目标网站的 JS 代码（你不能修改） ==========

// 网站有多个定时器在运行
setInterval(() => {
    console.log('[网站定时器1] 心跳检测...');
}, 1000);

setInterval(() => {
    console.log('[网站定时器2] 刷新广告...');
}, 500);

// 加密函数（在定时器中调用）
function encryptAndSend() {
    // 模拟复杂加密逻辑
    const timestamp = Date.now();
    const userAgent = navigator.userAgent;
    const signature = btoa(userAgent + timestamp);

    console.log('[加密] 生成签名:', signature);

    // 发送加密数据
    const xhr = new XMLHttpRequest();
    xhr.open('POST', 'https://api.target.com/verify');
    xhr.send(JSON.stringify({
        sig: signature,
        ts: timestamp,
        ua: userAgent
    }));

    return signature;
}

// 主定时器：每 2 秒执行一次加密
let count = 0;
setInterval(() => {
    count++;
    console.log(`[主任务] 第 ${count} 次执行`);

    if (count === 2) {
        // 第二次执行时发送加密数据
        encryptAndSend();
    }
}, 2000);

console.log('[网站] JS 初始化完成，定时器已启动');
"""

# ========== 你的 Hook 代码（可以修改） ==========
hook_code = """
// 重写 XMLHttpRequest.send 拦截加密数据
const originalXHR = XMLHttpRequest;
window['XMLHttpRequest'] = function(){
    const xhr = {};
    let method = 'GET';
    let url = '';

    xhr.open = function(m, u) {
        method = m;
        url = u;
    };

    xhr.setRequestHeader = function() {};

    xhr.send = function(data) {
        console.log('\\n[Hook 拦截] ========================================');
        console.log('[Hook] Method:', method);
        console.log('[Hook] URL:', url);
        console.log('[Hook] 加密数据:', data);
        console.log('========================================\\n');

        // 清除所有定时器（关键步骤！）
        if (typeof __neverjscore_clear_all_timers__ !== 'undefined') {
            __neverjscore_clear_all_timers__();
            console.log('[Hook] ✓ 已清除所有定时器');
        }

        // 返回拦截的数据到 Python
        __neverjscore_return__({
            method: method,
            url: url,
            encrypted_data: data,
            intercepted_at: Date.now()
        });

        // 下面的代码不会执行
        console.log('[Hook] 这行不会执行');
    };

    return xhr;
};

console.log('[Hook] XMLHttpRequest 已劫持\\n');
"""

print("\n1. 注入 Hook 代码...")
ctx.eval(hook_code)

print("2. 执行目标网站 JS（包含定时器）...\n")
result = ctx.evaluate(target_website_js)

print("\n" + "=" * 70)
print("拦截结果")
print("=" * 70)
print(f"请求方法: {result['method']}")
print(f"请求 URL: {result['url']}")
print(f"加密数据: {result['encrypted_data']}")
print(f"拦截时间: {result['intercepted_at']}")

print("\n" + "=" * 70)
print("说明")
print("=" * 70)
print("""
[OK] 成功拦截加密数据
[OK] 所有定时器已清除（不再执行）
[OK] 不需要修改目标网站的 JS 代码

关键代码（在你的 Hook 中添加）：

    __neverjscore_clear_all_timers__();  // 清除所有定时器
    __neverjscore_return__(data);        // 返回数据到 Python

适用场景：
- Akamai 传感器拦截
- 滑块验证码逆向
- API 签名算法提取
- 任何需要拦截加密数据的逆向场景
""")
