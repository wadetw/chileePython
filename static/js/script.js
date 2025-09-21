document.addEventListener('DOMContentLoaded', () => {
    // 獲取 DOM 元素
    const tempValue = document.getElementById('temp-value');
    const humidityValue = document.getElementById('humidity-value');
    const ledStatus = document.getElementById('led-status');
    const ledOnBtn = document.getElementById('led-on-btn');
    const ledOffBtn = document.getElementById('led-off-btn');

    // --- 模擬感測器數據更新 ---
    // 在真實世界中，您會使用 WebSocket 或 Fetch API 從後端獲取數據
    function updateSensorData() {
        // 產生隨機數據
        const randomTemp = (20 + Math.random() * 10).toFixed(1);
        const randomHumidity = (40 + Math.random() * 20).toFixed(1);

        // 更新網頁內容
        tempValue.textContent = randomTemp;
        humidityValue.textContent = randomHumidity;
    }

    // 每3秒更新一次數據
    setInterval(updateSensorData, 3000);
    // 立即執行一次以顯示初始值
    updateSensorData();


    // --- 設備控制事件監聽 ---
    ledOnBtn.addEventListener('click', () => {
        ledStatus.textContent = '開啟';
        ledStatus.style.color = 'var(--success-color)';
        console.log('LED 開啟指令已發送');
        // 在真實世界中，您會在這裡使用 fetch() 向 Flask 後端發送請求
        // fetch('/led/on', { method: 'POST' });
    });

    ledOffBtn.addEventListener('click', () => {
        ledStatus.textContent = '關閉';
        ledStatus.style.color = 'var(--danger-color)';
        console.log('LED 關閉指令已發送');
        // fetch('/led/off', { method: 'POST' });
    });
});
