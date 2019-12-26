function login() {

  var adminId = $("#inputUserId").val();
  var adminPw = $("#inputUserPw").val();

  var data = {};
  data['adminId'] = adminId;
  data['adminPw'] = adminPw;

  $.ajax({
    url: '/admin/loginValidation',
    type: 'POST',
    data: JSON.stringify(data),
    contentType: 'application/json;charset=UTF-8',
    success: function(res) {
      if (res == "0000"){
        console.log("로그인 인증 성공 ");
        alert("짱짱");
      } else if (res == "E0001") {
        console.log("로그인 인증 실패: 잘못된 패스워드");
        alert("로그인 인증 실패: 잘못된 패스워드");
      } else {
        console.log("로그인 인증 실패: 알 수 없는 오류");
        alert("로그인 인증 실패: 알 수 없는 오류");
      }
    },
    error: function(res) {
      console.log("로그인 인증 ajax 통신 실패");
      alert("로그인 인증 ajax 통신 실패");
    }

  });



}

function unsupported() {
  alert("unsupported login system");
}