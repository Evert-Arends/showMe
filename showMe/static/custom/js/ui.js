/**
 * Created by Evert Arends on 2/28/17.
 */
$(document).ready(function () {
    var content = getLog('Apache');
    console.log(content);
    // $('#LogArea').val('ok');
    // $('#LogArea').val(content);
});

function getLog(log) {
    var log_url = '/log/' + log;
    $.get(log_url).then(function (responseData) {
        var $textarea = $('#LogArea');
         $textarea.val(responseData);
         $textarea.scrollTop($textarea[0].scrollHeight);
        return true;
    });
}
