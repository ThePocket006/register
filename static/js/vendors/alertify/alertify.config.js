(function (factory) {
    if ( typeof define === 'function' && define.amd ) {
		// AMD
        define(['alertifyjs'], function (alertify ) {
            return factory(alertify, window, document );
		} );
	}
	else if ( typeof exports === 'object' ) {
		// CommonJS
        module.exports = function (root, alertify) {
			if ( ! root ) {
				root = window;
			}

            if ( !alertify ) {
				// Require DataTables, which attaches to jQuery, including
				// jQuery if needed and have a $ property so we can access the
				// jQuery object that is used
                alertify = require('alertifyjs');
			}

            return factory(alertify, root );
		};
	}
	else {
		// Browser
        factory(alertify, window );
    }
}(function (alertify, window) {
    'use strict';
    alertify.defaults.transition = "slide";
    alertify.defaults.theme.ok = "btn btn-primary";
    alertify.defaults.theme.cancel = "btn btn-danger";
    alertify.defaults.theme.input = "form-control";
    if (!window.alertify) window.alertify = alertify;
    return alertify;
}));