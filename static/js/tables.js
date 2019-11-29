function insertData(){
  var temp = $("#addDataForm").serializeArray();

  var params = {};
  for (var i=0; i<temp.length; i++){
    params[temp[i]['name']] = temp[i]['value'];
  }

  $.ajax({
    url: '/admin/addData',
    type: 'POST',
    data: JSON.stringify(params),
    contentType: 'application/json;charset=UTF-8',
    success: function(res){
      if (res == "0000") {
        console.log("DB INSERT 성공");
        location.reload();
      } else {
        alert("DB INSERT 결과코드 에러")
      }
    },
    error: function(){
      alert("DB INSERT ajax 통신 실패");
    }
  });
}

function updateData(){
  var params = {};
  params["table"] = $("input[name='table']").val();
  params["pkColumn"] = "";
  params["pkValue"] = []
  params["columns"] = [];

  if (confirm( "테이블을 업데이트 하시겠습니까?")){

    $(".tableRow").each(function () {
      temp = {};

      row = $(this);
      row.children().each(function(index) {
        var colNm = $(this).attr("class");
        var colVal = $(this).children().html();

        if (index == 2) {
          params["pkColumn"] = colNm;
          params["pkValue"].push(colVal);
        }

        if (colNm != undefined) {
          temp[colNm] = colVal;
        }
      });

      // alert(JSON.stringify(temp, null, 4));
      params["columns"].push(temp);
    });

    $.ajax({
      url: '/admin/update',
      type: 'POST',
      data: JSON.stringify(params),
      contentType: 'application/json;charset=UTF-8',
      success: function(res) {
        if (res == "0000"){
            console.log("DB DELETE 성공");
            location.reload();
        } else{
          alert("DB UPDATE 결과코드 에러");
        }
      },
      error: function(res){
        alert("DB UPDATE ajax 통신 실패");
      }
    });

  } else {
    console.log("DB DELETE 취소");
  }
}

function deleteData(btn) {
  var table = $("input[name='table']").val();
  var btnId = btn.id;
  var pkColumn = $("#"+btnId).parent().siblings(':nth-child(3)').attr('class');
  var pkValue = $("#"+btnId).parent().siblings(':nth-child(3)').text().trim();

  if (confirm( pkValue + " 데이터를 삭제하시겠습니까?")){
    var params = {
      "table":table,
      "pkColumn": pkColumn,
      "pkValue": pkValue
    };

    $.ajax({
      url: '/admin/delete',
      type: 'POST',
      data: JSON.stringify(params),
      contentType: 'application/json;charset=UTF-8',
      success: function (res) {
        if (res == "0000"){
          console.log("DB DELETE 성공");
          location.reload();
        } else {
          alert("DB DELETE 결과코드 에러")
        }
      },
      error: function () {
        alert("DB DELETE ajax 통신 실패");
      }
    });
  } else{
    console.log("DB DELETE 취소");
  }
}
