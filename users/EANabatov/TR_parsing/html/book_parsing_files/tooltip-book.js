 (function ($) {
    $.fn.newToolTip = function () {      
        $('body').on('click', '.tooltip_close', function (e) {
            e.preventDefault();
            $(this).parent().fadeOut(100);
        });
        if (!window.tooltip_settimeout) {
            window.tooltip_settimeout = 'null';
        }
        return this.each(function (index) {
            var i = index;
            var id = $(this).data('div');
            var tooltip = $('#' + id);
            if (tooltip.length < 1) {
                id = "jtooltip__" + i;
                var showClose = $(this).hasClass('showClose');
                $('body').append('<div id="' + id + '" class="tooltip-popup">' +
                (showClose ? '<a class="tooltip_close icon-close"></a>' : '') +
                '<p>' + $(this).attr('title') + '</p></div>');
                tooltip = $('#' + id);
            }
            $(this).data('div', id).removeAttr("title").mouseenter(function (e) {
                var t = $('#' + $(this).data('div'));
                $('.tooltip-popup').not(t).fadeOut();
                var pos = $(this).position();
                var h = $(this).outerHeight();
                t.css('top', pos.top + (h > 50 ? 20 : h) + 1);
                t.css('left', pos.left);
                t.fadeIn(100);
                clearTimeout(window.tooltip_settimeout);
            }).mouseleave(function () {
                var t = $('#' + $(this).data('div'));
                window.tooltip_settimeout = setTimeout(function () { t.fadeOut(100); }, 600);
                t.mouseover(function (e) { clearTimeout(window.tooltip_settimeout); });
            });
        });
    };

}(jQuery));
