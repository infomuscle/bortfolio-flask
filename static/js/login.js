function login(){

  var userId = $("#inputUserId").val();
  var userPw = $("#inputUserPw").val();

  var data = {};
  data['userId'] = userId;
  data['userPw'] = userPw;

  alert(JSON.stringify(data));

  $.ajax({
    url: '',
    data: JSON.stringify(data),
    success: function() {

    },
    error: function() {

    }

  });



}