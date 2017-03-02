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
         $('#LogArea').val(responseData);
        return true;
    });
}
