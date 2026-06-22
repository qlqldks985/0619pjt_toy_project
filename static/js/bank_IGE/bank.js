function goHome() {
    location.href = '/bank/bank_home';
}

function accountList() {
    location.href = '/bank/transaction_history_form';
}


// 계좌 신규 개설
function accountOpeningForm() {
    console.log('accountOpeningForm() CALLED')

    let form = document.account_opening_form;

    let uName = form.uName.value.trim();
    let accountName = form.accountName.value.trim();
    let accountPw = form.accountPw.value.trim();

    if (uName === '') {
        alert('성함을 입력 하세요.');
        form.uName.focus();

    } else if (accountName === '') {
        alert('계좌 이름을 입력 하세요.');
        form.accountName.focus();

    } else if (accountPw === '') {
        alert('비밀번호 입력 하세요.');
        form.accountPw.focus();
        
    } else if (accountPw.length !== 4){
        alert('비밀번호는 4자리로 입력해 주세요.');

    } else {
        form.submit();
    }
}

// 계좌 이체
function transferMoney() {
    let checkedAccounts = [];
    let accountCheckboxes = document.querySelectorAll('input[type="checkbox"]');

    accountCheckboxes.forEach(function(checkbox) {
        if (checkbox.checked) {
            console.log(checkbox.value);
            checkedAccounts.push(checkbox.value);
        }
    })

    if (checkedAccounts.length === 0) {
        alert('계좌를 선택해주세요!');

    } else if (checkedAccounts.length > 1) {
        alert('하나의 계좌만 선택해주세요!');

    }

}

// 계좌 상태 수정
function changeStatus() {

}

// 계좌해지
function closeAccount () {

}