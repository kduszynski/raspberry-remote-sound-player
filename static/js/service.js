function playSound(name){
    $.ajax({
        url: $SCRIPT_ROOT + "/start?soundName=" + name,
        type: "POST",
        success: function (data, status, xhr) {
            $("#now-playing").show()
            $("#volume").show()
            $("#now-playing").html("Playing " + data)
      },
    });
}

function resume(){
    $.ajax({
        url: $SCRIPT_ROOT + "/resume",
        type: "POST",
        success: function (data, status, xhr) {
            $("#now-playing").show()
            $("#volume").show()
            $("#now-playing").html("Playing " + data)
      },
    });
}

function stop(){
    $.ajax({
        url: $SCRIPT_ROOT + "/pause",
        type: "POST",
        success: function (data, status, xhr) {
            $("#now-playing").show()
            $("#volume").show()
            $("#now-playing").html("Stopped " + data)
      },
    });
}

function volUp(){
    $.ajax({
        url: $SCRIPT_ROOT + "/volume-up",
        type: "POST",
        success: function (data, status, xhr) {
            $("#volume").show()
            $("#volume").html("Volume " + data)
      },
    });
}

function volDown(){
    $.ajax({
        url: $SCRIPT_ROOT + "/volume-down",
        type: "POST",
        success: function (data, status, xhr) {
            $("#volume").show()
            $("#volume").html("Volume " + data)
      },
    });
}