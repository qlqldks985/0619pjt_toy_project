from flask import Blueprint, render_template ,request, redirect, session
from utils.json_bank import load_bank, save_bank
import datetime
import uuid

bank_bp = Blueprint (
    'bank',
    __name__,
    url_prefix='/bank',
)

# 메인홈
@bank_bp.route('/bank_home')
def bank_home():
    return render_template('bank/bank_home.html')

# 계좌개설
@bank_bp.route('/account_opening_form')
def account_opening_form():
    return render_template('bank/account_opening_form.html')

@bank_bp.route('/account_opening_confirm', methods=['POST'])
def account_opening_confirm():

    uName = request.form['uName']
    accountName = request.form['accountName']
    accountPw = request.form['accountPw']

    now = datetime.now()
    nows =  now.strftime('%Y-%m-%d %H:%M:%S')

    bankData = load_bank()
    uuids = str(uuid.uuid4())

    userId = session.get('signInedMemberId')
    
    bankData[userId] = {
    'uuids':uuids,
    'userId':userId,
    'uName':uName,
    'balance':0,
    'accountName':accountName,
    'accountPw':accountPw,
    'nows':nows,
    'histories':[]
    }

    save_bank(bankData)

    return render_template('bank/account_result.html')

# 계좌목록확인
@bank_bp.route('/transaction_history_form')
def transaction_history_form():

    bankData = load_bank()

    userId = session.get('signInedMemberId')

    if userId is None:
        return render_template('index.html')
    else:
        uName = bankData[userId]['uName']
        uuids = bankData[userId]['uuids']
        return render_template('bank/transaction_history_form.html', uName=uName, bankData=uuids )
    
# 계좌 송금
@bank_bp.route('/account_transfer', methods=['POST'])
def account_transfer():

    accountMoney = request.form['accountMoney']
    transferMemo = request.form['transferMemo']

    bankData = load_bank()
    userId = session.get('signInedMemberId')

    nows =  datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    deposit = {
        'accountMoney':accountMoney,
        'transferMemo':transferMemo,
        'nows':nows
    }
    if userId is None:
        if userId in bankData:

            accountMoney = int(request.form['accountMoney'])

            bankData[userId]['accountMoney'] += accountMoney
            bankData[userId]['transferMemo'].insert(0, deposit)

            save_bank(bankData)
            return render_template('bank/account_transfer_confirm')
        
        else:
            return render_template('index.html')
            






# 계좌해지관리
@bank_bp.route('/withdrawal_form')
def withdrawal_form():
    pass