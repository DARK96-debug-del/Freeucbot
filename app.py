from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Initial values
user_balance = 100  # Starting balance
user_referral = "https://t.me/your_referral_link"  # Example referral link
mission_list = [
    {"name": "Instagram Follow", "reward": 5},
    {"name": "Telegram Join", "reward": 3},
    {"name": "YouTube Subscribe", "reward": 10}
]

# Saytning bosh sahifasi
@app.route('/')
def index():
    return render_template('index.html', balance=user_balance, referral_link=user_referral)

# Tanga bosish (UC qo'shish)
@app.route('/coin', methods=['POST'])
def coin():
    global user_balance
    user_balance += 0.01  # Each coin adds 0.01 UC to the balance
    return redirect(url_for('index'))

# Referal tizimi (foydalanuvchi referal linkini nusxalaydi)
@app.route('/referral', methods=['POST'])
def referral():
    global user_balance
    user_balance += 12  # 12 UC will be added to the user's balance
    return redirect(url_for('index'))

# Missiyalarning bajarilishi
@app.route('/missions')
def missions():
    return render_template('missions.html', missions=mission_list)

# UC yechish
@app.route('/withdraw', methods=['POST'])
def withdraw():
    global user_balance
    uc_to_withdraw = float(request.form['uc_to_withdraw'])
    if uc_to_withdraw >= 120 and uc_to_withdraw <= user_balance:
        user_balance -= uc_to_withdraw
        pubg_id = request.form['pubg_id']
        return render_template('withdrawal_success.html', uc=uc_to_withdraw, pubg_id=pubg_id)
    else:
        return "Withdrawal failed. Please check your balance or the withdrawal amount."

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)