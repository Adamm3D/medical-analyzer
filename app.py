from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Когда человек заходит на главный адрес сайта, отдаем ему HTML
@app.route('/')
def home():
    return render_template('index.html')

# Скрытый маршрут, куда стучится наш JavaScript
@app.route('/analyze', methods=['POST'])
def analyze():
    # 1. Распаковываем данные от JS
    data = request.json
    value = float(data.get('indicator', 0))
    
    # 2. Наша бизнес-логика (то, ради чего всё затевалось)
    if value > 100:
        result_status = "🔴 Превышение нормы! Требуется внимание."
    else:
        result_status = "🟢 Показатель в норме."
        
    # 3. Упаковываем ответ и отправляем обратно курьеру (JS)
    return jsonify({"status": result_status})

if __name__ == '__main__':
    app.run(port=5000)
