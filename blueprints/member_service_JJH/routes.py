from flask import Blueprint, render_template, request, session, redirect
import json, os

MEMBER_FILE = 'db/members.json'

if os.path.exists(MEMBER_FILE):
    with open(MEMBER_FILE, 'r', encoding='utf-8') as f:
        members = json.load(f)
else:
    members = {}

member_bp = Blueprint(
    'member_service_jjh',
    __name__,
    template_folder='../../templates/member_service_JJH'
)

@member_bp.route('/signup/form')
def signup_form():
    return render_template('member_service_JJH/signup_form.html')

@member_bp.route('/signup/confirm', methods=['POST'])
def signup_confirm():

    user_id = request.form.get('user_id')
    user_pw = request.form.get('user_pw')
    user_mail = request.form.get('user_mail')
    user_phone = request.form.get('user_phone')

    if user_id in members:
        return render_template(
            'member_service_JJH/signup_result.html',
            msg='이미 존재하는 아이디입니다.'
        )
    
    members[user_id] = {
        'pw':user_pw,
        'mail':user_mail,
        'phone':user_phone,
    }

    with open(MEMBER_FILE, 'w', encoding='utf-8') as f:
        json.dump(members, f, ensure_ascii=False, indent=4)

    return render_template(
        'member_service_JJH/signup_result.html',
        msg=f'{user_id}님 회원가입이 완료되었습니다.'
    )

@member_bp.route('/signin/form')
def signin_form():
    return render_template('member_service_JJH/signin_form.html')

@member_bp.route('/signin/confirm', methods=['POST'])
def signin_confirm():
    
    user_id = request.form.get('user_id')
    user_pw = request.form.get('user_pw')

    if user_id not in members:
        return render_template(
            'member_service_JJH/signin_result.html',
            msg = '존재하지 않는 아이디'
        )
    
    if members[user_id]['pw'] != user_pw:
        return render_template(
            'member_service_JJH/signin_result.html',
            msg='비밀번호 불일치'
        )
    
    session['login_member'] = user_id

    return render_template(
        'member_service_JJH/signin_result.html',
        msg='로그인 성공'
    )

@member_bp.route('/logout')
def logout():
    
    session.pop('login_member', None)

    return redirect('/')
    
@member_bp.route('/modify/form')
def modify_form():
    return render_template('member_service_JJH/modify_form.html')

@member_bp.route('/modify/confirm', methods=['POST'])
def modify_confirm():

    user_id = session.get('login_member')
    new_pw = request.form.get('new_pw')

    if user_id in members:
        members[user_id]['pw'] = new_pw

        with open(MEMBER_FILE, 'w', encoding='utf-8') as f:
            json.dump(members, f, ensure_ascii=False, indent=4)

        return render_template(
            'member_service_JJH/modify_result.html',
            msg='수정 완료'
        )
    return render_template(
        'member_service_JJH/modify_result.html',
        msg='존재하지 않는 회원 정보입니다.'
    )

@member_bp.route('/member/form')
def member_form():
    return render_template(
        'member_service_JJH/member_form.html'
    )

@member_bp.route('/member/info')
def member_info():

    user_id = request.form.get('user_id')

    if user_id not in members:

        return render_template(
            'member_service_JJH/member_result.html',
            msg='존재하지 않는 회원입니다.'
        )
    
    member = members[user_id]

    return render_template(
        'member_service_JJH/member_result.html',
        user_id=user_id,
        user_mail=member['mail'],
        user_phone=member['phone']
    )

@member_bp.route('/delete/form')
def delete_form():

    return render_template(
        'member_service_JJH/delete_form.html'
    )

@member_bp.route('/delete/confirm', methods=['POST'])
def delete_confirm():

    user_id = request.form.get('user_id')

    if user_id in members:
        del members[user_id]

        session.pop('login_member', None)

        with open(MEMBER_FILE, 'w', encoding='utf-8') as f:
            json.dump(members, f, ensure_ascii=False, indent=4)

        return render_template(
            'member_service_JJH/delete_result.html',
            msg='탈퇴 완료'
        )
    
    return render_template(
        'member_service_JJH/delete_result.html',
        msg='회원 없음'
    )