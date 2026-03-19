function sendData() {
    // 1. Берем число из поля ввода
    let inputVal = document.getElementById("dataInput").value;

    // 2. Отправляем посылку (POST-запрос) по адресу /analyze
    fetch("/analyze", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ indicator: inputVal })
    })
    .then(response => response.json()) // 3. Ждем ответ от Python
    .then(data => {
        // 4. Выводим результат на экран без перезагрузки страницы
        document.getElementById("resultText").innerText = 
            "Статус: " + data.status;
    });
}
