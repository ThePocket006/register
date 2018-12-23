if (!JStranslate){
    window.JStranslate = function(french, english) {
        return String($('html').attr('lang')).toLowerCase() == "en"?french:english;
    }
}