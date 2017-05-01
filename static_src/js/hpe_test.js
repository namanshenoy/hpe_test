/**
 * Created by namanshenoy on 2/17/17.
 */
jQuery(document).ready(function ($) {
    $(".clickable-row").click(function () {
        window.location = $(this).data("url");
    });
});
$('#server-table td').hover(function () {
    $(this).addClass('hover');
}, function () {
    $(this).removeClass('hover');
});