$(document).ready(function () {
    $("#driver").click(function () {
        $.getJSON('mobile.json', function (jd) {
            var searchField = $('#search').val();
            var expression = new RegExp(searchField, "i");
            $('table').html("");
            if (!searchField.length) {
                alert("please give some input");
            } else {
                arr = jQuery.grep(jd, function (i) {
                    return (i.mobile.search(expression) != -1)
                });
                if (!arr.length) {
                    return alert("no thing found");
                } else {
                    $.each(arr, function (idx, obj) {
                        $('table').append("<tr><<td>" + obj.mobile + "</td><td>" + obj.price + "</td></tr>");
                    }); 
                }
            }
            document.getElementById("search").value="";
        });
    });
    $("#getdata").click(function () {
        $.post('/insert_data', {
            key: document.getElementById("ID").value,
            value: document.getElementById("VALUE").value
        })
        alert("data submitted");
        document.getElementById("ID").value="";
        document.getElementById("VALUE").value="";
    });
});

