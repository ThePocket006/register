(function (factory) {
    if (typeof define === 'function' && define.amd) {
        // AMD
        define(['sweetalert2'], function (swal) {
            return factory(swal, window, document);
        });
    }
    else if (typeof exports === 'object') {
        // CommonJS
        module.exports = function (root, swal) {
            if (!root) {
                root = window;
            }

            if (!swal) {
                // Require DataTables, which attaches to jQuery, including
                // jQuery if needed and have a $ property so we can access the
                // jQuery object that is used
                swal = require('sweetalert2');
            }

            return factory(swal, root);
        };
    }
    else {
        // Browser
        factory(swal, window);
    }
}(function (swal, window) {
    'use strict';

    swal = swal.mixin({
        confirmButtonClass: 'btn btn-success',
        cancelButtonClass: 'btn btn-danger',
        buttonsStyling: false,
    });

    if (!window.swal){
        window.swal = swal;
        window.toast = swal.mixin({
            toast: true,
            position: 'top-end',
            showConfirmButton: false,
            timer: 3000
        });
    }
    return swal;
}));