function xhrError(xhr) {
    if (xhr.status === 200) {
        swal({
            type: 'error',
            title: JStranslate('<h2>Oops...</h2>'),
            text: JStranslate('Une erreur est survenue lors du traitement de la requête.', 'An error occurred when the request was processed.'),
        });
    } else {
        swal({
            type: 'error',
            title: JStranslate('Erreur ' + xhr.status, xhr.status + ' Error'),
            text: xhr.statusText
        });
    }
}