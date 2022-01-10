$(function() {
    $(".btn-toggle").click(function(e) {
        if ( e.target != this ) {
            if ( $(this).find(".btn-primary").length > 0 ) {
                $(this).find(".active").toggleClass("btn-primary");
                $(this).find(".active").toggleClass("btn-secondary");
                $(this).find(e.target).toggleClass("btn-secondary");
                $(this).find(e.target).toggleClass("btn-primary");
            }
            if ( $(this).find(".btn-secondary").length > 0 ) {
                $(this).find(".active").toggleClass("btn-secondary");
                $(this).find(".active").toggleClass("btn-secondary");
                $(this).find(e.target).toggleClass("btn-secondary");
                $(this).find(e.target).toggleClass("btn-secondary");
            }
            if ( $(this).find(".btn-danger").length > 0 ) {
                $(this).find(".active").toggleClass("btn-danger");
                $(this).find(".active").toggleClass("btn-secondary");
                $(this).find(e.target).toggleClass("btn-secondary");
                $(this).find(e.target).toggleClass("btn-danger");
            }
            if ( $(this).find(".btn-success").length > 0 ) {
                $(this).find(".active").toggleClass("btn-success");
                $(this).find(".active").toggleClass("btn-secondary");
                $(this).find(e.target).toggleClass("btn-secondary");
                $(this).find(e.target).toggleClass("btn-success");
            }
            if ( $(this).find(".btn-info").length > 0 ) {
                $(this).find(".active").toggleClass("btn-info");
                $(this).find(".active").toggleClass("btn-secondary");
                $(this).find(e.target).toggleClass("btn-secondary");
                $(this).find(e.target).toggleClass("btn-info");
            }
            if ( $(this).find(".btn-warning").length > 0 ) {
                $(this).find(".active").toggleClass("btn-warning");
                $(this).find(".active").toggleClass("btn-secondary");
                $(this).find(e.target).toggleClass("btn-secondary");
                $(this).find(e.target).toggleClass("btn-warning");
            }
            if ( $(this).find(".btn-light").length > 0 ) {
                $(this).find(".active").toggleClass("btn-light");
                $(this).find(".active").toggleClass("btn-secondary");
                $(this).find(e.target).toggleClass("btn-secondary");
                $(this).find(e.target).toggleClass("btn-light");
            }
            if ( $(this).find(".btn-dark").length > 0 ) {
                $(this).find(".active").toggleClass("btn-dark");
                $(this).find(".active").toggleClass("btn-secondary");
                $(this).find(e.target).toggleClass("btn-secondary");
                $(this).find(e.target).toggleClass("btn-dark");
            }

            $(this).find(".active").toggleClass("active");
            $(this).find(e.target).toggleClass("active");
        }
    });
});
