function exibirvideoaula(link){
    $("#youtube").attr("src",link);
    const myModal = new bootstrap.Modal('#modal', {
        keyboard: false
    }).show();
}