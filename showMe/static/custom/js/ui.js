/**
 * Created by Evert Arends on 2/28/17.
 */
$(document).ready(function () {
    var content = getLog('Apache');
    console.log(content);
});

function getLog(log) {
    var log_url = '/log/' + log;
    $.get(log_url).then(function (responseData) {
        var $textarea = $('#LogArea');
        $textarea.val(responseData);
        console.log(responseData);
        $textarea.scrollTop($textarea[0].scrollHeight);
        return true;
    });
}
$(document).ready(function () {
    $("div.content-tab-menu>div.list-group>a").click(function (e) {
        e.preventDefault();
        $(this).siblings('a.active').removeClass("active");
        $(this).addClass("active");
        var index = $(this).index();
        $("div.content-tab>div.content-tab-content").removeClass("active");
        $("div.content-tab>div.content-tab-content").eq(index).addClass("active");
    });
});