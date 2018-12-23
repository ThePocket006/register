(function (factory) {
    "use strict";

    if (typeof define === 'function' && define.amd) {
        // AMD
        define(['jquery'], function ($) {
            return factory($, window);
        });
    }
    else if (typeof exports === 'object') {
        // CommonJS
        module.exports = function (root, $) {
            if (!root) {
                root = window;
            }

            if (!$) {
                $ = typeof window !== 'undefined' ? require('jquery') : require('jquery')(root);
            }

            return factory($, root);
        };
    }
    else {
        // Browser
        factory($, window);
    }
}(function ($, window) {
    'use strict';
    $.fn.extend({
        animateCss: function (animationName) {
            this.trigger('animate-css-start');
            var animationEnd = 'webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend';
            var animationClass = this.hasClass('animated') ? animationName : 'animated ' + animationName;

            this.attr('data-animated', animationName)
                .addClass(animationClass)
                .one(animationEnd, function () {
                    $(this).removeClass(animationName)
                        .trigger('animate-css-end');
                });
            return this;
        }
    });
    
    return window.$ = $;
}));