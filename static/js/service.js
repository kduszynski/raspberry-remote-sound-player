function playSound(name){
    $.ajax({
        url: $SCRIPT_ROOT + "/start?soundName=" + name,
        type: "POST",
        success: function (data, status, xhr) {
            $("#volume").show()
            $("#selected-sound").html(data.name)
      },
    });
}

function resume(){
    $.ajax({
        url: $SCRIPT_ROOT + "/resume",
        type: "POST",
        success: function (data, status, xhr) {
            $("#selected-sound-status").html("Playing:")
            $("#selected-sound").html(data.name)
      },
    });
}

function stop(){
    $.ajax({
        url: $SCRIPT_ROOT + "/pause",
        type: "POST",
        success: function (data, status, xhr) {
            $("#selected-sound-status").html("Stopped:")
            $("#selected-sound").html(data.name)
      },
    });
}

function volUp(){
    $.ajax({
        url: $SCRIPT_ROOT + "/volume-up",
        type: "POST",
        success: function (data, status, xhr) {
            $("#volume").html(data)
      },
    });
}

function volDown(){
    $.ajax({
        url: $SCRIPT_ROOT + "/volume-down",
        type: "POST",
        success: function (data, status, xhr) {
            $("#volume").html(data)
      },
    });
}