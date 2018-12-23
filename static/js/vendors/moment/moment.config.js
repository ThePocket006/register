(function (factory) {
    if (typeof define === 'function' && define.amd) {
        // AMD
        define(['moment-locales'], function (moment) {
            return factory(moment, window, document);
        });
    }
    else if (typeof exports === 'object') {
        // CommonJS
        module.exports = function (root, moment) {
            if (!root) {
                root = window;
            }

            if (!moment) {
                // Require DataTables, which attaches to jQuery, including
                // jQuery if needed and have a $ property so we can access the
                // jQuery object that is used
                moment = require('moment-locales');
            }

            return factory(moment, root);
        };
    }
    else {
        // Browser
        factory(moment, window);
    }
}(function (moment, window) {
    'use strict';

    if (!window.moment){
        window.moment = moment;
    }
    return moment;
}));